"""
Extra clue-driven key extractions from the BTCSEED output's 256-symbol payload
(odd stream minus I/O = 256 letters over 23 distinct symbols). Complements
decode_btcseed.py. Exact offline prize oracle.

Readings added here:
  - base-23 number over a canonical 23-symbol ranking (several rankings) mod N;
  - 5-bit square-index concatenation (256 x 5 = 1280 bits) -> mod N / first256 /
    last256;
  - the 23-symbol frequency rank of each letter as a digit (base 23);
  - "reinsert O as 0": map the 256 payload letters to base-23 digits by square
    rank, treat as a positional number, mod N.
Also appends candidates to candidates_extra.json for the vanity BSGS pass.
"""
import json, itertools
from btclib import scalar_mul, PRIZE_PT, N, point_to_address, PRIZE_ADDR
from collections import Counter

S = open('../../reproduction/results/bifid_full.txt').read().strip()
SQUARE = "DBIFHCEGAKLMNOPQRSTUVWXYZ"
POS = {c: i for i, c in enumerate(SQUARE)}
results, HITS, CANDS = [], [], {}
WATCH = {PRIZE_ADDR: "prize"}


def reg(name, k):
    if k is None:
        return
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


def bits_to_int(bits):
    v = 0
    for b in bits:
        v = (v << 1) | (b & 1)
    return v


for vname, s in {"fwd": S, "rev": S[::-1]}.items():
    odd = s[1::2] if vname == "fwd" else S[1::2][::-1]
    payload = ''.join(c for c in odd if c not in "IO")        # 256 letters
    assert len(payload) == 256

    # canonical 23-symbol rankings
    alpha23 = ''.join(sorted(set(payload)))                   # alphabetical
    sq23 = ''.join(c for c in SQUARE if c in set(payload))    # square order
    freq = Counter(payload)
    freq23 = ''.join(c for c, _ in sorted(freq.items(), key=lambda kv: (-kv[1], kv[0])))
    for rname, ranking in [("alpha", alpha23), ("square", sq23), ("freq", freq23)]:
        rank = {c: i for i, c in enumerate(ranking)}
        v = 0
        for c in payload:
            v = v * 23 + rank[c]
        reg(f"X.base23.{rname}.{vname}", v % N)

    # 5-bit square-index concatenation
    bits = []
    for c in payload:
        idx = POS[c]
        bits += [(idx >> b) & 1 for b in (4, 3, 2, 1, 0)]     # 5 bits MSB-first
    reg(f"X.5bit_sqidx.{vname}.modN", bits_to_int(bits) % N)
    reg(f"X.5bit_sqidx.{vname}.first256", bits_to_int(bits[:256]))
    reg(f"X.5bit_sqidx.{vname}.last256", bits_to_int(bits[-256:]))

    # even stream too: 285 letters {B,C,D,E} as base-4 over square-rank, mod N
    even = s[0::2] if vname == "fwd" else S[0::2][::-1]

print(json.dumps({"tested": len(results), "hits": HITS}, indent=2))
json.dump(results, open("results_extra.json", "w"), indent=0)
json.dump({k: hex(v) for k, v in CANDS.items()},
          open("candidates_extra.json", "w"), indent=0)
print("EXACT/watched hits:", len(HITS))
