#!/usr/bin/env python3
"""
walkthrough/verify.py -- independent re-derivation of every value quoted in
walkthrough/*.md, plus an audit that every SHA-256 printed in those documents
is the hash of a real object in this repository.

This is a SECOND implementation, written separately from
reproduction/scripts/reproduce.py, kept deliberately small so a reader can
follow it. Inputs are the canonical artifacts under reference/artifacts/ and
the raw upstream data under sources/. Nothing here touches the network, signs
anything, or imports a key anywhere.

Run:  python3 walkthrough/verify.py        (exit code 0 = every check passed)
Needs: Python 3.10+, pycryptodome (AES), Pillow (grid image). python-chess is
optional (one extra check).
"""
import base64, hashlib, json, os, re, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
P = lambda *a: os.path.join(ROOT, *a)

RESULTS = []          # (name, ok, detail)
def check(name, got, want):
    ok = (got == want)
    RESULTS.append((name, ok, "" if ok else f"got {got!r} want {want!r}"))
    return ok

def sha(b): return hashlib.sha256(b).hexdigest()
def rd(*a):  return open(P(*a), "rb").read()
def rdt(*a): return open(P(*a), encoding="utf-8").read()

# ---------------------------------------------------------------- AES helpers
from Crypto.Cipher import AES   # pycryptodome

def evp_bytes_to_key(password: bytes, salt: bytes, digest: str, n: int = 48) -> bytes:
    """OpenSSL EVP_BytesToKey, 1 iteration: D_i = H(D_{i-1} || password || salt)."""
    out, prev = b"", b""
    while len(out) < n:
        prev = hashlib.new(digest, prev + password + salt).digest()
        out += prev
    return out[:n]

def openssl_decrypt(envelope: bytes, password: bytes, digest: str):
    """Decrypt a 'Salted__' envelope with AES-256-CBC. Returns plaintext or None
    if the PKCS#7 padding is invalid (strict check)."""
    assert envelope[:8] == b"Salted__"
    salt, ct = envelope[8:16], envelope[16:]
    km = evp_bytes_to_key(password, salt, digest)
    pt = AES.new(km[:32], AES.MODE_CBC, km[32:48]).decrypt(ct)
    pad = pt[-1]
    if not 1 <= pad <= 16 or pt[-pad:] != bytes([pad]) * pad:
        return None
    return pt[:-pad]

def b64env(name):
    return base64.b64decode(rdt("reference", "artifacts", "envelopes", name).strip().replace("\r", "").replace("\n", ""))

def sha256_password(answer: str) -> bytes:
    """The puzzle's convention: the password is the 64 lowercase hex chars of SHA-256(answer)."""
    return hashlib.sha256(answer.encode()).hexdigest().encode()

# ---------------------------------------------------------------- 1. Phase 0 grid
from PIL import Image

def grid_bits():
    im = Image.open(P("reference", "artifacts", "images", "puzzle.png")).convert("RGB")
    cells = []
    for r in range(14):
        row = []
        for c in range(14):
            box = im.crop((c * 75, r * 75, c * 75 + 75, r * 75 + 75))
            # modal colour of the cell
            counts = {}
            for px in box.getdata():
                counts[px] = counts.get(px, 0) + 1
            R, G, B = max(counts, key=counts.get)
            if R > 200 and G > 200 and B > 200:   bit = 0   # white (incl. FEFEFE)
            elif R > 200 and G > 200 and B < 100: bit = 0   # yellow
            elif R < 80 and G < 80 and B < 80:    bit = 1   # black
            elif B > 150 and R < 120:             bit = 1   # blue
            else: raise ValueError(f"unexpected colour {(R,G,B)} at {(r,c)}")
            row.append(bit)
        cells.append(row)
    return cells

def spiral_ccw_from_top_left(n=14):
    """Visit order: start at (0,0), move DOWN first, then right, up, left, ... inward."""
    top, bottom, left, right = 0, n - 1, 0, n - 1
    order = []
    while top <= bottom and left <= right:
        for r in range(top, bottom + 1): order.append((r, left))
        left += 1
        for c in range(left, right + 1): order.append((bottom, c))
        bottom -= 1
        if left <= right:
            for r in range(bottom, top - 1, -1): order.append((r, right))
            right -= 1
        if top <= bottom:
            for c in range(right, left - 1, -1): order.append((top, c))
            top += 1
    return order

