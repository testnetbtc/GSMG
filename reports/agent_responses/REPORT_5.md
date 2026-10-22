# GSMG 5 BTC puzzle — evidence-based assessment

Date: 2026-10-22
Source archive: testnetbtc/GSMG (A = puzzlehunt/gsmgio-5btc-puzzle, B = Naddiseo fork, C = HosterjackAGV/gsmg-5btc-puzzle)

## Scope (so this can be weighed against other agents' answers)

- This session has no puzzle history: nothing was attempted here. "What we tested" below means the repo's own records (`research/`, B PR#15 ledger, C's 171 attempts, A PR#93/#106, `reproduction/`).
- Read first-hand: all 12 walkthrough pages, `reference/00,03–08`, both reports (`REASONING_REPORT_v2.md`, `MASTER_REASONING_REPORT.md`), the research journals, the B PR#15 LEDGER and NEXT_PASS, all 411 creator text messages (`creator_jrk.txt`), the 510-record creator dataset (`sowut-data.js`, parsed), Telegram windows (BTCSEED 2025-06, Cosmic 2025-08, "Bingo" 2026-03, 2021 entry recipe), ~27 discussion threads directly, and the two 2026-07-12 hint images. The remaining ~75 A issues were read via the repo's extraction notes (D1–D3, N2, N5, N6).
- Verification state: the solved chain Phase 0 → 3.2 → SalPhaseIon is fully reproduced (`verify.py` 102/102, `reproduce.py` 18/18, 0 discrepancies). Nothing past it is verified.
- Creator attribution = Telegram handle @SoWut / "Jrk Bgrt", unauthenticated. Message ids below refer to the hosterjack creator dataset.

---

## 1. Why has no one solved it?

### Structural (strongest evidence)

1. **All-or-nothing gate, no checkpoint.** Every solved stage uses the same convention: password = lowercase sha256hex(answer) → OpenSSL `EVP_BytesToKey` (SHA-256, one round) → AES-256-CBC → strict PKCS#7. The only creator-published checkpoint is the Phase-1 hash (`5ac40783…`, 2019-04-22). After Phase 3.2 the only oracle is the prize address. A wrong key yields a valid 1-byte PKCS#7 pad about 1/256 of the time (measured 1/243 in 300k and 1/236 in 49,664). Every community "opening" — chain1, chain2, Cosmic Set B, chain4, the 103×103 base-38 "Half/Better half" — has exactly that shape; three of them need an MD5 KDF that fails on all four solved stages; and the 2023 A#15 control shows unrelated passwords produce the same 79-byte / 1327-byte outputs (`walkthrough/09_frontier_containers.md`, `reference/05_COMMUNITY_MECHANISMS.md`).

2. **Three undefined inputs plus an undefined combiner.** The creator's 2023-02-23 binary names them in order — `yellowblueprimes`, `matrixsumlist`, `lastwordsbeforearchichoice` → `yinyang` — and adds "wewontgiveawaythepassworditsinfrontofyoureyesbutyourenotseeingit". The SalPhaseIon soup gives names (`matrixsumlist`, `lastwordsbeforearchichoice`, `thispassword`), not values; `yellowblueprimes` is not in the soup at all (it comes from the 2020 "Roses" poem and the 24 coloured cells of the opening image). The Architect speech warns "select from over twenty-three ciphers sixteen encryptions and or seven intertwined passwords … brute forcing might be required". There is no gradient, and a search over *interpretations* is unbounded.

