# GRAVEYARD -- every idea known to be tried or cut, one line each (check before every LAW 2 call)

Status words: **tried-reported** (a source says it was run; scripts/results not all held),
**tried-held** (scripts and results in this repo), **closed-by-control** (refuted by a held
control), **not pursued (Task 1 funnel)** (cut in `FUNNEL.md`; not a negative result).
Validator caveat: most reported sweeps used printable-text or 1-byte-pad gates and SHA-256
only (`reference/06` section 1); a "tried" line therefore excludes only its own candidates x
KDFs x validator.

## Community mechanisms (reference/05 M1-M15; mechanics reproduced where stated)
- M1 DBBI first-occurrence square -> full-period Bifid on FAED -> `BTCSEED...` -- reproduced; significance unverified; 0/66 as keys [B#13]; 0/396 as `urlblob` passwords (etheral-dev) -- `reference/03` section 3.1
- M2 b/c expansion of DBBI/FAED into 13^2 and 35^2 squares -- lengths reproduced; no decode [B#14]
- M3 2023 labels as values concatenated/hashed (literal four-label form fails on cosmic) -- tried-reported [C:.github/scripts/verify.mjs]
- M4 2023 labels as operations (RB's pipeline) -- never specified enough to run [A:_pr93/FINDINGS.md]
- M5 five literal tokens -> `salph_inner` (EVP-MD5) -> WIF -> `p32_trailing` (EVP-MD5) -- reproduced; 1-byte pads; no checkpoint; `E_S` undefined; 2023 A#15 control gives the same shapes -- closed-by-control for significance, not mechanics
- M6 seven hashed tokens XOR -> cosmic (Set B) -- reproduced; tokens 5-7 found by search [A#55]; self-referential digest -- significance unverified
- M6' Set A (`...sha256, theone`) -- opens nothing (reproduced) -- closed
- M7 OUT-cosmic -> 103x103 -> base-38 "Half/Better half" -- reproduced; fitted shift/offset/base; no prize match -- closed for significance
- M8 chain-4 masked nested envelope -- mask = output[158:166] XOR "Salted__"; crib control reproduced on cosmic_A -- closed-by-control
- M9 chain-4 block selection / XOR triangles / cosmic_A operands / LCP -- cannot be reproduced -- closed
- M10 prize point minus small residual -- no bound; BSGS +/-2^28 x 784 seeds null (tried-held) -- open-ended, not pursued
- M11 vanity => random key only in cosmic -- a non sequitur (`reference/07`) -- not a mechanism
- M12 donor funding / dust trigger -- no mechanism; rebutted repeatedly [A#69, #80, #83, #86] -- closed
- M13 OP_RETURN messages as clues -- creator-attributed "Correct" to "not his" (C-31) -- closed as clue source; on-chain addresses only as secondary checks (D-05)
- M14 YOUWON: DBBI minus VIC mod 26 -- arithmetic reproduced; layout forced; 0/200k shuffles; "Pfff. Coincidence." target disputed -- unverified; not pursued
- M15 2023 `MatrixSumlist AnsToo` padding-valid opens -- reproduced; the control that shows single-link openings are routine

## Containers (reference/06 section 2; counts as reported)
- `salph_inner`: soup-token literals and hashes (C, PR93, PR15, issues); Roses-poem normalisations; 400-word and 370k-word dictionaries; integer/short-alnum brute force (C ~33.5M, readability-gated); PBKDF2 x 6 iteration counts (PR15); Phase-2 table values [A#103] -- tried-reported
- `p32_trailing`: ~288 Phase-3.2 strings, EBCDIC letters, VIC digits fwd/rev, FEN variants, 370k dictionary (C); PR15 campaigns; [A#111] numeric re-encodings -- tried-reported
- `cosmic`: 4-ingredient combines, ~358k computed-value passphrases, XOR-of-N (N = 4..8), Merkle/Shamir, PBKDF2 x 29 counts, EBCDIC/UTF-16 passphrase bytes (C); concat permutations (PR93 joint attack 4,904 -> 0); PR15 campaigns -- tried-reported; raw-byte+MD5 forms outside M6 never swept
- `urlblob`: 76 tests (C); A#106 sweep -- community artifact, not a puzzle container
- A#106 "~2.5B" openssl sweep ({MD5,SHA1,SHA256,PBKDF2} x encodings x modes x 4 blobs x ~56k candidates) -- tried-reported, unaudited, no manifest
- B PR#15 52 campaigns ~33M trials (gate: pad >= 4 or magic or printable >= 0.85; KDFs m5/s2/rk/128-bit) -- tried-held (jsonl records in `sources/naddiseo/_pr15/neo/attempts/`)
- B PR#15 `endgame_aes_password_search.md`: ~14.8M candidates excluded -- tried-reported
- Report 1's nine predeclared families (~6.5M); Report 5's rounds A-E (44.8M); Report 6's ~240M; Report 2's local packages -- tried-reported (not held)
- Phase-1 lyric lines x normalisations POSTed to the live form (15 lines) -- tried-held [B:phase1.ipynb]; never on the AES containers

## DBBI / FAED (reference/06 section 2; research/)
- 9! digit permutations; 9! mono substitutions; transposition x substitution 3.27M; Vigenere/Beaufort periods 1-6; 3x3 Bifid; base-81; prime zero-out by value/position/insert/replace/remove (C `EXT-E0042`, attempts.js L1738) -- tried-reported, readability-gated
- Checkerboard / columnar / VIC full / hill-climb (PR93); b/c squares [B#14]; BYTENPHASE [A#115] -- tried-reported
- B campaigns 06/08: o->0 and drop-o "zeroed out" digit maps on head/faed -- tried-held
- B campaigns 12-19: 7x13 matrix row/column sums (`m7:*`); the 24 colour bits as selector / zero mask / add / sub on the FAED remainder, DBBI's 24 prime positions and the 7x13 matrices, both index bases (`p24:*`, 409,920 trials in campaign_19) -- tried-held (this is R5-W1a: not "never run")
- B campaign_07: mod-26 Vigenere/Beaufort decodes of head/faed under 8 puzzle keys; "reinsert 2357 at primes" into row sums; intertwined composites -- tried-held
- B campaign_20: chain-of-91 add/sub with VIC/YOUWON tails -- tried-held
- B tick 32: 11x11 `DBBI||FAED` prime-position matrixsumlist pipeline -- closed (B); its "14x14 already closed" claim is not backed by a logged prime-masked 14x14 family (see W-06)
- Research 2026-10-15 (held, exact oracle): 640 direct scalars from the Bifid output; 64 brain-wallet forms; 80 matrixsumlist-on-payload; 30 stream combines; 24 bitmap renderings; 228 +/-VIC operations -> no `YINYANG` (`YOUWON` control reproduced); zero-merge exhaustive (decimal rule, prime-position zeros, folds) -- tried-held, all negative
- Triangle model (91 = C(14,2)) -- refuted by a random-string control [A:_pr93/FINDINGS.md]
- Capacity: FAED as a number >= 2^1800, not seven 32-byte keys -- tried-reported [C]
- 83/84-token DBBI parses -- never located in any repository

## Keys and chain (reference/06 section 2; B ledger)
- 86,310 brain-wallet + 1,204 split-key derivations; ~17 DBBI/FAED scalars; 13 posted keys; posted WIFs/mnemonic (C `EXT-E0087`) -- tried-reported
- ECDSA nonce reuse: distinct nonces in both spends (B campaign_45) -- closed
- MITM against the prize key: 163,354-scalar pool, 8e10 pairs (B tick 37) -- tried-held, null
- Kangaroo tests A/B (operator-reported, cap 6x) and BSGS replay of 497 starts (Report 2) -- tried-reported
- `1NULY7...` vs 28 seed-derived keys (B tick 63): only the two controls hit -- tried-held
- "Good job, Neo!" recipients = Phase-0 seed as raw key, two encodings (B tick 63) -- explained; not an unpublished stage
- The 2021 "neighbors, half and double" dust: P-G, P/2, 2P, P+G -- reported; sender unknown; not compared with `17ucy1...` in any record

## Labels, hints, and readings
- `yellowblueprimes`: colour-bit integer `0xF73D92`; A007522 spiral primes; lab default `7233147103127`; ~4,156 derived strings incl. "URL with non-prime (or prime) positions zeroed out" (character-level; scripts absent) -- tried-reported (C `EXT-E0098`)
- `matrixsumlist`: row/column sums `610876654997879` / `8108108736759668` and concatenations; Janusz's integer (= URL << 4); Nihilist reading; FEFEFE-origin 59-digit value -- tried-reported
- `lastwordsbeforearchichoice`: ordered DELTA of the modified speech (~50k decrypts, all 7 KDFs, `EXT-E0217`); Matrix Reloaded Architect quotes (`EXT-E0183`); speech slices (`EXT-E0005`, `EXT-E0051`); final 11/21 words as keys (`EXT-E0270`); Report 5 round D (241,597 film-scene windows, reported) -- tried
- `yinyang` fed as a password component (B campaigns 01/03/05/10) -- backwards per C-38; closed
- "sha256 ans too" double-hash forms (`shabef`): B `try_family`, C double-sha -- tried
- *Looking Forward* (Fresco) strings -- pre-registered and closed (B ticks 79-80)
- Phase-2 table values from `fc0c1b02` [A#103] -- fitted; conflicts with the relayed "#..# wasn't used" (S-06)
- 104 / FEFEFE / 101010 numerology -- creator called the spelling a typo (C-18); solver text
- {2,3,5,7} as "the" primes -- solver text (S-02); all permutations/ordered subsets tried in the seven-token frame (B campaign_06)
- {1},{4},{21} April-Fools door (C-22) -- probably a joke; YOUWON marker reading built on it (M14)
- Wayback CDX of all gsmg.io URLs: 397 rows; the 64-hex "stage" pages are the SPA shell; /final_stage, /followthewhiterabbit, /TheArchitectChoice etc. are solver probes (`EXT-E0192`) -- closed
- Cosmic Duality book: OCR search of 27 solved answers -> 0/27 (`EXT-E0304`) -- tried-reported
- Site-text units of 2026 (finale page, "little bunny hunter" comment) through B's gate (`EXT-E0291`) -- tried-held

## Not pursued (Task 1 funnel) -- cut in `FUNNEL.md`, NOT negatives
- W-03 the song's third part ("The judgement") under the solved-stage lock -- cut round 1 (lowest score; lyric wording not held). Cheap; may return.
- W-05 the Telegram JSON export and PR93 attachments -- cut round 1 (an input we may never get); kept as a standing request to the user (`SELECTED.md` section 7).
- W-06 `matrixsumlist` as the prime-masked 14x14 sum list -- cut round 1 (tie-break on FREE parameters). The gap it names is real: no logged prime-masked 14x14 family. May return.
- W-08 the speech's cipher battery over the Bifid output -- cut round 1 (2 FREE incl. list membership; disputed input).
- W-09 "which GitHub was really getting close" (2023-01) -- cut round 1 (weak success test; held repos static).
- W-07 `17ucy1...` as an arithmetic image of the prize point -- cut round 2 (family bound is a fitted choice; a positive opens nothing).
- W-10 the April-2020 transcript window -- cut round 2 (simplest explanation already known; cannot open anything).
- W-04 the Decentraland parcel and the mp3 as a container -- cut round 3 (explains the fewest creator statements); the five-minute forensic half is in `IDEAS_INBOX.md`.
- (dropped before carding) the 24 colour bits as a selector/zero mask over DBBI/FAED (R5-W1a) -- already run: B campaigns 13 and 19.
- (not carded) P-01 primes + zero-out + sums -> literal yinyang on DBBI/FAED -- largely covered by `research/2026-10-15_yinyang_ops` and `zero_merge`; a typed sums variant exceeds two FREE parameters.
- (not carded) P-04 / P-07 asking the creator for a checkpoint hash or for the "zeroed out" operand -- user decisions, recorded in `SELECTED.md` section 7.
- (not carded) P-12 outreach to early solvers -- user decision.
- (not carded) P-17 / P-19 / P-21 (the 245.9M grammar on cosmic; the p32 padding census; the grid as a yin-yang logic puzzle) -- operator-local data or no mechanism.
- (not carded) P-20 "we won't" in the lastwords slot -- not testable alone (needs the other two values).
