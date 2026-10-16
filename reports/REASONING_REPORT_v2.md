# GSMG -- reasoning report v2

Prepared 15 October 2026 from the consolidated archive in this repository. It builds on `reports/MASTER_REASONING_REPORT.md` (14 October 2026, "the prior report"), whose structure it follows. Every factual statement cites `repo@commit:path`, an issue or comment, or a record in `reproduction/results/reproduction_results.json`; the citation legend is `reference/00_INDEX.md`. Object names follow `reference/08_GLOSSARY.md`.

**This is an evidence report, not a solution announcement.** Two verdicts are kept apart throughout: **mechanics reproduced** (bytes re-derived here from fresh code) and **intended significance unverified** (no independent checkpoint shows the bytes are a puzzle stage).

## Contents

0. [What changed since the prior report](#0-what-changed-since-the-prior-report)
1. [Executive assessment](#1-executive-assessment)
2. [Sources and completeness](#2-sources-and-completeness)
3. [Solved chain](#3-solved-chain)
4. [Unresolved artifacts](#4-unresolved-artifacts)
5. [Creator clues](#5-creator-clues)
6. [Community mechanisms](#6-community-mechanisms)
7. [Experiment coverage](#7-experiment-coverage)
8. [Contradictions](#8-contradictions)
9. [Structured assessments](#9-structured-assessments)
10. [The prior report's five next checks](#10-the-prior-reports-five-next-checks)
11. [New next checks](#11-new-next-checks)
12. [Validation](#12-validation)

## 0. What changed since the prior report

**Upstream state.** The default-branch HEADs are unchanged (A `fb92dd1`, B `9e61693`, C `caaa77a`; `sources/REFS.tsv`). One new A issue, [A#116] (2026-10-15 01:18 UTC), contains no technical values. No comment in A was created or edited after the prior collection (2026-10-14 22:18 UTC; agent D2 scan, `sources/discussions/puzzlehunt/COUNTS.json`). B and C: no comment newer than the prior collection (B's last 2026-10-05, C's 2026-08-01); counts unchanged (agent D3).

**Material this collection includes that the prior report did not use** (the prior report deliberately excluded Telegram corpora; this build is not under that restriction, but uses only what the three repositories ship):

- the full Telegram transcript of the "GSMG Puzzle Solvers" group, 51,177 text messages from 2019-04-20 to 2026-06-12 [A:_pr93/_work/chat_transcript.txt@2c97f44];
- B PR #15's user-supplied Wayback captures of the SalPhaseIon and Phase-2 pages, raw halving transactions and a third-party Drive export [B:_pr15/@1e913fd];
- all unmerged PR heads and non-default branches of A, B and C (unique files under `sources/*/_pr*/`, `_branches/`; every head tagged `archive/*`).

**Discrepancies with the prior report's claims** (detail: `reference/07_CONTRADICTIONS.md` section 1):

1. The 2021 "Christmas" hint was posted **2021-12-26** (20:18 UTC), not 2021-12-25. Two independent timestamps agree [C:content/sowut-data.js@caaa77a id 8000] [T L19304].
2. The "445 vs 510 creator messages" contradiction is **resolved**. All 411 text messages under @SoWut in the dataset window match transcript messages by display name `Jrk Bgrt`. 445 = 411 text + 34 media records up to 2026-05-28; the dataset was later extended by 65 messages.
3. Jrk's "Ancient spelling 😅. One of the many many typos." was a Telegram **reply to** Janusz's "FORTY but hundred FOUR = 104 is the fefefe square" message. It characterises the spelling as a typo, which is evidence **against** the FEFEFE/104 numerology. The prior report called it merely "not explicit confirmation".
4. The friends/family remark (9595) answers a question about who could continue if the author **disappeared** [T L22780-L22783]; the prior report lacked this context.
5. The prior report's section 6 row "Cosmic binary -> 103x103 sums -> base-38" is now **reproduced** (no prize match).

No reproduced byte differs from the prior report: 18 comparisons with prior-report or published values confirmed (17 against the prior report), 0 discrepancies.

**New evidence bearing on significance:**

- **A selection step behind the Cosmic recipe.** Its originator wrote "Uniqueness (p5-p7 search)" about tokens 5-7 [A#55 comment 3223858361]. The XOR-of-seven-hashes idea appears 2025-04-11 [A#27 comment 2796116788]; jackdevs66 claimed a Cosmic decrypt on 2025-08-18 [B#3] and posted the recipe link 2025-08-23 [A#55 body], all before the prior report's earliest pointer [B#6] (2025-08-24). Naddiseo's "verified not working" reply in [B#6] hashed the hex text of the key rather than using its raw bytes (agent D3 hash check), so it is not a mechanical refutation.
- **A 2023 control.** Unrelated published passwords open `salph_inner` to 79 bytes and `cosmic` to 1,327 bytes with valid padding [A#15 comments 1668268853, 1674478225] -- reproduced (`a15_padding_controls`).
- **A refuted variant.** "Set A" (`...sha256, theone`, key `818af53d...`) claims the same Cosmic output; reproduced: it opens nothing under the four encodings.
- **A crib control for chain 4.** The same offset-158 `Salted__` crib applied to another padding-valid Cosmic decrypt (`cosmic_A.bin`) yields another well-formed "nested envelope" (salt `0391bdb016191c9d`) -- reproduced.
- **Page provenance.** The held SalPhaseIon captures' textareas equal the soup and `cosmic.txt` byte-for-byte, and the page carries no checkpoint, comment or verification value (reproduced on the captures as supplied).

## 1. Executive assessment

The solved chain reproduces end to end from the three repositories alone: opening grid, Phase-1 checkpoint, the three AES stages (Python and OpenSSL agree), CP1141/Beaufort speech, checkerboard sentence, audio, entry hash and soup tokens. Nothing in the solved chain is in doubt.

Past the soup, the archive holds four open containers. Three of them (`salph_inner`, `p32_trailing`, `cosmic`) are on puzzle pages or inside creator-encrypted plaintext; `urlblob` is a community URL artifact. Several community recipes open the three page containers with valid PKCS#7, and this build reproduces every one of them byte-for-byte. **None of those openings has an independent checkpoint.** Every one has 1-byte padding, the ordinary wrong-key shape (~1/256). Every one rests on at least one choice made after looking at outputs: invented tokens, a duplicated token, MD5 instead of the chain's SHA-256, a WIF representation, a fitted mask, or a base equal to the observed range. The new evidence moves the balance further toward "selected false positives":

- an admitted token search for Cosmic;
- an older unrelated recipe that produced the same output shapes;
- a refuted competing token set;
- a crib rule shown to manufacture envelope headers on demand.

It does not prove that. The fixed two-link chain (`salph_inner` -> WIF -> `p32_trailing`) remains the one construction whose joint padding event is rarer than a single pass; its weight cannot be computed without the search history behind it.

The creator-attributed record, now checkable against a near-complete transcript, contains **no** verification value beyond the 2019 Phase-1 hash. It never mentions E_S, WIF, seed, vanity, matrixsumlist values or Cosmic. Several "creator rules" in circulation are solver text (FEFEFE/104, {2,3,5,7}, "encrypted private key stored online", "second half ... another puzzle", the 2021-05-06 entry recipe). The strongest creator-attributed constraints are thematic: primes are required; some characters are "zeroed out"; "yellow has a number and so does blue"; "ying yang" is the next milestone; a "regular Bitcoin private key" is the target; close friends "have the best chance".

**Bottom line:** mechanics reproduced for every published fixed recipe; intended significance unverified for all of them; no bound, seed model or checkpoint exists that would justify a search.

## 2. Sources and completeness

### 2.1 Repository identities

| Repo | Default | HEAD (= prior) | Files at HEAD | Commits at HEAD | Extra refs imported |
|---|---|---|---:|---:|---|
| A puzzlehunt | master | `fb92dd15487c6e2d275adb8c923698b7166c328e` | 7 | 11 | 9 PR heads (#3, 8, 11, 16, 30, 68, 93, 101, 102) |
| B Naddiseo (fork of A) | master | `9e61693404ef74e8e681598116d371924f399ffa` | 89 | 27 | 7 PR heads (#1, 8, 9, 10, 12, 15, 16) |
| C HosterjackAGV | main | `caaa77a8c218e97f9fdaae8908d580e51118edec` | 160 | 187 | 1 PR head (#2), branches `feat/arcade-phase-games-governance`, `game-rebuild` |

No source has tags. The full import, dedup and coverage proof is `MANIFEST.md`.

### 2.2 Discussions

| Repo | Issues | PRs | Comments expected / fetched | Reviews | Review comments | Attachments attempted / fetched / 404 |
|---|---:|---:|---:|---:|---:|---:|
| A | 103 | 9 | 606 / 605 | 3 | 0 | 69 / 66 / 3 |
| B | 10 | 7 | 36 / 35 | 1 | 1 | 1 / 1 / 0 |
| C | 3 | 1 | 2 / 2 | 0 | 0 | 0 |

Identical to the prior report except A#116. Full table and gaps: `MANIFEST.md` section 2 and section 5. Counter mismatches: [A#25] 19/18 and [B#2] 2/1, the same as the prior report. Two A comments survive only as quotes ([A#72 comment 3935458653] quotes a "ZION" text; [A#114 comment 6128068004] quotes AomDEV).

### 2.3 Identity limits

Creator attribution is by handle (`@SoWut`) and display name (`Jrk Bgrt`) only. The transcript has no numeric ids or reply targets; C's dataset supplies reply targets but no numeric id for @SoWut. The 2026-07-13 messages exist only in C's dataset.

## 3. Solved chain

Unchanged from the prior report section 3 and fully reproduced; see `reference/01_SOLVED_CHAIN.md` for every answer string and hash. Additions:

- placement: `ENV-phase2` and `ENV-phase3` both appear on the archived Phase-2 page (2020-11-12 capture);
- the Phase-2 equation decode in B (Q=82, H=42, B=25 -> 51 deg52'28.0"N 4 deg24'23.2"E) is recorded (reported) [B:phase2.ipynb@9e61693 cell 4];
- the creator-attributed handle stated other misspellings "would be nice, not required" to fix [T L3971];
- the audio's eighth hex group is partly occluded in our rendering, so its reading relies on a partial glyph.

## 4. Unresolved artifacts

`reference/03_UNRESOLVED.md` is the full register. In summary:

| Object | Mechanics | Significance | Change vs prior |
|---|---|---|---|
| `salph_inner` -> `OUT-chain1` | reproduced | unverified | 2023 unrelated 79-byte opening also reproduced |
| `p32_trailing` -> `OUT-chain2` | reproduced | unverified | no independent `E_S` definition anywhere (now checked against the full transcript) |
| `cosmic` -> `OUT-cosmic` (Set B) | reproduced | unverified | selection admitted; Set A refuted; 2023 unrelated 1,327-byte opening reproduced |
| `OUT-cosmic` -> 103x103 -> base-38 | **reproduced (new)** | unverified; offset and base fitted to data | -- |
| chain 4 | reproduced | header forced by the mask; **crib control reproduced** | strengthened |
| [A#84] `chain4.bin` | not reproducible | unexplained | -- |
| `urlblob` | bytes reproduced | community URL artifact | provenance sharpened |
| `DBBI`, `FAED`, `BIFID-OUT` | structure reproduced | unverified | first BTCSEED appearance: 2025-06-11 (Sycorax) |

## 5. Creator clues

`reference/04_CREATOR_CLUES.md` holds the deduplicated register with raw context. Changes relative to prior section 5: dates P1/P2; FEFEFE reply target (P4); friends/family context (P5); "encrypted private key stored online" was the solver's wording [T L18932]; the 2023 decode's first public decoder was a Deleted Account (2023-02-24), and the handle's only reaction was "👆🤷‍♂"; five "dot" messages preceded the 2026 binary; the 2026-07-13 session included "NOTE: that is a hint.", a "hidden laptop" and self-declared intoxication.

## 6. Community mechanisms

`reference/05_COMMUNITY_MECHANISMS.md` lists 15 mechanisms with lineage and first unsupported transitions. The shared structure of every "opening" -- pick tokens, accept 1-byte padding, impose a layout, validate with derived values -- is set out there with the 2023 control.

## 7. Experiment coverage

`reference/06_EXPERIMENT_COVERAGE.md` and `reference/data/EXPERIMENT_COVERAGE.csv` (prior rows + extracted rows: C's 171 attempts, B PR #15's 52 campaigns ~ 32M decrypts, A PR #93's scripts, issue sweeps). The decisive limit: most negatives used printable-text validators and/or EVP-SHA256 only. They **cannot** register the MD5 binary openings, so they neither support nor refute M5/M6.

## 8. Contradictions

`reference/07_CONTRADICTIONS.md`: 19 rows against the prior report and about 45 source-vs-source rows, each with an assessment. Additional detail from the B threads: only the **title** of [B#17] says "inner blob" (its body names the trailing blob correctly), and BTCSEED circulated in B PR #8 (opened 2026-06-12) and in Telegram (2025-06-11) before [B#13].

## 9. Structured assessments

Each follows Question / Evidence / Assumptions / Alternatives / Prior coverage / Prediction / Discriminator / Assessment.

### 9.1 Is the seven-token Cosmic opening an intended stage?

**Question.** Does the 1,327-byte `OUT-cosmic` (`4f7a1e4e...`) reflect the creator's intended password?

**Evidence.** Mechanics reproduced: raw 32-byte XOR of the seven digests + EVP-MD5 is the only one of four encodings that opens it. Its proposer searched tokens 5-7 [A#55 comment 3223858361]. Tokens 6-7 (`yourlastcommand`, `secondanswer`) are solver readings first seen in chat in 2023-09 and 2025-08. The duplicate `matrixsumlist` digests cancel, so the key depends on five tokens. The output digest is self-referential [A#72 comment 3830122705]. An unrelated 2023 password also opens `cosmic` to 1,327 bytes (reproduced). The competing Set A opens nothing (reproduced). No creator-attributed message mentions Cosmic.

**Assumptions.** Raw-bytes password; MD5 rather than the SHA-256 used by every solved stage; token readings of the soup; XOR as the combiner.

**Alternatives.** (a) Intended stage reached by a correct reading; (b) a selected false positive found by searching token variants and KDF/encoding variants; (c) correct tokens but a different intended combiner/KDF, with this opening coincidental.

**Prior coverage.** The prior report reproduced mechanics and left significance unverified. C's sweeps never tested this encoding; B PR #15's gate would reject it.

**Prediction.** If (a), downstream structure should appear without further fitting: a field that matches something published independently, or a key relation to the prize point. If (b), every further "structure" requires fitted parameters, and comparable openings arise from unrelated searches.

**Discriminator.** Any pre-registered, parameter-free test on `OUT-cosmic` with a reject-capable target, such as an address equality fixed before inspection.

**Assessment.** Mechanics reproduced. Intended significance unverified, and now **less** likely than before: there is direct selection evidence, an independent control of the same shape, and every observed downstream structure (103x103 base-38, chain-4 mask) is fitted. Not proven accidental.

### 9.2 Are the two 79-byte chains legitimate binary stages?

**Question.** Is the fixed recipe `salph_inner` -> WIF(K_C1) -> `p32_trailing` the intended path?

**Evidence.** Both links reproduce (Python, OpenSSL). The recipe appears first in [A#68 comment 3704010992] (2026-01-01). `E_S` has no definition anywhere except as the residual 15 bytes of the output it would validate. It appears inside the chain-4 password (bytes 15-29) [A#68 comment 3704010992], and its claimed confirmation via `E_C` is circular [A#108 body]. Neither creator corpus mentions E_S, WIF or checksums. A 2023 unrelated password also opens `salph_inner` to 79 bytes (reproduced). The creator-attributed handle said "There must at least be something hidden in there" about Phase 3.2 (2020-03-25, id 2918) -- compatible with `p32_trailing` being meaningful, but it names no container.

**Assumptions.** Duplicate-token literal concatenation; MD5; uncompressed mainnet WIF; a 32/32/15 field layout.

**Alternatives.** Intended chain; a selected pair of padding passes; a genuine first link with a wrong continuation.

**Prior coverage.** Prior section 9.2/ section 10. Nothing in the B PR #15 campaigns or C's attempts covers this recipe.

**Prediction.** An intended chain should meet some condition not manufactured from its own bytes.

**Discriminator.** A creator-published value equal to a function of `K_S1`, `K_S2` or `E_S`, or an address/point relation to the prize key specified in advance. Both corpora have now been searched: none exists.

**Assessment.** Mechanics reproduced. Significance unverified. Two fixed successive padding passes remain the strongest observation in the endgame, but their weight is unquantifiable without the search history. The 2023 control shows single-link openings were routinely found.

### 9.3 Do the 2023 labels mean values or operations?

**Question.** What grammar does `yellowblueprimes|matrixsumlist|lastwordsbeforearchichoice|yinyang` prescribe?

**Evidence.** The exact decode has no spaces (reproduced). Only two labels are literal soup text. `matrixsumlist` = row/column sums is labelled INFERRED by C's own audit. `yellowblueprimes` has an undocumented lab default (`7233147103127`). The handle confirms primes are "required to proceed" and "some characters need to be 'zeroed out'" (2021-12-26); "yinyang" is "the next phase" (2025-04-28); "Once you hit a 'ying yang', you'll be able to solve it the same day" (2023-08-06).

**Assumptions.** Word boundaries; that "zeroed out" and "primes" act on the soup blocks; the serialisation of numeric values.

**Alternatives.** Values to concatenate/hash; operations on DBBI/FAED (e.g. prime-position zeroing producing `yinyang`); a dependency list.

**Prior coverage.** C's harness tests the literal four-label concatenation (fails); many value guesses in C (~358k passphrases), all readability-gated and mostly SHA-256.

**Prediction.** A correct operations reading should output the literal word `yinyang` (or "ying yang") from a held block without tuning, giving a reject-capable checkpoint that a values reading lacks.

**Discriminator.** A typed operation table using only creator-attributed operations (primes, zero-out, sums) whose output is checkable against the literal milestone word.

**Assessment.** Decoding reproduced; grammar unestablished. The operations reading has the better-defined checkpoint ("ying yang" as an output) and is the only one that would make the 2023-08-06 "solve it the same day" statement testable. This is a hypothesis, not a finding.

### 9.4 Does chain 4 validate the Cosmic output?

**Question.** Is the masked nested envelope evidence that `OUT-cosmic` is a real stage?

**Evidence.** The mask `b657264f2f6e6921` = `OUT-cosmic[158:166]` XOR `Salted__` (reproduced). Applying the same rule to `OUT-cosmic-A` yields another envelope (reproduced). Offset 158 = 2x(32+32+15), the layout imposed by the analyst. The chain-4 password reuses `E_C`/`E_S`/`E_B`. [A#84]'s 1,168-byte hash is reconciled with nothing.

**Assumptions.** Offset, trim, mask and password composition.

**Alternatives.** Intended nested container vs fitted crib.

**Prior coverage.** Prior section 9.4 anticipated the forced header.

**Prediction.** A real nested envelope would be visible without a mask fitted to the target header.

**Discriminator.** A clue-derived rule that computes the mask without reference to `Salted__`. None exists in any source.

**Assessment.** Mechanics reproduced. The header is **not evidence**: the crib control demonstrates that this rule turns any 1,327-byte decrypt into an "envelope". Chain 4's 1,151-byte output is a padding pass on a fitted object.

### 9.5 Is there a bounded-key interval or seed model?

**Question.** Does any source supply a finite search region or generator?

**Evidence.** None found in any of the three repos, the transcript or the dataset. The handle says the target is a "Regular Bitcoin Private key" (2024-01-26) and that "a few might not require the internet anymore" (2021-01-21). The "neighbors, half and double" OP_RETURN points to P+/-G, P/2, 2P (reported); the handle confirmed that on-chain messages are not his (id 12653). Naddiseo identifies a circulating `keyinfo.txt` as his own split-key vanity tooling [A#109 comment 5903808733].

**Assessment.** No bound; computational escalation is not justified (prior section 9.5, unchanged).

### 9.6 Hypothesis matrix (updated)

| Interpretation | New support | New counter-evidence | Status |
|---|---|---|---|
| Remaining objects encode readable instructions | creator "Breaking salphation should give the feeling of the phase's name"; every solved stage produced text | -- | open; consistent with all held evidence |
| Remaining objects are binary key material reached by M5/M6 | -- | admitted token search; 2023 control; Set A refuted; crib control; no E_S definition | weakened |
| Labels are operations on DBBI/FAED producing "yinyang" | primes required, zeroing required, yinyang = "next phase", "same day" | no typed specification exists | open, testable in principle |
| Labels are values to concatenate | -- | label values unauthenticated; literal form fails | open, under-specified |
| BTCSEED is a seed instruction | -- | no generator; structure explained by coordinates | unchanged |
| A bounded interval exists | -- | no source | unchanged |

## 10. The prior report's five next checks

| # | Prior question | What the three repos allowed | Still blocked by (exact missing input) |
|---|---|---|---|
| 1 | Was `E_S` published independently before the recipe? | Searched the full Telegram transcript (51,177 messages to 2026-06-12), C's 510-record dataset to 2026-09-01, all A/B/C threads and PR files: `E_S`, `740a25de`, `38d4f4c9`, `5K2byJMssx` never appear before [A#68 comment 3704010992]; the transcript never contains them at all. No creator-attributed checksum/verification statement exists. The only earlier 79-byte reference is a file name, `salphaseion_plain_79.bin`, in A PR #93's Telegram attachment listing. | the bytes and post date of `salphaseion_plain_79.bin` (a Telegram ChatExport attachment not shipped in any repo); Telegram messages after 2026-06-12 other than @SoWut's. **Stop condition met** for the repos. |
| 2 | Is the chain-4 mask/offset clue-derived? | No source derives offset 158, the trim or the mask; offset 158 = 2x79 from the imposed layout; the crib control reproduces the "envelope" phenomenon on another decrypt. | none needed to conclude "fitted"; a pre-fit derivation would have to come from the recipe's author (GalloClaudio64), who published none. **Stop condition met.** |
| 3 | Which creator constraints survive complete original context? | Done for every promoted row via transcript + dataset reply targets: FEFEFE/104 removed (solver text, creator called it a typo); {2,3,5,7} removed (solver's); friends/family = succession; encrypted-online-key = solver wording, no container; entry recipe = Deleted Account; Christmas date corrected. | verified numeric account ids (absent from the transcript; C's dataset has none for @SoWut); the raw Telegram JSON/HTML export behind both (`ChatExport`, cited by A PR #93's `parse_chat.py`, group id `1166734859` per [A#114 body]). |
| 4 | Can a labels-as-values or labels-as-operations reading be fully specified? | New creator-context constraints narrow the operations reading (primes required; zeroing; yinyang = next phase; "same day"). No source provides a typed table; C's 4-label literal fails. | a creator-defined meaning for `matrixsumlist` / `yellowblueprimes`, or a reading whose output is the literal milestone word. First unspecified transformation: what "zeroed out" acts on, and the prime index convention. |
| 5 | Is there an uncovered BTCSEED continuation? | First appearance dated (Sycorax 2025-06-11, [T L122236]); B PR #9 output hash equals ours; [A#112] mentions "BTCSEED sha256 15d62c82..." without stating the object; [A#115] is a different FAED construction. No generator or suffix encoding anywhere. | E054 and any generator specification; the object behind [A#112]'s hash. **Stop condition met.** |

## 11. New next checks

At most five evidence questions -- **not** authorisations for sweeps.

| Rank | Question | Smallest discriminating check | Stop condition |
|---:|---|---|---|
| 1 | Does any **operations** reading of the creator-confirmed themes (primes + zero-out + sums) turn DBBI or FAED into the literal word `yinyang`/`yingyang` without free parameters? | Write a typed specification (inputs, prime convention, what is zeroed, output alphabet) **before** running anything; pre-register it; run once. | stop if the specification needs a parameter not fixed by a creator-attributed statement. |
| 2 | When and with what context did `salphaseion_plain_79.bin` first circulate? | Obtain the ChatExport attachment and its message from the Telegram export (group `1166734859`) -- a retrieval, not a computation. | stop if the file is unavailable. |
| 3 | What produced `cosmic_A.bin` and [A#84]'s `a80a399a...`? | Ask the posters for exact recipes; byte-compare. | stop if no recipe is supplied; both remain unverified objects. |
| 4 | Does the "Dualite" title [A:_pr102/README.md@7656174] exist in any capture? | Inspect the 2023-06-01 / 2023-11-27 captures cited by C and B PR #15 (not held). | stop if they match the held captures. |
| 5 | Is there a pre-2026 published definition of any 79-byte field? | Search Reddit/Discord/bitcointalk archives named in the sources (outside the three repos). | stop on absence; M5 stays unverified. |

## 12. Validation

| Gate | Work | Verdict |
|---|---|---|
| A -- collection | 3 subtree imports at frozen HEADs; 17 PR heads + 2 branches tagged and unique files imported; issues/PRs/comments/reviews/review comments/files/commits via the REST API (unauthenticated, paced); attachments attempted | see `MANIFEST.md` section 2 and section 5 for counts and gaps |
| B -- dedup | every file hashed; byte-identical groups and near-identical variant groups with diffs; `check_manifest.py` | `MANIFEST.md` section 3-4 |
| C -- reproduction | 32 records; 18 comparisons with prior-report or published values confirmed (17 against the prior report), 0 discrepancies; Python vs OpenSSL agree on every AES path; iconv vs Python cp273 agree on CP1141 | `reproduction/results/reproduction_results.json` |
| D -- adversarial | crib control, 2023 control, Set A refutation, self-reference of digests, circular E_C validation, selection evidence | this report section 9 |
| E -- provenance | every claim cited; extraction agents' notes preserved in `reference/data/extraction/`; repository content treated as data (`reference/data/INJECTIONS.jsonl`) | performed by this build; not external review |

No transaction was signed or broadcast, no live form was contacted, no keyspace or candidate sweep was run, and no private key was imported anywhere. The WIF used in section 9.2 is a published puzzle intermediate, used only as an AES password string.