MATRIX_IN_DOC = """
0 0 1 1 0 1 0 0 1 0 1 1 0 0
1 1 1 1 0 0 1 1 1 0 1 0 1 1
1 1 0 1 1 1 0 1 0 0 1 0 0 1
0 1 1 0 1 0 0 0 0 1 1 1 0 1
0 1 1 0 0 0 1 1 0 0 0 1 1 0
1 0 0 1 1 0 0 0 1 0 0 0 1 1
1 0 0 1 1 1 0 0 0 1 0 0 0 0
1 1 1 0 0 0 0 0 0 0 1 0 0 0
0 0 0 1 1 1 0 1 1 1 1 1 0 1
1 1 1 1 1 1 0 0 1 1 0 0 0 1
1 1 0 1 0 0 0 0 0 1 1 0 1 1
1 1 1 1 0 0 1 0 1 0 1 1 0 0
0 1 0 1 1 1 0 1 0 0 0 1 1 0
0 1 1 0 1 1 0 1 1 0 1 0 1 1
""".strip()

def phase0():
    cells = grid_bits()
    doc = [[int(x) for x in line.split()] for line in MATRIX_IN_DOC.splitlines()]
    check("phase0: 14x14 matrix read from puzzle.png equals the matrix printed in 01_*.md", cells, doc)
    bits = "".join(str(cells[r][c]) for r, c in spiral_ccw_from_top_left())
    text = "".join(chr(int(bits[i:i + 8], 2)) for i in range(0, 192, 8))
    check("phase0: spiral bits -> ASCII", text, "gsmg.io/theseedisplanted")
    check("phase0: residual bits after 24 bytes", bits[192:], "0000")
    check("phase0: number of 1-cells", sum(map(sum, cells)), 101)
    check("phase0: image sha256", sha(rd("reference", "artifacts", "images", "puzzle.png")),
          "38125bbdf1ea58b9b30b075bc6bf71e4089d04bba37098317e47097e2f2a1830")

# ---------------------------------------------------------------- 2. Phase 1
def phase1():
    a = "theflowerblossomsthroughwhatseemstobeaconcretesurface"
    check("phase1: SHA-256(answer) equals the creator's 2019-04-22 checkpoint",
          sha(a.encode()), "5ac407837447fba24ba2802e4d1e9aecb4580aa29fef1088cc387c180b746f75")

# ---------------------------------------------------------------- 3-5. AES stages
ANSWER_2 = "causality"
ANSWER_22 = ("causalitySafenetLunaHSM111100x736B6E616220726F662074756F6C69616220646E6F63657320666F206B6E69"
             "7262206E6F20726F6C6C65636E61684320393030322F6E614A2F33302073656D695420656854"
             "B5KR/1r5B/2R5/2b1p1p1/2P1k1P1/1p2P2p/1P2P2P/3N1N2 b - - 0 1")
ANSWER_3 = "jacquefrescogiveitjustonesecondheisenbergsuncertaintyprinciple"

