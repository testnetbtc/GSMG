# REPORT_ANALYSIS -- Task 1, Stages A and B

Scrutiny of the six agent reports in `reports/agent_responses/` (hashes verified against that
folder's README: all six match). Yardstick: the repo's own records (`reference/03-07`,
`reference/data/CREATOR_CLUES.jsonl`, `reference/data/EXPERIMENT_COVERAGE.csv`, the creator
dataset, the transcript, `research/2026-10-15_SESSION_JOURNAL.md`, `walkthrough/08-11`,
`sources/naddiseo/_pr15/neo/LEDGER.md`). Clue IDs refer to `SOLVE/CLUES.md`.

Verdict words: **VERIFIED** (checked against a held source), **CONTRADICTED** (a held source
says otherwise), **UNVERIFIABLE** (rests only on material the repo does not hold),
**INTERPRETATION** (a reading, labelled as such or not). Experiment totals are **reported**
unless scripts and results are in the repo.

**Declaration of interest.** Report 3 is this agent's own earlier answer (same session,
2026-10-22). It is scrutinised with the same table and the same standard as the others, and
its errors are listed without softening.

---

## Stage A -- one dossier per report

### A.1 Report 1 -- "GSMG.IO 5 BTC Puzzle -- Honest Assessment"

**1. Scope and basis.** Says it used the archive, the full transcript and creator dataset, and
"a fresh experiment session (nine predeclared families, ~6.5M decrypts, exact secp256k1/address
oracle -- all null)". Sources the repo does not hold: that session (no scripts, manifests or
results); the totals "~380M decrypts, 1.4B graded keys" (the closest held figures are
floflo777's ~335M submissions [prior report section 7 = `PRIOR-E001`] and A#106's "~2.5B"
[`EXT-E0017`]); the text of *Looking Forward*; the bytes of `salphaseion_plain_79.bin` (only
its name and size, 79 B, are held [A:_pr93/_work/files_listing.txt@2c97f44 L119]). Claims
resting only on these are reported, unverifiable.

**2. Claim table.**

| # | Claim | Section | Type | Checked against | Verdict | Notes |
|---|---|---|---|---|---|---|
| R1-C1 | There is no checkpoint past SalPhaseIon; only the 2019 hash and the website form ever verified anything | Why 1 | fact | `reference/03_UNRESOLVED.md` section 1; C-01 | VERIFIED | -- |
| R1-C2 | "the recipe's four values ... must all be right before anything opens" | Why 1 | interpretation | `reference/03` section 4; v2 section 9.3 | INTERPRETATION | assumes labels = values and one password; the archive leaves values vs operations open |
| R1-C3 | "~380M decrypts, 1.4B graded keys" | Why 2 | statistic | `reference/06`, `EXPERIMENT_COVERAGE.csv`, MASTER report | UNVERIFIABLE | no such totals in the archive |
| R1-C4 | fresh 6.5M clue-interpolated decrypts, nine families, all null | Basis, Why 2 | experiment | repo | UNVERIFIABLE | reported only |
| R1-C5 | values "hand-chosen by one person in two sloppy days in April 2019" | Why 2 | creator quote | C-47 (70336 "Couple hours", 70377 "Same same" to "two sloppy days") | VERIFIED (substance) | the original "two sloppy days" message is quoted by a solver (70373); the handle said "Same same" |
| R1-C6 | "By his own words he forgot the details by 2021" | Why 3 | creator quote | S-08: [T L65060] posted by "Jerry" 2024-04-11 as a forward; D-06 | CONTRADICTED (attribution/date) | second-hand; the held first-person statement is C-42 (hidden laptop, 2026) |
| R1-C7 | 104/FEFEFE numerology, {2,3,5,7} and the April Fools doors were solver text or banter | Why 3 | fact | S-01, S-02, C-18, C-22; `reference/07` section 2.3 | VERIFIED | -- |
| R1-C8 | ~1-in-256 wrong passwords "open" with valid padding; MD5 chains are "demonstrably this artifact"; most sweeps used validators blind to binary output | Why 4 | fact + interpretation | `reference/03` section 1; `reference/06` section 1; `reference/05` section 4 | VERIFIED / INTERPRETATION | the archive says "consistent with an accident, not proven to be one" |
| R1-C9 | "The strongest hint says the key is personal" | Why 5 | interpretation | C-43; D-03 | INTERPRETATION | one of two readings; C-30(b), C-32, C-35 cut the other way |
| R1-C10 | the archive's section 9.3: the operations reading is the only one with a reject-capable checkpoint and the only one that makes "same day" true | What | fact about v2 | `reports/REASONING_REPORT_v2.md` section 9.3 | VERIFIED | v2 says "better-defined checkpoint ... only one that would make the 2023-08-06 statement testable"; "hypothesis, not a finding" |
| R1-C11 | the creator "released one [checkpoint] every single time progress stalled (2019 hash, 2020 poem, 2021 mini-hint, 2023 binary, 2026 binary)" | What | interpretation | C-01, C-06, C-25, C-28, C-39 | CONTRADICTED as stated | these are hints; only C-01 is a checkpoint; the 2026 binary carries no puzzle content |
| R1-C12 | `salphaseion_plain_79.bin` is named in A PR #93's listing; "the only 79-byte reference predating the community chains" | How 1 | fact | files_listing.txt L119; `reference/03` section 1.1; v2 section 10 row 1 | VERIFIED (name, size) | "predating" is unverified: the listing is undated |
| R1-C13 | *Looking Forward* is "the 'Bingo'-confirmed reading (2026-03-03)" | How 1 | interpretation | D-01: recovered context [B:_pr15/unverified/recovered_reply_context_2026-09-26.txt@1e913fd]; B PR#15 ticks 60, 79-80 (`sources/discussions/naddiseo/pulls/015.md` L346-347) | CONTRADICTED | "Bingo" follows the Cartman quote; Jrk never answered the *Looking Forward* question; the direction was pre-registered and closed |
| R1-C14 | next step: primes + zero-out + sums with a typed specification; success = literal `yinyang` | How 2 | recommendation | v2 section 11 rank 1; `research/2026-10-15_yinyang_ops` (228 ops, none), `zero_merge` (exhaustive, none) | partly tried | the typed primes+zero-out+sums spec itself has not been written |
| R1-C15 | ask the creator publicly for a hash of the yinyang value, citing 2019 | How 3 | recommendation | C-01; C-30(d) | INTERPRETATION | a hash is not a hint; the creator has refused hints, not hashes |
| R1-C16 | the prize moves within hours of yinyang ("I only need to look at the address...") | How 4 | creator quote | C-38 ("2 hours max"), C-40 | VERIFIED (paraphrase) | -- |
| R1-C17 | Shor against the exposed key; creator jokes about qubits and worries about BIP-360 | No matter what | fact | C-44; [C id 66555, 66590, 66909] | VERIFIED | -- |
| R1-C18 | giveit/givetit: a silent typo made a stage "nearly impossible" | Questions | creator quote | [T L2070] (C-03) | VERIFIED | -- |
| R1-C19 | "If wallet != empty, puzzle not solved. (Most likely.)" | Questions | creator quote | C-37 [T L90253] | VERIFIED | -- |
| R1-C20 | "Same same" (2026-09-01) "says the method is uniform across objects (DBBI, grid, FAED)" | Questions | interpretation | C-47: 70377 replies to 70373 ("two sloppy days"?) | CONTRADICTED | it compares two build-time statements |
| R1-C21 | prize ~1.2565 BTC, 17ucy ~3.7506 BTC unspent | Method note | statistic | `reference/03` section 6 (1.25649674 on 2026-10-14; 3.75055310) | VERIFIED (consistent) | -- |
| R1-C22 | the creator fears the puzzle looking like a scam | What | creator quote | C-30(d) [T L22864] | VERIFIED | -- |

**3. Errors and overreach.** R1-C6 (a relayed 2024 forward presented as the creator's own 2021
words); R1-C11 (hints recast as checkpoints to build a "pattern"); R1-C13 (a disputed "Bingo"
promoted to a confirmation, and the Fresco direction presented as open although B PR#15 closed
it); R1-C20 ("Same same" misread); "demonstrably this artifact" (R1-C8) and "the missing values
aren't derivable from public material" (Why 2) state the stronger of two live readings as fact.

**4. Unique contributions.** (a) The explicit ordering "retrieval before computation"; (b) the
2019 precedent framed as a request for a *hash*, not a hint -- which survives scrutiny as an
option for the user; (c) the address as a free canary (supported by C-20 and C-40); (d) the
observation that each new test family "fixed a mechanism, not a value" -- a fair diagnosis of
the null results in `research/`. Its 6.5M session cannot be assessed.

