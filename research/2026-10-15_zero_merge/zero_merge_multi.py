#!/usr/bin/env python3
"""H-ZM2: zeros may hide in ANY letter of a set X (each occurrence of a letter in X is its digit or 0)."""
import itertools, sys
from zero_merge import DIG, LOWER, PRINT
sys.setrecursionlimit(20000)

def solve(letters, Xs, allowed, node_cap=3_000_000, limit=5):
    rev = letters[::-1]; L = len(rev); sols = []; nodes = [0]; capped = [False]
    def dfs(p, S):
        nodes[0] += 1
        if nodes[0] > node_cap: capped[0] = True; return
        if len(sols) >= limit: return
        if p == L:
            b = S.to_bytes((S.bit_length() + 7) // 8, "big")
            if S and all(x in allowed for x in b): sols.append(b)
            return
        ch = rev[p]
        opts = [DIG[ch], 0] if ch in Xs and p != L - 1 else [DIG[ch]]
        for v in opts:
            S2 = S + v * 10 ** p; q = p + 1
            if q % 8 == 0 and q < L - 2 and ((S2 >> (8 * (q // 8 - 1))) & 255) not in allowed: continue
            dfs(q, S2)
    dfs(0, 0)
    return sols, nodes[0], capped[0]

if __name__ == "__main__":
    dbbi = open('../../reproduction/results/dbbi.txt').read().strip(); faed = open('../../reproduction/results/faed.txt').read().strip()
    s = open('../../reference/artifacts/pages/salphaseion_soup.txt').read().replace(' ', '').replace('\n', '')
    z1 = s.split('z')[1]
    # control: hide z1's zeros spread across two letters
    ctl = "".join(("b" if i % 2 else "e") if c == "o" else c for i, c in enumerate(z1))
    print("control", solve(ctl, set("be"), LOWER)[0])
    letters = "abcdefghi"
    for name, blk, sizes in (("DBBI", dbbi, (2, 3)), ("FAED", faed, (2,))):
        for direction, t in (("fwd", blk), ("rev", blk[::-1])):
            for k in sizes:
                for Xs in itertools.combinations(letters, k):
                    if name == "FAED" and "g" not in Xs: continue
                    for an, al in (("lower", LOWER), ("print", PRINT)):
                        sols, n, cap = solve(t, set(Xs), al)
                        if sols or cap:
                            print(name, direction, "".join(Xs), an, "sols", [x[:50] for x in sols], "nodes", n, "CAPPED" if cap else "")
    print("done")
