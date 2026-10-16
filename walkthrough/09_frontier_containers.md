# The frontier, part 1 -- the four open containers and every community "opening", with verdicts

Status: OPEN. Several community recipes produce bytes with valid padding; none has a checkpoint.
Previous: [08_salphaseion_soup.md](08_salphaseion_soup.md) --
Next: [10_frontier_dbbi_faed_btcseed.md](10_frontier_dbbi_faed_btcseed.md)

This page is deliberately plain-spoken. For each proposal it separates two
questions that the community often blurs: **mechanics** (if you run the
recipe, do you get the bytes they say?) and **significance** (is the result
a real step of the puzzle?). Every "yes" on mechanics below has been re-run
here from fresh code; every significance verdict is "unverified", and the
page explains why in each case.

## 1. The four containers

All four are OpenSSL `Salted__` envelopes (8-byte header, 8-byte salt, then
AES-256-CBC ciphertext).

| Name | Where it lives | Envelope | Salt | Ciphertext | SHA-256 of envelope | Provenance |
|---|---|---:|---|---:|---|---|
| `salph_inner` | SalPhaseIon soup, reassembled around the `enter` insertion (08) | 96 B | `3ab585348552415d` | 80 B | `9e2831e1b34b5f34796df47ccaf6530d48d371c61a6bff84d60db1064fa7a258` | on the puzzle page |
| `p32_trailing` | last 128 base64 chars of `PT-phase32` (06) | 96 B | `b45a5e3d827593ca` | 80 B | `291dfd6f3e759ec2e272b35a00c24907da70c3e7a9291b4c13605c7b0b4f3de9` | INSIDE creator-encrypted text -- the strongest provenance of the four |
| `cosmic` | SalPhaseIon page, "Cosmic Duality" textarea (08) | 1,344 B | `2d3f6fe06dc950e6` | 1,328 B | `b18950551a4dd0cb8a9378f0906ba18c03a15f0ee83eb98c6bc90165c5f79805` | on the puzzle page |
| `urlblob` | hex-encoded in a URL path that someone requested from gsmg.io in 2026 (Wayback 2026-01-05 and 2026-02-07 captures of a generic error page) | 112 B | `74c974e3f92e64b5` | 96 B | `25b3619a18174794d4ddd0d743f78f04007c0cf1830f6cf9301bc671631799bb` | a community artifact, NOT a page-embedded container; bytes 53-111 have no stated source |

Names: the community uses "inner blob", "small blob", "Short 79B", "3.2.2",
"Cosmic Duality 79B" (a mislabel) and more for these. When in doubt, go by
the salt.

## 2. Why "it decrypted!" proves nothing by itself

Decrypting with a WRONG key still produces bytes -- random ones. OpenSSL then
checks PKCS#7 padding: if the last byte happens to be `0x01`, the padding
is "valid" and a plaintext one byte shorter than the ciphertext is returned.
That happens for about 1 in 256 wrong keys. So an 80-byte container yields a
79-byte "plaintext" roughly once per 256 wrong passwords, and a 1,328-byte
container yields 1,327 bytes at the same rate. Measured in the sources:
1,235 such hits in 300,000 wrong passwords (1 in 243), and "255 times out of
65536" in chat.

Consequences that every proposal below has to answer:

- an output whose padding is exactly one byte (`0x01`) and whose bytes look
  random is the ORDINARY wrong-key shape;
