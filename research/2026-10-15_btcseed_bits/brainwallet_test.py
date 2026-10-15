"""
Brain-wallet hypothesis: the decoded puzzle text is a PASSPHRASE whose hash is
the private scalar (classic single-key brain wallet). Strongly motivated:
  - every solved AES stage used SHA-256(answer) as the secret;
  - the prize public key is UNCOMPRESSED (classic brain-wallet / Core era);
  - creator: target is a "Regular Bitcoin Private key"; "its in front of your
    eyes but you're not seeing it".

For each candidate passphrase we test, as the private scalar:
  sha256(p), sha256(sha256(p)), sha256(hex_of_sha256(p)) [the puzzle's own
  double-hashing idiom], and the raw utf-8 bytes right-padded/truncated to 32.
Each scalar -> public point, compared EXACTLY to the prize point (offline).

Passphrase set = the decoded strings themselves and their obvious normalisations
(the exact Bifid output, with/without the BTCSEED head, case variants, the two
period-2 streams, the raw FAED/DBBI letters, and the literal label words). This
is the "exact decoded-string" coverage the archive says prior brain-wallet
sweeps (vocabulary-only) did not do.
"""
import hashlib, json
from btclib import scalar_mul, PRIZE_PT, N, point_to_address, PRIZE_ADDR

BIFID = open('../../reproduction/results/bifid_full.txt').read().strip()
DBBI = open('../../reproduction/results/dbbi.txt').read().strip()
FAED = open('../../reproduction/results/faed.txt').read().strip()

even = BIFID[0::2]
odd = BIFID[1::2]
odd_noio = ''.join(c for c in odd if c not in "IO")
body = BIFID[7:]                      # output after the "BTCSEED" head

# candidate passphrases (name -> string)
PHRASES = {
    "bifid_full": BIFID,
    "bifid_full_lower": BIFID.lower(),
    "bifid_body": body,
    "bifid_body_lower": body.lower(),
    "bifid_even": even,
    "bifid_odd": odd,
    "bifid_odd_noio": odd_noio,
    "bifid_even_lower": even.lower(),
    "btcseed_word": "BTCSEED",
    "btcseed_lower": "btcseed",
    "faed_raw": FAED,
    "dbbi_raw": DBBI,
    "dbbi_faed": DBBI + FAED,
    # literal 2023-hint labels, joined and separate
    "labels_concat": "yellowblueprimesmatrixsumlistlastwordsbeforearchichoiceyinyang",
    "yinyang": "yinyang",
    "yingyang": "yingyang",
}

results = []
HITS = []
WATCH = {PRIZE_ADDR: "prize",
         "1MixpoELBvfkFSRUQtDCGXbdG53cjqknZT": "chain2_K_S1",
         "176ysPe7FdevdQjZWaFCK2nnVbzX9Tgydy": "chain2_K_S2"}


CANDS = {}
def test(name, k):
    k %= N
    if k == 0:
        return
    CANDS[name] = k
    pt = scalar_mul(k)
    if pt is None:
        return
    ac, au = point_to_address(pt, True), point_to_address(pt, False)
    exact = pt == PRIZE_PT
    w = WATCH.get(ac) or WATCH.get(au)
    rec = {"name": name, "addr_c": ac, "addr_u": au, "exact": exact, "watch": w}
    results.append(rec)
    if exact or w:
        rec["k_hex"] = hex(k); HITS.append(rec)


for pname, p in PHRASES.items():
    pb = p.encode()
    h = hashlib.sha256(pb).digest()
    test(f"{pname}|sha256", int.from_bytes(h, 'big'))
    test(f"{pname}|dsha256", int.from_bytes(hashlib.sha256(h).digest(), 'big'))
    # puzzle idiom: sha256 of the lowercase-hex of sha256
    hexlow = hashlib.sha256(pb).hexdigest().encode()
    test(f"{pname}|sha256_of_hexdigest",
         int.from_bytes(hashlib.sha256(hexlow).digest(), 'big'))
    # raw bytes as scalar (pad/truncate to 32)
    raw = pb[:32].rjust(32, b'\x00')
    test(f"{pname}|raw32", int.from_bytes(raw, 'big'))

print(json.dumps({"tested": len(results), "hits": HITS}, indent=2))
json.dump(results, open("results_brainwallet.json", "w"), indent=0)
json.dump({k: hex(v) for k, v in CANDS.items()},
          open("candidates_brainwallet.json", "w"), indent=0)
print("EXACT/watched hits:", len(HITS))
