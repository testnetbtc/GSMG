"""
Fast Baby-Step/Giant-Step bounded discrete-log for the vanity-grind hypothesis.

For each candidate seed k0, test whether the prize key = k0 +/- m for some
m < BOUND (the grind distance to the "1GSMG" vanity prefix). Fully offline:
we only ever compare points derived from k0 against the public prize point.

Speed: the giant-step walk stays in JACOBIAN coordinates (constant affine step,
no per-step modular inverse); one Montgomery batch inversion per candidate+
direction converts the whole walk to affine for table lookup. ~100x faster than
affine-per-step, so BOUND can be large.

Progress is written to bsgs_progress.txt (flushed) for live monitoring.
Usage: python3 bsgs_fast.py [log2_bound]   (default 28)
"""
import json, glob, math, sys, time
from btclib import P as FP, N, G, scalar_mul, PRIZE_PT

LOG2 = int(sys.argv[1]) if len(sys.argv) > 1 else 28
BOUND = 1 << LOG2
M = 1 + int(math.isqrt(BOUND))
PROG = open("bsgs_progress.txt", "w")

def log(msg):
    PROG.write(msg + "\n"); PROG.flush()
    print(msg, flush=True)

# ---- affine helpers (used sparingly) ----
def inv(a): return pow(a % FP, FP - 2, FP)

def aff_add(A, B):
    if A is None: return B
    if B is None: return A
    x1, y1 = A; x2, y2 = B
    if x1 == x2:
        if (y1 + y2) % FP == 0: return None
        s = (3 * x1 * x1) * inv(2 * y1) % FP
    else:
        s = (y2 - y1) * inv(x2 - x1) % FP
    x3 = (s * s - x1 - x2) % FP
    return (x3, (s * (x1 - x3) - y1) % FP)

def aff_neg(A): return None if A is None else (A[0], (FP - A[1]) % FP)

# ---- Jacobian mixed add: J=(X,Y,Z) + affine (x2,y2) [Z2=1], P1!=+-P2 ----
def jac_madd(J, x2, y2):
    X1, Y1, Z1 = J
    Z1Z1 = Z1 * Z1 % FP
    U2 = x2 * Z1Z1 % FP
    S2 = y2 * Z1 % FP * Z1Z1 % FP
    H = (U2 - X1) % FP
    if H == 0:
        if (S2 - Y1) % FP == 0:   # doubling case (rare in a walk); handle exactly
            return _jac_from_affine(aff_add((X1 % FP, Y1 % FP), (x2, y2))) \
                if Z1 == 1 else _slow_madd(J, x2, y2)
        return (1, 1, 0)          # infinity sentinel (won't match baby)
    HH = H * H % FP
    I = 4 * HH % FP
    Jc = H * I % FP
    r = 2 * (S2 - Y1) % FP
    V = X1 * I % FP
    X3 = (r * r - Jc - 2 * V) % FP
    Y3 = (r * (V - X3) - 2 * Y1 * Jc) % FP
    Z3 = ((Z1 + H) * (Z1 + H) - Z1Z1 - HH) % FP
    return (X3, Y3, Z3)

def _jac_from_affine(A):
    return (1, 1, 0) if A is None else (A[0], A[1], 1)

def _slow_madd(J, x2, y2):
    X1, Y1, Z1 = J
    zi = inv(Z1); zi2 = zi * zi % FP
    A = (X1 * zi2 % FP, Y1 * zi2 % FP * zi % FP)
    return _jac_from_affine(aff_add(A, (x2, y2)))

def load_candidates():
    c = {}
    for f in glob.glob("candidates_*.json"):
        for name, kh in json.load(open(f)).items():
            c[name] = int(kh, 16) % N
    return c

def build_baby():
    """affine table {(x,y): j} for j in [0,M); j=0 -> infinity (skipped)."""
    log(f"building baby table M={M} ...")
    table = {}
    cur = G
    for j in range(1, M):
        table[cur] = j
        cur = aff_add(cur, G)
    log(f"baby table ready: {len(table)} points")
    return table

def batch_affine_x(points_jac):
    """Convert list of Jacobian points to affine (x,y) via one batch inverse."""
    n = len(points_jac)
    zs = [pz for (_, _, pz) in points_jac]
    pref = [1] * (n + 1)
    for i in range(n):
        pref[i + 1] = pref[i] * (zs[i] if zs[i] else 1) % FP
    acc = inv(pref[n])
    out = [None] * n
    for i in range(n - 1, -1, -1):
        X, Y, Z = points_jac[i]
        if Z == 0:
            out[i] = None; continue
        zi = acc * pref[i] % FP
        acc = acc * (zs[i] if zs[i] else 1) % FP
        zi2 = zi * zi % FP
        out[i] = (X * zi2 % FP, Y * zi2 % FP * zi % FP)
    return out

def walk_hits(R0_aff, cx, cy, baby):
    """Walk R_i = R0 + i*C (C=(cx,cy)) for i in [0,M); return (i,j) if R_i==j*G."""
    if R0_aff is None:
        return (0, 0)
    pts = []
    J = (R0_aff[0], R0_aff[1], 1)
    for _ in range(M):
        pts.append(J)
        J = jac_madd(J, cx, cy)
    affs = batch_affine_x(pts)
    for i, a in enumerate(affs):
        if a is None:          # R_i is the point at infinity -> j = 0
            return (i, 0)
        if a in baby:
            return (i, baby[a])
    return None

def main():
    log(f"BOUND=2^{LOG2}  M={M}")
    cands = load_candidates()
    log(f"candidates: {len(cands)}")
    baby = build_baby()
    C = scalar_mul((M * (N - 1)) % N)    # -M*G  (giant step)
    cx, cy = C
    hits = []
    t0 = time.time()
    for idx, (name, k0) in enumerate(cands.items()):
        k0G = scalar_mul(k0)
        for direction, R0 in (("plus", aff_add(PRIZE_PT, aff_neg(k0G))),
                              ("minus", aff_add(k0G, aff_neg(PRIZE_PT)))):
            res = walk_hits(R0, cx, cy, baby)
            if res is not None:
                i, j = res
                m = i * M + j
                kp = (k0 + m) % N if direction == "plus" else (k0 - m) % N
                rec = {"seed": name, "direction": direction, "offset": m,
                       "k_prize_hex": hex(kp),
                       "verified": scalar_mul(kp) == PRIZE_PT}
                hits.append(rec); log("HIT " + json.dumps(rec))
        if (idx + 1) % 50 == 0:
            log(f"  {idx+1}/{len(cands)}  ({time.time()-t0:.0f}s)")
    json.dump(hits, open("results_bsgs_fast.json", "w"), indent=2)
    log(f"DONE seeds={len(cands)} hits={len(hits)} time={time.time()-t0:.0f}s")

if __name__ == "__main__":
    main()
