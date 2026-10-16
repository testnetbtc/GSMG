# 03 -- Unresolved artifacts and open constructions

This file covers everything past the solved chain in [01_SOLVED_CHAIN.md](01_SOLVED_CHAIN.md). Two verdicts are kept separate throughout:

- **mechanics** -- whether a published recipe yields the stated bytes (`reproduced` when re-run here);
- **significance** -- whether those bytes are an intended puzzle stage. **No open object below has an independently validated significance.**

## 1. The open containers

| Container | Envelope / ciphertext | Strongest provenance | Proposed openings (mechanics) | Significance |
|---|---|---|---|---|
| `salph_inner` | 96 / 80 B, salt `3ab585348552415d` | on the SalPhaseIon page (reproduced against held captures) | five-token raw literal + EVP-MD5 -> 79 B (`OUT-chain1`), reproduced | unverified |
| `p32_trailing` | 96 / 80 B, salt `b45a5e3d827593ca` | embedded at the end of `PT-phase32` (reproduced) | uncompressed WIF of `OUT-chain1[0:32]` + EVP-MD5 -> 79 B (`OUT-chain2`), reproduced | unverified |
| `cosmic` | 1,344 / 1,328 B, salt `2d3f6fe06dc950e6` | on the SalPhaseIon page (reproduced against held captures) | raw XOR of SHA-256 of seven tokens (Set B) + EVP-MD5 -> 1,327 B (`OUT-cosmic`), reproduced; Set A key `818af53d...` opens nothing under four encodings (reproduced) | unverified |
| `urlblob` | 112 / 96 B, salt `74c974e3f92e64b5` | a URL path requested of gsmg.io in 2026 -- community artifact | none | not a puzzle container on current evidence |

**Padding arithmetic** (prior report section 10.4; restated, not re-derived): for a wrong key, PKCS#7 is valid with probability ~ 1/255. One-byte padding accounts for ~99.6% of those cases. An 80-byte ciphertext therefore yields a 79-byte "valid" plaintext about once per 256 wrong passwords. Measured in sources: 1,235/300,000 (1 in 243) on the real 80-byte ciphertext [B:_pr15/unverified/why_false_decrypts_recur.md@1e913fd], and "255 times out of 65536" in chat [A:_pr93/_work/chat_transcript.txt@2c97f44 L174337]. Every proposed opening above has 1-byte padding; that shape is the ordinary false-positive shape.

### 1.1 The two 79-byte chains (Naddiseo #17 lineage)

**Mechanics: reproduced.** Python and OpenSSL agree byte-for-byte. Password for `salph_inner`:

```text
matrixsumlistenterlastwordsbeforearchichoicethispasswordmatrixsumlist
```

`OUT-chain1` (79 B, `1449a217...26bf`); `E_C` = `38d4f4c90cb45fdfc8cff50d0ed1c5`. Password for `p32_trailing` = the 51 ASCII characters of the uncompressed mainnet WIF of `OUT-chain1[0:32]`:

```text
5K2byJMssxFKuTgnk9YQjpBz5FhkwwF2LaZoAyTus8HjGEpz8AT
```

`OUT-chain2` (79 B, `b40fce72...d004`): `K_S1` = `b06fa6f20561756c865dac7190f063480a371e4a13206e529ee7e9078f309c4b`, `K_S2` = `b11d211ca0a17cd68c580308f3e6f21d3f935c8da3c4373b6f73ab5ccfaea597`, `E_S` = `740a25de4b8e946d0a5ae2667a23a2`. Uncompressed addresses of `K_S1`/`K_S2` are `1MixpoELBvfkFSRUQtDCGXbdG53cjqknZT` / `176ysPe7FdevdQjZWaFCK2nnVbzX9Tgydy`, neither the prize (reproduced).

