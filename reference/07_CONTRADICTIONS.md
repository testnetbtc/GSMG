# 07 -- Contradictions and corrections

Both sides of every conflict are given with citations, followed by an assessment of which is better supported and why. Nothing is silently resolved. Machine-readable rows extracted from each source are in `reference/data/CONTRADICTIONS.jsonl`.

## 1. Where this build disagrees with, corrects or extends the prior report

| # | Prior report says | This build finds | Evidence | Assessment |
|---|---|---|---|---|
| P1 | 2021 Christmas hint dated **2021-12-25** (section 5) | posted **2021-12-26** 20:18 UTC (15:18 UTC-5) | [C:content/sowut-data.js@caaa77a id 8000]; [A:_pr93/_work/chat_transcript.txt@2c97f44 L19304] | two independent timestamps agree; the 12-25 date comes from B's image filename. **Correction.** |
| P2 | close-friends hint dated 2026-07-12 | 2026-07-13 00:51 UTC = 2026-07-12 19:51 UTC-5 | [C:content/sowut-data.js@caaa77a id 66573] | timezone only; both are right in their zone. |
| P3 | "445 vs 510 creator messages" listed as an unresolved contradiction (section 2.4, section 8) | **resolved**: 445 = 411 text + 34 media records up to 2026-05-28; C later extended the dataset by 65 messages (2026-07-13->09-01) | transcript <-> dataset match 411/411 (agent N6); [C:docs/CREATOR-INTEL.md@caaa77a L3] | no remaining conflict; completeness of either corpus is still unproven. |
| P4 | Jrk's "Ancient spelling" reply "is not explicit confirmation" of FEFEFE/104 | it is a **Telegram reply to** Janusz's "FORTY but hundred FOUR = 104 is the fefefe square" and calls the spelling a typo | reply_to 5952 in [C:content/sowut-data.js@caaa77a id 5960]; [T L13992-L14013] | stronger than the prior reading: evidence **against** the 104 numerology. |
| P5 | friends/family (9595): "underlying reply context incomplete" | context found: answer to "if you need to disappear... is there someone else who knows the solutions... And someone to half the prize" | [T L22780-L22783] | sharpens the prior reading (succession/data-access), confirmed. |
| P6 | Cosmic -> 103x103 -> base-38 "not reproduced in this task" (section 6) | **reproduced**; matches every published value; no prize match | `reproduction/results/reproduction_results.json` step `cosmic_103x103_base38` | extension. |
| P7 | earliest public pointer for the 7-token Cosmic family: [B#6] 2025-08-24 (section 6) | XOR-of-7-hashes concept 2025-04-11 [A#27 comment 2796116788]; jackdevs66 claims 2025-08-18 [B#3] and 2025-08-18/19 [A#51]; link 2025-08-23 [A#55 body] and Telegram [T L133743]; token list 2025-08-31 [A#56 body] | dated issue comments and transcript | earlier lineage; still not first private discovery. |
| P8 | Cosmic recipe selection history unknown | jackdevs66: "Uniqueness (p5-p7 search)" | [A#55 comment 3223858361] | direct evidence of a **search** over tokens 5-7 -- weakens the recipe's chance argument. |
| P9 | (not mentioned) | a different padding-valid 1,327-byte Cosmic output and a 79-byte `salph_inner` output were published in **2023-08** from unrelated passwords | [A#15 comments 1668268853, 1674478225]; reproduced (`a15_padding_controls`) | new control: same shapes, unrelated recipe. |
| P10 | (not mentioned) | Set A seven-token key `818af53d...` claims the same Cosmic output; it opens nothing | [A#62 comment 3432403162] [A#69 body]; reproduced | new; refutes Set A's claim. |
| P11 | (not mentioned) | the chain-4 crib rule applied to another padding-valid decrypt yields another "nested envelope" | B PR#15 drive files; reproduced `chain4_crib_control_cosmic_A` | new; strengthens the prior report's section 9.4 "header can be forced". |
| P12 | 83/84-token DBBI parses "not located" (section 4.2) | a DBBI parse reading `b` as a prime marker with labels 2...83 exists | [A#21 comment 2599707789] | possible lead; its token count and grammar are not stated, so it is **not** confirmed to be the brief's parse. |
| P13 | `jackdevs66/GSMG5_CDuality` README: ordering called critical (section 6) | agreed, and Set B's own proposer later concedes the output digest is "NOT an externally-known expected checksum" | [A#72 comment 3830122705] | agreement, extra citation. |
| P14 | prize address facts: balance and spent outputs only (section 8) | second address `17ucy1K9ZUAaoY6JVtM932W9jUp5LXfyHa` received 2.5 BTC (2020-05-11) and 1.25 BTC (2024-04-24) from the prize key; never spent | [A:_pr101/README.md@68d09aa]; tx hex in B PR#15 (prize pubkey in 2020 spend inputs reproduced) | extension (reported on-chain facts). |
| P15 | 2023-08-03/06 "images" | 2023-08-03 creator media were video/GIF; the hints are typed text | [C:content/sowut-data.js@caaa77a ids 8792-8796] | minor. |
| P16 | puzzlehunt 102 issues / 9 PRs; comments 606/605 | 103 issues (new: #116, 2026-10-15 01:18 UTC) / 9 PRs; comments 606/605; #25 still 19/18 | `sources/discussions/puzzlehunt/COUNTS.json` | one new issue since the prior collection; no new comments in #61-#116. |
| P18 | [B#17] concerns the "inner blob" | only the **title** says inner blob; the body correctly names the phase-3.2 trailing blob (salt `b45a5e3d`); the thread gives neither the chain-1 recipe nor any "documented value" source | [B#17 body] | refinement of prior section 10.1. |
| P19 | earliest public BTCSEED: [B#13] lineage | Telegram 2025-06-11 (Sycorax) [T L122236]; B PR#8 (opened 2026-06-12) before [B#13] (2026-08-24) | agents N6, D3 | earlier lineage. |
| P17 | default-branch frozen commits fb92dd1 / 9e61693 / caaa77a | unchanged | `sources/REFS.tsv` | confirmed. |

No reproduced byte differed from the prior report's values (`reproduction_results.json`: 17 confirmed against the prior report plus 1 against a published key, 0 discrepancies).

## 2. Source-versus-source contradictions

### 2.1 Cryptographic mechanics

| Conflict | Side A | Side B | Better supported |
|---|---|---|---|
| Was Cosmic opened? | "decrypted" (1,327 B, `4f7a1e...`) [A:_pr68/GAP_ANALYSIS.md@27ea50e] [A#72 body] | "decrypts nothing... fabricated" [C:docs/ENDGAME-ANALYSIS.md@caaa77a section 7] [C:content/attempts.js@caaa77a] | **mechanics: A** (reproduced). C never tested raw bytes + EVP-MD5, and its demo uses a different token list. Significance: neither side established it. |
| "Verified not working" for the Cosmic key | Naddiseo tested SHA-256 of the **hex text** of `a795de11...` (`36b5a88e...`) [B#6] | jackdevs66's KEY `6ac438fa...`/IV `c6ff2e39...` come from the **raw** 32 bytes with salt `2d3f6fe06dc950e6` [B#6] [A#96 body] | **jackdevs66 on mechanics** (reproduced: raw bytes + EVP-MD5 opens); Naddiseo's test used a different input form (agent D3 hash check). |
| Same output from two token sets | Set A `...sha256, theone` [A#69 body] | Set B `...yourlastcommand, secondanswer` [A#72 body] | **Set B** (reproduced); Set A opens nothing. |
| Does `Salted__` fix the KDF? | yes [C:content/attempts.js@caaa77a L3626]; "Cosmic uses SHA-256 EVP" [C:docs/ENDGAME-ANALYSIS.md@caaa77a section 8c] | no -- the envelope does not name a digest (prior report section 3.1); [B:_pr15/unverified/salted_header_proves_password.md@1e913fd] says it proves password mode only | **B / prior**: the Cosmic and chain openings use MD5 under the same header. |
| Plaintext length from an 80-byte ciphertext | 64 bytes [C:content/attempts.js@caaa77a L3695] | 64-79 bytes (prior section 4.1) | **prior**; the reproduced chains are 79 bytes. |
| EVP IV | "IV = D3[:16]" [C:docs/VERIFIED-SOLUTIONS.md@caaa77a#L266] | IV = D2[:16] [C:.github/scripts/verify.mjs@caaa77a] | **D2** (reproduced). |
| Hidden `Salted__` in `cc[158:]` | exists [A#88 body] | no marker or salt anywhere in the 1,327 bytes [A#103 body] | **#103** (reproduced: absent before masking). |
| #84 `chain4.bin` | 1,168 B `a80a399a...` from a "2,432-byte Phase 3.2 blob" [A#84 body] | masked envelope is `f0bd54d1...`, chain 4 is `e4269ed5...` [A#84 comment 4322070842] | **comment 4322070842** (both hashes reproduced); #84's file remains unexplained. |
| "Typos in the live small blob" | R->J, k->s fixed [A#108 body] | the "fixed" blob is the canonical one; the variant is a transcription in [A#17]'s title | **canonical** (byte comparison). |
| Bifid BTCSEED reproducible? | "coincidental/unverified, cannot reproduce" [C:content/attempts.js@caaa77a L1760] | reproduces with the 5x5 square at period 570 [B#13] | **B#13** (reproduced); C modelled 3x3 squares. |
| a-i/o fields | "base-9" [C:docs/WALKTHROUGH.md@caaa77a#L1783] | decimal with o=0 [B:salphaseion.ipynb@9e61693] | **decimal** (reproduced). |
| Blob independence | "provably independent" [C:docs/BLOB-COMBINATION-ANALYSIS.md@caaa77a] | different salts/blocks do not exclude related passwords or plaintexts (prior section 8) | **prior**. |
| Grid residual | "one null padding byte" [C:docs/verify-findings.json@caaa77a] / "no residual" (various) | four zero bits | **four zero bits** (reproduced). |
| Grid colours | blue (40,40,200), yellow (240,240,0), "no third colour" [C:docs/ENDGAME-ANALYSIS.md@caaa77a section 6] | (63,72,204), (255,242,0), one FEFEFE cell [C:content/matrix.js@caaa77a] | **matrix.js / prior** (reproduced). |
| Grid counts | black 87, white 84 [A#68 comment 3704010992] | 86 / 85 | **86 / 85** (reproduced on the held PNG). |
| FEFEFE index | "spiral ~103/104" [C:docs/CREATOR-INTEL.md@caaa77a O6]; "spiral index 177" [A#111 body] | spiral 163 (0-based), row-major 102 | **163 / 102** (reproduced). |
| 2023 hint byte offsets | taunts at bytes 100-161 [C:docs/LOOSE-ENDS.md@caaa77a#L463] | bytes 62-160 | **62-160** (reproduced decode). |
| 2023 hint spacing | spaced words [B:README.md@9e61693#L345-L350] [C:docs/CREATOR-INTEL.md@caaa77a H8] | no spaces in the bytes | **no spaces** (reproduced). |
| VIC alphabet | `FUBCDORA.LETHINGKYMVPS/JQZXW` and `...PS.JQZXW` [A:README.md@fb92dd1#L332-L336] | `fubcdora/lethingkymvpszjqwx.` [B:README.md@9e61693#L140] | equivalent for this plaintext (reproduced decode); C misattributes A's form to Naddiseo. |
| B README password truncated? | yes, "...B5KR" [C:docs/WALKTHROUGH.md@caaa77a#L1071] | only in old snapshots [A:_pr16/README.md@f646872#L102] [A:_pr30/README.md@290c334#L104]; B HEAD is complete | **B HEAD**. C is stale. |
| Heisenberg spelling | `heisenbergs...` [A:README.md@fb92dd1#L266] | `heisenberg...` [C:docs/WALKTHROUGH.md@caaa77a#L2226] | **heisenbergs** (reproduced). |
| SHA256(causality) | `...5a0b8b...` [A#74 comment 3919889051] [A#68 comment 3909565527] | `...5b0a8b...` | **`...5b0a8b...`** (reproduced). |
| Cosmic offset-140 bytes | `81221210780f...` [A#74 comment 3919699171] | actual `81221010780f...4a3b4a0a367eedeaaee31d26` | **actual** (agent D2 on reproduced output). |
| PR #68's `cosmic.hex` | used as reference | diverges from byte 142 and has speech text appended (agent D1) | do not use. |
| #55 head16 | `44d19415...` (jackdevs66) | `8badeb45...` (Naddiseo) | both right: Naddiseo decrypted with the 16-byte header included (agent D1). |

### 2.2 Names and provenance

| Conflict | Side A | Side B | Better supported |
|---|---|---|---|
| "inner" | `inner96.b64` = `p32_trailing` [B:_pr15/neo/materials/inner96.b64@1e913fd]; [B#17] title "inner blob" | `salph_inner` = SalPhaseIon envelope | use salts (see 08). |
| "Cosmic Duality 79B (salt 3ab58534...)" | [A#68 comment 3704010992] | salt `3ab58534...` is `salph_inner`; Cosmic is `2d3f6fe0...` | registry (reproduced). |
| "phase 3.2.2" | VIC digits [A:README.md@fb92dd1#L323] | trailing container (prior report alias) | different objects; not merged. |
| "Dualite" title in page markup | [A:_pr102/README.md@7656174] | held 2024-11-23 and 2025-10-31 captures say `Cosmic Duality`; "Dualite" absent | **captures** (reproduced grep); the 2023 capture is not held, so an earlier markup cannot be excluded. |
| `urlblob` | "community artifact" [C:docs/ENDGAME-ANALYSIS.md@caaa77a section 8c] | "oracle" [C:docs/CREATOR-INTEL.md@caaa77a O10]; "not committed" [C:docs/LOOSE-ENDS.md@caaa77a#L587] | **community artifact** (Wayback URL-path evidence); "not committed" is stale. |
| `p32_trailing` "never noted by the community" | [C:docs/ENDGAME-ANALYSIS.md@caaa77a section 2] [C:docs/LOOSE-ENDS.md@caaa77a#L329-L332] | used in [A#68 comment 3704010992] (2026-01-01), [B#17] | **lineage**. |
| `cosmic_A.bin` | "Confirmed" operand [A#88 body] | "made up by llms" [A#88 comment 5873152000]; no recipe anywhere [A#92] | **unknown origin**; the file exists in B PR#15 drive (bytes held), recipe absent. |
| Drive `chain2_decrypted.bin` | named "chain 2" | 1,151 B, != the 79-byte chain 2 of [B#17] | different object. |
| Entry recipe author | "finally revealed" [B:README.md@9e61693]; "Official instruction" [C:docs/WALKTHROUGH.md@caaa77a#L2157] | posted by a Deleted Account; a solver adds "We did say to hash the text.." [T L18392-L18410] | **community**, not creator-authenticated. |
| Creator display name | "Jrk Bgrk" [B:README.md@9e61693#L415] | "Jrk Bgrt" [T, 411 messages]; [C:docs/CREATOR-INTEL.md@caaa77a] | **Bgrt** (transcript). |
| Halving date | "second time on Apr 19, 2024" [B:README.md@9e61693] | transfer tx on 2024-04-24 [A:_pr101/README.md@68d09aa] | compatible: halving date vs transfer date. |
| Prize amount | 2.5 BTC [A:README.md@fb92dd1#L18] [A:_pr68/GAP_ANALYSIS.md@27ea50e] | 1.25 BTC [B:README.md@9e61693] and later | dated statements; A's are stale. |
| Second-half sentence | "the second half will probably be used for ANOTHER PUZZLE" attributed to the creator [C:docs/ENDGAME-ANALYSIS.md@caaa77a section 5] | written by solver senape; the creator replied "Or the same puzzle, or just not at all" | **transcript** (agent N5/N6). |

### 2.3 Creator-attributed meaning

| Conflict | Side A | Side B | Better supported |
|---|---|---|---|
| FEFEFE/104/101010 | creator-stated [C:docs/CREATOR-INTEL.md@caaa77a C11] [C:docs/LOOSE-ENDS.md@caaa77a#L60] | solver's text; creator replied on spelling only [C:docs/ENDGAME-ANALYSIS.md@caaa77a section 5] [C:content/sowut-data.js@caaa77a 5952/5960] | **solver's text** (raw reply chain). |
| {2,3,5,7} vs A007522 | "creator rejected {2,3,5,7}; A007522 required" [C:content/attempts.js@caaa77a L3809] | "creator never says A007522" [C:content/attempts.js@caaa77a L3649]; {2,3,5,7} is Janusz's | **no creator statement on either**. |
| 9595 friends/family | "key derives from knowable information" [C:docs/CREATOR-INTEL.md@caaa77a C27] | succession / data-access remark | **raw context** (P5). |
| 7830-7834 | "the cosmic blob is the hosted encrypted key" [C:docs/CREATOR-INTEL.md@caaa77a C2/C20] | no container named; solver's wording | **no container identified**. |
| 39237 yinyang | "yinyang is a decode output, THE gate" [C:docs/CREATOR-INTEL.md@caaa77a C7] | "It's the next phase..." in reply to an AES question, not explicitly affirmed | over-reading by C. |
| "#...# wasn't used" | Phase-2 table resolved by `fc0c1b02` [A#103 body] | relayed creator remark [A#106 body]; Naddiseo "hypothesis at best" [A#103 comment 5357859255] | **unresolved**; the relayed remark is second-hand. |
| "Bingo" (2026-03-04) | confirms gnomad's 9/15/24 reading [B:_pr9/other-puzzles/gsmg-salphaseion/NOTES.md@041ee64] | confirms a South Park quote [B:_pr15/unverified/recovered_reply_context_2026-09-26.txt@1e913fd] | **unresolved** (screenshot context only). |
| Vanity => random key only in Cosmic | [C:docs/ENDGAME-ANALYSIS.md@caaa77a section 8c]; [A#82 body] | deterministic seed-and-counter can also be prefix-filtered (prior section 11) | **prior**; the vanity argument is a non sequitur. |
| Prize "unspent" | [C:content/attempts.js@caaa77a L260] | spent at both halvings [A:_pr101/README.md@68d09aa]; [C:content/attempts.js@caaa77a L4154] | **spent** (reproduced pubkey in 2020 spend). |
| "3.2 is the last part" | [C:docs/CREATOR-INTEL.md@caaa77a C26] | "Don't know but most see 3.2 as the last part." [C:content/sowut-data.js@caaa77a 2026] | **the creator did not assert it**. |

## 3. Counter mismatches (collection)

| Record | Counter | Fetched | Note |
|---|---:|---:|---|
| [A#25] | 19 | 18 (also on per-issue refetch) | no quoted text points to the missing comment; last update = last visible comment + 1 s (agent D1). A hidden/flagged-account comment is plausible; unproven. |
| [B#2] | 2 | 1 | see `sources/discussions/naddiseo/COUNTS.json` |

Two comments in A survive only as quotes inside other comments: a "ZION" text quoted in [A#72 comment 3935458653] and AomDEV comments quoted in [A#114 comment 6128068004] (agent D2). They are recorded as missing originals.