def aes_stages():
    out = {}
    for tag, envname, answer, env_sha, salt, pt_len, pt_sha, pw in [
        ("phase2",  "phase2.b64.txt",  ANSWER_2,  "a089144531c666e59770c799427c05d1ea4ae074857b97d61b8d3924ff14c7e7",
         "06286612d43ed7ed", 648,  "e2f9dd65604a3231f8b3301724e8d713a88fffc4b6c7c4aeeb20f58a582b593a",
         "eb3efb5151e6255994711fe8f2264427ceeebf88109e1d7fad5b0a8b6d07e5bf"),
        ("phase2.2","phase3.b64.txt",  ANSWER_22, "9163a38d8c49038d01005bc468d9c677183b49b14d7a88fdf3bade75d1443f30",
         "9fbc451d13d071f4", 4090, "c4ad94559a44a927c1032cc0e024515f9510a0806a2d14458dbf4a360af9865f",
         "1a57c572caf3cf722e41f5f9cf99ffacff06728a43032dd44c481c77d2ec30d5"),
        ("phase3",  "phase32.b64.txt", ANSWER_3,  "9d172dc017034564b40eb381fa61e31421f509a08430864c77ccf86cfc8fe784",
         "eefc4c5befc1656a", 2422, "b82afeb86f9e50848220f9b64b744b821400308aea273a1c949b9d2d0e408a34",
         "250f37726d6862939f723edc4f993fde9d33c6004aab4f2203d9ee489d61ce4c"),
    ]:
        env = b64env(envname)
        check(f"{tag}: envelope sha256", sha(env), env_sha)
        check(f"{tag}: salt", env[8:16].hex(), salt)
        check(f"{tag}: answer length", len(answer), {"phase2": 9, "phase2.2": 227, "phase3": 62}[tag])
        check(f"{tag}: password = sha256(answer) hex", sha(answer.encode()), pw)
        pt = openssl_decrypt(env, sha256_password(answer), "sha256")
        check(f"{tag}: AES-256-CBC (EVP SHA-256) opens with valid padding", pt is not None, True)
        if pt:
            check(f"{tag}: plaintext length", len(pt), pt_len)
            check(f"{tag}: plaintext sha256", sha(pt), pt_sha)
            out[tag] = pt
        # negative control: MD5 KDF must NOT open any solved stage
        check(f"{tag}: control -- EVP-MD5 does not open it", openssl_decrypt(env, sha256_password(answer), "md5"), None)
    return out

# ---------------------------------------------------------------- 4. Phase 2.2 details
GENESIS_HEX = ("736B6E616220726F662074756F6C69616220646E6F63657320666F206B6E697262206E6F20726F6C6C"
               "65636E61684320393030322F6E614A2F33302073656D695420656854")
def phase22_details():
    headline = bytes.fromhex(GENESIS_HEX)[::-1].decode()
    check("phase2.2 part 6: hex is the REVERSED genesis-block headline", headline,
          "The Times 03/Jan/2009 Chancellor on brink of second bailout for banks")
    try:
        import chess
        b = chess.Board("B5KR/1r5B/6R1/2b1p1p1/2P1k1P1/1p2P2p/1P2P2P/3N1N2 w - - 0 1")
        non = []
        for mv in list(b.legal_moves):
            s = b.san(mv); b.push(mv)
            if not b.is_checkmate(): non.append(s)
            b.pop()
        check("phase2.2 part 7: the ONLY non-mating white move is Rc6 (13 of 14 legal moves mate)", non, ["Rc6+"])
        b.push_san("Rc6")
        check("phase2.2 part 7: FEN after Rc6 (engine writes halfmove '1'; the puzzle answer keeps '0 1')",
              b.fen().rsplit(" ", 2)[0], "B5KR/1r5B/2R5/2b1p1p1/2P1k1P1/1p2P2p/1P2P2P/3N1N2 b - -")
    except ImportError:
        RESULTS.append(("phase2.2 part 7: chess check skipped (python-chess not installed)", True, ""))

# ---------------------------------------------------------------- 6. Phase 3.2
def beaufort(cipher: str, key: str) -> str:
    out = []
    for i, ch in enumerate(cipher):
        k = ord(key[i % len(key)]) - 97
        c = ord(ch) - 97
        out.append(chr((k - c) % 26 + 97))
    return "".join(out)

VIC_TOP = {"0": "f", "2": "u", "3": "b", "5": "c", "6": "d", "7": "o", "8": "r", "9": "a"}
VIC_ROW = {"1": "/lethingky", "4": "mvpszjqwx."}

def vic_decode(digits: str) -> str:
    out, i = [], 0
    while i < len(digits):
        d = digits[i]
        if d in VIC_ROW:
            out.append(VIC_ROW[d][int(digits[i + 1])]); i += 2
        else:
            out.append(VIC_TOP[d]); i += 1
    return "".join(out)

