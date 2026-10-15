"""
"matrixsumlist" as a LITERAL operation on the BTCSEED output's 256-structure.

Rationale:
  - "matrixsumlist" is a creator-attributed 2023 label; the community reading of
    it is "row sums then column sums of a matrix" (it was applied to the Phase-0
    grid). Here we apply the same operation to the next object that is actually a
    perfect square: the odd stream minus I/O is 256 = 16x16.
  - 16 row sums + 16 column sums = 32 numbers. Taken mod 256 that is exactly 32
    bytes = a 256-bit scalar = "a regular Bitcoin private key".
  - "yin yang" = the matrix read as a 2-colour (duality) grid is also tried.

Value maps for a letter: square index (0..24), A=0..Z=25, row, col.
Fills: row-major / column-major. Orders: rows+cols / cols+rows.
Also: sums concatenated as decimal digits -> big number mod N (the community's
"list" was a digit concatenation).

Exact offline prize-point oracle; no sweep, no network.
"""
import json, itertools
from btclib import scalar_mul, PRIZE_PT, N, point_to_address, PRIZE_ADDR

S = open('../../reproduction/results/bifid_full.txt').read().strip()
SQUARE = "DBIFHCEGAKLMNOPQRSTUVWXYZ"
POS = {c: i for i, c in enumerate(SQUARE)}
VALMAPS = {
    "sqidx": lambda c: POS[c],
    "alpha": lambda c: ord(c) - ord('A'),
    "row": lambda c: POS[c] // 5,
    "col": lambda c: POS[c] % 5,
    "alpha1": lambda c: ord(c) - ord('A') + 1,
}
WATCH = {PRIZE_ADDR: "prize"}
results, HITS, CANDS = [], [], {}


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


def bytes_to_scalar(bts):
    return int.from_bytes(bytes(bts), 'big')


for vname, s in {"fwd": S, "rev": S[::-1]}.items():
    odd = s[1::2] if vname == "fwd" else S[1::2][::-1]
    odd_noio = ''.join(c for c in odd if c not in "IO")
    assert len(odd_noio) == 256
    for mapn, mp in VALMAPS.items():
        vals = [mp(c) for c in odd_noio]
        for fill in ("rowmajor", "colmajor"):
            # build 16x16
            M = [[0] * 16 for _ in range(16)]
            for idx, v in enumerate(vals):
                r, c = (idx // 16, idx % 16) if fill == "rowmajor" else (idx % 16, idx // 16)
                M[r][c] = v
            rowsums = [sum(M[r]) for r in range(16)]
            colsums = [sum(M[r][c] for r in range(16)) for c in range(16)]
            # (a) 32 bytes = rowsums mod256 ++ colsums mod256 (and swapped)
            reg(f"msl.{vname}.{mapn}.{fill}.rows+cols.mod256",
                bytes_to_scalar([x % 256 for x in rowsums] + [x % 256 for x in colsums]))
            reg(f"msl.{vname}.{mapn}.{fill}.cols+rows.mod256",
                bytes_to_scalar([x % 256 for x in colsums] + [x % 256 for x in rowsums]))
            # (b) digit-concatenation of the sums, as a big number mod N
            digs_rc = ''.join(str(x) for x in rowsums + colsums)
            digs_cr = ''.join(str(x) for x in colsums + rowsums)
            reg(f"msl.{vname}.{mapn}.{fill}.rows+cols.decimal", int(digs_rc) % N)
            reg(f"msl.{vname}.{mapn}.{fill}.cols+rows.decimal", int(digs_cr) % N)

print(json.dumps({"tested": len(results), "hits": HITS}, indent=2))
json.dump(results, open("results_matrixsumlist.json", "w"), indent=0)
json.dump({k: hex(v) for k, v in CANDS.items()},
          open("candidates_matrixsumlist.json", "w"), indent=0)
print("EXACT/watched hits:", len(HITS))
