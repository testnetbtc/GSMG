# 05 -- Community mechanisms and their lineage

Each mechanism below is a community proposal for getting past the solved chain. For each one the table gives its earliest located public appearance, every repository source that carries it, the mechanical status here, and the **first unsupported transition**: the earliest step that rests on choice rather than on a clue or checkpoint. Same claim, several sources: it is stated once and cited to all of them. A compilation repeating its source is one evidence family; byte-identical restatements are not corroboration.

## 1. Summary table

| # | Mechanism | Earliest located public appearance | Carried by | Mechanics here | First unsupported transition |
|---|---|---|---|---|---|
| M1 | DBBI first-occurrence square -> full-period Bifid on FAED -> `BTCSEED...` | Telegram, "Sycorax", 2025-06-11 [A:_pr93/_work/chat_transcript.txt@2c97f44 L122236] | B PR#8 (opened 2026-06-12, credits Telegram user "X" and CyberChef `Bifid_Cipher_Decode('dbifhceg')`) [B:_pr8/@821acd5]; [B#13] (Loupi201, 2026-08-24); [B:_pr9/other-puzzles/gsmg-salphaseion/SALPH_bifid_decoded.txt@041ee64]; [A#112] | **reproduced** | prefix -> an intended seed definition |
| M2 | b/c expansion of DBBI/FAED into 13^2 and 35^2 squares | [B#14] (saama143, 2026-09-07) | -- | lengths **reproduced** | chosen integer decomposition -> an intended encoding |
| M3 | 2023 labels as **values** to concatenate/hash | 2023-02-24 chat decode [T L20391]; [C:.github/scripts/verify.mjs@caaa77a#L100] | C labs; many issues | literal 4-token SHA-256 form fails on `cosmic` (source-reproduced in C; re-run here as part of C's harness logic) | value of `yellowblueprimes` and `yinyang`; join/serialisation |
| M4 | 2023 labels as **operations** (e.g. RB's pipeline: `sha256(first hint)` -> checkerboard key -> ANSWER -> `sha256(ANSWER)` -> Cosmic; `matrixsumlist` = mod-9 over-encryption) | [A:_pr93/FINDINGS.md@2c97f44#L37-L40] (credited to solver RB) | -- | not specified enough to run | checkerboard alphabet / a-i mapping (>=4 unknowns, per its own author) |
| M5 | five literal tokens -> `salph_inner` (EVP-MD5) -> WIF -> `p32_trailing` (EVP-MD5) | [A#68 comment 3704010992] 2026-01-01 | [B#17]; [A#108 body]; [A#88 comment 4330221649] | **reproduced** (both 79-byte outputs) | duplicate-token raw concatenation + MD5 + WIF representation -> correct passwords; no independent checkpoint for `E_S` |
| M6 | seven hashed tokens XOR -> `cosmic` (Set B: `...yourlastcommand, secondanswer`) | concept "XOR all 7 SHA-256 hashes": deleted account 2025-04-11 [A#27 comment 2796116788]; decrypt claim jackdevs66 2025-08-18 [B#3] and 2025-08-18/19 [A#51]; link 2025-08-23 [A#55 body] and Telegram the same day [T L133743]; [B#6] (jackdevs66) 2025-08-24; explicit token list 2025-08-31 [A#56 body] | [A:_pr68/GAP_ANALYSIS.md@27ea50e]; [A#68 comment 3704010992]; [A#72 body]; [A#74 body]; [A#96 body]; [A#103 body]; [B:_pr15/unverified/salphaseion_xor_token_hashes.md@1e913fd] | **reproduced** (raw 32 bytes + EVP-MD5 only) | tokens 5-7 were **found by search** -- "Uniqueness (p5-p7 search)" [A#55 comment 3223858361]; validation is by its own output digest |
| M6' | seven hashed tokens XOR -> `cosmic` (Set A: `...sha256, theone`) | [A#62 comment 3432403162] 2025-10-22; [A#69 body] key `818af53d...b402` | -- | key **reproduced**; opens nothing under 4 encodings (**reproduced**) | its claim to the Set-B output is false |
| M7 | `OUT-cosmic` -> 103x103 bit matrix -> shifted row+col sums -> base-38 -> "Half"/"Better half" scalars + `fc0c1b02` | [A#72 body] 2026-01-29 | [A#79 body]; [A#81 body]; [A#97 body]; [A#104 comment 5386157636]; [B:_pr15/neo/LEDGER.md@1e913fd#L2747-2766] | **reproduced** (no prize match) | shift 7, offset 80 and base 38 chosen from the observed min/range; the 32/32/4 split |
| M8 | masked nested envelope -> chain 4 | [A#68 comment 3704010992] | [A#88 body]; [A#108 body]; B PR#15 drive `chain4_final.bin` | **reproduced** | mask = `OUT-cosmic[158:166]` XOR `Salted__` (a crib fit; crib control reproduced on `OUT-cosmic-A`) |
| M9 | chain-4 block selection / XOR triangles / `cosmic_A` operands / LCP scores | [A#69 comment 3694520497]; PR#68 comment 3691156333; [A#84 body]; [A#88 body] | [A#92]; [A#87] | cannot be reproduced (`cosmic_A` recipe unknown; #84 hash unreconciled) | the operand files themselves |
| M10 | prize point subtraction -> a small residual scalar | prior brief; "neighbors, half and double" OP_RETURN (B PR#15) | -- | no bound exists | existence of a residual -> assumption it is small |
| M11 | vanity prefix -> the key is random and lives only in `cosmic` | [C:docs/ENDGAME-ANALYSIS.md@caaa77a section 8c]; [C:docs/CREATOR-INTEL.md@caaa77a] | [A#82 body] (softer form) | -- | prefix -> a specific generation method; excludes deterministic-then-filtered derivations |
| M12 | donor funding / dust trigger ("they also need funds to live") | [A#56 body]; [A#69 body] 2025-12-27; PR#30 author funded two "finder" addresses (3,000 sat each) [A#30 body] | [A#74 body] ("multisig", "dust transaction") | none; no mechanism shown | a sentence about funds -> an on-chain activation rule; rebutted repeatedly ([A#69 comment 5848569640] [A#80 comment 3973945917] [A#83 body] [A#86 body] [A#50]) |
| M13 | OP_RETURN messages as clues | on-chain dust from 2020 on (50 messages catalogued) [C:docs/LOOSE-ENDS.md@caaa77a#L514-L549] | [A#69] [A#74] [A#78] | -- | creator-attributed "Correct" to "the blockchain messages are not his" [C:content/sowut-data.js@caaa77a id 12653]; Naddiseo relays the same [A#114 comment 6128068004] |
| M14 | YOUWON: DBBI - VIC sentence (mod 26) | B PR#8 [B:_pr8/unverified/dbbi-youwon-otp.md@821acd5]; community msg #23799 2024-04-06 (per [C:content/attempts.js@caaa77a]) | B PR#15; B PR#9; C | arithmetic source-reproduced | the subtraction rule; layout forced once VIC and a-i are fixed |
| M15 | 2023 padding-valid Cosmic/salph_inner opens via `MatrixSumlist AnsToo` and reversed-printable text | [A#15 comments 1668268853, 1674478225] (eazytest, 2023-08) | -- | **reproduced** (79 B and 1,327 B, SHA-256 KDF) | every step after the first padding pass |

## 2. Shared structure of M5-M8 and M15

All of these:

1. pick a password family by reading soup text (with invented or duplicated tokens);
2. accept a decryption on **valid PKCS#7 alone** -- always 1-byte padding, the ordinary false-positive shape (~1 in 256 wrong keys);
3. impose a field layout on the output (32/32/15; 103x103; base 38);
4. validate later steps with values derived from the same outputs (`E_C` in the chain-4 password; `4f7a1e4e...` as its own checksum).

M15 is the control. A different, unrelated recipe published in 2023 also produced a 79-byte `salph_inner` output and a 1,327-byte `cosmic` output (reproduced here, SHA-256 KDF). Output length and padding validity therefore cannot distinguish M5/M6 from chance. What distinguishes M5 is that **two successive** fixed links both pass, which is a genuinely rarer event. Its evidential weight, however, depends on how many password families and KDF variants were tried before it was published, and that search history is not held (prior report section 10.4). jackdevs66's admitted search over tokens 5-7 (M6) shows such selection happened for at least one of these recipes.

## 3. Arithmetic facts that dissolve some claims

- XOR is commutative and associative: token order cannot matter, and the two `matrixsumlist` digests cancel. Set B's key is the XOR of five digests (reproduced). Claims that "order is critical" for this XOR [jackdevs66 README, per prior report section 6] are false.
- Set A and Set B give different keys (`818af53d...` vs `a795de11...`) and cannot both open `cosmic` to the same bytes; only Set B does (reproduced).
- The "hidden blob at `cc[158:]`" [A#88 body] does not exist before masking: no `Salted__` and no salt `5bbd88ac32481bca` appear anywhere in `OUT-cosmic` (reproduced; also [A#103 body]).
- The community `matrixsumlist` integer `40585734329412479690520338541901772425587069158131163878976` is `int("gsmg.io/theseedisplanted") << 4` (agent N4 arithmetic) -- it re-encodes the URL.
- `#108`'s "two typos in the live small blob" is a transcription error first seen in the title of [A#17] (2023-12-06). Its "fixed" blob is byte-identical to the canonical `salph_inner` (agent D2 comparison).
- The 32-byte "Half"/"Better half" values of M7 are public, so signatures from their addresses ([A#79], [A#80], [A#97]) prove nothing.

## 4. Status of the most-cited claims

| Claim | Verdict here |
|---|---|
| "Cosmic Duality has been decrypted" [A:_pr68/GAP_ANALYSIS.md@27ea50e] | mechanics reproduced (one padding-valid opening); intended significance unverified |
| "Cosmic was never decrypted / 4f7a1e... is fabricated" [C:docs/ENDGAME-ANALYSIS.md@caaa77a section 7] | refuted on mechanics; C never tested raw-bytes + MD5 |
| "Matching E_S independently verifies chain 2" [B#17] | not supported: `E_S` has no definition outside the output that produced it |
| "Cosmic is definitively a padding accident" (floflo777 section 14, per prior report) | goes beyond the evidence: consistent with an accident, not proven to be one |
| "Readable English is required at every stage" (Naddiseo [A#51 comment 3201181780], [A#55 comment 3222014134], [B:README.md@9e61693#L9-L16]) | an inference, not a creator rule; still a reasonable discriminator in the absence of any other checkpoint |