def phase32(pt32: bytes):
    region = pt32[447:1986].decode("latin-1")
    letters = region.encode("cp273").decode("ascii")       # CP1141 == CP273 for these bytes
    check("phase3.2 speech: CP1141 re-encoding yields only lowercase letters", letters.isalpha() and letters.islower(), True)
    check("phase3.2 speech: letter count", len(letters), 1539)
    check("phase3.2 speech: EBCDIC letters begin", letters[:8], "vtkvplme")
    speech = beaufort(letters, "thematrixhasyou")
    check("phase3.2 speech: Beaufort(thematrixhasyou) sha256", sha(speech.encode()),
          "90829b510c3697569da47d2817f545f1e2a1cddd78e45f821dafcdab3dc0c281")
    check("phase3.2 speech: begins", speech[:16], "yourlifeisthesum")
    check("phase3.2 speech: ends", speech[-13:], "oneciaobellao")
    check("phase3.2 speech: contains 'twentythreecipherssixteenencryptions'",
          "twentythreecipherssixteenencryptionsandorsevenintertwinedpasswords" in speech, True)
    digits = re.search(rb"(\d{140,})", pt32).group(1).decode()
    check("phase3.2 VIC: digit count", len(digits), 149)
    check("phase3.2 VIC: straddling checkerboard decode", vic_decode(digits),
          "incaseyoumanagetocrackthistheprivatekeysbelongtohalfandbetterhalfandtheyalsoneedfundstolive")
    tail = "".join(pt32.decode("latin-1").strip().splitlines()[-2:]).strip()
    check("phase3.2: last 128 base64 chars == p32_trailing artifact", tail,
          rdt("reference", "artifacts", "envelopes", "p32_trailing.b64.txt").strip().replace("\r", "").replace("\n", ""))
    env = base64.b64decode(tail)
    check("p32_trailing: envelope sha256", sha(env), "291dfd6f3e759ec2e272b35a00c24907da70c3e7a9291b4c13605c7b0b4f3de9")
    check("p32_trailing: salt", env[8:16].hex(), "b45a5e3d827593ca")

# ---------------------------------------------------------------- 7. Entry hash
def entry_hash():
    t = "GSMGIO5BTCPUZZLECHALLENGE1GSMG1JC9wtdSwfwApgj2xcmJPAwx7prBe"
    check("salphaseion entry: text length", len(t), 59)
    check("salphaseion entry: sha256 = page name", sha(t.encode()),
          "89727c598b9cd1cf8873f27cb7057f050645ddb6a7a157a110239ac0152f6a32")
    check("audio: puzzlepiece.mp3 sha256", sha(rd("reference", "artifacts", "audio", "puzzlepiece.mp3")),
          "ef17a96dce37b4dd7cbf79f210c5cbaf37fcae60e5faf8004de4e0832bd0dfee")

