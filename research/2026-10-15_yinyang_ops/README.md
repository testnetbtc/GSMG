# Research 2026-10-15 -- operations on DBBI/FAED, and the Architect speech as a decode manual

## 1. Pre-registered "operations -> milestone word" test (`ops_test.py`)

Report v2's #1 next-check: can an operation using only creator-confirmed themes
turn DBBI/FAED into the literal milestone word **`YINYANG`/`YINGYANG`** (the
creator's "yin yang" is "the next phase"; "once you hit a yin yang you'll solve
it the same day")? Reject-capable: we only report exact target-word occurrences.

- **Positive control reproduced:** `DBBI(a=1..i=9) - VIC(a=1..z=26) mod 26`
  contains **`YOUWON`** at offset 21 (community finding; also reproduced here
  under two other digit/offset conventions). This confirms the harness.
- **Target result: NEGATIVE.** Across 228 operations (blocks DBBI / FAED-head /
  FAED-tail x digit maps {a=1.., a=0.., DBBI-first-occurrence} x VIC maps x
  {sub, rsub, add} x output-base {0,1} x {forward, reversed}, plus DBBIxFAED),
  **no operation produced `YINYANG` or `YINGYANG`.** One lone `YANG` appears in
  `FAED_head - VIC` (reversed) but sits inside gibberish with no `YIN` before it
  -- consistent with chance for a 4-letter word at this scan size.

So the simple additive/subtractive combination of these blocks with the VIC
sentence does **not** yield the yin-yang milestone. `YOUWON` remains the only
word that falls out, and its significance stays contested (the archive notes the
layout is forced once VIC and a-i are fixed).

## 2. NEW observation -- the Architect speech describes the BTCSEED output's structure

The Phase-3.2 Architect speech (already decoded, part of the solved chain) says:

> "...**reinserting the prime basics** after which you will be required to select
> from over **twenty-three ciphers**, **sixteen encryptions** and or **seven
> intertwined passwords** to find the actual private key, note that also brute
> forcing might be required..."

Measured on the FAED->Bifid "BTCSEED" output (`reproduction/results/bifid_full.txt`):

| Speech phrase | Measured structural count | Match |
|---|---|---|
| "twenty-three ciphers" | odd stream minus I/O uses **23 distinct symbols** | exact |
| "sixteen encryptions" | the output contains exactly **16 `O`** letters (`O` = the "zeroed-out" char) | exact |
| "seven ... passwords" | `BTCSEED` header is **7** letters (and `T` occurs exactly 7x) | plausible |

Two of three numbers match the output *exactly* and non-trivially. The reference
layer notes "256 over 23 symbols" but does not connect it to the speech. Read
this way, the **already-solved Architect speech is an instruction manual for the
final object**: reinsert prime basics -> select among 23 ciphers / 16 encryptions
/ 7 passwords -> brute forcing may be required. That last clause predicts the
endgame is a (bounded) search, not a single clean decode -- which fits why it is
still open.

Caveat: "16" is a common count and "23 symbols" was reached by removing I/O, so
this is a lead, not proof. But the exactness of 23 **and** 16 together, both
tied by the speech to "find the actual private key," is the most concrete
structural correspondence found this session and should steer the cipher-trial
work (see the sibling `2026-10-15_btcseed_bits` directory).

## Files
- `ops_test.py` -- the pre-registered operations search (deterministic).
- `ops_results.json` -- every operation's output text + any target-word hits.