**Lineage:** first published as a chain in [A#68 comment 3704010992] (GalloClaudio64, 2026-01-01 19:07:36 UTC), restated in [B#17] (2026-10-05) and [A#108 body] (2026-08-27, "CADEIA"). The PR93 file listing names a Telegram attachment `salphaseion_plain_79.bin` (79 B, undated) [A:_pr93/_work/files_listing.txt@2c97f44]. A 79-byte "anchor" `e2590f15...` in [A#82 body] equals neither chain output (agent D2 arithmetic; reported).

**Significance: unverified.** No source defines `E_S` (or `E_C`) as a verification field before the recipe produced it. Neither creator corpus contains "E_S", "checksum", "verification" or "WIF" (see [04_CREATOR_CLUES.md](04_CREATOR_CLUES.md) section 5). [A#108 body] treats `E_C` reappearing in the chain-4 password as validation; that is **circular**, because the chain-4 password was built from `E_C`. B PR #15, a 33-million-trial campaign, never tried the five-token recipe [B:_pr15/neo/LEDGER.md@1e913fd] (agent N4). Most published negatives on `salph_inner` used printable-text validators that would reject any binary output; see [06_EXPERIMENT_COVERAGE.md](06_EXPERIMENT_COVERAGE.md).

### 1.2 Cosmic

**Mechanics: reproduced.** Tokens (Set B) `matrixsumlist, enter, lastwordsbeforearchichoice, thispassword, matrixsumlist, yourlastcommand, secondanswer`; XOR of their SHA-256 digests:

```text
a795de117e472590e572dc193130c763e3fb555ee5db9d34494e156152e50735
```

Of the four encodings (raw/hex x MD5/SHA-256), only **raw 32 bytes + EVP-MD5** gives valid padding: 1,327 B, SHA-256 `4f7a1e4efe4bf6c5581e32505c019657cb7b030e90232d33f011aca6a5e9c081` (reproduced). The two `matrixsumlist` digests cancel, so the key is the XOR of five digests (reproduced).

**Lineage:** announced 2025-08-23 in Telegram by "Mauro Etrade" with a link to `jackdevs66/GSMG5_CDuality`. The same day, solver k1ng judged it a padding false positive ("treated as hex ... md5 ... padding byte was 01 ... 99.9% false positive"; his description of "hex" does not match the raw-byte form that reproduces) [A:_pr93/_work/chat_transcript.txt@2c97f44 L133743-L133912]. It was then republished in [A:_pr68/GAP_ANALYSIS.md@27ea50e], [A#68 comment 3704010992] and [A#72 body]. A different token set, Set A (`...matrixsumlist, sha256, theone`, key `818af53d...b402`), claims the same output in [A#62 comment 3432403162] and [A#69 body]. **Reproduced: Set A opens nothing** under the four encodings.

`yourlastcommand` and `secondanswer` are solver readings of `shabefourfirsthintisyourlastcommand` / `shabefanstoo`. The token `yourlastcommand` first appears in chat 2023-09-01, `secondanswer` 2025-08-23 [A:_pr93/_work/chat_transcript.txt@2c97f44 L32680, L133896]. C's claim that these tokens "originated as solver dust" on-chain [C:docs/LOOSE-ENDS.md@caaa77a] is undated.

**Significance: unverified.** The output digest `4f7a1e4e...` is self-referential: its proposer conceded it is "NOT an externally-known 'expected checksum'" [A#72 comment 3830122705]. Wayback captures of `gsmg.io/4f7a1e4e...` begin 2026-06-02 (error) and 2026-07-08 (parked placeholder), i.e. solver probes, not a puzzle page [A#104 body] [B:_pr15/neo/materials/wayback/INDEX.tsv@1e913fd]. Entropy 7.87 bits/byte [A:_pr68/GAP_ANALYSIS.md@27ea50e]. C calls the output "fabricated" [C:docs/ENDGAME-ANALYSIS.md@caaa77a section 7], but C never tested the raw-byte/MD5 form; that claim is refuted on mechanics (see 07).

### 1.3 Derived constructions on `OUT-cosmic`

| Construction | Mechanics | What makes it weak |
|---|---|---|
| **103x103 -> base-38 "Half / Better half"** [A#72 body] [A#79 body] [A#81 body] | **reproduced.** Secondary string of 103 chars (values 80-117); 68 bytes = `0423d911...` (32) || `48cc46e6...` (32) || `fc0c1b02`; addresses `1JG648ya...`/`15E3pcDD...` and `145ZQ9si...`/`1FhbJnrd...`; **no prize match** | shift 7, offset 80 (= observed minimum), base 38 (= observed range) and the 32/32/4 split were all chosen after inspecting the bytes. The 32-byte values are fully public [A#79 body] [A#97 body], so signatures or on-chain activity at those addresses prove nothing. |
| **Chain 4** [A#68 comment 3704010992] | **reproduced.** `OUT-cosmic[158:-1]` XOR repeating `b657264f2f6e6921` -> 1,168 B envelope (`f0bd54d1...`, salt `5bbd88ac32481bca`); EVP-MD5 with `E_C||E_S||E_B[:2]` -> 1,151 B `e4269ed5...` | **the mask equals `OUT-cosmic[158:166]` XOR `"Salted__"`**, so the header is forced by construction (reproduced). The same rule applied to a different padding-valid Cosmic decrypt (`OUT-cosmic-A`) yields a different well-formed "nested envelope" (`ENV-ca158`, salt `0391bdb016191c9d`) -- reproduced crib control. No source derives offset 158, the trim or the mask from a clue. |
| **#84 `chain4.bin`** 1,168 B `a80a399a...` [A#84 body] | not reproduced | equals neither the masked envelope (`f0bd54d1...`) nor chain 4 (`e4269ed5...`); its stated "2,432-byte Phase 3.2 blob" source matches no held object [A#84 comment 4322070842] |
| `cosmic_A`, `ca[280:312]`, XOR triangles, "LCP" scores [A#88 body] | cannot be reproduced | `cosmic_A.bin`'s recipe is unknown; Naddiseo: "made up by llms" [A#88 comment 5873152000] |
| trailing `fc0c1b02` -> Phase-2 table values X=-4, H=12, Y=27, Q=2 [A#103 body] | arithmetic only | conflicts with the reported creator remark "#...# wasn't used." [A#106 body] |

## 2. DBBI

- 91 letters over a-i, no `o`, `SOUP[0:91]`, SHA-256 `71fe4625...c5ca`; first-occurrence order `DBIFHCEGA`; 91 = 7x13 (reproduced).
- Letter counts b25 e18 f10 g10 c8 h8 i5 d4 a3 (reported [C:content/attempts.js@caaa77a]); IoC 0.151 [A:_pr93/FINDINGS.md@2c97f44#L35-L36]. `b` falls at prime positions 2,3,5,7,11,31,79, and the first segment `dbbibfbhcc` has b exactly at 2,3,5,7 [A:_pr93/_work/prime_out.txt@2c97f44] (source-reproduced output; descriptive only).
- b/c expansion (`d->bb`, `e->bc`, `f->cc`, `g->bbc`, `h->bcc`, `i->ccc`) gives 169 = 13^2 (reproduced) [B#14].
- **YOUWON**: DBBI (a=1...i=9) minus the VIC sentence (A=1...Z=26), mod 26, contains `YOUWON` at offset 21 [B:_pr15/unverified/salphaseion_dbbi_youwon.md@1e913fd] [B:_pr8/unverified/dbbi-youwon-otp.md@821acd5]. 0/200,000 shuffles reproduce it (reported). B PR #15 notes the layout is forced once VIC and a-i are fixed; a solver says "OTP was never used" [B:_pr9/other-puzzles/gsmg-salphaseion/NOTES.md@041ee64 Finding 23]. Interpretation contested.
- Triangle model (91 = C(14,2)) refuted by a random-string null [A:_pr93/FINDINGS.md@2c97f44#L71-L73].
- No authenticated decode to `yellowblueprimes`. The two DBBI parses (83/84 tokens) named in the prior brief were **not located** in any of the three repositories.

## 3. FAED

- 570 letters, `SOUP[195:765]`, SHA-256 `066191b4...f3c2`; counts a54 b49 c52 d49 e69 f57 g107 h58 i75 (reproduced); IoC ~ 0.118 [A:_pr93/FINDINGS.md@2c97f44]; b/c expansion 1,225 = 35^2 (reproduced) [B#14].
- Capacity arguments (reported, engine-generated, scripts absent): read as a number, FAED is always >= 2^1800, i.e. 226 bytes, and cannot be seven 32-byte keys [C:content/attempts.js@caaa77a L77].
- [A#115] BYTENPHASE construction (drop `FAE`, sum groups of 9, Vigenère-subtract `THEPROBLEMIS`, ...) is arithmetic-consistent (agent D2) but has unjustified choices, by its author's own admission.

### 3.1 Full-period Bifid -> `BTCSEED`

**Mechanics: reproduced.** Square `DBIFHCEGAKLMNOPQRSTUVWXYZ` (DBBI first-occurrence + rest, J omitted), decrypt, row-then-column, period 570 -> 570 letters, SHA-256 `0c5d984f90e9baefc09f1d3888e62acbd101f9b0194887e2ae88fc6c9967745e`, head `BTCSEED`, single `Z` at zero-based index 97 [B#13]. Even positions use only `{B,C,D,E}`; odd positions minus I/O = 256 letters over 23 symbols; the period-2 interleaved identity holds (all reproduced). The structure follows from all FAED letters lying in square rows 0-1 (prior report section 4.4).

**Lineage:** first posted in Telegram by "Sycorax" on 2025-06-11 (keyword `dbifhceg`, period 570) [A:_pr93/_work/chat_transcript.txt@2c97f44 L122236]. B PR #9 holds `SALPH_bifid_decoded.txt`, which matches the reproduced output (agent N4 hash check) [B:_pr9/other-puzzles/gsmg-salphaseion/SALPH_bifid_decoded.txt@041ee64]. C modelled Bifid with 3x3 squares and could not reproduce it [C:content/demos.js@caaa77a] -- not a negative for this construction.

**Significance: unverified.** No generator, suffix encoding or checkpoint is specified. [A#112] cites "BTCSEED, sha256 15d62c82..." without stating which object was hashed.

## 4. The 2023 labels

`yellowblueprimes`, `matrixsumlist`, `lastwordsbeforearchichoice`, `yinyang` (exact concatenated decode in [04_CREATOR_CLUES.md](04_CREATOR_CLUES.md) section 3). Only `matrixsumlist` and `lastwordsbeforearchichoice` appear as literal soup text. No source gives an authenticated value for `yellowblueprimes` or `yinyang`, or an authenticated meaning for `matrixsumlist` (row/column sums are one reading, labelled INFERRED by C itself). C's harness test of the literal four-token concatenation under SHA-256 fails on `cosmic` [C:.github/scripts/verify.mjs@caaa77a#L100]; that excludes only that one string.

## 5. Seed, interval, vanity

- No source supplies an interval [L,U], a seed-to-key function, a generator version or a stopping bound. A vanity prefix shows filtering, not the candidate-generation method (prior report section 11, agreed). C's "vanity => random key only inside cosmic" [C:docs/ENDGAME-ANALYSIS.md@caaa77a section 8c] is an interpretation.
- Naddiseo identifies a `keyinfo.txt` circulating in issues as "an output file from split-key vanity address generation, which is my tooling and unrelated to the puzzle's data" [A#109 comment 5903808733].
- An on-chain message "GSMG.io neighbors, half and double" paid dust to the addresses of P-G, P/2, 2P and P+G of the prize point (reported, B PR #15; agent N4) [B:_pr15/neo/LEDGER.md@1e913fd#L2114-2129]. Who sent it is unknown, and the creator-attributed handle confirmed that blockchain messages "are not his and are not part of the puzzle" [C:content/sowut-data.js@caaa77a id 12653].

## 6. On-chain facts (dated, reported)

| Fact | Source |
|---|---|
| Prize address funded with 5 BTC on 2019-04-13 | [A:_pr101/README.md@68d09aa] |
| 2020-05-11 tx `2aa9a4a90be819d5122d70c993280785a0508f163521e7b38cebb4db0b071b13` (locktime 629998): 2.5 BTC -> `17ucy1K9ZUAaoY6JVtM932W9jUp5LXfyHa`, change -> prize; its three inputs carry the uncompressed prize public key (**reproduced**: 3 occurrences in the held tx hex [B:_pr15/neo/materials/chain/tx_halving_spend.hex@1e913fd]) | [A:_pr101/README.md@68d09aa] |
| 2024-04-24 tx `88cdb3cdca12b471551b1b26188508a14ca5fd8a415223ffb7c190381c9b9df3` (locktime 840003): 1.25 BTC -> `17ucy...`, change -> prize | [A:_pr101/README.md@68d09aa] [B:_pr15/neo/materials/chain/tx_halving2024_spend.hex@1e913fd] |
| `17ucy...` never spent; 3.75055310 BTC on 2026-08-18 | [A:_pr101/README.md@68d09aa] |
| Prize balance 1.25634510 BTC (2026-06-26 C; 2026-08-18 A PR #101); 1.25649674 BTC (2026-10-14, prior report) | dated observations, consistent with incoming dust |
| Prize-key spends use distinct ECDSA nonces | [B:_pr15/neo/attempts/campaign_45_affine_nonce_tx_halving_spend_tx_halving2024_spend.jsonl@1e913fd] (reported) |

The prize key has **spent** (at both halvings). The coins remaining at the address are not evidence that nobody else knows the key; only a spend to an unrelated address would be (prior report section 8, agreed). The creator-attributed handle: "If wallet != empty, puzzle not solved.\n\n(Most likely)." [A:_pr93/_work/chat_transcript.txt@2c97f44 L90252].
