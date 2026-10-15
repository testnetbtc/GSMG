#!/usr/bin/env python3
"""Hypothesis H-ZM: in an a-i letter block (a=1..i=9, like the solved z-sections), one letter X stands
for BOTH its own digit and 0 ("zeroed out"). Find every assignment of X-occurrences to {digit(X), 0}
such that the decimal integer converts (big-endian, minimal length) to bytes that are ALL in an allowed set.

Method: N mod 2^(8k) depends only on the last 8k decimal digits (10^p divisible by 2^p), so byte k is
fixed once digits p < 8(k+1) are fixed. Depth-first from the least-significant digit, pruning on each byte.
"""
import sys

DIG = {c: i + 1 for i, c in enumerate("abcdefghi")}
DIG["o"] = 0


def solve(letters, X, allowed, limit=50, zero_only=False):
    rev = letters[::-1]                      # rev[p] = digit at 10^p
    L = len(rev)
    pow10 = [10 ** p for p in range(L)]
    sols, nodes = [], [0]

    def dfs(p, S):
        nodes[0] += 1
        if len(sols) >= limit or nodes[0] > 5_000_000:
            return
        if p == L:
            if S == 0:
                return
            b = S.to_bytes((S.bit_length() + 7) // 8, "big")
            if all(x in allowed for x in b):
                sols.append(b)
            return
        ch = rev[p]
        opts = [0] if (zero_only and ch == X) else ([DIG[ch], 0] if ch == X else [DIG[ch]])
        if p == L - 1:
            opts = [v for v in opts if v != 0] or opts   # no leading zero
        for v in opts:
            S2 = S + v * pow10[p]
            q = p + 1
            if q % 8 == 0:                    # byte (q/8 - 1) now fixed
                k = q // 8 - 1
                if q < L or True:
                    byte = (S2 >> (8 * k)) & 255
                    # the top byte(s) may be shorter than a full byte once digits run out; checked at the end
                    if q < L - 2 and byte not in allowed:
                        continue
            dfs(q, S2)
    sys.setrecursionlimit(10000)
    dfs(0, 0)
    return sols, nodes[0]


LOWER = set(range(0x61, 0x7B))
PRINT = set(range(0x20, 0x7F))

if __name__ == "__main__":
    # positive control: the solved agda z-section with its zeros hidden inside letter 'a'
    agda = "agdafaoaheiecggchgicbbhcgbehcfcoabicfdhhcdbbcagbdaioobbgbeadedde"
    for X in "abcdefghi":
        hidden = agda.replace("o", X)
        sols, n = solve(hidden, X, LOWER)
        print(f"control X={X}: {len(sols)} solution(s), {n} nodes", [s.decode() for s in sols][:3])
