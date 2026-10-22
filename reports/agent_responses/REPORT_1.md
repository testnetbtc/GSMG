# GSMG.IO 5 BTC Puzzle — Honest Assessment

**Date:** 2026-10-22
**Basis:** the consolidated archive (testnetbtc/GSMG: solved chain, unresolved register, experiment coverage, contradictions, reasoning report v2); the full 51,177-message Telegram transcript and 510-record creator dataset; and a fresh experiment session (nine predeclared families, ~6.5M decrypts, exact secp256k1/address oracle — all null).

---

## Why has no one solved it?

1. **There is no checkpoint past SalPhaseIon.** Every solved stage had a verifier (the website form, the 2019 hash). The endgame has none: the recipe's four values (`yellowblueprimes · matrixsumlist · lastwordsbeforearchichoice · yinyang`) must *all* be right before anything opens, and the only exact oracle is the prize address. You cannot know whether you have one of four correct — iterative search is dead by design.
2. **The missing values aren't derivable from public material.** Seven years, ~380M decrypts, 1.4B graded keys, plus the new 6.5M clue-interpolated decrypts (cipher batteries, pair algebra, prime-position derivations, DBBI↔grid alignments) — all null. The values were hand-chosen by one person in two sloppy days in April 2019; that entropy is human, not computational.
3. **The creator no longer knows the answer.** By his own words he forgot the details by 2021, solvers know the puzzle "WAAAY better" than him, and the only complete record sits on a hidden laptop. His hints are nostalgic, not technical — and several celebrated "clues" were typos or banter (104/FEFEFE numerology; the {2,3,5,7} prime set was a *solver's*; the April Fools doors).
4. **The padding false-positive economy.** Roughly 1-in-256 wrong passwords "open" an OpenSSL container with valid padding. Years of community effort went into MD5 chains that are demonstrably this artifact, and most historical sweeps used validators (printable-text gates, SHA-256-only KDFs) that could not even register binary outputs. Much of the "coverage" looked where the light was, not where the key is.
5. **The strongest hint says the key is personal.** *"My close friends have the best chance of solving it… NOTE: that is a hint."* (2026-07-13). If any endgame value is personal knowledge, the public corpus is insufficient by construction.

## What is required to solve it, and why

Exactly one thing: **a verified anchor past SalPhaseIon.** The evidence gives only three possible forms:

- **A container opened by a clue-derived (not searched) password** — this starts the "seven intertwined passwords" chain reaction;
- **The literal word `yinyang` produced by a parameter-free operation** on DBBI/FAED — the archive's own section 9.3 conclusion: the operations reading is the only one with a reject-capable checkpoint, and the only one that makes "once you hit yinyang, you solve it the same day" true;
- **A new creator checkpoint** — he has released one *every single time* progress stalled (2019 hash, 2020 poem, 2021 mini-hint, 2023 binary, 2026 binary). It is his established pattern, driven by his stated fear of the puzzle looking like a scam.

Why nothing else suffices: without an anchor, candidate generation is unbounded, and every negative is only a statement about its own search space. That is what the 380M prior trials — and this session's experiments — actually proved.

## How can a solver solve it — and "no matter what the answer is"?

In order of expected value:

1. **Retrieval, not computation.** Obtain the two objects every repository lacks:
   - `salphaseion_plain_79.bin` — the Telegram ChatExport attachment (group `1166734859`) named in A PR #93's file listing; the only 79-byte reference predating the community chains;
   - the text of ***Looking Forward*** (Jacque Fresco & Ken Keyes Jr., 1969) — the "Bingo"-confirmed reading (2026-03-03) of *"it's in front of your eyes but you're not seeing it"*.
2. **One pre-registered, parameter-free operations test.** Primes + zero-out + sums, with a typed specification (inputs, prime convention, what is zeroed, output alphabet) written *before* running; success criterion = the literal word `yinyang`. If the specification needs a parameter not fixed by a creator statement, stop. That discipline alone would have saved the community years.
3. **Collective pressure for a checkpoint.** Ask the creator publicly for a hash of the yinyang value, citing the 2019 precedent. This is currently the single highest-probability unlock.
4. **Watch the address.** He says the prize moves within hours of yinyang being reached ("I only need to look at the address… the price is taken in no-time") — a free canary that someone has entered the endgame.

And the honest answer to *"no matter what the answer is"*: **there is no puzzle-solving method with that guarantee**, because the password is human-chosen and unchecked. The only truly answer-agnostic paths are not solves at all: Shor's algorithm against the prize's *exposed* public key (exposed since the 2020-05-11 halving spend; the creator himself jokes about qubits and worries about BIP-360) — years away, and constituting key extraction rather than solving — or the hidden laptop, which the rules rightly exclude.

## Questions worth adding

- **Is it still solvable in principle?** The giveit/givetit precedent shows the puzzle contains a silent typo that made a stage "nearly impossible". If an endgame value embeds a misremembered artifact, even the correct method fails — and nobody can detect that.
- **What falsifies the whole enterprise?** A spend from the prize address or 17ucy to an unrelated address. (*"If wallet != empty, puzzle not solved. (Most likely.)"*)
- **Why did the recent test families fail?** Each fixed a mechanism, not a value; the creator's "Same same" (2026-09-01) says the *method* is uniform across objects (DBBI, grid, FAED). The marginal value of further mechanism sweeps is approximately zero — that is evidence to stop computing and start retrieving.

## Bottom line

The puzzle is not unsolved for lack of compute or cleverness — it is unsolved because the last mile is anchored to a person, not to the artifacts. The way forward is anchors: the missing Telegram attachment, the book, a creator checkpoint — in that order.

---

*Method note: all experiments were observe-only; candidate keys were verified exclusively by exact secp256k1 point / hash160 match against the prize and 17ucy targets; padding-valid decrypts without an address match were treated as the documented 1-in-256 false positive. Nothing was signed or broadcast. Prize (~1.2565 BTC) and 17ucy (~3.7506 BTC) were unspent at the time of writing.*
