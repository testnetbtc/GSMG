"""
Vanity-grind hypothesis (offline, decisive).

Rumour the user raised: the puzzle yields a "seed start point" k0 and the real
key is produced by GRINDING the address forward to a vanity prefix. The prize
address 1GSMG... is itself a vanity ("GSMG"). If true, prize_key = k0 + m for a
small m (the grind distance), or k0 = prize_key + m.

We do NOT grind forward (we don't have the key). Instead, for each candidate
seed k0 we solve a bounded discrete log with Baby-Step/Giant-Step:

    P = prize public point.   Want m with  m*G = P - k0*G   (prize = k0 + m),
    and also with            m*G = k0*G - P   (prize = k0 - m).

m is found iff |prize_key - k0| < BOUND. The baby table (j*G) is shared across
all candidates, so this scans every candidate cheaply. A hit prints the exact
offset; otherwise the vanity-from-this-seed hypothesis is rejected up to BOUND.

Grind-distance intuition: a 4-significant-char base58 vanity ("GSMG") is ~1e7
tries; 5 chars ~6e8. BOUND defaults to 2^30 (~1.07e9), covering both.
"""
import json, glob, math, sys
from btclib import P as FP, N, G, scalar_mul, PRIZE_PT

BOUND = 1 << 30
M = 1 + int(math.isqrt(BOUND))          # giant-step stride

# ---- affine point ops (secp256k1, a=0) ----
def neg(Pt):
    return None if Pt is None else (Pt[0], (FP - Pt[1]) % FP)

def add(Pa, Pb):
    if Pa is None: return Pb
    if Pb is None: return Pa
    x1, y1 = Pa; x2, y2 = Pb
    if x1 == x2:
        if (y1 + y2) % FP == 0:
            return None
        s = (3 * x1 * x1) * pow(2 * y1, FP - 2, FP) % FP
    else:
        s = (y2 - y1) * pow(x2 - x1, FP - 2, FP) % FP
    x3 = (s * s - x1 - x2) % FP
    y3 = (s * (x1 - x3) - y1) % FP
    return (x3, y3)

def load_candidates():
    cands = {}
    for f in glob.glob("candidates_*.json"):
        for name, kh in json.load(open(f)).items():
            cands[name] = int(kh, 16) % N
    return cands

def main():
    cands = load_candidates()
    print(f"candidates: {len(cands)}   BOUND=2^{BOUND.bit_length()-1}  M={M}")

    # baby table: {point(j*G): j} for j in [0, M)
    print("building baby table...", flush=True)
    baby = {}
    cur = None                     # 0*G = infinity
    for j in range(M):
        baby[cur] = j
        cur = add(cur, G)
    giant = scalar_mul((M * (N - 1)) % N)      # -M*G  (step for subtracting M*G)
    print(f"baby table: {len(baby)} points", flush=True)

    hits = []
    for idx, (name, k0) in enumerate(cands.items()):
        k0G = scalar_mul(k0)
        for direction, R0 in (("plus", add(PRIZE_PT, neg(k0G))),   # prize = k0 + m
                              ("minus", add(k0G, neg(PRIZE_PT)))):  # prize = k0 - m
            R = R0
            for i in range(M):
                if R in baby:
                    j = baby[R]
                    m = i * M + j
                    k_prize = (k0 + m) % N if direction == "plus" else (k0 - m) % N
                    hit = {"seed": name, "direction": direction, "offset": m,
                           "k_prize_hex": hex(k_prize)}
                    # verify
                    hit["verified"] = scalar_mul(k_prize) == PRIZE_PT
                    hits.append(hit)
                    print("HIT:", json.dumps(hit), flush=True)
                    break
                R = add(R, giant)
        if (idx + 1) % 100 == 0:
            print(f"  scanned {idx+1}/{len(cands)}", flush=True)

    json.dump(hits, open("results_bsgs_vanity.json", "w"), indent=2)
    print(f"\nDONE. seeds scanned: {len(cands)}, offset hits: {len(hits)}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        BOUND = 1 << int(sys.argv[1]); M = 1 + int(math.isqrt(BOUND))
    main()