**5. Ways forward proposed (verbatim).**
- R1-W1: "Obtain ... `salphaseion_plain_79.bin` -- the Telegram ChatExport attachment (group `1166734859`) named in A PR #93's file listing"
- R1-W2: "the text of *Looking Forward* (Jacque Fresco & Ken Keyes Jr., 1969)"
- R1-W3: "One pre-registered, parameter-free operations test. Primes + zero-out + sums, with a typed specification ... success criterion = the literal word `yinyang`"
- R1-W4: "Collective pressure for a checkpoint. Ask the creator publicly for a hash of the yinyang value, citing the 2019 precedent"
- R1-W5: "Watch the address."

**6. Reliability grade: C.** Of 22 claims, 13 verified, 4 contradicted (C6, C11, C13, C20),
3 unverifiable totals, the rest interpretations stated as facts. The contradictions all run in
the same direction -- reactions and banter read as confirmations -- which is the failure mode
the archive documents for the community. The structural points (C1, C7, C8, C16-C19) are right.

---

### A.2 Report 2 -- "GSMG -- honest solvability assessment"

**1. Scope and basis.** An evidence review; "No new puzzle experiment, password trial,
decryption campaign or interval search was performed." It checked the public HEAD (`d4db275`)
through the GitHub API and cites "local task packages" (September artifact checks, October
parser/marker/payload reports, a seed/bound ledger) and "VPS summaries". Sources the repo does
not hold: every row marked "Executed here" or "Operator-reported" in its table (none has
scripts or results in this repo); upstream issue #117 (the archive holds A#1-#116; the GitHub
API is not reachable from this session); "the extra padding clarification on Naddiseo #17".

**2. Claim table.**

