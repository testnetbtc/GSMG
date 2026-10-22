# SELECTED -- the single way forward from the Task 1 funnel

Selected: **W-02 Exact-oracle sweep over the held "openings"** (`FUNNEL.md` round 4).
Runner-up: **W-01 Clear the marked bit** (becomes ACTIVE as soon as W-02 has run).
Status: awaiting the user's go-ahead. Nothing has been run.

## 1. The card, tightened

Every community "opening" (`reference/05` M5, M6, M8, M15 and the B drive files) is a
padding-valid byte string that has only ever been read through imposed field layouts or text
gates. Slide the archive's exact key oracle over all of them, and over the published controls,
with four creator-sourced transforms, against the prize public key and the hash160s of the two
puzzle addresses. A match is a solve (and triggers the stop rule). A clean negative closes, for
good, the claim that "the key sits in those bytes" -- a claim the community keeps reopening
([B#17] 2026-10-05, [A#108]) and that no held sweep has ever tested exactly.

Stage: the community openings after SalPhaseIon (LAW 3). Clues (LAW 1): C-33 "Regular Bitcoin
Private key" -> a 256-bit scalar, both encodings; C-23 "The one to be found by solving the
puzzle yes ... the solver will find a way to 'decrypt' it" -> the key may sit raw in a
decrypted container; C-10 "There must at least be something hidden in there" -> the
`p32_trailing` output is in scope; A-06 "the private keys belong to half and better half" and
C-12 "Well spotted" / "The price is in half" -> the second target `17ucy1...` and the x2 and
/2 transforms. Prior coverage (LAW 2): `reference/03` section 1.1 (K_S1/K_S2 as uncompressed
addresses only); `EXT-E0087` (posted keys, dbbi/faed bytes, split halves); B LEDGER L1349 ("No
sliding windows, no substrings"); `research/2026-10-15` (exact oracle on BTCSEED scalars only);
C's "universal inspector" (fixed readings, scripts absent). FREE parameters (LAW 4): 0.

## 2. Typed specification (implementable without questions)

### 2.1 Inputs (all held; verify each SHA-256 before use)

| # | File | SHA-256 | Bytes | Role |
|---|---|---|---|---|
| F1 | `reproduction/results/chain1.bin` | `1449a2178eea7c0e3fabac8c1ad2afa294be4fc1800c594a025a056e88c626bf` | 79 | M5 link 1 output |
| F2 | `reproduction/results/chain2.bin` | `b40fce72ef5638e4f79b3233e653f8a5dbdb0d4ae2009d2d3da2c98b70f4d004` | 79 | M5 link 2 output |
| F3 | `reproduction/results/cosmic_output.bin` | `4f7a1e4efe4bf6c5581e32505c019657cb7b030e90232d33f011aca6a5e9c081` | 1,327 | M6 output |
| F4 | `reproduction/results/chain4.bin` | `e4269ed5fbb202a81e5e1aa6b5190fdd1ea126b2c8547ea7cdbdf45387ea135b` | 1,151 | M8 output |
| F5 | `sources/naddiseo/_pr15/unverified/drive-2026-05/cosmic_A.bin` | prefix `cd3fea3d697a7fbf` (full value in `reference/data/SOURCE_LINEAGE.csv`) | 1,327 | unverified operand |
| F6 | `sources/naddiseo/_pr15/unverified/drive-2026-05/ca158_hidden_blob.bin` | prefix `d895da1ba96e924c` | 1,169 | crib-control envelope |
| F7 | `sources/naddiseo/_pr15/unverified/drive-2026-05/chain2_decrypted.bin` | prefix `74f0e46cdb463748` | 1,151 | drive file |
| F8 | A#15 control, `salph_inner` | regenerate: password `26770c535632f626daefc0736dd4f85fd6126f647e6a160a2b58c51c0693d40f` on `reference/artifacts/envelopes/salph_inner.b64.txt` (`f8b89da5...`), KDF as recorded in `reproduction/results/reproduction_results.json` step `a15_padding_controls` (expected 79 B, SHA-256 `c27ea25ddfb54f49da06c1dce13abe0fde6890500ae6125927996bbfb601d4bd`) | 79 | 2023 control |
| F9 | A#15 control, `cosmic` | regenerate: password `93de0175aa3d0a6a2768ba650009a35a36530fa31898da6f3c46757a693f108f` on `reference/artifacts/envelopes/cosmic.b64.txt` (`92f9dddf...`), KDF as recorded in the same step (expected 1,327 B; source says it begins `5d2ec2af4c2f9dfb191fce6a70e4a75a`) | 1,327 | 2023 control |
| F10 | the 103x103 construction's 68 bytes | regenerate with `reproduce.py` step `cosmic_103x103_base38` from F3: `0423d911...` (32) \|\| `48cc46e6...` (32) \|\| `fc0c1b02` | 68 | M7 output |
| T1 | prize public key (uncompressed, from `sources/naddiseo/_pr15/neo/materials/chain/tx_halving_spend.hex`, reproduced) | `04f4d1bbd91e65e2a019566a17574e97dae908b784b388891848007e4f55d5a4649c73d25fc5ed8fd7227cab0be4e576c0c6404db5aa546286563e4be12bf33559` | 65 | target point |
| T2 | hash160 of `1GSMG1JC9wtdSwfwApgj2xcmJPAwx7prBe` (base58check decoded, checksum verified) | `a9553269572a317e39f0f518cb87c1a0ee1dbae4` | 20 | target |
| T3 | hash160 of `17ucy1K9ZUAaoY6JVtM932W9jUp5LXfyHa` (base58check decoded, checksum verified) | `4bc468447fe1b048ad030a2f9a125478eabc4ed6` | 20 | target |
| L | `research/2026-10-15_btcseed_bits/btclib.py` (`9a384842...1755`): `scalar_mul`, `hash160`, `pubkey_bytes`, `N` | -- | oracle library |

Constants: secp256k1 order `N = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141`;
`INV2 = (N + 1) // 2` (so that `k * INV2 mod N` is "half" of k).

### 2.2 Steps, in order

1. Verify the SHA-256 of F1-F7, L and the two envelopes; regenerate F8, F9, F10 and check
   their recorded hashes/prefixes. Abort on any mismatch.
2. Parse T1 into the affine point `Pprize = (x, y)` and assert it lies on the curve and that
   `hash160(uncompressed(Pprize)) == T2` (sanity).
3. For each file F in F1..F10 and each byte offset `i` from 0 to `len(F) - 32` inclusive:
   `w = F[i:i+32]`.
   - base scalars: `k_fwd = int.from_bytes(w, "big")`, `k_rev = int.from_bytes(w[::-1], "big")`;
   - for each base `k` in {k_fwd, k_rev}: candidates `{k, (2*k) % N, (k*INV2) % N}`;
   - for each candidate `c` with `1 <= c < N`: `Q = scalar_mul(c)`; record a HIT if `Q == Pprize`;
     compute `hash160(pubkey_bytes(Q, compressed=True))` and `hash160(pubkey_bytes(Q, compressed=False))`;
     record a HIT if either equals T2 or T3.
4. Substring scan on each file decoded as latin-1: every match of `[0-9a-fA-F]{64}` -> scalar
   `int(m, 16)`; every match of `5[1-9A-HJ-NP-Za-km-z]{50}` or `[KL][1-9A-HJ-NP-Za-km-z]{51}` ->
   base58check-decode, take bytes 1..32 as the scalar (ignore the compression flag); apply
   step 3's candidate set and checks to each.
5. Write `research/2026-10-22_w02_oracle_sweep/log.jsonl` (one line per file: offsets scanned,
   candidates checked, hits) and `RESULT.md` (the table of counts, the verdict, the
   SHA-256 of every input used, runtime). Record the run in `SOLVE/STATE.md`, `SOLVE/PLAN.md`
   and, if negative, `SOLVE/GRAVEYARD.md` ("tried-held").
6. **Stop rule (non-negotiable).** On any HIT: stop the run; write only the file name, offset
   and transform to a file *outside* the repository; never print, log or commit the scalar;
   do not push; tell the user. Moving funds is never the agent's decision.

### 2.3 Parameters and sources

| Parameter | Value | Source |
|---|---|---|
| window length | 32 bytes | C-33 (a regular 256-bit key) |
| offsets | every byte offset (exhaustive) | no choice |
| byte orders | forward, reversed | solved-stage convention: Phase 2.2 part 6 (reversed headline), the 2023 binary (whole-string reversal) |
| multipliers | x1, x2, x1/2 (mod N) | A-06 "half and better half"; C-12 |
| encodings | compressed and uncompressed | C-33 leaves it unspecified |
| targets | prize point; hash160 of the prize and of `17ucy1...` | T1-T3; A-06, C-12 |
| files | F1-F10 | `reference/05` M5-M8, M15; B drive files |
| FREE count | 0 | -- |

Expected size: about 7,450 windows x 2 byte orders x 3 multipliers = ~44,700 scalar
multiplications plus ~89,400 hash160s; pure-Python `btclib.py` at a few ms per multiplication
-> roughly 2-5 minutes on one core.

### 2.4 Output format

`RESULT.md`: a table (file, bytes, windows, candidates, hex/WIF substrings found, hits) and one
verdict line: `NEGATIVE: no window, transform or substring of any held opening or control
matches the prize point or either target hash160` or `HIT: see the out-of-repo note`.

## 3. Pre-registered success test and negative criterion (word for word)

**Success:** a candidate scalar `c` (from any window, byte order, multiplier or substring of
F1-F10) whose public point equals the prize point T1 exactly, or whose compressed or
uncompressed hash160 equals T2 or T3 exactly. Nothing else is success: padding validity,
printable output, "looks like a key", or a near-miss of any kind do not count.

**Negative:** every window, byte order, multiplier and substring of every file F1-F10 has been
checked and none meets the success condition. The negative is then recorded as "tried-held"
and retires the claim that the prize key or the `17ucy1...` key sits raw, byte-reversed,
doubled or halved inside any held community opening or control.

## 4. Clue tick-box (CORE clues from `CLUES.md` section 5)

| Clue | Mark | How |
|---|---|---|
| C-06 | -- | not addressed |
| C-10 | [x] used | "something hidden" in Phase 3.2 -> the `p32_trailing` output (F2) is in scope |
| C-12 | [x] used | "better half" = the halving address -> target T3; x2 and x1/2 |
| C-13 | -- | not addressed |
| C-14 | -- | not addressed |
| C-17 | -- | consistent (fully offline) |
| C-19 | -- | not addressed (no primes) |
| C-20 | -- | not addressed |
| C-21 | -- | not addressed |
| C-23 | [x] used | the key is stored encrypted and the solver "decrypts" it -> look for it raw in decrypted outputs |
| C-24 | -- | not addressed |
| C-25 | -- | not addressed (no zeroing); a positive would not need it -- acceptable because this is a closure test, not a model of the endgame |
| C-26 | -- | not addressed |
| C-27 | -- | not addressed |
| C-28 | -- | not addressed; a positive would leave the labels unexplained (acceptable for the same reason) |
| C-29 | -- | consistent ("the hardest part is done") |
| C-30 | -- | consistent with (b) "You have all the info" |
| C-31 | -- | not involved (no on-chain messages used) |
| C-32 | -- | consistent (offline) |
| C-33 | [x] used | a regular private key, both encodings |
| C-35 | -- | consistent (one check away) |
| C-38 | -- | not addressed |
| C-40 | -- | not addressed |
| C-42, C-43, C-44 | -- | not addressed |
| A-03 | -- | not addressed |
| A-05 | -- | consistent ("take the private key") |
| A-06 | [x] used | two keys -> two targets; "half" -> the multipliers |
| A-07, A-08, A-09 | -- | the containers are the sources of the files scanned |
| A-10, A-11 | -- | not addressed |

Contradicted: none. Used: C-10, C-12, C-23, C-33, A-06.

## 5. Why this and not the runner-up

W-01 explains more of the creator's own words (eleven CORE clues against six) and is the
project's first genuine hypothesis about the endgame; W-02 explains the frontier's *record*,
not the creator. The funnel's last round asks which idea, run once, gives the clearest answer
either way for the least cost. W-02's positive is an exact point match -- a solve -- and its
negative closes a branch that is still being argued in the public threads and that no held
sweep ever tested as such; W-01's negative closes one literal reading of one hint. Both cost
minutes and need nothing the repo does not hold, and W-02 has the fewer free parameters. So
W-02 runs first; W-01 follows immediately, whatever W-02 returns (unless it returns a hit).

## 6. What a negative result would teach, and what becomes ACTIVE next

A negative means: none of the community's padding-valid outputs -- including the two 2023
controls that nobody ever claimed as stages -- carries a key in any raw, reversed, doubled or
halved form, and no hex or WIF string inside them is a key. The 79-byte chains and the Cosmic
output can then be set aside as key carriers without further argument; anyone reasserting
them must produce a different derivation. It does not touch the question of whether those
outputs are intended *text* stages (they are not readable) or whether `salph_inner` /
`p32_trailing` / `cosmic` have other passwords.

Next ACTIVE: **W-01 Clear the marked bit** (`FUNNEL.md` card). Its specification is already
complete: three candidate strings (`fslf.ho/thesdedhsplanted`, `grlg.in/thdsdedirplantdd`,
``gslf.ho.thereddispl`nted``), password = sha256hex of each, EVP SHA-256 one round, AES-256-CBC,
on `salph_inner`, `cosmic` and `p32_trailing`; success S1/S2/S3 of `FUNNEL.md`; nine decrypts.
After W-01: W-06 (prime-masked 14x14 sums; 24 decrypts), then W-03 once the lyric text is
confirmed.

## 7. Inputs the user needs to obtain or decide

- For W-02: nothing. Go-ahead only.
- For the queue: the official lyric text of the song's third part (W-03); the Telegram JSON
  export of group `1166734859` and the A PR #93 attachments (W-05, a standing request --
  `salphaseion_plain_79.bin`, `cosmic_decrypted_verified.bin`, `Jrk Bgrt Chat History.txt`).
- Decisions outside the laws' frame: whether to ask the creator for a hash of the next-stage
  value (P-04, the 2019 precedent) or for the operand of "zeroed out" (P-07); whether to use
  public facts about the creator (R5-W5); the rule proposals PR-1..PR-6 in `REPORT_ANALYSIS.md` B.6.
- Repository: push access for the `solve:` commits (denied to this session) or a push by the user.
