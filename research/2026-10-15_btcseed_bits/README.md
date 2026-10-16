# Research 2026-10-15 -- BTCSEED structure, offline prize oracle, direct-key & brain-wallet tests

**Session goal (user mission):** attack the *unsolved* parts of the puzzle with
fresh, outside-the-box ideas; push everything (ideas, code, tests, negatives) to
the private repo. This directory is self-contained and deterministic.

## The one tool that makes this safe and decisive: `btclib.py`

A dependency-free secp256k1 + address implementation that gives a **fully
offline, reject-capable oracle**: turn a candidate scalar into its public point
and compare it *exactly* to the puzzle's known prize public point.

- Prize address `1GSMG1JC9wtdSwfwApgj2xcmJPAwx7prBe`.
- Prize **uncompressed public key** is public -- it is in the 2020 halving-spend
  scriptSig (`sources/naddiseo/_pr15/neo/materials/chain/tx_halving_spend.hex`):
  `X = f4d1bbd9...a464`, `Y = 9c73d25f...3559`. Self-test confirms `hash160(04||X||Y)`
  base58check == the prize address.

Why this matters: a wrong candidate scalar fails the point comparison with
probability ~ 1 - 2^-160, so **there are effectively no false positives**. Unlike
the padding-validity and printable-text validators that produced the archive's
long list of disputed "openings", this oracle cannot be fooled. We can therefore
test *many principled structural interpretations* and trust every negative.

Nothing in this directory touches the network, signs or broadcasts a
transaction, or imports a key into a wallet. Deriving a public key from a
candidate scalar and comparing points is pure arithmetic on public data -- the
intended way to recognise a solution.

Run: `python3 btclib.py` (self-tests pass).

## What the BTCSEED output actually looks like (confirmed empirically)

`reproduction/results/bifid_full.txt` -- FAED decrypted with a full-period Bifid
over the square `DBIFHCEGAKLMNOPQRSTUVWXYZ` (DBBI first-occurrence order + the
rest, J omitted). 570 letters, begins **`BTCSEED`**. Period-2 structure:

| Stream | Length | Alphabet | Note |
|---|---:|---|---|
| EVEN positions (0,2,...) | 285 | exactly `{B,C,D,E}` | = top-left 2x2 of the square -> a clean (row,col) **2-bit** stream |
| ODD positions (1,3,...) | 285 | 24 letters | contains 13x`I` + 16x`O` = **29**; removing I/O leaves **256 = 2^8** |

Two clue-resonant facts fall straight out of the data:
- **256** surviving odd letters = a 256-bit key's worth of symbols. `I`/`O` look
  like `1`/`0` and the creator said some characters are *"zeroed out"*.
- the two interleaved streams are a literal **duality** -- the central
  *"yin yang"* milestone (*"once you hit a yin yang you'll solve it the same day"*).

## Experiments run this session

### 1. Direct-scalar readings of the BTCSEED output -- `decode_btcseed.py`
628 candidate scalars, each an exact-prize check. Families (all clue-driven):
- **A** even-stream row/col/2-bit streams (all 24 symbol->value assignments), as
  285-bit / first-256 / last-256 / mod-N numbers;
- **B** even letters with the I/O-paired positions dropped -> 256 bits;
- **C** odd-noIO (256 letters) under 6 single-bit "yin/yang" classifiers x polarity;
- **D** base-4 / base-25 conversions mod N;
- **E** prime-index selections;
- **F** "half and better half" sums/products of two stream scalars.
- each x {forward, reversed stream} x {msb, lsb, byteswap}.

**Result: 0 exact-prize hits, 0 watched-address hits.** -> `results_btcseed.json`.
The obvious "the output *is* the 256-bit key" readings are falsified.

### 2. Brain-wallet readings -- `brainwallet_test.py`
64 candidates: `sha256 / double-sha256 / sha256(hexdigest) / raw32` of the exact
decoded strings (full output, body after `BTCSEED`, the two streams, raw
FAED/DBBI, the literal label words). Motivated by the chain's own
`SHA-256(answer)` idiom and the uncompressed prize key.

**Result: 0 exact-prize hits.** -> `results_brainwallet.json`. The archive notes
prior brain-wallet sweeps were "vocabulary-only"; these exact decoded strings
are now covered and excluded.

## Reading so far

The BTCSEED output is almost certainly a genuine, intended object (getting the
literal word `BTCSEED` out of a Bifid decode, plus the exact 256/2-bit period-2
structure, is not luck). But it is **not** a direct encoding of the prize key in
any natural single-step form, and it is not a brain-wallet passphrase in its
obvious forms. It is an *intermediate*. The next moves pursued are the
creator-confirmed operation themes -- **primes + "reinsert the prime basics" +
"zeroed out"** -- on DBBI/FAED, with the literal milestone word `yinyang` as a
reject-capable target (see sibling research dir).