- a real stage must show something that could not be manufactured: readable
  text in the puzzle's style (every solved stage did), or a value fixed
  BEFORE the test (as the creator's 2019 Phase-1 hash was), or a key whose
  address is the prize;
- "the output contains a 32-byte field" or "the hash of the output" is not
  evidence, because every 79-byte string contains 32-byte fields and has a
  hash.

A control that settles the point: in August 2023 a solver published
completely different passwords that also open `salph_inner` to 79 bytes and
`cosmic` to 1,327 bytes with valid padding (reproduced here, step
`a15_padding_controls`). Same shapes, unrelated recipe.

## 3. The proposals, one by one

### 3.1 "Chain 1" -- `salph_inner` opened with five soup tokens (MD5)

- Recipe (first published 2026-01-01 by GalloClaudio64 in A issue #68;
  restated in B #17 and A #108): password = the literal string
  `matrixsumlistenterlastwordsbeforearchichoicethispasswordmatrixsumlist`
  (five soup tokens run together, `matrixsumlist` twice), key derivation
  `EVP_BytesToKey` with **MD5** (every solved stage used SHA-256),
  AES-256-CBC.
- Mechanics: **reproduced.** 79 bytes, SHA-256
  `1449a2178eea7c0e3fabac8c1ad2afa294be4fc1800c594a025a056e88c626bf`
  (`reproduction/results/chain1.bin`; hex view `chain1.hex`). Python and
  the OpenSSL CLI agree.
- What the bytes look like: random. There is no text in them -- that is why
  GitHub shows the file as garbage. The proposers cut them as 32 + 32 + 15
  bytes and call the pieces `K_C1`, `K_C2`, `E_C`
  (`E_C = 38d4f4c90cb45fdfc8cff50d0ed1c5`).
- Significance: **unverified.** One-byte padding; no creator mention of
  `E_C`, checksums or MD5; nothing defines `E_C` before the recipe produced
  it; the search that led to this password is not published. A 2026 "fixed
  typos" version of the container turned out to be byte-identical to the
  original.

### 3.2 "Chain 2" -- `p32_trailing` opened with a WIF string (MD5)

- Recipe: take the first 32 bytes of chain 1, write them as an uncompressed
  mainnet WIF string (`5K2byJMssxFKuTgnk9YQjpBz5FhkwwF2LaZoAyTus8HjGEpz8AT`,
  51 characters) and use that text as the password, MD5 derivation.
- Mechanics: **reproduced.** 79 bytes, SHA-256
  `b40fce72ef5638e4f79b3233e653f8a5dbdb0d4ae2009d2d3da2c98b70f4d004`
  (`chain2.bin` / `chain2.hex`). Fields named `K_S1`, `K_S2`, `E_S`
  (`E_S = 740a25de4b8e946d0a5ae2667a23a2`). The addresses of `K_S1` and
  `K_S2` are `1MixpoELBvfkFSRUQtDCGXbdG53cjqknZT` and
  `176ysPe7FdevdQjZWaFCK2nnVbzX9Tgydy` -- neither is the prize.
- Significance: **unverified**, but this is the strongest community
  observation: two FIXED successive padding passes (chain 1 then chain 2)
  are rarer than one. Its weight cannot be computed, because nobody knows
  how many password families and encodings were tried before this pair was
  published. `E_S` has no definition anywhere except as "the last 15 bytes
  of the output". Claims that `E_S` "independently verifies" the chain, or
  that `E_C` reappearing in the chain-4 password is a confirmation, are
  circular (the chain-4 password was built from `E_C`).

### 3.3 "Cosmic" -- the seven-token XOR key (MD5)

- Recipe (concept 2025-04-11; decrypt claimed 2025-08-18 by jackdevs66;
  recipe link 2025-08-23; token list 2025-08-31; carried by A #68/#72 and
  many others): take the SHA-256 of each of seven tokens
  `matrixsumlist, enter, lastwordsbeforearchichoice, thispassword,
  matrixsumlist, yourlastcommand, secondanswer`, XOR the seven digests
  (`a795de117e472590e572dc193130c763e3fb555ee5db9d34494e156152e50735`),
  use the 32 raw bytes as the password, MD5 derivation.
- Mechanics: **reproduced.** 1,327 bytes, SHA-256
  `4f7a1e4efe4bf6c5581e32505c019657cb7b030e90232d33f011aca6a5e9c081`
  (`cosmic_output.bin` / `cosmic_output.hex`). Of the four encodings (raw
  bytes or hex text as password, MD5 or SHA-256 derivation) ONLY raw + MD5
  passes padding. Because XOR cancels the duplicate, the key really depends
  on five tokens, and token order cannot matter (so "order is critical"
  claims are false).
- Significance: **unverified, and weakened by the evidence**: the proposer
  wrote "Uniqueness (p5-p7 search)" -- tokens 5-7 were found by searching;
  tokens 6-7 are solver readings of the soup's plain pieces that first
  appear in chat in 2023-09 and 2025-08; the output is random-looking (7.87
  bits of entropy per byte) and its proposer conceded its hash is "NOT an
  externally-known expected checksum"; a solver called it a padding false
  positive the day it was announced. A rival "Set A" (`... sha256, theone`,
  key `818af53d...`) claims the same output and opens nothing (reproduced).
  A claim in C that Cosmic "decrypts nothing / is fabricated" is also wrong
  on mechanics: C never tested raw bytes + MD5.

### 3.4 "Chain 4" -- a nested envelope "hidden" in the Cosmic output

- Recipe: take bytes 158 to the end minus one of the Cosmic output, XOR
  with the repeating 8-byte mask `b657264f2f6e6921`; the result (1,168
  bytes) begins `Salted__` with salt `5bbd88ac32481bca`; decrypt it with
  the password `E_C || E_S || first 2 bytes of E_B` (32 bytes), MD5.
- Mechanics: **reproduced.** 1,151 bytes, SHA-256
  `e4269ed5fbb202a81e5e1aa6b5190fdd1ea126b2c8547ea7cdbdf45387ea135b`
  (`chain4.bin` / `chain4.hex`).
- Why it proves nothing: the mask is exactly `output[158:166] XOR
  "Salted__"` -- it was chosen to make the header appear (a "crib fit").
  Applying the same rule to a DIFFERENT padding-valid Cosmic decrypt
  (`cosmic_A.bin`, of unknown recipe) also produces a well-formed
  "envelope" (salt `0391bdb016191c9d`) -- reproduced control. Offset 158 is
  2 x 79, the layout the analysts imposed. There is no `Salted__` and no
  salt anywhere in the 1,327 bytes before masking.

### 3.5 "103 x 103 -> base 38 -> Half and Better half"

- Recipe (A #72, #79, #81): the first 10,609 bits of the Cosmic output as a
  103 x 103 matrix; secondary value = row sum plus the column sum seven
  places over; subtract 80; read in base 38; split 32 + 32 + 4 bytes.
- Mechanics: **reproduced.** Two 32-byte values beginning `0423d911` and
  `48cc46e6`, trailer `fc0c1b02`, addresses `1JG648ya.../15E3pcDD...` and
  `145ZQ9si.../1FhbJnrd...`. **No prize match.**
- Why it proves nothing: shift 7, offset 80 (= the smallest value observed),
  base 38 (= the range observed) and the split were all chosen after looking
  at the numbers. The two 32-byte values are public, so signatures from
  their addresses prove nothing.

### 3.6 Others, briefly

| Proposal | Status |
|---|---|
| A #84's `chain4.bin` (1,168 B, `a80a399a...`) | equals neither the masked envelope nor chain 4; its stated source matches no held object; unexplained |
| `cosmic_A.bin`, "XOR triangles", "LCP scores" (A #88) | recipe unknown ("made up by llms", says the B maintainer); cannot be reproduced |
| trailer `fc0c1b02` -> Phase-2 table values X = -4, H = 12, Y = 27, Q = 2 (A #103) | arithmetic only; conflicts with the relayed creator remark "#...# wasn't used" |
| `urlblob` (76 tests in C; A #106 sweep) | treated as a container by some sweeps although it is a URL path someone requested |
| the 2023 "MatrixSumlist AnsToo" opening (A #15) | 79 B and 1,327 B with SHA-256 derivation from unrelated passwords -- the control of section 2 |
| donor funding / "they need funds to live" as an on-chain trigger | no mechanism shown; rebutted repeatedly in the threads |
| OP_RETURN messages as clues | the creator-attributed handle confirmed on-chain messages "are not his and are not part of the puzzle" |

## 4. Verdict table

| Proposal | Mechanics | Significance | First step that rests on choice rather than clue |
|---|---|---|---|
| chain 1 | reproduced | unverified | the duplicated-token literal and MD5 |
| chain 2 | reproduced | unverified (strongest) | the WIF representation; no independent `E_S` |
| cosmic (Set B) | reproduced | unverified, weakened | tokens 5-7 found by search; MD5; raw-byte password |
| cosmic (Set A) | refuted | -- | its claim is false |
| chain 4 | reproduced | not evidence | the mask is a crib fit (control reproduced) |
| 103x103 base 38 | reproduced | unverified | shift/offset/base/split fitted to the data |

## 5. What has already been tried on these containers

The sources record enormous sweeps: C's ~33.5 million null decrypts on
`salph_inner`, B PR #15's ~33 million trials over 52 campaigns, an
unaudited "~2.5 billion verified tests" in A #106, plus dictionaries (400
words to 370,000 words), soup-token combinations, integer brute force,
PBKDF2 variants, EBCDIC and UTF-16 passphrases and more
(`reference/06_EXPERIMENT_COVERAGE.md`). Two limits apply to almost all of
them: most used a "printable text" validator, which rejects any binary
output and therefore cannot even see the MD5 chains above; and most used
SHA-256 derivation only. So those negatives neither support nor refute
chains 1-4 -- they simply looked elsewhere. A negative is a statement about
its own candidates x derivations x validator, nothing more.

## 6. On-chain facts (reported, dated)

| Fact | Source |
|---|---|
| Prize address funded with 5 BTC on 2019-04-13 | A PR #101 |
| 2020-05-11, tx `2aa9a4a90be819d5122d70c993280785a0508f163521e7b38cebb4db0b071b13` (locktime 629998): 2.5 BTC to `17ucy1K9ZUAaoY6JVtM932W9jUp5LXfyHa`, change back to the prize. Its three inputs carry the uncompressed prize public key (reproduced: 3 occurrences in the held tx hex) | A PR #101; B PR #15 |
| 2024-04-24, tx `88cdb3cdca12b471551b1b26188508a14ca5fd8a415223ffb7c190381c9b9df3` (locktime 840003): 1.25 BTC to `17ucy...`, change back | A PR #101 |
| `17ucy...` never spent: 3.75055310 BTC (2026-08-18) | A PR #101 |
| prize balance about 1.256 BTC through 2026 (dust keeps arriving) | dated observations |
| the two spends used distinct ECDSA nonces (no nonce-reuse weakness) | B PR #15 |

The prize key has SPENT twice (the halvings), so whoever ran the puzzle
holds it. Coins still sitting at the address are not proof that nobody else
knows the key; a spend to an unrelated address would be. Creator-attributed:
"If wallet != empty, puzzle not solved. (Most likely)."

## 7. What a real opening would look like

Any of these would settle it without argument, and each can be checked
offline in seconds:

1. readable text in the puzzle's style (every solved stage produced text);
2. a value that matches something published BEFORE the recipe (the creator's
   only such value is the 2019 Phase-1 hash);
3. a 32-byte value whose secp256k1 public point is the prize public key
   (`research/2026-10-15_btcseed_bits/btclib.py` does exactly this check,
   with no network and no wallet).

## 8. Verification pointers

`reproduce.py` steps `naddiseo17_chain1_salph_inner`,
`naddiseo17_chain2_p32_trailing`, `cosmic_seven_token_xor`,
`cosmic_seven_token_xor_set_A`, `chain4_masked_nested_envelope`,
`chain4_crib_control_cosmic_A`, `a15_padding_controls`,
`cosmic_103x103_base38`, `prize_pubkey_to_address`; `verify.py` re-derives
chain 1, chain 2 and Cosmic (and the two negative encodings) independently.
Hex views of every binary output are in `reproduction/results/*.hex`.

Sources: `reference/03_UNRESOLVED.md`, `reference/05_COMMUNITY_MECHANISMS.md`,
`reference/06_EXPERIMENT_COVERAGE.md`, `reference/07_CONTRADICTIONS.md`,
`reference/08_GLOSSARY.md`.
