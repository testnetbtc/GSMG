# Research log 2026-10-15 -- "zeroed out" and "yin-yang" structural tests

Status: **all negative.** No key material, wallet or network involved; every test is a deterministic
decode of `DBBI`/`FAED` with a reject-capable output criterion.

## Motivation
The solved z-sections encode text as a decimal integer written with a=1...i=9, **o=0**, then -> bytes -> ASCII
([01_SOLVED_CHAIN section 3.9](../../reference/01_SOLVED_CHAIN.md)). DBBI and FAED use the same a-i letters but contain
**no `o`**, while ~10% zeros are expected in decimal text. The creator-attributed hint "some characters need to be
'zeroed out'" (2021-12-26) and "primes ... required to proceed" suggest zeros must be restored.
Statistical check: FAED is far from uniform over 1-9 (chi^2=43.7, 8 df) but fits uniform decimal if `g` carries both
7 and 0 (chi^2=11.5, p~0.17); no other letter comes close. DBBI best fit: `b` (chi^2=20.5).

## H-ZM: one letter carries both its digit and 0 (`zero_merge.py`)
Exact solver: N mod 2^(8k) depends only on the last 8k decimal digits, so each byte is fixed digit-block by
digit-block from the right; depth-first search prunes every byte outside the allowed set. **Positive control:** with
the zeros of the solved z-sections hidden inside any letter, the solver recovers `lastwordsbeforearchichoice` and
`thispassword` uniquely (90-450 nodes).
Run: X  in  {a...i} x {DBBI, FAED, DBBI+FAED, FAED+DBBI} x {forward, reversed} x {lowercase, printable ASCII}.
Result: **0 solutions**; every search exhausted early (exhaustive, not sampled). The a=1...i=9 decimal model with one
zero-carrying letter is falsified for these blocks.

## Literal zero-out rules (inline script, see session log)
14 rules (prime positions 0/1-based -> 0 / deleted / kept; prime-valued digits b,c,e,g -> 0 / deleted; non-primes -> 0;
spiral indices of the 24 blue/yellow cells and their prime subset -> 0; single-letter -> 0 for b,e,g,i) x 3 blocks x
2 directions = 84 decodes. Best printable fraction 0.62 on a 13-byte output (chance level); nothing lowercase.

## Yin-yang fold of FAED and DBBIxVIC
Pairings (k,285+k), (k,569-k), (2k,2k+1) x digit maps {a=1...i=9, DBBI first-occurrence order 0...8} x combiners
{+, -, reverse -, 9x+y, 10x+y, xor, x} x output {mod 26 A=0/A=1, direct ASCII}; and DBBI against the equal-length
91-letter VIC sentence. 154 variants. Top index-of-coincidence values come from reduced alphabets (xor of 0-8),
outputs are gibberish; no English.

## What this rules out / leaves open
Ruled out: DBBI/FAED as the soup's decimal encoding with zeros hidden in one letter, or zeroed by the obvious prime
rules. Open: a non-decimal reading of DBBI/FAED; personal-knowledge inputs ("close friends have the best chance");
the raw Telegram export.

## H-ZM2: zeros hidden in a SET of letters (`zero_merge_multi.py`)
Control (z-section zeros spread over two letters) recovered. DBBI: every 2- and 3-letter set, both directions;
FAED: every 2-letter set containing `g`, both directions. **Lowercase criterion: 0 solutions, all searches
exhaustive.** Printable-ASCII criterion: many searches hit the 3M-node cap (unresolved, listed in the run log).
