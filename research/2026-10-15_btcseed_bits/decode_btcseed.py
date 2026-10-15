"""
BTCSEED structural decoder -> candidate private scalars -> OFFLINE prize check.

The FAED->Bifid output (570 letters, square DBIFHCEGAKLMNOPQRSTUVWXYZ) begins
"BTCSEED" and has a period-2 structure:
  EVEN positions: 285 letters, alphabet exactly {B,C,D,E} = top-left 2x2 of the
                  square -> a clean (row,col) 2-bit stream.
  ODD positions : 285 letters; removing I and O (they look like 1 and 0;
                  creator: some characters "zeroed out") leaves exactly 256 = 2^8.
Creator themes used: "yin yang" (binary duality of the two streams), primes
"required to proceed", chars "zeroed out", a regular Bitcoin private key, and
the VIC sentence "half and better half" (two keys).

Each hypothesis fixes ONE scalar (x a few orientation variants). The oracle is
an exact point comparison with the known prize public point, so a wrong
hypothesis is rejected -- it is not turned into a false positive. This is not a
keyspace sweep.
"""
import json, itertools
from btclib import scalar_mul, PRIZE_PT, N, point_to_address, PRIZE_ADDR

S = open('../../reproduction/results/bifid_full.txt').read().strip()
SQUARE = "DBIFHCEGAKLMNOPQRSTUVWXYZ"          # 5x5, J omitted
POS = {c: i for i, c in enumerate(SQUARE)}
ROW = {c: POS[c] // 5 for c in SQUARE}
COL = {c: POS[c] % 5 for c in SQUARE}

results = []
HITS = []
CANDS = {}      # name -> scalar, for downstream reuse (e.g. BSGS vanity search)
# addresses of interest besides the exact prize point (public, from archive)
WATCH_ADDR = {
    PRIZE_ADDR: "prize",
    "1MixpoELBvfkFSRUQtDCGXbdG53cjqknZT": "chain2_K_S1",
    "176ysPe7FdevdQjZWaFCK2nnVbzX9Tgydy": "chain2_K_S2",
}


def sieve(n):
    s = [True] * (n + 1)
    s[0] = s[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if s[i]:
            for j in range(i * i, n + 1, i):
                s[j] = False
    return {i for i, v in enumerate(s) if v}


def bits_to_int(bits):
    v = 0
    for b in bits:
        v = (v << 1) | (b & 1)
    return v


def base_int(s, fn, base=25):
    v = 0
    for c in s:
        v = v * base + fn(c)
    return v


def reg(name, k):
    """Register a candidate scalar; record any watched-address or exact hit."""
    if k is None:
        return None
    k %= N
    if k == 0:
        return None
    pt = scalar_mul(k)
    if pt is None:
        return None
    ac = point_to_address(pt, True)
    au = point_to_address(pt, False)
    exact = pt == PRIZE_PT
    watch = WATCH_ADDR.get(ac) or WATCH_ADDR.get(au)
    rec = {"name": name, "k_hex": hex(k), "addr_c": ac, "addr_u": au,
           "exact_prize_point": exact, "watch": watch}
    CANDS[name] = k
    results.append(rec)
    if exact or watch:
        HITS.append(rec)
    return k


def reg_bits(name, bits):
    bits = list(bits)
    k1 = reg(name + "|msb", bits_to_int(bits))
    k2 = reg(name + "|lsb", bits_to_int(bits[::-1]))
    if len(bits) == 256:
        by = bytes(bits_to_int(bits[i:i + 8]) for i in range(0, 256, 8))
        reg(name + "|msb_byteswap", int.from_bytes(by[::-1], 'big'))
    return k1, k2


def run():
    primes = sieve(1200)
    stream_keys = {}     # for half+betterhalf combination tests

    # Streams come from the FORWARD string (reversing the whole string flips
    # even/odd parity). Orientation variants reverse each stream in place.
    EVEN0 = S[0::2]
    ODD0 = S[1::2]
    for vname, (even, odd) in {"fwd": (EVEN0, ODD0),
                               "rev": (EVEN0[::-1], ODD0[::-1])}.items():
        odd_noio = ''.join(c for c in odd if c not in "IO")
        whole_noio = ''.join(c for c in (S if vname == "fwd" else S[::-1])
                             if c not in "IO")

        # ---- Family A: even-stream bits ----
        for bitname, fn in [("row", lambda c: ROW[c]), ("col", lambda c: COL[c])]:
            for pol in (0, 1):
                bits = [fn(c) ^ pol for c in even]            # 285 bits
                reg_bits(f"A.even.{bitname}.pol{pol}.{vname}.all285", bits)
                reg_bits(f"A.even.{bitname}.pol{pol}.{vname}.first256", bits[:256])
                reg_bits(f"A.even.{bitname}.pol{pol}.{vname}.last256", bits[-256:])
        for perm in itertools.permutations(range(4)):
            amap = dict(zip("BCDE", perm))
            bits = []
            for c in even:
                v = amap[c]; bits += [(v >> 1) & 1, v & 1]    # 570 bits
            tag = ''.join(str(amap[x]) for x in "BCDE")
            reg(f"A.even.2bit.{tag}.{vname}.modN", bits_to_int(bits) % N)
            reg_bits(f"A.even.2bit.{tag}.{vname}.first256", bits[:256])
            reg_bits(f"A.even.2bit.{tag}.{vname}.last256", bits[-256:])

        # ---- Family B: even letters, drop positions whose paired odd is I/O ----
        kept = [even[i] for i in range(len(even)) if odd[i] not in "IO"]
        if len(kept) == 256:
            for bitname, fn in [("row", lambda c: ROW[c]), ("col", lambda c: COL[c])]:
                for pol in (0, 1):
                    bits = [fn(c) ^ pol for c in kept]
                    reg_bits(f"B.even_dropIOpair.{bitname}.pol{pol}.{vname}", bits)

        # ---- Family C: odd-noIO single-bit classifiers (256 letters -> 256 bits) ----
        classifiers = {
            "rowpar": lambda c: ROW[c] & 1,
            "colpar": lambda c: COL[c] & 1,
            "sqidx_hi": lambda c: 1 if POS[c] >= 12 else 0,
            "alpha_hi": lambda c: 1 if c >= 'N' else 0,
            "rows01": lambda c: 0 if ROW[c] <= 1 else 1,
            "vowel": lambda c: 1 if c in "AEIOUY" else 0,
        }
        for cname, fn in classifiers.items():
            for pol in (0, 1):
                bits = [fn(c) ^ pol for c in odd_noio]
                k, _ = reg_bits(f"C.oddnoIO.{cname}.pol{pol}.{vname}", bits)
                if vname == "fwd" and pol == 0:
                    stream_keys[f"oddC.{cname}"] = k

        # ---- Family D: base conversions mod N ----
        for perm in itertools.permutations(range(4)):
            amap = dict(zip("BCDE", perm))
            v = 0
            for c in even:
                v = v * 4 + amap[c]
            reg(f"D.even.base4.{''.join(str(amap[x]) for x in 'BCDE')}.{vname}", v % N)
        swhole = S if vname == "fwd" else S[::-1]
        reg(f"D.odd.base25sq.{vname}", base_int(odd, lambda c: POS[c]) % N)
        reg(f"D.oddnoIO.base25sq.{vname}", base_int(odd_noio, lambda c: POS[c]) % N)
        reg(f"D.whole.base25sq.{vname}", base_int(swhole, lambda c: POS[c]) % N)
        reg(f"D.wholenoIO.base25sq.{vname}", base_int(whole_noio, lambda c: POS[c]) % N)

        # ---- Family E: prime-position selection ----
        for base in (0, 1):
            sel = [odd_noio[i] for i in range(len(odd_noio)) if (i + base) in primes]
            if sel:
                reg_bits(f"E.oddnoIO.primeidx{base}.rows01.{vname}",
                         [0 if ROW[c] <= 1 else 1 for c in sel])
            sel2 = [even[i] for i in range(len(even)) if (i + base) in primes]
            if sel2:
                reg_bits(f"E.even.primeidx{base}.row.{vname}", [ROW[c] for c in sel2])

    # ---- Family F: "half and better half" -- combine two stream scalars ----
    ks = {k: v for k, v in stream_keys.items() if v}
    names = list(ks)
    for i in range(len(names)):
        for j in range(len(names)):
            if i == j:
                continue
            a, b = ks[names[i]], ks[names[j]]
            reg(f"F.sum.{names[i]}+{names[j]}", (a + b) % N)
            reg(f"F.mul.{names[i]}*{names[j]}", (a * b) % N)

    out = {"n_candidates": len(results), "hits": HITS,
           "sample": results[:5]}
    json.dump(results, open("results_btcseed.json", "w"), indent=0)
    json.dump({k: hex(v) for k, v in CANDS.items()},
              open("candidates_btcseed.json", "w"), indent=0)
    print(json.dumps(out, indent=2))
    print(f"\nTOTAL candidates tested: {len(results)}")
    print(f"EXACT prize / watched hits: {len(HITS)}")


if __name__ == "__main__":
    run()
