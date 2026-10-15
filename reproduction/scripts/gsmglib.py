"""Independent helpers for the GSMG reproduction (written fresh for this archive).

Nothing here is copied from upstream notebooks or harnesses. Only Python stdlib,
pycryptodome (AES primitive, RIPEMD-160) and numpy/PIL are used.
"""
import base64, hashlib, os, subprocess, tempfile

from Crypto.Cipher import AES
from Crypto.Hash import RIPEMD160

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))


def src(path):
    """Absolute path of a file under sources/."""
    return os.path.join(REPO, "sources", path)


def sha256(b):
    return hashlib.sha256(b).hexdigest()


# ---------------------------------------------------------------- OpenSSL envelope
def parse_envelope(b64text):
    raw = base64.b64decode("".join(b64text.split()))
    if raw[:8] != b"Salted__":
        raise ValueError("no Salted__ header")
    return raw, raw[8:16], raw[16:]


def evp_bytes_to_key(password, salt, md, klen=32, ivlen=16):
    """OpenSSL EVP_BytesToKey, one iteration: D_i = H(D_{i-1} || pw || salt)."""
    out, d = b"", b""
    while len(out) < klen + ivlen:
        d = hashlib.new(md, d + password + salt).digest()
        out += d
    return out[:klen], out[klen:klen + ivlen]


def strict_unpad(pt):
    """Return unpadded bytes or None when PKCS#7 padding is invalid."""
    n = pt[-1]
    if n < 1 or n > 16 or pt[-n:] != bytes([n]) * n:
        return None
    return pt[:-n]


def aes_decrypt(b64text, password, md):
    _, salt, ct = parse_envelope(b64text)
    key, iv = evp_bytes_to_key(password, salt, md)
    return strict_unpad(AES.new(key, AES.MODE_CBC, iv).decrypt(ct))


def openssl_decrypt(b64text, password, md):
    """Second implementation: the OpenSSL CLI does its own EVP + AES + unpadding.

    The password is supplied through a file when it is a single line without NUL;
    otherwise EVP_BytesToKey is computed with `openssl dgst` (CLI) and -K/-iv is used.
    """
    raw, salt, ct = parse_envelope(b64text)
    with tempfile.TemporaryDirectory() as td:
        ctf = os.path.join(td, "ct.bin"); open(ctf, "wb").write(raw)
        outf = os.path.join(td, "pt.bin")
        if b"\n" not in password and b"\0" not in password and b"\r" not in password:
            pwf = os.path.join(td, "pw"); open(pwf, "wb").write(password)
            cmd = ["openssl", "enc", "-d", "-aes-256-cbc", "-md", md, "-in", ctf, "-out", outf, "-pass", f"file:{pwf}"]
        else:
            d, out = b"", b""
            while len(out) < 48:
                f = os.path.join(td, "chunk"); open(f, "wb").write(d + password + salt)
                d = subprocess.run(["openssl", "dgst", "-" + md, "-binary", f], capture_output=True, check=True).stdout
                out += d
            ctf2 = os.path.join(td, "ct2.bin"); open(ctf2, "wb").write(ct)
            cmd = ["openssl", "enc", "-d", "-aes-256-cbc", "-nosalt", "-K", out[:32].hex(), "-iv", out[32:48].hex(), "-in", ctf2, "-out", outf]
        r = subprocess.run(cmd, capture_output=True)
        if r.returncode != 0:
            return None
        return open(outf, "rb").read()


# ---------------------------------------------------------------- secp256k1 (pure python)
P = 2**256 - 2**32 - 977
N = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141
G = (0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798,
     0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8)


def _add(a, b):
    if a is None: return b
    if b is None: return a
    if a[0] == b[0] and (a[1] + b[1]) % P == 0: return None
    if a == b:
        l = 3 * a[0] * a[0] * pow(2 * a[1], -1, P) % P
    else:
        l = (b[1] - a[1]) * pow(b[0] - a[0], -1, P) % P
    x = (l * l - a[0] - b[0]) % P
    return x, (l * (a[0] - x) - a[1]) % P


def point_mul(k, pt=G):
    r = None
    while k:
        if k & 1: r = _add(r, pt)
        pt = _add(pt, pt); k >>= 1
    return r


def on_curve(pt):
    return (pt[1] ** 2 - pt[0] ** 3 - 7) % P == 0


def ser(pt, compressed):
    if compressed:
        return bytes([2 + (pt[1] & 1)]) + pt[0].to_bytes(32, "big")
    return b"\x04" + pt[0].to_bytes(32, "big") + pt[1].to_bytes(32, "big")


B58 = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"


def b58check(payload):
    data = payload + hashlib.sha256(hashlib.sha256(payload).digest()).digest()[:4]
    n = int.from_bytes(data, "big"); s = ""
    while n:
        n, r = divmod(n, 58); s = B58[r] + s
    return "1" * (len(data) - len(data.lstrip(b"\0"))) + s


def hash160(b):
    return RIPEMD160.new(hashlib.sha256(b).digest()).digest()


def p2pkh(pubkey_bytes):
    return b58check(b"\x00" + hash160(pubkey_bytes))


def wif_uncompressed(scalar32):
    """Mainnet uncompressed WIF text of 32 bytes (used here only as a published AES password)."""
    return b58check(b"\x80" + scalar32)