3. **The key is random, so no mathematical shortcut exists.** `1GSMG1…` is a ~58⁵ vanity prefix (trivial to generate with vanitygen), so the private key is stored inside a container, not derived from puzzle material. Confirmed negatives: 640 direct scalars, 64 brainwallets, BSGS ±2²⁸ around 784 seeds, MITM halves, 0/66 BTCSEED-derived keys (`research/2026-10-15_*`, B#13). The prize public key (`04f4d1bb…`) is public via the 2020 spend, which matters only for route (iii) in section 4.

4. **The end was built in a rush by one person.** Creator: "Couple hours, and no" / "two sloppy days" / "Same same" (#70336, #70377); "A. I rushed (t)it" (#70311); "sad rushed mistakes" verified "many times back then" (#66589); "I have these moment where I get into a frenzy and zone in with 800%. A day later I can hardly understand what I have done" (#66561). The cipher convention stayed constant across stages; the final-step formatting is one person's whim — exactly where enumeration fails.

### Social

5. **Signal collapsed under noise.** 51,177 Telegram messages, 103 A issues, LLM-generated claim floods, and parameters fitted after the fact (the Cosmic Set B proposer admitted a "p5–p7 search"; chain4's mask is a crib fit — output[158:166] XOR "Salted__"; the 103×103 parameters were fitted). Until B PR#15 and A PR#93 imposed a claim standard, "progress" was unfalsifiable and people built on sand (BTCSEED → YOUWON → …).

6. **Deliberate withholding, possibly a knowledge gate.** 2026-07-13: "My close friends have the best chance of solving it (a few tried). But they don't have the skills some of you do." / "NOTE: that is a hint." (#66573–74). B PR#15's conclusion: *terminal state* — the missing input is not in the creator-authenticated corpus. Against that: "You have all the info", "internet not required", "If you guys got 1 microstep further, the puzzle will likely be solved the same day" (2024-11-29, #32579), "when yingyang is reached, 2 hours max" (2025-04-28, #39224), "I only need to look at the address. If any of you reaches the next phase, the price is taken in no-time" (2026-03-04, #60314), "good puzzles don't need hints" (#32579).

   **My weighting: ~60% the block is a recognition step on public material; ~40% it needs a fact about the creator's life or company.** The evidence does not separate these; anyone who claims it does is guessing.

### Corrections to things the community believes (from recovered context in the repo)

- The 2026-03-03 "Bingo" (#60312) followed D1rty Byrd's Cartman/chatroulette quote, not a puzzle claim (`_pr15/unverified/recovered_reply_context_2026-09-26.txt`).
- "Looks at gnomad 👀" (#60309) pointed at gnomad's "no hints, only free will" / "it's in front of your eyes" stance, not at a method.
- The Fresco "Looking Forward" lead was pre-registered and closed (B PR#15 ticks 79–80).
- "Pfff. Coincidence." (2026-09-01, #70307) most likely targeted the YOUWON/VIC {1,4,21} claim posted just before it (#70303).

---

## 2. What is required, and why

- **R1 — the exact next-stage string(s)** under the fixed convention: three values + combiner + formatting. *Why:* the convention held for four stages, and the soup's tokens are explicitly password-shaped (`thispassword`, `shabefourfirsthintisyourlastcommand`, `enter`, `shabefanstoo`).
- **R2 — exact oracles fixed before searching:** (a) scalar → secp256k1 point == prize pubkey (no false positives); (b) the creator's own on-chain stamp convention, compressed-P2PKH(sha256(X)) — he used it in 2020 to confirm every solved stage with OP_RETURN dust from `3GSMG24…` — tested against `1NULY7DhzuNvSDtPkFzNo6oRTZQWBqXNE9` (creator-stamped, preimage unknown: a free offline answer-oracle) and the other stamped addresses; (c) readable plaintext under the SHA-256 KDF only; 1-byte-pad and MD5 outputs are rejected. *Why:* without this, the 1/256 false-positive rate guarantees endless phantom progress.
- **R3 — a bounded candidate space derived from the creator's own grammar,** not open sweeps. *Why:* ~33.5M (C on `salph_inner`), ~33M across 52 campaigns (B PR#15), ~2.5B (A#106, unaudited), ~14.8M (`endgame_aes_password_search.md`) → zero verified hits. Volume is not the problem; the shape of the space is.
- **R4 — the early material:** the raw Telegram JSON export (not shipped in the archive), deleted or edited 2019–2020 creator messages, and the January-2020 hint missing from GitHub (creator-confirmed, #4094). *Why:* his vocabulary (yinyang, matrixsumlist) and his only checkpoint come from that period.
- **R5 — if the gate is biographical:** a fact about the creator. No computation substitutes; only OSINT or people who have met him ("Some of you, can find me. Quite a few in this chat, already met me", #66571).
- **R6 — or one checkpoint hash from the creator.** He did exactly this in 2019 ("just try hit your options against that hash"). It is the smallest ask with the largest effect, and it is not a hint.

---

## 3. How a solver can solve it

1. **Freeze the oracles.** The repo already has `btclib.py` (scalar → point), `aes_try.py`, `gate.py`, `btc_addr.py`; add the stamp check from R2(b).
2. **Pre-register every candidate** — derivation and expected string — *before* testing it (B PR#15's intake format works).
3. **Enumerate the grammar.** For each of the three names, list derivations from the solved artifacts only:
   - `yellowblueprimes`: the 24 coloured cells (blue spiral indices 7, 15, 23, 31, 47, 55, 63, 87, 95, 103, 111, 127, 135, 159, 183; yellow 39, 71, 79, 119, 143, 151, 167, 175, 191; sequence `BBBBYBBBYYBBBBYBBYYBYYBY`), their counts (15/9), the primes among them, the colours as bits.
   - `matrixsumlist`: row/column sums of the 14×14 bit grid, of the DBBI 5×5 square, of the 24-cell colour vector; as decimal lists, concatenated, hex, with/without separators.
   - `lastwordsbeforearchichoice`: the last words before "choice" in the decoded Architect speech and in the film script.
   - Formatting from the puzzle's own rules (`aaa`/`aBa`, `connected enf`/`not enf`, reversed, `0x`-uppercase hex, decimal lists); combiners from its own vocabulary (concatenation in 2023-binary order, interleave = "intertwined", sha256 of each then concat/XOR).
   - Keep each dimension ≤ ~100 → ≤ 10⁷ total; run against all four containers plus the stamps; log every negative in the archive's format.
4. **Target `salph_inner` first.** The creator says yinyang is "the next phase" reached after decoding an AES ciphertext (#39237), and the soup places `thispassword` / `enter` / `shabef…` around the two 64-character base64 halves that form it.
5. **Accept a hit only if** the plaintext is readable text, or matches a value fixed before the test, or is a scalar whose point is the prize. Treat BTCSEED, YOUWON, chain1–4 and Cosmic Set B as unverified and do not build on them.
6. **In parallel, the social route:** obtain the Telegram export, talk to the 2019–2021 solvers, and study what the creator *reacted to* rather than what was said (reactions, 🤐, "That is very specific").

---

## 4. "No matter what" — the complete list of routes

1. **The intended passphrase route** — the only one under a solver's control.
2. **Creator cooperation** — a checkpoint hash, or a reveal. He has floated moving the coins because of BIP-360 (#66555) and worried about dying before a public solution (#66540).
3. **ECDLP on the exposed public key** — classically ~2¹²⁸ operations, infeasible; quantum ("a few stable qubits", his own joke, #66589) needs thousands of logical qubits, and when it arrives every exposed-key address falls, so it is not a puzzle solution.
4. **Brute force of the AES-256 keys** — 2²⁵⁶, impossible; the passphrase space is bounded only if the grammar model is right.
5. **OSINT for a biographical gate**, if one exists.

There is no sixth route. Anyone offering one is selling noise.

---

## 5. Extra questions worth putting to every agent

- Has the "three inputs → one password" model itself been falsified? Zero hits across ~2.6B trials is evidence *either* against the model *or* for a knowledge gate — which one, and how would you tell them apart?
- Which container is next? Evidence favours `salph_inner` (salt `3ab585348552415d`, 80 B) over `cosmic` (1328 B) and `p32_trailing` (salt `b45a5e3d827593ca`, 80 B).
- What is the preimage of `1NULY7DhzuNvSDtPkFzNo6oRTZQWBqXNE9`? Nobody has explained the one creator-stamped address with no known answer.
- What does the 2021-07-18 "neighbors, half and double" dust (P±G, P/2, 2P) say about key arithmetic, given the VIC sentence "the private keys belong to half and better half"?
- Who are the "Some [who] already found it. And understood not to risk it" (#66600)? If any of them can produce a stamp preimage, the gate is public.
- How long does the prize last? ~1.256 BTC remains; the halving mirror predicts 0.625 BTC moved around the 2028 halving.

---

## 6. Way forward (recommendation)

Stop open-ended sweeps. Build the oracle set, pre-register, enumerate the grammar space once (auditable, ≤ 10⁷) and log the negatives. In parallel, pursue the Telegram export and early-solver interviews, and ask the creator for a *checkpoint hash* of the next stage rather than a hint. If both the grammar enumeration and the social route come up empty, the honest conclusion is that the remaining step is not derivable from published material, and the puzzle is solved only by the creator or by a future ECDLP break.

---

## Appendix — key facts used above

| Item | Value |
|---|---|
| Prize address | `1GSMG1JC9wtdSwfwApgj2xcmJPAwx7prBe` (funded 5 BTC 2019-04-13; 2.5 BTC moved 2020-05-11; 1.25 BTC moved 2024-04-24 to `17ucy1K9ZUAaoY6JVtM932W9jUp5LXfyHa`) |
| Only published checkpoint | SHA-256(Phase-1 answer) = `5ac407837447fba24ba2802e4d1e9aecb4580aa29fef1088cc387c180b746f75` |
| AES convention | sha256hex(answer) → `EVP_BytesToKey` SHA-256 ×1 → AES-256-CBC → PKCS#7; MD5 fails on every solved stage |
| Open containers | `p32_trailing` (80 B ct), `salph_inner` (80 B ct), `cosmic` (1328 B ct), `urlblob` (community artifact) |
| 2023 creator binary | `yellowblueprimesmatrixsumlistlastwordsbeforearchichoiceyinyangwewontgiveawaythepassworditsinfrontofyoureyesbutyourenotseeingitverylaststepisatruegiveawaypromised` |
| Creator stamp convention | compressed-P2PKH(sha256(stage answer)) ← OP_RETURN dust from `3GSMG24TujqfMJG1kQoBX18DzJHQLeJYMK`, 2020-03/04 |
| Unexplained stamp | `1NULY7DhzuNvSDtPkFzNo6oRTZQWBqXNE9` (1050 sat, preimage unknown) |
| Search volume with zero verified hits | ~33.5M (C), ~33M/52 campaigns (B), ~2.5B (A#106, unaudited), ~14.8M (endgame sheet), plus this archive's 640 scalars / 64 brainwallets / 784×±2²⁸ BSGS / 228 ops / exhaustive zero-merge |