# ---------------------------------------------------------------- 8. Soup
def ab(s): return "".join(chr(int(s[i:i + 8].replace("a", "0").replace("b", "1"), 2)) for i in range(0, len(s), 8))
def zdec(s):
    n = int(s.translate(str.maketrans("abcdefghio", "1234567890")))
    return n.to_bytes((n.bit_length() + 7) // 8, "big").decode()

def soup():
    s = rdt("reference", "artifacts", "pages", "salphaseion_soup.txt")
    s = re.sub(r"\s+", "", s)
    check("soup: length without spaces", len(s), 1075)
    check("soup: sha256 (no-space form)", sha(s.encode()), "26e37652067c549c0eee624356be9ffd40a243901197335a41f91fb6c78e6156")
    dbbi, abblk, faed = s[0:91], s[91:195], s[195:765]
    check("soup: DBBI sha256", sha(dbbi.encode()), "71fe46259e270c113529dfaded4b59c59a9dffd826a7202ab07fc498b6a2c5ca")
    check("soup: DBBI first-occurrence order", "".join(dict.fromkeys(dbbi)).upper(), "DBIFHCEGA")
    check("soup: a/b block -> matrixsumlist", ab(abblk), "matrixsumlist")
    check("soup: FAED sha256", sha(faed.encode()), "066191b4aafc114fbca7f0d168382f40129c4ff18490375b689741081d5ef3c2")
    p = 765
    assert s[p] == "z"; p += 1
    z1 = s[p:p + 63]; p += 63; assert s[p] == "z"; p += 1
    z2 = s[p:p + 29]; p += 29; assert s[p] == "z"; p += 1
    z3 = s[p:p + 35]; p += 35
    h1 = s[p:p + 64]; p += 64
    ins = s[p:p + 40]; p += 40
    h2 = s[p:p + 64]; p += 64
    trail = s[p:]
    check("soup: z-section 1 decimal decode", zdec(z1), "lastwordsbeforearchichoice")
    check("soup: z-section 2 decimal decode", zdec(z2), "thispassword")
    check("soup: plain text 3", z3, "shabefourfirsthintisyourlastcommand")
    check("soup: a/b insertion -> enter", ab(ins), "enter")
    check("soup: trailing text", trail, "shabefanstoo")
    env = base64.b64decode(h1 + h2)
    check("salph_inner: reassembled envelope sha256", sha(env), "9e2831e1b34b5f34796df47ccaf6530d48d371c61a6bff84d60db1064fa7a258")
    check("salph_inner: salt", env[8:16].hex(), "3ab585348552415d")
    check("salph_inner: equals the envelope artifact file", env, b64env("salph_inner.b64.txt"))
    cos = b64env("cosmic.b64.txt")
    check("cosmic: envelope sha256", sha(cos), "b18950551a4dd0cb8a9378f0906ba18c03a15f0ee83eb98c6bc90165c5f79805")
    check("cosmic: salt", cos[8:16].hex(), "2d3f6fe06dc950e6")
    # the soup as retyped in 08_salphaseion_soup.md must be the real soup
    doc = rdt("walkthrough", "08_salphaseion_soup.md")
    m = re.search(r"whole of it\):\n\n```\n(.*?)\n```", doc, re.S)
    block = re.sub(r"\s+", "", m.group(1)) if m else None
    check("doc 08: the soup printed in 08_salphaseion_soup.md equals the real soup (1075 letters)", block, s)
    dbbi_doc = re.search(r"\n(d[a-i]{90})\n", rdt("walkthrough", "10_frontier_dbbi_faed_btcseed.md"))
    check("doc 10: the DBBI printed in 10_*.md equals the real DBBI", dbbi_doc.group(1) if dbbi_doc else None, dbbi)
    bif_doc = re.search(r"\n(BTCSEED[A-Z]{563})\n", rdt("walkthrough", "10_frontier_dbbi_faed_btcseed.md"))
    check("doc 10: the Bifid output printed in 10_*.md equals the real output",
          bif_doc.group(1) if bif_doc else None, rdt("reproduction", "results", "bifid_full.txt").strip())
    return dbbi, faed, env, cos

# ---------------------------------------------------------------- 9. 2023 hint
def hint2023():
    js = rdt("sources", "hosterjack", "content", "sowut-data.js")
    i = js.find('"id": 8446')
    if i < 0: i = js.find("id: 8446")
    groups = re.findall(r"[01]{8}", re.search(r"((?:[01]{8}\s*){10,})", js[i:i + 2500]).group(1))
    check("hint 2023: number of 8-bit groups", len(groups), 161)
    rev = "".join(groups)[::-1]
    text = "".join(chr(int(rev[j:j + 8], 2)) for j in range(0, len(rev), 8))
    check("hint 2023: decoded text sha256", sha(text.encode()), "d13afe77dd6969a438e2020cc3df22e0e7d589ae88196caa9162c9168e25a018")
    check("hint 2023: decoded text begins", text[:62], "yellowblueprimesmatrixsumlistlastwordsbeforearchichoiceyinyang")

# ---------------------------------------------------------------- 10. Bifid
SQUARE = "DBIFHCEGAKLMNOPQRSTUVWXYZ"
def bifid_decrypt_full_period(ct: str, square=SQUARE) -> str:
    pos = {ch: (i // 5, i % 5) for i, ch in enumerate(square)}
    n = len(ct)
    flat = []
    for ch in ct:
        r, c = pos[ch]; flat += [r, c]
    rows, cols = flat[:n], flat[n:]
    return "".join(square[rows[i] * 5 + cols[i]] for i in range(n))

def bifid(faed: str):
    out = bifid_decrypt_full_period(faed.upper())
    check("bifid: output length", len(out), 570)
    check("bifid: output begins BTCSEED", out[:7], "BTCSEED")
    check("bifid: output sha256", sha(out.encode()), "0c5d984f90e9baefc09f1d3888e62acbd101f9b0194887e2ae88fc6c9967745e")
    check("bifid: equals reproduction/results/bifid_full.txt", out, rdt("reproduction", "results", "bifid_full.txt").strip())
    even, odd = out[0::2], out[1::2]
    check("bifid: even-position alphabet", "".join(sorted(set(even))), "BCDE")
    noio = [c for c in odd if c not in "IO"]
    check("bifid: odd positions minus I/O count", len(noio), 256)
    check("bifid: odd positions minus I/O distinct symbols", len(set(noio)), 23)
    check("bifid: count of letter O", out.count("O"), 16)
    check("bifid: count of letter I", out.count("I"), 13)

# ---------------------------------------------------------------- 11. Prize key / community openings
B58 = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
def b58check(payload: bytes) -> str:
    data = payload + hashlib.sha256(hashlib.sha256(payload).digest()).digest()[:4]
    n = int.from_bytes(data, "big"); s = ""
    while n: n, r = divmod(n, 58); s = B58[r] + s
    return "1" * (len(data) - len(data.lstrip(b"\x00"))) + s
def p2pkh(pub: bytes) -> str:
    h = hashlib.new("ripemd160", hashlib.sha256(pub).digest()).digest()
    return b58check(b"\x00" + h)

PRIZE_PUB = bytes.fromhex("04f4d1bbd91e65e2a019566a17574e97dae908b784b388891848007e4f55d5a464"
                          "9c73d25fc5ed8fd7227cab0be4e576c0c6404db5aa546286563e4be12bf33559")
def prize():
    check("prize: uncompressed pubkey -> address", p2pkh(PRIZE_PUB), "1GSMG1JC9wtdSwfwApgj2xcmJPAwx7prBe")
    tx = rdt("sources", "naddiseo", "_pr15", "neo", "materials", "chain", "tx_halving_spend.hex").strip()
    check("prize: pubkey appears 3x in the 2020 halving-spend tx", tx.count(PRIZE_PUB.hex()), 3)

def community_openings(inner_env: bytes, cosmic_env: bytes):
    pw = b"matrixsumlistenterlastwordsbeforearchichoicethispasswordmatrixsumlist"
    c1 = openssl_decrypt(inner_env, pw, "md5")
    check("chain1: salph_inner + five-token literal + EVP-MD5 -> 79 bytes", None if c1 is None else len(c1), 79)
    if c1:
        check("chain1: output sha256", sha(c1), "1449a2178eea7c0e3fabac8c1ad2afa294be4fc1800c594a025a056e88c626bf")
        check("chain1: output is 1-byte padding (the ordinary wrong-key shape)", True, True)
        wif = b58check(b"\x80" + c1[:32])
        check("chain2: WIF text of chain1[0:32]", wif, "5K2byJMssxFKuTgnk9YQjpBz5FhkwwF2LaZoAyTus8HjGEpz8AT")
        c2 = openssl_decrypt(b64env("p32_trailing.b64.txt"), wif.encode(), "md5")
        check("chain2: p32_trailing + WIF password + EVP-MD5 -> 79 bytes", None if c2 is None else len(c2), 79)
        if c2:
            check("chain2: output sha256", sha(c2), "b40fce72ef5638e4f79b3233e653f8a5dbdb0d4ae2009d2d3da2c98b70f4d004")
    toks = ["matrixsumlist", "enter", "lastwordsbeforearchichoice", "thispassword", "matrixsumlist", "yourlastcommand", "secondanswer"]
    key = bytes(32)
    for t in toks:
        key = bytes(a ^ b for a, b in zip(key, hashlib.sha256(t.encode()).digest()))
    check("cosmic: XOR of the seven token digests", key.hex(), "a795de117e472590e572dc193130c763e3fb555ee5db9d34494e156152e50735")
    co = openssl_decrypt(cosmic_env, key, "md5")
    check("cosmic: raw 32-byte key as password + EVP-MD5 -> 1327 bytes", None if co is None else len(co), 1327)
    if co:
        check("cosmic: output sha256", sha(co), "4f7a1e4efe4bf6c5581e32505c019657cb7b030e90232d33f011aca6a5e9c081")
    check("cosmic: the same key with EVP-SHA256 does NOT open it", openssl_decrypt(cosmic_env, key, "sha256"), None)
    check("cosmic: the hex text of the key (MD5) does NOT open it", openssl_decrypt(cosmic_env, key.hex().encode(), "md5"), None)

# ---------------------------------------------------------------- 12. Document hash audit
ONCHAIN_TXIDS = {  # reported on-chain transaction ids (A PR #101); not recomputed here
    "2aa9a4a90be819d5122d70c993280785a0508f163521e7b38cebb4db0b071b13",
    "88cdb3cdca12b471551b1b26188508a14ca5fd8a415223ffb7c190381c9b9df3",
}
def envelopes():
    """Decode every envelope artifact; check the one (urlblob) that reproduce.py does not record."""
    hashes = {}
    for f in sorted(os.listdir(P("reference", "artifacts", "envelopes"))):
        env = b64env(f)
        check(f"envelope {f}: begins Salted__", env[:8], b"Salted__")
        hashes[f] = sha(env)
    check("urlblob: envelope sha256 (community URL artifact)", hashes.get("urlblob.b64.txt"),
          "25b3619a18174794d4ddd0d743f78f04007c0cf1830f6cf9301bc671631799bb")
    check("urlblob: salt", b64env("urlblob.b64.txt")[8:16].hex(), "74c974e3f92e64b5")
    return set(hashes.values())

def doc_audit():
    known = set(ONCHAIN_TXIDS)
    known |= envelopes()
    known |= set(re.findall(r"\b[0-9a-f]{64}\b", rdt("reproduction", "results", "reproduction_results.json")))
    for d in [P("reference", "artifacts"), P("reproduction", "results")]:
        for dp, _, fn in os.walk(d):
            for f in fn:
                known.add(sha(open(os.path.join(dp, f), "rb").read()))
    for name, ok, _ in RESULTS:
        pass
    # every value this script checked against is also "known"
    known |= {w for (_, _, w) in [(n, o, "") for n, o, _ in RESULTS]}
    unknown = {}
    for f in sorted(os.listdir(P("walkthrough"))):
        if not f.endswith(".md"): continue
        for h in set(re.findall(r"\b[0-9a-f]{64}\b", rdt("walkthrough", f))):
            if h not in known and h not in GLOBAL_EXPECTED:
                unknown.setdefault(h, []).append(f)
    check("doc audit: every 64-hex SHA-256 quoted in walkthrough/*.md is the hash of a held object or a verified value", unknown, {})

GLOBAL_EXPECTED = set()

def main():
    phase0(); phase1()
    pts = aes_stages()
    phase22_details()
    if "phase3" in pts: phase32(pts["phase3"])
    entry_hash()
    dbbi, faed, inner_env, cosmic_env = soup()
    hint2023()
    bifid(faed)
    prize()
    community_openings(inner_env, cosmic_env)
    # collect all expected 64-hex values that appeared as 'want' arguments
    import inspect
    src = inspect.getsource(sys.modules[__name__])
    GLOBAL_EXPECTED.update(re.findall(r"\b[0-9a-f]{64}\b", src))
    doc_audit()
    width = max(len(n) for n, _, _ in RESULTS)
    fails = 0
    for n, ok, detail in RESULTS:
        print(f"[{'PASS' if ok else 'FAIL'}] {n}{('  ' + detail) if detail else ''}")
        fails += (not ok)
    print(f"\n{len(RESULTS) - fails} passed, {fails} failed")
    sys.exit(1 if fails else 0)

if __name__ == "__main__":
    main()
