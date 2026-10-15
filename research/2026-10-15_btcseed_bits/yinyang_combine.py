"""
"Yin yang" read as COMBINING the two interleaved period-2 streams (not reading
one). For each position i, even[i] in {B,C,D,E} (2 bits) and odd[i] (a letter)
are merged, then reduced to a 256-bit scalar. Exact offline prize oracle.
"""
import json
from btclib import scalar_mul, PRIZE_PT, N, point_to_address, PRIZE_ADDR

S = open('../../reproduction/results/bifid_full.txt').read().strip()
SQUARE = "DBIFHCEGAKLMNOPQRSTUVWXYZ"
POS = {c: i for i, c in enumerate(SQUARE)}
ROW = {c: POS[c] // 5 for c in SQUARE}
COL = {c: POS[c] % 5 for c in SQUARE}
EVEN2 = {"D": 0, "B": 1, "C": 2, "E": 3}      # square 2x2 (row,col) 2-bit

results, HITS, CANDS = [], [], {}
WATCH = {PRIZE_ADDR: "prize"}

def reg(name, k):
    if not k:
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

def bint(bits):
    v = 0
    for b in bits:
        v = (v << 1) | (b & 1)
    return v

for vname in ("fwd", "rev"):
    even = S[0::2] if vname == "fwd" else S[0::2][::-1]
    odd = S[1::2] if vname == "fwd" else S[1::2][::-1]

    # (1) parallel bit XOR: even-rowbit XOR odd-classifier-bit, drop IO -> bits
    for oddbitname, ofn in [("rows01", lambda c: 0 if ROW[c] <= 1 else 1),
                            ("rowpar", lambda c: ROW[c] & 1),
                            ("alpha_hi", lambda c: 1 if c >= 'N' else 0)]:
        for evbitname, efn in [("evrow", lambda c: ROW[c]), ("evcol", lambda c: COL[c])]:
            bits = [efn(even[i]) ^ ofn(odd[i]) for i in range(len(odd)) if odd[i] not in "IO"]
            reg(f"YY.xor.{evbitname}^{oddbitname}.{vname}.msb", bint(bits))
            reg(f"YY.xor.{evbitname}^{oddbitname}.{vname}.lsb", bint(bits[::-1]))

    # (2) packed byte: (even 2 bits << 6) | (odd sqidx & 0x3F); drop IO; first 32 bytes
    packed = []
    for i in range(len(odd)):
        if odd[i] in "IO":
            continue
        packed.append(((EVEN2[even[i]] & 3) << 6) | (POS[odd[i]] & 0x3F))
    reg(f"YY.pack.e2_o6.{vname}.first32", int.from_bytes(bytes(packed[:32]), 'big'))
    reg(f"YY.pack.e2_o6.{vname}.last32", int.from_bytes(bytes(packed[-32:]), 'big'))

    # (3) sum pair values mod 26 -> letter stream -> sha256 as scalar (brain-wallet-ish)
    import hashlib
    merged = ''.join(chr(((EVEN2[even[i]] + POS[odd[i]]) % 26) + 97)
                     for i in range(len(odd)) if odd[i] not in "IO")
    reg(f"YY.summerge.sha256.{vname}",
        int.from_bytes(hashlib.sha256(merged.encode()).digest(), 'big'))

print(json.dumps({"tested": len(results), "hits": HITS}, indent=2))
json.dump(results, open("results_yinyang_combine.json", "w"), indent=0)
json.dump({k: hex(v) for k, v in CANDS.items()},
          open("candidates_yinyang_combine.json", "w"), indent=0)
print("EXACT/watched hits:", len(HITS))
