# Session journal -- 2026-10-15 -- attacking the unsolved endgame

Mission (user): work the *unsolved* parts of the GSMG 5 BTC puzzle with fresh,
outside-the-box ideas; push every test, result and idea to the private repo.
Repo confirmed **private** (`testnetbtc/GSMG`).

This journal ties together the two working directories created this session:
- `research/2026-10-15_btcseed_bits/` -- the FAED->Bifid "BTCSEED" object and key tests
- `research/2026-10-15_yinyang_ops/` -- operations on DBBI/FAED, and a speech finding

## The decisive enabler: an exact, offline key-recognition oracle

Everything here leans on `btcseed_bits/btclib.py`: a dependency-free secp256k1
+ address implementation. The prize **public key** is public (it is in the 2020
halving-spend scriptSig), so for any candidate scalar we can compute its public
point and compare it *exactly* to the prize point. A wrong guess fails with
probability ~ 1-2^-160, so **this oracle produces no false positives** -- unlike
the padding-validity / printable-text validators behind the archive's disputed
"openings". We can therefore test many principled interpretations and trust
every negative. Nothing here touches the network, signs, or broadcasts.

## What the unsolved objects are (plain-language, for the user's questions)

- **DBBI** -- 91 letters over a-i (no `o`). Its role is confirmed: the letters'
  *first-occurrence order* (`DBIFHCEGA`) builds the 5x5 square used to Bifid-
  decrypt FAED. So DBBI is the **key/alphabet**, not the payload.
- **FAED** -- 570 letters over a-i. Decrypted with the DBBI-square full-period
  **Bifid**, it yields 570 letters that begin with the literal word **`BTCSEED`**.
  That is the object the community calls "btcseed". It is almost certainly a
  real, intended object (you do not get the literal word `BTCSEED` out of a
  Bifid by luck), and its purpose is evidently to carry the **BTC seed / key
  material** for the endgame -- hence the name.
- **salph_inner / p32_trailing / cosmic** -- AES containers with no independently
  verified opening (the "community openings" are 1-byte-padding false positives).
  Not the focus of this session.

### The BTCSEED output's structure (all confirmed empirically here)
570 letters, period-2:
- **even positions** (0,2,...): 285 letters, alphabet *exactly* `{B,C,D,E}` = the
  top-left 2x2 of the square -> a clean 2-bit (row,col) stream.
- **odd positions** (1,3,...): 285 letters; it contains 13 `I` + 16 `O` = 29 of
  the two "look-like-1-and-0" letters. Removing them leaves **exactly 256 = 2^8**
  letters over **23 distinct symbols**.

## NEW structural insight -- the Architect speech is a manual for this object

The already-decoded Phase-3.2 speech says: *"...reinserting the prime basics after
which you will be required to select from over **twenty-three ciphers**,
**sixteen encryptions** and or **seven intertwined passwords** to find the
actual private key, note that also brute forcing might be required..."*

Measured on the BTCSEED output: **23** distinct non-I/O symbols; **16** `O`s;
`BTCSEED` head = **7** letters. Two of three numbers match exactly, and the
speech ties them directly to "find the actual private key". I did not find this
correspondence anywhere in the reference layer. If it holds, the endgame is a
*bounded search* ("brute forcing might be required"), not a single clean decode
-- which is consistent with the puzzle still being open. This should steer future
work toward cipher-trial over the output, not more single-shot readings.

## Experiments run this session (all with the exact oracle unless noted)

| # | Hypothesis | Candidates | Result |
|---|---|---:|---|
| 1 | BTCSEED output *is* the 256-bit key: even/odd bit-streams, I/O zero-out, base-4/23/25, 5-bit index, prime-index picks, half+better-half sums | 628+12 | **0 prize hits** |
| 2 | Brain-wallet: sha256 / dsha256 / sha256(hexdigest) / raw32 of the exact decoded strings | 64 | **0 prize hits** |
| 3 | `matrixsumlist` read literally on the 256=16x16 payload (row-sums||col-sums = 32 bytes) | 80 | **0 prize hits** |
| 4 | Visual: 256-payload as 16x16 bitmaps under 6 yin/yang binarizations | 24 images | **no QR/glyph/text/yin-yang -- noise** |
| 5 | Pre-registered operations -> literal `YINYANG` (DBBI/FAED +/- VIC mod 26) | 228 ops | `YOUWON` control reproduced; **no `YINYANG`** |
| 6 | Yin-yang = *combine* the two streams (XOR / pack / sum-merge) -> key | 30 | **0 prize hits** |
| 7 | Vanity-grind: prize = seed +/- m for m < 2^28 (~268M), BSGS over all seeds | 784 seeds | **0 hits** -- rejected up to +/-2^28 |

**Takeaway:** the BTCSEED output is a genuine, high-entropy intermediate, but it
is **not** the prize key under any natural *direct*, *brain-wallet*, *matrix-sum*,
*visual*, or (within bound) *vanity-offset* reading, and the DBBI/FAED+/-VIC
operations do **not** yield the yin-yang milestone word. These are clean
negatives that remove large, natural parts of the hypothesis space -- the parts
prior sweeps could not even register, because they used printable/padding
validators and mostly EVP-SHA256, whereas these use an exact key oracle.

## Ideas not yet tested (for the next pass / collaborators)

1. **The speech as a literal recipe.** "reinsert the prime basics" then "select
   from 23 ciphers / 16 encryptions / 7 passwords". Enumerate classical ciphers
   over the output / odd-payload; validate only with reject-capable targets
   (exact prize point from any hex/WIF that appears; the literal word `yinyang`).
2. **`yellowblueprimes` from the opening image.** The 2020 "Roses" hint
   ("yellow has a number and so does blue, go back to the first puzzle piece")
   plus "primes". Derive the first 2023-label from the blue/yellow cells at
   prime positions of the Phase-0 grid -- no source derives it today.
3. **Two keys ("half and better half").** The VIC sentence says *two* private
   keys exist. The output may encode two scalars that combine (sum/split) to the
   prize scalar, or the "better half" sits at a second address. Extend the
   combine tests with a proper 2-scalar model.
4. **DBBI as a transposition/permutation** of the output (beyond first-occurrence).
5. **Cross-object intertwining** ("seven intertwined passwords"): the endgame key
   may require combining the BTCSEED output with the other containers' plaintext,
   not the output alone.

## Honesty note
No key was found. Nothing here claims a solve. The value delivered is: a reusable
exact oracle, a batch of rigorous negatives that the archive's validators could
not produce, and one concrete new structural lead (speech <-> output numbers).

## Correction added 2026-10-16

The "period-2 structure" of the BTCSEED output (even positions only ever
B/C/D/E) is a mathematical consequence of the Bifid construction, not an
extra signal: every FAED letter sits in rows 0-1 of the square, so the digit
stream alternates row, column, row, column and every even output position
receives a row and a column that are both 0 or 1 (the top-left 2x2 square).
Odd positions receive column coordinates in both slots and can be any letter.
What remains as a candidate for meaning is only the exact counts -- 256
non-I/O odd letters over 23 symbols, 16 letters O -- and those may be chance,
even though they match the speech's "twenty-three ciphers, sixteen
encryptions". The tests and negatives recorded above are unaffected; the
enthusiasm in the earlier wording is tempered accordingly. The readable
account is now in `walkthrough/10_frontier_dbbi_faed_btcseed.md`.
