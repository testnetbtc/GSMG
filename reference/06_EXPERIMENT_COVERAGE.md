# 06 -- Prior experiment coverage

`reference/data/EXPERIMENT_COVERAGE.csv` is the row-level register. It holds the prior report's section 7 rows (`PRIOR-E...`) plus every experiment or attempt row extracted from the sources (`EXT-E...`): all 171 entries of Hosterjack's attempts data, B PR #15's campaigns, A PR #93's scripts and outputs, and the issue-thread sweeps. **Every row is a source-reported negative or claim. None was re-run here** except the published fixed recipes in [01](01_SOLVED_CHAIN.md) and [03](03_UNRESOLVED.md). This file explains what the negatives do and do not cover.

## 1. Why most negatives do not cover the disputed constructions

The validator decides what a sweep can find. Across the sources:

| Validator used | Who | Can it register a binary 79-byte or 1,327-byte output? |
|---|---|---|
| printable ratio >= 0.80-0.92 / English score | most of C before 2026-07-13 [C:content/attempts.js@caaa77a]; A PR #93 scripts [A:_pr93/_work/*.py@2c97f44]; B notebooks | **no** -- rejects any binary output |
| strict PKCS#7 + (pad >= 4 **or** magic prefix **or** printable >= 0.85) | B PR #15 `aes_try.check_pt` [B:_pr15/neo/harness/aes_try.py@1e913fd] | **no** for 1-byte-pad binary |
| PKCS#7 only | C blob-combination; several issues | yes, but then every ~1/256 hit is "valid" and needs another check |
| address match / "universal inspector" | C from 2026-07-13 [C:content/attempts.js@caaa77a L3603, L3832] | only for outputs interpreted as keys in the inspector's fixed readings |

KDF coverage is just as decisive. Many families tried **EVP-SHA256 only**, e.g. A PR #93 `joint_attack.py`, `cosmic_concat.py`, `decrypt3.py` [A:_pr93/_work/@2c97f44] and C's harness and demos [C:content/demos.js@caaa77a]. The reproduced openings of `salph_inner`, `p32_trailing` and `cosmic` all use **EVP-MD5**.

Consequences:

- C's "~33.5M null decrypts" on `salph_inner` [C:content/attempts.js@caaa77a L3419] used a readability gate and does not list the five-token MD5 literal; it **does not cover** M5.
- C's Cosmic families (~1.07M decrypts) never tested raw XOR bytes + EVP-MD5 (agent N2); they **do not cover** M6.
- B PR #15's ~33M trials across 52 campaigns (count in the register) never ran the five-token recipe on `salph_inner`, and its gate rejects 1-byte-pad binary (agent N4).
- [A#106 body Part C] reports "~2.5B verified tests" over {EVP-MD5, SHA1, SHA256, PBKDF2-SHA256(10k)} x encodings x modes x all four blobs x ~56k candidates. No candidate list or manifest is shipped, and the post does not reconcile with the reproducible MD5 chain on `salph_inner`.
- A negative is a statement about **its own candidates x KDFs x validator**, and nothing more. Some family totals rely on private registers or absent scripts (108 of C's 171 entries reference scripts not in the repository; B PR #15 cites an uncommitted 445-message transcript; the prior report's floflo777 and E054 registers are not held). Those totals cannot be audited.

## 2. Coverage by target (summary)

| Target | Families reported | Notable gaps |
|---|---|---|
| `salph_inner` | soup-token literals and hashes (C, PR93, PR15, issues); Roses-poem normalisations; 400-word and 370k-word dictionaries; integer and short-alnum brute force (C, 33M); PBKDF2 x6 iteration counts (PR15); table values (A#103) | binary-output validators; the full search history behind M5 |
| `p32_trailing` | ~288 Phase-3.2 strings, EBCDIC letters, VIC digits fwd/rev, FEN variants, 370k dictionary (C); PR15 campaigns; A#111 numeric re-encodings | WIF-family coverage outside the single published WIF; [B#17]'s continuation family is reported without a manifest (prior section 7) |
| `cosmic` | 4-ingredient combines, ~358k computed-value passphrases, XOR-of-N (N = 4...8), Merkle/Shamir, PBKDF2 x 29 iteration counts, EBCDIC/UTF-16 passphrase bytes (C); concat permutations (PR93); PR15 campaigns | raw-byte + MD5 forms (outside M6); a selection-free protocol |
| `urlblob` | 76 tests (C); A#106 sweep | treated as a puzzle container by some sweeps although its provenance is a URL path |
| `DBBI` / `FAED` | 9! digit permutations, 9! mono substitutions, transposition x substitution 3.27M, Vigenère/Beaufort periods 1-6, 3x3 Bifid, base-81, prime zero-out, OTP against the VIC sentence, capacity and statistical nulls (C); checkerboard / columnar / VIC full / hill-climb (PR93); b/c squares ([B#14]); full-period 5x5 Bifid ([B#13]); BYTENPHASE ([A#115]) | readability-only for most; C's Bifid used 3x3 squares, not the [B#13] 5x5 square |
| prize key | 86,310 brainwallet + 1,204 split-key derivations; ~17 DBBI/FAED scalars; 13 posted keys; ECDSA nonce reuse (distinct nonces) (C, PR15) | vocabulary-only; no interval or seed model |

## 3. Selection evidence (relevant to any chance argument)

- jackdevs66 searched tokens 5-7 of the Cosmic recipe [A#55 comment 3223858361].
- A 2023 recipe produced padding-valid `salph_inner` (79 B) and `cosmic` (1,327 B) outputs from unrelated passwords [A#15]; reproduced here.
- Chain-4's mask is a crib fit, shown by applying the same rule to a second Cosmic decrypt (reproduced).
- The 103x103 recipe's offset and base equal the observed minimum and range (reproduced).

Each published "hit" therefore sits on an unknown number of tried alternatives. No source supplies a pre-registered protocol that would let its chance weight be computed (prior section 10.4, agreed).

## 4. What is genuinely not covered (by any held source)

Listed to steer the next checks, **not** as an authorisation to sweep:

1. any **pre-registered** binary-output validation of M5 (a creator commitment, or an address relation fixed before testing);
2. the 83/84-token DBBI parses named in the prior brief (not located; [A#21 comment 2599707789] is a different b-as-prime parse);
3. a typed specification of the 2023 labels as values or as operations (prior section 9.3) -- neither exists;
4. any seed/interval model with a stated generator and bound.