| # | Claim | Section | Type | Checked against | Verdict | Notes |
|---|---|---|---|---|---|---|
| R2-C1 | the reviewed record contains no publicly verified complete solution | 1 | fact | `reference/03` ("No open object ... has an independently validated significance") | VERIFIED | -- |
| R2-C2 | the frontier has lost the link between object, operation and recognisable next result; a constraint problem before a computation problem | 1 | interpretation | v2 sections 9.3, 9.6 | INTERPRETATION | consistent with the archive |
| R2-C3 | CBC padding is not authentication; a reproduced hash proves repetition, not intent; re-encryption is not confirmation | 1 | fact | `reference/05` section 2; `EXT-E0004` (round trip "tautological") | VERIFIED | -- |
| R2-C4 | some recognizers discard binary intermediates, others accept padding-only accidents; totals cannot be summed | 1 | fact | `reference/06` section 1 | VERIFIED | -- |
| R2-C5 | "Our corrected DBBI parser ... an earlier negative did not cover the reproducible grammar"; "Exact prime-token DBBI grammar: exactly two complete parses; both match 20 URL-parity prefix bits" | 1, table | experiment | repo: `reference/03` section 2 (the 83/84-token parses "not located"); `EXT-E0146` (a ~20-bit DBBI yellow/blue vs grid match that did NOT reproduce under C's re-test) | UNVERIFIABLE | the only related held record is a failed reproduction of a similar 20-bit claim; flagged |
| R2-C6 | 329 register rows = 288 reported + 41 source-reproduced | failures | statistic | recount of `EXPERIMENT_COVERAGE.csv` | VERIFIED | exact |
| R2-C7 | 642 archived issue comments, four review records, one review comment, two counter mismatches | scope | statistic | `MANIFEST.md` L45-56 (605+35+2 = 642; A#25 19/18, B#2 2/1); `reference/07` section 3 | VERIFIED | -- |
| R2-C8 | upstream issue #117 (21 Oct) argues impossibility from remarks; its "dead laptop" wording is stronger than the held statement | questions | fact | archive holds A#1-#116; API blocked here | UNVERIFIABLE | the held statement is C-42 ("hidden laptop ... haven't touched in years") |
| R2-C9 | "A same-funder earlier branded address is reported" | findings 6 | fact | B LEDGER tick 38: `1EtbTv...` -> `1GSMG1CLx...` (2018), -> prize (2019) | VERIFIED (reported) | -- |
| R2-C10 | no held source identifies a unique book text/normalisation; the title is a lead, not an extraction rule | findings 7 | fact | C-26 (referent inferred); `EXT-E0304` (OCR search 0/27) | VERIFIED | -- |
| R2-C11 | no established scalar interval, generator or stopping distance; a vanity prefix permits several creation procedures | findings 5 | fact | v2 section 9.5; `reference/07` ("vanity argument is a non sequitur") | VERIFIED | -- |
| R2-C12 | kangaroo tests A/B: cap 6x not 4x; BSGS replay of 497 starts, m < 2^28, null | table | operator-reported | held: `research/2026-10-15_btcseed_bits` (784 seeds, +/-2^28, null) | PARTIAL / UNVERIFIABLE | the held replay has 784 seeds, not 497; the kangaroo runs are not held |
| R2-C13 | September closure audit: 581,875 records reproduced, 627,363 outputs graded | table | operator report | not held | UNVERIFIABLE | -- |
| R2-C14 | ten non-separator soup segments are a description, not proof of ten password ingredients | findings 2 | interpretation | `walkthrough/08` | INTERPRETATION (sound) | -- |
| R2-C15 | the first-five-marker/square dependency and the alternating-alphabet restriction reduce BTCSEED's independent evidence | findings 3 | interpretation | `walkthrough/10` (period-2 structure is forced) | INTERPRETATION (consistent) | -- |
| R2-C16 | nine "corrections to rules" | corrections | argument | -- | proposals | recorded in Stage B.6 |
| R2-C17 | single clarification worth asking: "What existing object does the instruction about characters being zeroed out apply to?" | questions | recommendation | C-25 | INTERPRETATION | a user decision |
| R2-C18 | it did not check balances; a balance cannot establish what everyone knows | 1 | scope | C-37 | VERIFIED (consistent) | -- |

**3. Errors and overreach.** None of its checkable factual claims failed. The weakness is
different: a whole table of "Executed here" / "Operator-reported" results that this repo
cannot see, presented alongside repo-recorded ones; R2-C5 asserts a concrete "record error"
(a parser the earlier negative "did not cover") without any held artifact, while the nearest
held record is a failed reproduction. Its BSGS/kangaroo numbers do not match the held replay.
It chooses no direction and says so.

**4. Unique contributions.** The four-way evidence typology (executed / repo-recorded /
operator-reported / proposed) -- adopted below for every experiment claim; the nine rule
corrections (several are right as stated, see B.6); the point that a text-only or final-output
recognizer could miss a *correct intermediate* (independently raised by R6); the clarification
question (R2-C17), which would name the operand of C-25 without giving away the answer.

**5. Ways forward proposed (verbatim).**
- R2-W1: "recover a sequence of locally justified, independently checkable transitions ... specify the operation, check exact prior coverage, predict something not used to choose the operation, and evaluate the complete result"
- R2-W2: "What existing object does the instruction about characters being zeroed out apply to?" (a question to the creator)
- R2-W3: "Compare source accuracy, handling of counterevidence, exact coverage and testable predictions" (how to compare agents)
- R2-W4 (implicit): explain the BTCSEED residual and the marker-order structure before building on them

**6. Reliability grade: B.** Every checkable claim survived (C1, C3, C4, C6, C7, C9-C11, C18);
nothing contradicted. Held back from A by the volume of unverifiable local work it leans on,
one unsupported "record error" (C5) and the absence of any direction.

---

### A.3 Report 3 -- "GSMG 5 BTC puzzle -- evidence-based assessment" (this agent's own report)

**1. Scope and basis.** Repo-only; no experiments; says it read the walkthrough, reference
files, both prior reports, the research journals, the B PR#15 ledger, all 411 creator text
messages, the parsed creator dataset, transcript windows and ~27 threads first-hand, the rest
via the extraction notes. All of that is held. It also leans on two things that are weaker than
it says: the recovered "Bingo" context (USER-grade screenshot) and B PR#15's on-chain readings
(interpretations). Nothing external is cited.

**2. Claim table.**

| # | Claim | Section | Type | Checked against | Verdict | Notes |
|---|---|---|---|---|---|---|
| R3-C1 | one convention for all solved stages; one checkpoint (2019); padding false positives 1/243 (300k) and 1/236 (49,664) | 1.1 | fact | `reference/03` section 1; `reference/data/extraction/D2.md` L83 (A#106) | VERIFIED | -- |
| R3-C2 | every community opening has the 1-byte-pad shape; three need MD5; the 2023 A#15 control | 1.1 | fact | `reference/03`, `05`, `07` P9 | VERIFIED | chain 4 also uses MD5; the 103x103 construction is not an AES opening |
| R3-C3 | the 2023 binary names the labels in order; `yellowblueprimes` is not in the soup | 1.2 | fact | C-28; A-07 | VERIFIED | -- |
| R3-C4 | `1GSMG1...` is a ~58^5 vanity prefix, "so the private key is stored inside a container, not derived" | 1.3 | interpretation | `reference/07` section 2.3 ("the vanity argument is a non sequitur"); v2 section 9.5 | OVERREACH | prefix-filtering does not exclude deterministic derivations; the "Only 4 chars" remark is in a corpus the repo does not hold |
| R3-C5 | negatives: 640 scalars, 64 brain wallets, BSGS +/-2^28 x 784 seeds, MITM halves, 0/66 BTCSEED keys | 1.3 | experiment | `research/2026-10-15_SESSION_JOURNAL.md`; B LEDGER tick 37; [B#13] | VERIFIED (held) | -- |
| R3-C6 | "Couple hours", "two sloppy days", "Same same", "I rushed (t)it", "800% frenzy" | 1.4 | creator quotes | C-47; [C id 66561, 66589] | VERIFIED | -- |
| R3-C7 | Cosmic Set-B proposer admitted a "p5-p7 search"; chain-4 mask is a crib fit; 103x103 parameters fitted | 1.5 | fact | `reference/07` P8, P11; `reference/05` M7, M8 | VERIFIED | -- |
| R3-C8 | B PR#15 concluded "terminal state" | 1.6 | fact (reported) | B LEDGER tick 35 | VERIFIED (reported) | B's conclusion, not a finding |
| R3-C9 | "~60% recognition step on public material; ~40% personal knowledge" | 1.6 | judgment | -- | INTERPRETATION | labelled as such |
| R3-C10 | "Bingo" followed the Cartman quote | corrections | fact | D-01 (USER-grade context) | VERIFIED (USER-grade) | should have said the context is a screenshot, not an export |
| R3-C11 | "Looks at gnomad" pointed at "no hints, only free will" | corrections | fact | same source | VERIFIED (USER-grade) | -- |
| R3-C12 | the *Looking Forward* lead was pre-registered and closed (B ticks 79-80) | corrections | fact | `sources/discussions/naddiseo/pulls/015.md` L346-347; `_pr15/neo/intake/2026-09-26-fresco/PREREG.md` | VERIFIED | -- |
| R3-C13 | "Pfff. Coincidence." most likely targeted the YOUWON/VIC claim | corrections | interpretation | D-02 (dataset note; reply_to null) | INTERPRETATION | -- |
| R3-C14 | "the creator's own on-chain stamp convention, compressed-P2PKH(sha256(X)) -- he used it in 2020 to confirm every solved stage"; `1NULY7...` "creator-stamped" | 2 R2(b), 5 | interpretation stated as fact | C-31 ("blockchain messages are not his and are not part of the puzzle" -- "Correct"); `reference/03` section 5 ("Who sent it is unknown"); B LEDGER ticks 37-39, 59, 63 (B's attribution rests on the prize key having spent a dust output it received) | CONTRADICTED / DISPUTED (D-05) | the substantive error of the report: B PR#15's reading presented as the creator's convention |
| R3-C15 | "the creator says yinyang is 'the next phase' reached after decoding an AES ciphertext (#39237)" | 3.4, 5 | creator quote (paraphrase) | C-38; `reference/04` ("the AES part of the question is not explicitly affirmed") | OVERREACH | the AES clause is the solver's question |
| R3-C16 | the soup places `thispassword` / `enter` / `shabef...` around the two base64 halves of `salph_inner` | 3.4 | fact | A-07 | VERIFIED | -- |
| R3-C17 | "the January-2020 hint missing from GitHub (creator-confirmed, #4094)" listed among early material to obtain | 2 R4 | fact | C-13: 4094 "It is" / 4096 "This one" -- the January hint is the Roses poem, which is held (C-06) | MISLEADING | it was missing from a GitHub hints page in May 2020, not from the record |
| R3-C18 | "He has floated moving the coins because of BIP-360 (#66555)" | 4 | creator quote (paraphrase) | [C id 66555] "if bip360 is going to be a thing. I have to come up with something." | OVERREACH | "come up with something" is not "move the coins" |
| R3-C19 | search volumes ~33.5M (C), ~33M/52 campaigns (B), ~2.5B (A#106, unaudited), ~14.8M (endgame sheet) | 2 R3 | statistic | `reference/06` section 1; `_pr15/unverified/endgame_aes_password_search.md` L3 | VERIFIED (reported figures) | -- |
| R3-C20 | the halving mirror predicts 0.625 BTC moved around 2028 | 5 | interpretation | B LEDGER tick 61 | INTERPRETATION | -- |
| R3-C21 | 2021-07-18 "neighbors, half and double" dust to P+/-G, P/2, 2P | 5 | fact (reported) | `reference/03` section 5 | VERIFIED (reported; sender unknown) | -- |
| R3-C22 | evidence favours `salph_inner` as the next container | 3.4, 5 | interpretation | rests partly on R3-C15 | INTERPRETATION | weakened by the C15 overreach |
| R3-C23 | the five routes ("no sixth") | 4 | interpretation | -- | INTERPRETATION | -- |

**3. Errors and overreach.** R3-C14 is a real error: an inferred on-chain "stamp convention"
written as the creator's own, in direct tension with C-31, and then used as a proposed oracle.
R3-C15 and R3-C18 paraphrase beyond the words. R3-C17 implies a missing hint that is in fact
held. R3-C4 repeats the vanity non sequitur the archive had already flagged. The 60/40 figure
is a judgment presented with a precision it does not have.

**4. Unique contributions.** The "three undefined inputs + undefined combiner" framing of
C-28; the corrections list (Bingo, gnomad, Fresco closed, Pfff target) -- three of four hold,
the fourth is a reading; the extra questions (has the three-input model been falsified? which
container is next? what is `1NULY7...`'s preimage?); and the proposal to use on-chain addresses
as zero-cost oracles, which this review downgrades to a *secondary* check because D-05 is
disputed.

**5. Ways forward proposed (verbatim).**
- R3-W1: "Freeze the oracles ... add the stamp check"
- R3-W2: "Pre-register every candidate -- derivation and expected string -- before testing it"
- R3-W3: "Enumerate the grammar ... Keep each dimension <= ~100 -> <= 10^7 total; run against all four containers plus the stamps"
- R3-W4: "Target `salph_inner` first"
- R3-W5: "the social route: obtain the Telegram export, talk to the 2019-2021 solvers, and study what the creator reacted to"
- R3-W6: "ask the creator for a checkpoint hash of the next stage rather than a hint"

**6. Reliability grade: B.** Of 23 claims, 14 verified, 1 contradicted/disputed (C14), 3
overreaches (C4, C15, C18), 1 misleading (C17), the rest labelled interpretations. The same
grade as Report 2 for a different reason: more direction and more first-hand checking, but
one substantive error that a reader would have carried into an oracle design.

---

### A.4 Report 4 -- "GSMG -- Solver brief" (a method, not an assessment)

**1. Scope and basis.** An earlier version of the Task-1 brief: the five laws, a map of the
repo, a six-part idea gate (G1-G6), a `SOLVE/` file set, a session ritual and safety rules. It
processes only the two archive reports (MASTER, v2) and the research journal. Not an
independent opinion; scrutinised here as a method.

**2. Claim table (the facts it says the system must carry, section 3).**

| # | Claim | Type | Checked against | Verdict | Notes |
|---|---|---|---|---|---|
| R4-C1 | a wrong key gives valid PKCS#7 ~1/256, almost always a 1-byte pad; every published opening has a 1-byte pad | fact | `reference/03` section 1 | VERIFIED | -- |
| R4-C2 | the Cosmic digest and the chain-4 "nested envelope" are self-referential; the mask is forced by construction | fact | `reference/05` section 2; v2 section 9.4 | VERIFIED | -- |
| R4-C3 | {2,3,5,7}, FEFEFE/104/101010, "encrypted private key stored online" are solvers' words | fact | S-01, S-02, S-03 | VERIFIED | -- |
| R4-C4 | creator disclaimers: typos are not clues (2020); OP_RETURN dust is not puzzle material (2023); the 2020 hint was not required | fact | C-07, C-31, C-04 | VERIFIED | note: C-31 is exactly what Report 3's stamp oracle ignored |
| R4-C5 | the 2023 decode, exact and without spaces | fact | C-28 | VERIFIED | -- |
| R4-C6 | the prize public key is public; `btclib.py` compares a candidate scalar's point exactly, offline | fact | `research/2026-10-15_btcseed_bits/btclib.py`; `reference/03` section 6 | VERIFIED | -- |
| R4-C7 | no authenticated value for `yellowblueprimes` or `yinyang`, no authenticated meaning for `matrixsumlist` | fact | `reference/03` section 4 | VERIFIED | -- |

**3. Soundness of the gate -- what it would wrongly reject or accept.**
- *Wrong rejections.* (a) G1 = 0 -> reject would throw out pure retrievals (the Telegram
  export, the PR93 attachments, a Decentraland re-fetch) that no report could anchor on a
  clue, yet most reports rank them highest; the fix is to anchor a retrieval on the clue whose
  context it recovers (C-13, C-26, C-40, C-46). (b) G3's ">2 FREE -> reject" would have passed
  Phase 2.2 part 5 (eight executive orders, one enumerated choice) but could reject the true
  construction if the creator's rushed build (C-47) involved three idiosyncratic choices; the
  Task-1 scale keeps the rule and makes the count explicit, which is right, but the user should
  know what it costs. (c) G4 ("fits the puzzle's own pattern": SHA-256/EVP, readable text)
  assumes the endgame keeps the solved-stage convention, while A-03 announces "twenty-three
  ciphers sixteen encryptions"; treat G4 as a score, never as a reject.
- *Wrong acceptances.* (d) G5's "readable English or a recognisable puzzle word" is subjective;
  require a word list or a dictionary-rate threshold fixed in advance. (e) The literal
  milestone must accept the creator's three spellings (`yinyang` C-28, `ying yang` C-30,
  `yingyang` C-38). (f) "a further envelope with a clue-derived password" is fine only if the
  derivation is written before the envelope is seen (chain 4 shows how a header is forced).
- *Ranking.* "Highest G1 first" favours clue-dense ideas over decisive ones; the Task-1 funnel's
  round 4 (decisiveness per cost) corrects this.
- *Overhead.* `HYPOTHESES.md`, `CLUE_COVERAGE.md`, `DEEP_THINK.md`, `RULES.md` and per-hypothesis
  work folders duplicate what `FUNNEL.md`, `SELECTED.md` and `CLUES.md` carry; the Task-1 brief
  supersedes this file set.

**4. Unique contributions.** The gate card itself (G1-G6) and the hard-reject list, which the
Task-1 scale inherits; the "solvers' words are not clues" and "self-referential checks" rules
as explicit system facts; the stop-immediately rule for a prize-key match.

**5. Ways forward proposed.** None as puzzle ideas; as process: R4-W1 "every idea ... goes
through this card before any compute is spent"; R4-W2 "PARK ... with the exact input needed so
the user can try to obtain it" (names `salphaseion_plain_79.bin`, the raw ChatExport, a Wayback
capture).

**6. Grade.** Not graded as an opinion. As a method: sound, with the six refinements above
(a-f) proposed to the user in B.6.

---

### A.5 Report 5 -- "GSMG 5 BTC puzzle: why it's unsolved, and how it could be solved"

**1. Scope and basis.** Claims Telegram "both groups, Apr 2018 -> 10 Oct 2026", every prior
agent report on a VPS, the repo at `d4db275`, "our test rounds 1-4" and the blockchain; says
it checked 61 creator quotes against the raw Telegram data. Its `SOL-` ids coincide with the C
dataset's message ids (checked for a dozen). Sources the repo does not hold: the second group
("COM-" ids: 28876, 28526/7, 26065, 28522, 67741, 67742); any `SOL-` id above 70377 (e.g.
message 74724) and the 2026-09-01 -> 2026-10-10 window; `EXHAUSTED.md` and the "~10^9" total;
test rounds 1-4 (44,767,476 decrypts); the "245.9 M recipe grammar"; the p32 padding census;
"470 scam records", "18,452 Solvers messages in 2026"; the live-site check of 2026-10-21.

**2. Claim table.**

| # | Claim | Section | Type | Checked against | Verdict | Notes |
|---|---|---|---|---|---|---|
| R5-C1 | prize 1.2565 BTC; 17ucy 3.7506 BTC never spent; next halving block 1,050,000 (~Apr 2028) | Where | statistic | `reference/03` section 6; arithmetic | VERIFIED | -- |
| R5-C2 | half moves to 17ucy at every halving, announced 2019-04-21 (COM-28876) | Where | creator quote | creator_jrk.txt L444 ("halving the price money at every bitcoin halving event"), L453 | VERIFIED (substance); COM id UNVERIFIABLE | -- |
| R5-C3 | a team got past the second route by Aug 2020 but was "stuck in the next phase" (SOL-4694) | Where | creator quote | [C id 4694] = [T L10635] (C-16) | VERIFIED | -- |
| R5-C4 | "Nr 5 in salph" by 2021-03-22 (SOL-6712) | Where | creator quote | [C id 6712] "Nr 5 in salph" | VERIFIED | -- |
| R5-C5 | never opened: dbbi, faed; four sealed blobs incl. urlblob (origin disputed) | Where | fact | `reference/03` section 1 | VERIFIED | -- |
| R5-C6 | nobody has reached yinyang (SOL-39237, SOL-60314) | Where | creator quotes | C-38, C-40 | VERIFIED | -- |
| R5-C7 | all agents ~10^9 guesses (EXHAUSTED.md); our 44.8M; validated openings 0 | Where | statistic | not held / `reference/03` | UNVERIFIABLE / VERIFIED (0 validated) | -- |
| R5-C8 | "The 'last' part of the puzzle will ensure that there's quite some time" (SOL-879) | 1.1 | creator quote | [C id 879] [T L2106] (C-02) | VERIFIED | -- |
| R5-C9 | the 2023 hint names four ingredients, none with a value; "I gave an unforseen hint already" (SOL-6509) | 1.1 | creator quotes | C-28, C-21 | VERIFIED | -- |
| R5-C10 | primes required (SOL-8000, 5966/5969, 8330); "zeroed out" (SOL-8000) | 1.1 | creator quotes | C-25, C-19, C-27 | VERIFIED | -- |
| R5-C11 | dbbi and faed use the labels' a-i letters but contain no "o", the zero digit | 1.1 | fact | letter counts recomputed from `salphaseion_soup.txt` | VERIFIED | -- |
| R5-C12 | "I checked the literal readings. Zeroing or deleting the prime positions gives random bytes." | 1.1 | experiment | not held; related held negatives: `research/2026-10-15_zero_merge`, `EXT-E0042` | UNVERIFIABLE (consistent) | -- |
| R5-C13 | ~1 in 255 passes padding; that fed the md5 chain (republished as B#17, 2026-10-05), btcseed, and message 74724 | 1.2 | fact | `reference/03`; [B#17] date 2026-10-05 | VERIFIED except: BTCSEED is a Bifid decode, not a padding event; 74724 not held | minor misclassification |
| R5-C14 | "two sloppy days" (COM-67741), "couple hours" (SOL-70336), "I rushed (t)it" (SOL-70311) | 1.3 | creator quotes | C-47 | VERIFIED (COM id unverifiable) | -- |
| R5-C15 | "tested the entire puzzle 3 times with the same string which had the typo in it" (SOL-871) | 1.3 | creator quote | [T L2083] (C-03) | VERIFIED | -- |
| R5-C16 | "I forgot the last details ..." (2021, a member's forward, SOL-24156) | 1.3 | relayed quote | S-08 [T L65060] posted 2024-04-11 by "Jerry" | RELAYED; 2021 date UNVERIFIABLE | correctly flagged as a forward |
| R5-C17 | "Most of you know the puzzle WAAAY better than me" (SOL-66568) [drinking] | 1.3 | creator quote | C-42 | VERIFIED | -- |
| R5-C18 | {1},{4},{21} disowned as April Fools (SOL-7529) | 1.4 | creator quote | C-22 | VERIFIED ("disowned" is a reading) | -- |
| R5-C19 | "high likely no hints anymore" (SOL-9621, 2023); "without giving any hints" (COM-67742, 2026) | 1.4 | creator quotes | [T L22864] / not held | VERIFIED / UNVERIFIABLE | -- |
| R5-C20 | the close-friends hint [drinking] vs the sober "You have all the info" (SOL-9607) and no internet (SOL-16624) | 1.5 | creator quotes | C-43, C-30(b), C-32; [C id 9607] answers "is there another URL to find? otherwise ... big brute force" | VERIFIED | the 9607 context adds: no further URL is needed |
| R5-C21 | early teams reported progress by private message (SOL-6497) | 1.6 | creator quote | C-20 | VERIFIED | -- |
| R5-C22 | 470 scam records; 18,452 Solvers messages in 2026 | 1.6 | statistic | post-transcript | UNVERIFIABLE | -- |
| R5-C23 | graders looked only for printable text; the biggest grammar sweep never ran on cosmic | 1.6 | fact / operator | `reference/06` section 1 / not held | VERIFIED / UNVERIFIABLE | -- |
| R5-C24 | vanity address ("few seconds ... Only 4 chars", COM-28526/7), so the key is effectively random | 1.7 | creator quote + interpretation | not held; `reference/07` (non sequitur) | UNVERIFIABLE + INTERPRETATION | -- |
| R5-C25 | judgement 60% intact / 25% outside piece / 15% broken | 1 | judgment | -- | INTERPRETATION | labelled |
| R5-C26 | one convention for every solved lock; md5 and sha1 fail | 2.1 | fact | `reference/01`; controls in `reproduce.py` | VERIFIED | -- |
| R5-C27 | accept only readable text / a full 16-byte pad (80-byte blob holding 64 hex) / a nested `Salted__` / an address match | 2.2 | recommendation | -- | sound | a 64-byte plaintext gives a 16-byte pad: correct arithmetic |
| R5-C28 | the end product is a "Regular Bitcoin Private key" (SOL-20223), "stored encrypted online (SOL-7830/7832/7834)" | 2.3 | creator quotes | C-33 / S-03 (assent to a solver's wording) | VERIFIED / OVERREACH | "stored encrypted online" is the solver's phrase |
| R5-C29 | cosmic is page-sized so probably the yinyang page; the 80-byte blobs are a 64-hex key plus padding | 2.3 | interpretation | -- | INTERPRETATION (labelled "inference") | -- |
| R5-C30 | drop btcseed, the md5 chain, 3GSMG24, {1},{4},{21}, YOUWON ("Pfff. Coincidence." most likely answered that morning's YOUWON/VIC post) | 3.1 | recommendation | D-02 | INTERPRETATION | -- |
| R5-C31 | "Bingo" followed a member quoting the Cartman line the creator had just mentioned | corrections | fact | D-01 source | VERIFIED (USER-grade) | -- |
| R5-C32 | several 2026 "creator" messages are members forwarding old posts ("Equivalent of 25 btc", "The puzzle talks for me", the Dutch lines) | corrections | fact | transcript: "Equivalent of 25 btc" occurs at 8 lines (L109998-L172327) | PLAUSIBLE, not fully checked | the C dataset's attribution per message was not re-audited here |
| R5-C33 | "Friends and family can get to all my data" (SOL-9595) is about succession | corrections | fact | S-07; `reference/07` P5 | VERIFIED | -- |
| R5-C34 | "it might appear unsolvable, but it's not" (SOL-8360, sober); "salphaseion is 100% solveable?" -> "Yes" (SOL-66588) | 4 | creator quotes | [C id 8360] / [C id 66588] "Yes" with the question not preserved in the dataset | VERIFIED / UNVERIFIABLE | -- |
| R5-C35 | the site went down in May 2026 (SOL-63942) and is back up; on 21 Oct its content matched the April 2026 copy | 5 | fact | C-41 / not checked (held: gsmg.io parked from 2026-07-07; a root "finale" page captured 2026-08-19) | VERIFIED / UNVERIFIABLE | if true, the April pages are served again under the finale root; no capture held |
| R5-C36 | tests A-E: 359,575 + 642,369 + 241,597 + 11,100; 44,767,476 decrypts; 176,187 padding passes vs 175,559 expected | 7 | experiment | not held | UNVERIFIABLE | the pass ratio (~1/254) is the expected chance rate, i.e. no signal |
| R5-C37 | the Phase-3.2 plaintext is only ~60% printable, so a partly-binary correct plaintext would have been missed by a >=90% gate | 7 | fact | `phase32_plaintext.bin`: 2,422 bytes, printable ratio 0.598 (recomputed) | VERIFIED | a good point against readability gates set high |
| R5-C38 | "p32 padding excess: 185 passes vs 148.5 expected" | 6.3 | statistic | not held | UNVERIFIABLE | at 1/255 over ~37,900 trials the excess is ~2.9 sigma; needs its manifest |

**3. Errors and overreach.** R5-C28 (a solver's wording as the creator's); R5-C13 (BTCSEED
listed as a padding event); R5-C16 ("2021" for a 2024 forward); R5-C35 (a live-site claim that
sits uneasily with the held captures). Otherwise disciplined: it tags intoxication, separates
"Judgement" from evidence, and corrects forwards.

**4. Unique contributions.** The [drinking] tagging; "decode before you decrypt" (a correct
decode proves itself); the context of 9607 ("You have all the info" answers "is there another
URL to find?"); the 16-byte-pad acceptance criterion; the untried specifics -- yellow/blue
selectors on dbbi/faed, "we won't" in the lastwords slot, the grid as a yin-yang logic puzzle,
the "unforseen hint" and "our first hint" reading tasks, the p32 padding census; the
observation that a >=90% printable gate would miss a Phase-3.2-like plaintext.

**5. Ways forward proposed (verbatim).**
- R5-W1: "Decode-first tests on dbbi and faed, judged by readability": (a) "Selectors from the image's yellow and blue cells"; (b) "The 2023 words read as operations, not values"; (c) "Prime selection combined with zeroing (SOL-8000)"
- R5-W2: "Reading only, no compute": (a) "Find the 'unforseen hint' for matrixsumlist"; (b) "Pin down 'our first hint'"
- R5-W3: "Cheap closures of known blind spots": (a) "Run the existing 245.9 M recipe grammar on cosmic, with sha256 and md5"; (b) "Regrade everything that passed the padding check, using a grader that also catches binary plaintext"; (c) "Audit the p32 padding excess"; (d) "Try 'we won't' in the lastwords slot"; (e) "Solve the 14x14 grid as a yin-yang logic puzzle"
- R5-W4: "Request the Telegram JSON export"
- R5-W5 (user decisions): "whether to use public facts the creator has posted about themselves"; "whether to report a suspected build error to the creator"

**6. Reliability grade: B.** Of 38 claims, 26 verified in whole or part, 0 contradicted, 10
unverifiable (second group, own tests, post-2026-09 messages), 2 overreaches. The most
carefully sourced of the six; held back from A because a third of its evidence base cannot be
seen from here.

---

### A.6 Report 6 -- "GSMG 5 BTC Puzzle -- Why It Remains Unsolved"

**1. Scope and basis.** Says it read the archive in full (116 issues, 17 PRs, ~640 comments),
the three source repositories' documents, "our own test record" (~240 million trials) and the
creator's Telegram messages. Sources the repo does not hold: the 240M trials; the probability
figures "about 4 in 10 million" and "about 1 in 1,400"; the "116,000-candidate sweep" voided by
a wrong KDF; the song's lyrics (the repo holds only chat quotations, S-12).

**2. Claim table.**

| # | Claim | Section | Type | Checked against | Verdict | Notes |
|---|---|---|---|---|---|---|
| R6-C1 | 116 issues, 17 pull requests, ~640 comments | scope | statistic | `MANIFEST.md` (103+10+3; 9+7+1; 642) | VERIFIED | -- |
| R6-C2 | ~1.25 BTC at the prize; 3.75 BTC at 17ucy | scope | statistic | `reference/03` section 6 | VERIFIED | -- |
| R6-C3 | one checkpoint (2019); padding 1/243 and 1/236; every claimed opening is one byte short of a block, random bytes | 1 | fact | `reference/03` section 1 | VERIFIED | -- |
| R6-C4 | the Cosmic decryption was copied and "verified" by >10 people over ~8 months; two different keys were claimed to give the same output | 1 | fact | `reference/05` M6/M6'; `reference/07` P10 | VERIFIED (the count is not audited) | -- |
| R6-C5 | the creator's hints are themes, not operations; the Phase-2 page gave formatting, SalPhaseIon gives none | 2 | fact | A-01, A-08 | VERIFIED | -- |
| R6-C6 | entry into SalPhaseIon took ~2 years and needed Roses, Decentraland and hash-the-text | 3 | fact | timeline (C-06 2020-01; C-08 2020-02; S-05 2021-05; C-20 2021-03) | VERIFIED | -- |
| R6-C7 | no operational hint since Feb 2023; in 2023 a further hint "would probably be a give away" | 3 | creator quote | [T L22864] (C-30d) | VERIFIED | -- |
| R6-C8 | FEFEFE/104 and {2,3,5,7} are solvers'; "#..# wasn't used / 2nd way wasn't found" is a community summary from Feb 2021 | 4 | fact | S-01, S-02; S-06 [T L13564] (Deleted Account, 2021-02-12) | VERIFIED | -- |
| R6-C9 | from 2025 LLM-generated solutions dominate; maintainers tell AI agents to ignore threads | 4 | fact | `reference/data/INJECTIONS.jsonl` | VERIFIED | -- |
| R6-C10 | "one public tool used the wrong [KDF], voiding a 116,000-candidate sweep" | 5 | fact | searched `reference/`, both archive reports, C docs: no such figure | UNVERIFIABLE | -- |
| R6-C11 | "Our own roughly 240 million trials share the same blind spot: an output that is raw key bytes ... would pass a padding check unnoticed" | 5 | experiment + fact | not held / `reference/06` section 1 | UNVERIFIABLE / VERIFIED | the blind spot is real for the held sweeps too (B LEDGER L1349: "No sliding windows") |
| R6-C12 | BTCSEED: "chance of that exact word under that key about 4 in 10 million"; "if any key ordering counts ... about 1 in 15" | 6 | statistic | held: 8/362,880 key permutations [B#13]; ~1/5,200 per recipe and ~1/15 for the Bifid family (etheral-dev, `walkthrough/10`) | UNVERIFIABLE; "4 in 10 million" is not a held figure | -- |
| R6-C13 | YOUWON "about 1 in 1,400 by chance"; the creator's only reaction was "Pfff. Coincidence." | 6 | statistic + interpretation | held: 0/200,000 shuffles; ~3.2e-6 at DBBI frequencies; a plantable offset ~21% once the layout is forced (B LEDGER L2540); D-02 | UNVERIFIABLE; target DISPUTED | -- |
| R6-C14 | the creator admits rushed work; "WAAAY better than me"; close friends "best chance"; "Some already found it"; "If wallet != empty" | 7 | creator quotes | C-42, C-43, C-45, C-37, C-47 | VERIFIED | -- |
| R6-C15 | "1 microstep", "the hardest part is done", "no need, you have all the info", and "the remaining steps are easier than the solved ones" | What | creator quotes | C-35, C-29, C-30(b) / the last is a solver's inference [T L24304] | VERIFIED x3 / OVERREACH x1 | -- |
| R6-C16 | the small envelope's plaintext can only be 64-79 bytes; "sha256 ans too" plausibly feeds Cosmic; yin yang "next phase", "same day", "2 hours max" | What | fact + interpretation | prior section 4.1; A-07; C-30(a), C-38 | VERIFIED / INTERPRETATION | -- |
| R6-C17 | vanity address, so the key was ground at random and must be written inside a plaintext | What | interpretation | `reference/07` ("non sequitur") | INTERPRETATION (contested) | -- |
| R6-C18 | the two spends used distinct ECDSA nonces | routes | fact | `reference/03` section 6; B campaign_45; `extraction/N2.md` L90 | VERIFIED (reported) | -- |
| R6-C19 | one team "managed to find something" (2020); another passed "partly" (2023) | questions | creator quotes | C-11, C-30(c) | VERIFIED | -- |
| R6-C20 | the puzzle used the song's first two parts verbatim; its third part turns on a choice between two roses and "has never been tried in the standard lock" | way forward 3 | fact + claim of non-coverage | S-12 [T L7943-L7947]; coverage: no row for "judgement"; `EXT-E0295` tried 15 lyric lines on the Phase-1 form only; discussed in chat 2019-04-24 [T L1069], 2020-05-21 [T L9850], 2023-08-20 [T L25685] | PLAUSIBLE; non-coverage is an absence of record, not a verified fact | -- |
| R6-C21 | the Phase-0 URL is the song's phase-one line | way forward 3 | fact | [T L32947] (a solver: "Png and the seed is planted are both phase one part a and b") | PLAUSIBLE (lyrics not held) | -- |
| R6-C22 | self-corrections: YOUWON now "unconfirmed"; BTCSEED "a probable intended intermediate" | corrections | judgment | -- | INTERPRETATION | the BTCSEED upgrade rests on its own unheld statistic |

**3. Errors and overreach.** Three statistics with no source in the archive (C10, C12, C13),
two of which conflict with held figures; one solver inference quoted as the creator's (C15);
the vanity non sequitur (C17); "more than ten people" unaudited. The structural account (C3-C9)
is accurate.

**4. Unique contributions.** The song's third part as an untested candidate (holds up as
"not recorded as tested"); the raw-key-bytes blind spot in *stored* padding-valid outputs
(holds up: no held sweep slid an exact-key oracle over them); the demand for a shared negatives
ledger (adopted: `GRAVEYARD.md`); the "two keys, same output, impossible" observation.

**5. Ways forward proposed (verbatim).**
- R6-W1: "re-check stored padding-valid outputs (and all future ones) for raw key material against the prize public key"
- R6-W2: "Work only the DBBI/FAED -> 'thispassword' step, starting from BTCSEED and YOUWON"
- R6-W3: "Test one untried lead ... [the song's] third part, which turns on a choice between two roses, has never been tried in the standard lock"
- R6-W4: "Request the Telegram JSON export"
- R6-W5: "Keep a shared ledger of negatives so nothing is repeated"
- R6-W6: "no oracle run until a reading's free checks pass and the test is written down in advance"

**6. Reliability grade: C.** Of 22 claims, 15 verified, 0 contradicted outright, 3 unsourced
statistics (two in tension with held figures), 2 overreaches. The grade is C rather than B
because the numbers it uses to rank its own leads (C12, C13) are the ones that cannot be
checked; with sourced statistics it would be a B.

---

## Stage B -- cross-report synthesis

### B.1 Agreement matrix

A = agrees, D = disagrees, P = partial / nuanced, S = silent. R4 is a method and is marked for
the assumptions its gate makes.

| Proposition | R1 | R2 | R3 | R4 | R5 | R6 |
|---|---|---|---|---|---|---|
| No checkpoint past SalPhaseIon; the only exact oracle is the prize address | A | A | A | A | A | A |
| The prize key is random (vanity) and so must be stored inside a container | A | D (several procedures possible) | A | S | A | A |
| Every community opening is a padding false positive | A ("demonstrably") | P (unvalidated, not proven accidental) | A (shape) | A | A | A |
| The missing input may be personal knowledge (C-43) | A (strongest hint) | P (possible, undemonstrated) | P (40%) | S | P (25%) | P (unquantifiable) |
| The key is derivable from public material | D | P (undetermined) | P (60%) | S | P (60%) | S |
| BTCSEED is intended | S | P (worth explaining) | D (do not build on it) | S | D (drop it) | A (probable) |
| YOUWON is intended | S | S | D | S | D | P (suggestive, unconfirmed) |
| *Looking Forward* / "Bingo" is a confirmed lead | A | S | D | S | D | S |
| The operations reading (labels as operations producing `yinyang`) is the best path | A | P (literal word is a detector, not a requirement) | S (grammar enumeration instead) | A (v2 pointer) | A | P (start from BTCSEED/YOUWON) |
| A new creator hint/checkpoint is the most likely unlock | A | S (clarification question) | A ("smallest ask") | S | P (uncertain) | P (one of four routes) |
| `salph_inner` is the next container | S | D (do not promote the ordering) | A | S | P (cosmic = yinyang page; 80-byte blobs = keys) | P (small envelope feeds Cosmic) |
| MD5-KDF openings are void because every solved stage uses SHA-256 | A | D (does not fix every object's KDF) | A | A | A | A |
| The 2023 labels are values to combine into one password | A | P (one of five architectures) | A (three inputs + combiner) | S | A (three things to find) | A |
| Retrieval (Telegram export / attachments) beats computation now | A | S | A | A (PARK) | A | A |
| Readable text is required of a correct opening | P | D (a recognised binary format could validate) | A | A | A (or a 16-byte pad) | A |

### B.2 Conflicts resolved

| # | Conflict | Evidence each side | Ruling | Citation | If the repo cannot settle it, what would |
|---|---|---|---|---|---|
| K1 | "Bingo" confirms *Looking Forward* (R1) vs a South Park quote (R3, R5) | R1: the 2026-03-03 sequence; R3/R5: the recovered screenshot shows "Bingo" after D1rty Byrd's Cartman line, and the *Looking Forward* question was never answered; B PR#15 pre-registered and closed the Fresco direction | reading 2; *Looking Forward* is not a lead | D-01; B PR#15 ticks 60, 79-80 | the JSON export's `reply_to` of message 60312 |
| K2 | vanity implies a random key stored in a container (R1, R3, R5, R6) vs several creation procedures (R2) | the archive calls the inference a non sequitur (prefix-filtering a deterministic generator is possible); no held model derives the key either | R2 is right on logic; in practice no bounded derivation exists, so the key is treated as "not computable by any held model", not as "random by proof" | `reference/07` section 2.3; v2 section 9.5 | a creator statement on how the key was made |
| K3 | personal-knowledge gate (R1) vs corpus-derivable (R3, R5) | C-43 (explicitly a hint) vs C-30(b), C-32, C-35, C-38, C-40 (all info available; offline; one microstep; same day) | unresolved; both readings coexist; no idea may assume either | D-03 | the creator (R2-W2's clarification), or a solve |
| K4 | BTCSEED intended (R6) vs unverified/drop (R3, R5) vs explain first (R2) | mechanics reproduced; forced structure; no generator; the creator never mentions it; C-46 may target it | significance unverified; it is a SOLVER construction and cannot anchor an idea (LAW 1), but may be an input where the anchoring lies elsewhere | S-10; `reference/03` section 3.1; `walkthrough/10` | a continuation that produces readable text or a prize-point hit |
| K5 | MD5 openings void (R1, R3, R5, R6) vs not proven for unopened objects (R2) | MD5 fails on all four solved stages (control); the envelope header names no digest | R2 is right that nothing fixes the unopened objects' KDF; LAW 4 nevertheless makes SHA-256 the sourced choice and MD5 a FREE parameter that must be declared | `reference/07` ("Does `Salted__` fix the KDF?"); A-01 | -- |
| K6 | the creator "forgot by 2021" (R1) vs a 2024 relay (S-08) | the only held text is a member's post of 2024-04-11 | relayed; use C-42 for the creator's own words | [T L65060]; D-06 | the forwarder's original |
| K7 | yinyang is reached "after decoding an AES ciphertext" (R3 par. 3.4, R5 sec. 2.3) vs not affirmed (`reference/04`) | the AES clause is the solver's question; the answer is "It's the next phase" | not affirmed; ideas must not assume yinyang is a container plaintext | C-38 | -- |
| K8 | the site is back up and matched the April copy on 2026-10-21 (R5) vs parked / finale page (held captures) | held: parked from 2026-07-07, finale root 2026-08-19; R5's check is not held | unresolved | `walkthrough/08` section 6; A-14 | a fresh capture by the user (no form submission) |
| K9 | R6's chance figures (4e-7; 1/1,400) vs the held figures (8/362,880 permutations; 0/200k shuffles, ~3.2e-6; 1/15 Bifid family) | R6's are unsourced | use the held figures and their stated conditioning | `walkthrough/10`; B LEDGER L2540; `_pr15/unverified/salphaseion_dbbi_youwon.md` L41, L113 | R6's derivation |
| K10 | the 2020 `3GSMG24...` dust is the creator's "stamp convention" (R3, after B PR#15) vs "blockchain messages are not his" (C-31; R4-C4) | B's attribution: the prize key spent a dust output received from `3GSMG24...`; the handle's 2023 "Correct" is general | DISPUTED (D-05); on-chain addresses may serve as a secondary, zero-cost check, never as an anchor or a success test | `reference/03` section 5; B LEDGER ticks 37-39, 59, 63 | the creator, or a signed message from `3GSMG24...` |
| K11 | "You have all the info" means no brute force (R5, R6) vs its actual context | [C id 9607] answers "is there another URL to find? otherwise I am going to do a big brute force" | it means: no further URL/page is needed and no brute force; both readings are supported | C-30(b) | -- |

### B.3 Shared blind spots (what all six assume or ignore)

1. **The opening image beyond "LSB markers".** All six accept that the 24 coloured cells are
   the URL's LSBs (A-10) and stop there. Solvers explicitly dismissed the colours as "just
   marking the LSB ... no more information to extract" [T L21871, L31809]. Yet C-06 ("Yellow
   has a number and so does Blue ... Go back to the first puzzle piece"), C-13 ("answer is
   there", "First or zero"), C-14/C-24/C-25 (an extra door in the first piece, unfound in
   2020-08 and 2021-12), C-25 ("some characters need to be 'zeroed out'" + primes) and C-28
   (`yellowblueprimes`) all point back at that object. No report proposes an *operation* on the
   URL or its coloured bits. The documented community belief is a specific reason it was missed.
2. **What "one team ... found" in April 2020 (C-11) and what the "club" was stuck past (C-16).**
   None asks. The transcript window around 2020-03-24 -> 2020-04-10 is held; so are the
   on-chain events of those days (B LEDGER ticks 38-39, 63). Whatever was found then predates
   SalPhaseIon (reached 2021-03) and may be the "another door".
3. **The Decentraland parcel beyond one audio file (C-05, C-08).** The archive holds the mp3
   and screenshots only; the scene's other assets were never catalogued; a 2021 solver summary
   says "blobs in mp3 didnt recovered" (S-06); A PR #30 reports an in-world "door" that "does
   nothing". No report looks.
4. **The reply link of C-21.** "I gave an unforseen hint already" is a Telegram reply to a
   request for a `matrixsumlist` hint. If the unforeseen hint is C-19 ("the prime part"), then
   `matrixsumlist` is defined by primes -- a typed reading nobody writes down (R5-W2a asks the
   question, no report answers it).
5. **The exact key oracle has never been run over the held padding-valid outputs.** R6 names
   the blind spot; none has done it (B LEDGER L1349: "No sliding windows"; `EXT-E0087` checked
   posted keys and dbbi/faed bytes, not the chain/cosmic outputs). `17ucy1...`'s hash160 is
   a second target (A-06: two keys) that only B PR#15 ever used.
6. **The Phase-2 equation line (A-12)** -- creator-authored, unused by any solved stage,
   dismissed on a solver's summary (S-06/D-07). Nobody examines it.
7. **The 2026-01-01 "tiny hint" (C-39)** -- five dot messages and "<3". Nobody examines it.
8. **All six assume the three-label password model** (C-28 read as values or operations feeding
   one password). Only R3 asks whether the model is falsifiable; none tests the alternative
   that the labels are a *dependency list* (R2's architecture 2).
9. **All six work without reply targets**: the transcript has none, the dataset's replies are
   cut at 160 characters, and every "unresolved" ruling above (K1, K3, D-02) turns on a missing
   `reply_to`. All six ask for the JSON export; none has it.
10. **C-27's "certain GitHub"** (2023-01-11: "for whoever set that up, nicely done. You guys
    are really getting close") is never examined. The held repos had no commits between
    2022-10 and 2023-02 (A master unchanged since 2021-05-25; A issues #1-#7 only), so either
    the creator meant A's 2021 README plus seven issues, or a GitHub the archive does not hold.

### B.4 Combined "why unsolved" model (the ideas in Stage C must attack this)

1. Every solved stage was `answer -> sha256hex -> AES-256-CBC (EVP SHA-256)`, with the answer
   either a quotation or a join of found pieces, and instructions inside each plaintext (A-01,
   A-02). The frontier keeps the containers but drops the instructions (A-08).
2. Past SalPhaseIon there is no verifier: one 2019 hash (C-01), no page checkpoint (A-08), and
   a wrong key passes PKCS#7 ~1/256 (`reference/03` section 1). Every "opening" since 2023 has
   that shape; three need MD5, which fails on all solved stages (`reference/05` section 2).
3. The creator named the ingredients (C-28) but no values and no join; he confirmed primes and
   "zeroing" as operations (C-25, C-27) without an operand; "yinyang" is a phase, not a value
   (C-38), reached after "1 microstep" (C-35) with "all the info" in hand (C-30b, C-32).
4. The public record therefore contains the ingredients and not the recipe. Searches have been
   enormous but unstructured and validator-blind (`reference/06`): ~33M (B), ~33.5M (C), ~2.5B
   (A#106), plus unheld hundreds of millions, with zero verified hits; readability gates set
   above ~0.6 would have rejected a Phase-3.2-like plaintext (R5-C37).
5. The build was rushed (C-47, C-03, C-44); the last steps are one person's formatting whims,
   which no enumeration over "natural" readings need contain.
6. The creator may have gated the end on something personal (C-43, D-03); the evidence does
   not separate that from a public recognition step (K3).
7. The community's own record is polluted: solvers' words became "creator rules" (S-01..S-05),
   reactions became confirmations (K1, D-02), and self-validating outputs became "stages"
   (`reference/05` M5-M8). A dated, reply-linked corpus does not exist in the archive (B.3-9).
8. What is *not* the cause: compute (K2, K5), the padding economy per se (it is a symptom),
   and a lack of ideas -- the pool below has thirty; what is missing is an idea whose success
   test is exact and whose parameters are sourced.

### B.5 Pool of ways forward (deduplicated)

| ID | Way forward | Proposed by | Already tried? (held record) | LAW 1 first pass |
|---|---|---|---|---|
| P-01 | Operations reading of the 2023 labels (primes + zero-out + sums) producing the literal milestone word | R1-W3, R5-W1b, R5-W1c; v2 section 11 rank 1 | partly: 228 +/-VIC operations (`research/2026-10-15_yinyang_ops`), exhaustive decimal-rule zero insertion (`zero_merge`), C's prime zero-out on DBBI (`EXT-E0042`); no typed primes+zero-out+*sums* spec exists | C-25, C-27, C-28, C-30a, C-38: yes |
| P-02 | Retrieve `salphaseion_plain_79.bin` and the other PR93 Telegram attachments (`cosmic_decrypted_verified.bin`, `Jrk Bgrt Chat History.txt`, the book PDF) | R1-W1, R4-W2 | no; A#114 asked publicly (2026) | none directly; anchors via C-10/C-23 only loosely -- a retrieval |
| P-03 | *Looking Forward* text | R1-W2 | closed: B PR#15 ticks 79-80 (pre-registered, null) | D-01 only -> fails LAW 1 (DISPUTED-only anchor) |
| P-04 | Ask the creator for a hash of the next-stage value (not a hint) | R1-W4, R3-W6 | never asked as a hash; hint requests refused (C-30d, C-35) | C-01 precedent; a user decision, not an agent idea |
| P-05 | Watch the address | R1-W5 | ongoing (dated balances) | C-20, C-40; not a solving step |
| P-06 | Process: locally justified, frozen-prediction transitions; one idea = one pre-registered test; shared negatives ledger | R2-W1, R4-W1, R5 (standing rule), R6-W5, R6-W6 | adopted (this folder) | -- |
| P-07 | Ask the creator which object "zeroed out" applies to | R2-W2 | no | C-25; a user decision |
| P-08 | Freeze oracles: prize point; readable text; (on-chain addresses as secondary) | R3-W1 | exists in part (`btclib.py`, `aes_try.py`) | C-33; process |
| P-09 | Enumerate the creator-grammar space of the three labels x formats x combiners (<= 10^7) | R3-W3 | partly: C's ~358k computed-value passphrases, `EXT-E0157` (literal four labels, every order), `EXT-E0098` (4,156 yellowblueprimes strings), R5 rounds A/B/D (unheld) | C-28: yes; but 10^7 is a sweep under the brief's section 8.2 unless each cell is clue-sourced |
| P-10 | Target `salph_inner` first | R3-W4, R6-W2 (small envelope), R5-C29 | an ordering, not a test | C-38 weakly (K7) |
| P-11 | Obtain the Telegram JSON export (reply targets, media, deleted accounts, dates) | R3-W5, R5-W4, R6-W4 | requested publicly (A#114), not obtained | C-13, C-26, C-40, C-46 contexts: a retrieval |
| P-12 | Interview early solvers / social route | R3-W5 | no record | C-11, C-16, C-30c; a user decision |
| P-13 | Yellow/blue cell selectors on DBBI/FAED, judged by readability | R5-W1a | "planned by an earlier agent, never run" (unheld); `EXT-E0146` (a related DBBI yellow/blue prime-index match failed to reproduce) | C-06, C-28: yes |
| P-14 | Prime selection + zeroing on DBBI/FAED | R5-W1c | tried: `EXT-E0042`; `research/2026-10-15_zero_merge` (exhaustive for the decimal-rule family) | C-25: yes |
| P-15 | Identify the "unforseen hint" (C-21) | R5-W2a | reading; the dataset links it to C-19 | C-21, C-19: yes |
| P-16 | Pin down "our first hint" (A-07) | R5-W2b | reading; candidates C-01, C-06, "Follow the white rabbit" [T L22449] | A-07: yes (a reading) |
| P-17 | Run the 245.9M recipe grammar on cosmic (sha256 + md5) | R5-W3a | operator-local; a sweep | not runnable here (brief section 8.2) |
| P-18 | Re-grade every held padding-valid output with an exact key oracle (raw 32-byte windows vs the prize point and `17ucy1...`) | R5-W3b, R6-W1 | no: B LEDGER L1349 ("No sliding windows"); `EXT-E0087` covers posted keys and dbbi/faed bytes only | C-33, C-23, C-10, A-06: yes |
| P-19 | Audit the p32 padding excess (185 vs 148.5) | R5-W3c | operator data not held | -- |
| P-20 | "we won't" in the lastwords slot | R5-W3d | no CSV row; the string sits inside C-28 ("wewont") | C-28: yes (loose) |
| P-21 | Solve the 14x14 grid as a yin-yang logic puzzle | R5-W3e | no record | C-28 (yinyang), C-06: vague |
| P-22 | Start from BTCSEED / YOUWON read through the 2023 ingredient order | R6-W2 | partly: 640 scalars, 64 brain wallets, 80 matrix-sum, 30 combine, 784-seed BSGS (held) | S-10/S-11 are solver constructions; anchoring must come from A-03/C-28 |
| P-23 | The song's third part ("The judgement") in the standard lock | R6-W3 | no record (CSV: 0 rows; `EXT-E0295` tried lyric lines on the Phase-1 form only); discussed in chat 2019/2020/2023 | C-06 line 1 (loose) + the solved-stage convention |
| P-24 | User decisions: the close-friends route; reporting a suspected build error | R5-W5 | -- | -- |

### B.6 Arguments against the five laws, recorded as proposals to the user

The laws are fixed. These are recorded, with an assessment, for the user to decide.

| # | Source | Argument | Assessment | Proposal |
|---|---|---|---|---|
| PR-1 | R2 ("Every parameter must be a creator quotation ... would rule out ordinary puzzle inference") | solved stages themselves needed small inferences (part 5: eight executive orders; part 7: the halfmove-clock trap) | LAW 4 already admits "solved-stage conventions" and the scale admits <= 2 FREE choices if fully enumerated; the risk is only that "convention" is read too narrowly | keep LAW 4; publish an explicit list of solved-stage conventions in `CLUES.md` section 4 (A-01, A-02: case/space markers, reversal, `0x`-uppercase hex, file-name style, sha256hex) so that an idea citing one is not counted as FREE |
| PR-2 | R2 ("Yin-yang must appear literally" is an exploratory detector, not a requirement) | C-38 calls yin yang a phase; the word may never appear | the Task-1 scale already accepts readable text, a value fixed in advance, or an exact key match; the literal word is one success test among several | no change; accept all three creator spellings (`yinyang`, `ying yang`, `yingyang`) when it is used |
| PR-3 | R2 ("A known SHA-256 stage proves every MD5-based unsolved attempt void" is wrong) | true as logic | LAW 4 makes SHA-256 the sourced choice and MD5 a declared FREE parameter; no law says MD5 is void | no change; MD5 counts as one FREE choice when declared |
| PR-4 | R4 gate (G1 = 0 -> reject) applied to retrievals | pure retrievals have no clue to cite yet every report ranks them | LAW 1 can be met by naming the clue whose *context* the retrieval recovers (e.g. C-13's missing questions, C-26's missing media, C-40/C-46's missing reply targets) | the user to confirm that reading of LAW 1 for retrievals |
| PR-5 | R2 ("The correct intermediate must be mostly printable" is too strong); R5-C37 (Phase 3.2 is only ~60% printable) | a recognised binary format or an independently constrained relation could validate | the scale's success test already allows an exact key match; a "recognised binary format" is acceptable only if named before the run | keep; require the format to be pre-registered |
| PR-6 | R4 gate ranking "highest G1 first" | favours clue-dense over decisive | the funnel's round 4 fixes it | no change to the laws |

No report argues against LAW 2, LAW 3 or LAW 5.
