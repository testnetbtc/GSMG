"""
Minimal, dependency-free secp256k1 + Bitcoin address helpers.

Purpose in this archive: a reject-capable, fully OFFLINE check for candidate
private keys proposed by puzzle decodes. Nothing here touches the network,
signs a transaction, or imports a key into a wallet. A "candidate scalar" is
turned into a public point and compared to the puzzle's known prize point /
address. That is pure arithmetic on public data.

Known public anchors (public data, from the archive):
  - Prize address: 1GSMG1JC9wtdSwfwApgj2xcmJPAwx7prBe
  - Prize uncompressed public key (from the 2020 halving-spend scriptSig,
    sources/naddiseo/_pr15/neo/materials/chain/tx_halving_spend.hex):
    04 || X || Y with
      X = f4d1bbd91e65e2a019566a17574e97dae908b784b388891848007e4f55d5a464
      Y = 9c73d25fc5ed8fd7227cab0be4e576c0c6404db5aa546286563e4be12bf33559
"""
import hashlib

# secp256k1 domain parameters
P  = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F
N  = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141
Gx = 0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798
Gy = 0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8
G  = (Gx, Gy)

PRIZE_ADDR = "1GSMG1JC9wtdSwfwApgj2xcmJPAwx7prBe"
PRIZE_X = 0xf4d1bbd91e65e2a019566a17574e97dae908b784b388891848007e4f55d5a464
PRIZE_Y = 0x9c73d25fc5ed8fd7227cab0be4e576c0c6404db5aa546286563e4be12bf33559
PRIZE_PT = (PRIZE_X, PRIZE_Y)

# ---- EC math (Jacobian, one inverse per scalar mult) ----
def _inv(a, m=P):
    return pow(a % m, m - 2, m)

def _jac_double(Pt):
    X1, Y1, Z1 = Pt
    if Y1 == 0:
        return (0, 0, 0)
    S = (4 * X1 * Y1 * Y1) % P
    M = (3 * X1 * X1) % P            # a = 0 for secp256k1
    X3 = (M * M - 2 * S) % P
    Y3 = (M * (S - X3) - 8 * (Y1 ** 2) ** 2) % P
    Z3 = (2 * Y1 * Z1) % P
    return (X3, Y3, Z3)

def _jac_add(Pt, Qt):
    X1, Y1, Z1 = Pt
    X2, Y2, Z2 = Qt
    if Z1 == 0:
        return Qt
    if Z2 == 0:
        return Pt
    Z1Z1 = (Z1 * Z1) % P
    Z2Z2 = (Z2 * Z2) % P
    U1 = (X1 * Z2Z2) % P
    U2 = (X2 * Z1Z1) % P
    S1 = (Y1 * Z2 * Z2Z2) % P
    S2 = (Y2 * Z1 * Z1Z1) % P
    if U1 == U2:
        if S1 != S2:
            return (0, 0, 0)
        return _jac_double(Pt)
    H = (U2 - U1) % P
    R = (S2 - S1) % P
    HH = (H * H) % P
    HHH = (H * HH) % P
    V = (U1 * HH) % P
    X3 = (R * R - HHH - 2 * V) % P
    Y3 = (R * (V - X3) - S1 * HHH) % P
    Z3 = (H * Z1 * Z2) % P
    return (X3, Y3, Z3)

def _to_affine(Pt):
    X, Y, Z = Pt
    if Z == 0:
        return None  # point at infinity
    zi = _inv(Z)
    zi2 = (zi * zi) % P
    zi3 = (zi2 * zi) % P
    return ((X * zi2) % P, (Y * zi3) % P)

def scalar_mul(k, point=G):
    """Return affine (x,y) of k*point, or None for the point at infinity."""
    k %= N
    if k == 0:
        return None
    R = (0, 0, 0)                     # infinity in Jacobian
    Q = (point[0], point[1], 1)
    while k:
        if k & 1:
            R = _jac_add(R, Q)
        Q = _jac_double(Q)
        k >>= 1
    return _to_affine(R)

# ---- hashing / encoding ----
def sha256(b): return hashlib.sha256(b).digest()
def ripemd160(b):
    h = hashlib.new('ripemd160'); h.update(b); return h.digest()
def hash160(b): return ripemd160(sha256(b))

_B58 = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
def b58encode(b):
    n = int.from_bytes(b, 'big')
    s = ""
    while n > 0:
        n, r = divmod(n, 58); s = _B58[r] + s
    pad = 0
    for ch in b:
        if ch == 0: pad += 1
        else: break
    return "1" * pad + s

def b58check(payload, version=0x00):
    data = bytes([version]) + payload
    chk = sha256(sha256(data))[:4]
    return b58encode(data + chk)

def pubkey_bytes(pt, compressed=True):
    x, y = pt
    xb = x.to_bytes(32, 'big')
    if compressed:
        return bytes([2 + (y & 1)]) + xb
    return b"\x04" + xb + y.to_bytes(32, 'big')

def point_to_address(pt, compressed=True):
    return b58check(hash160(pubkey_bytes(pt, compressed)))

def scalar_to_addresses(k):
    """(compressed_addr, uncompressed_addr) for scalar k, or (None,None)."""
    pt = scalar_mul(k)
    if pt is None:
        return (None, None)
    return (point_to_address(pt, True), point_to_address(pt, False))

def wif(k, compressed=True):
    payload = k.to_bytes(32, 'big') + (b"\x01" if compressed else b"")
    return b58check(payload, version=0x80)

# ---- the one test that matters ----
def matches_prize(k):
    """True iff scalar k generates the prize public point (either sign of k)."""
    pt = scalar_mul(k)
    if pt is None:
        return False
    if pt == PRIZE_PT:
        return True
    # -k gives the same x with negated y; the prize point is fixed, so also
    # accept the exact point only. (A puzzle key is one specific scalar.)
    return False

def check(k):
    """Return a dict describing how scalar k relates to known anchors."""
    k %= N
    pt = scalar_mul(k)
    if pt is None:
        return {"k": 0, "infinity": True}
    ca, ua = point_to_address(pt, True), point_to_address(pt, False)
    return {
        "point_is_prize": pt == PRIZE_PT,
        "addr_c": ca,
        "addr_u": ua,
        "hits_prize_addr": PRIZE_ADDR in (ca, ua),
    }


if __name__ == "__main__":
    # Self-test 1: generator-based known vector (k=1 -> G -> known address).
    a_c, a_u = scalar_to_addresses(1)
    assert a_u == "1EHNa6Q4Jz2uvNExL497mE43ikXhwF6kZm", a_u
    assert a_c == "1BgGZ9tcN4rm9KBzDn7KprQz87SZ26SAMH", a_c

    # Self-test 2: the embedded prize pubkey must hash to the prize address.
    pk_u = b"\x04" + PRIZE_X.to_bytes(32, 'big') + PRIZE_Y.to_bytes(32, 'big')
    assert b58check(hash160(pk_u)) == PRIZE_ADDR, b58check(hash160(pk_u))

    # Self-test 3: the prize point must lie on the curve.
    assert (PRIZE_Y * PRIZE_Y - PRIZE_X ** 3 - 7) % P == 0

    # Self-test 4: round-trip a small scalar through the prize comparison.
    assert matches_prize(1) is False
    print("btclib self-tests PASS")
    print("prize uncompressed address from embedded pubkey:", b58check(hash160(pk_u)))
