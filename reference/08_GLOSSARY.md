# 08 -- Glossary and canonical names

Sources disagree on what "Phase 3.2", "3.2.2", "inner blob", "SalPhaseIon" or "Cosmic" mean. This file fixes **one canonical name per object**, keyed by bytes rather than by phase label. All other reference files use only the canonical names in the first column. Citation keys are defined in [00_INDEX.md](00_INDEX.md).

## 1. Encrypted containers (OpenSSL `Salted__` envelopes)

Every envelope below was base64-decoded and hashed by `reproduction/scripts/reproduce.py` (status **reproduced** for bytes, salt and length). "Envelope" = the whole decoded object (`Salted__` || 8-byte salt || ciphertext).

| Canonical name | Envelope bytes | Salt | Ciphertext bytes | SHA-256 of envelope | Where it lives | Aliases found in sources |
|---|---:|---|---:|---|---|---|
| `ENV-phase2` | 672 | `06286612d43ed7ed` | 656 | `a089144531c666e59770c799427c05d1ea4ae074857b97d61b8d3924ff14c7e7` | Phase-2 page ("choiceisanillusion...") | phase2.txt, phase2_aes.txt, "AES #1" |
| `ENV-phase3` | 4,112 | `9fbc451d13d071f4` | 4,096 | `9163a38d8c49038d01005bc468d9c677183b49b14d7a88fdf3bade75d1443f30` | second envelope on the same Phase-2 page (both base64 heads present in the 2020-11-12 capture [B:_pr15/neo/materials/wayback/pages/choiceisanillusion_2020-11-12.html@1e913fd]) | phase3_aes.txt, phase3.txt (C), "7-part blob" |
| `ENV-phase32` | 2,448 | `eefc4c5befc1656a` | 2,432 | `9d172dc017034564b40eb381fa61e31421f509a08430864c77ccf86cfc8fe784` | inside `PT-phase3` | phase3.2-aes.txt, phase32.txt (C), "BLOB_PHASE32" (mislabelled with the p32_trailing salt in [A#68 comment 3704010992]) |
| `salph_inner` | 96 | `3ab585348552415d` | 80 | `9e2831e1b34b5f34796df47ccaf6530d48d371c61a6bff84d60db1064fa7a258` | SalPhaseIon soup, split by the `enter` a/b insertion | `salphaseion.txt` (C, byte-identical alias), `miniAB` = `miniA`||`miniB` [B:_pr15/neo/LEDGER.md@1e913fd], `sa.b64.txt` [A:_pr93/_work/files_listing.txt@2c97f44], "SalPhaselon AES blob" [A:_pr68/GAP_ANALYSIS.md@27ea50e], **"Cosmic Duality 79B"** (mislabel, [A#68 comment 3704010992]), "inner blob" [B#17], "small blob `3ab58534...`" [A#106] |
| `p32_trailing` | 96 | `b45a5e3d827593ca` | 80 | `291dfd6f3e759ec2e272b35a00c24907da70c3e7a9291b4c13605c7b0b4f3de9` | last 128 base64 chars of `PT-phase32` | **`inner96.b64` / `P32T`** [B:_pr15/neo/materials/inner96.b64@1e913fd] (name collides with "inner"), "Short 79B" [A#68 comment 3704010992], `p32b.b64.txt` [A:_pr93/_work/files_listing.txt@2c97f44], source alias `phase3.2.2` in the prior report, "the small one of 96 bytes" [A:_pr102/README.md@7656174] |
| `cosmic` | 1,344 | `2d3f6fe06dc950e6` | 1,328 | `b18950551a4dd0cb8a9378f0906ba18c03a15f0ee83eb98c6bc90165c5f79805` | SalPhaseIon page, second textarea under `<h1> Cosmic Duality </h1>` | Cosmic Duality, "Dualite" [A:_pr102/README.md@7656174] (not present in the archived markup -- see 07), `cd.b64.txt`, `cosmic_blob.txt`, `cosmic_duality_envelope_1344B.bin`, "chain 3 input" |
| `urlblob` | 112 | `74c974e3f92e64b5` | 96 | `25b3619a18174794d4ddd0d743f78f04007c0cf1830f6cf9301bc671631799bb` | hex-encoded in a requested gsmg.io **URL path** (Wayback 2026-01-05/2026-02-07, SPA-shell responses) | "4th orphaned blob", "O10" [C:docs/CREATOR-INTEL.md@caaa77a]; a community URL artifact, **not** a page-embedded container |

`miniA` (first 64 base64 chars of `salph_inner`) is itself a well-formed 48-byte envelope with the same salt; some campaigns targeted it separately [B:_pr15/unverified/endgame_aes_password_search.md@1e913fd].

## 2. Plaintexts and derived objects

| Canonical name | Bytes | SHA-256 | Definition | Status | Aliases |
|---|---:|---|---|---|---|
| `PT-phase2` | 648 | `e2f9dd65604a3231f8b3301724e8d713a88fffc4b6c7c4aeeb20f58a582b593a` | `ENV-phase2` under answer `causality` | reproduced | phase2.1.txt |
| `PT-phase3` | 4,090 | `c4ad94559a44a927c1032cc0e024515f9510a0806a2d14458dbf4a360af9865f` | `ENV-phase3` under the 227-char seven-part answer | reproduced | phase3.txt |
| `PT-phase32` | 2,422 | `b82afeb86f9e50848220f9b64b744b821400308aea273a1c949b9d2d0e408a34` | `ENV-phase32` under the 62-char three-part answer | reproduced | phase3.2.txt |
| `SPEECH` | 1,539 letters | `90829b510c3697569da47d2817f545f1e2a1cddd78e45f821dafcdab3dc0c281` | `PT-phase32[447:1986]` -> CP1141 -> Beaufort `thematrixhasyou` | reproduced | Architect speech / monologue; "Oracle's message" (PR68, a misnomer); A calls the block **phase 3.2.1** |
| `VIC-DIGITS` | 149 digits | -- | the digit run in `PT-phase32` | reproduced | A calls it **phase 3.2.2** (!= `p32_trailing`) |
| `VIC-SENTENCE` | 91 letters | -- | straddling-checkerboard decode of `VIC-DIGITS` | reproduced | "half and better half" sentence |
| `SOUP` | 1,075 letters (no spaces) | `26e37652067c549c0eee624356be9ffd40a243901197335a41f91fb6c78e6156` (no-space form); space-separated page text `d39d10b1e1902d2620eb19ebcad4215e23c048de639466cca9a26bdc9303330c` | first textarea of the SalPhaseIon page | reproduced (byte agreement of 3 copies) | salph page, "the soup" |
| `DBBI` | 91 | `71fe46259e270c113529dfaded4b59c59a9dffd826a7202ab07fc498b6a2c5ca` | `SOUP[0:91]` | reproduced | dbbi, dbbib, PREFIX_91 |
| `FAED` | 570 | `066191b4aafc114fbca7f0d168382f40129c4ff18490375b689741081d5ef3c2` | `SOUP[195:765]` | reproduced | faed |
| `BIFID-OUT` | 570 | `0c5d984f90e9baefc09f1d3888e62acbd101f9b0194887e2ae88fc6c9967745e` | full-period Bifid decrypt of `FAED` with square `DBIFHCEGAKLMNOPQRSTUVWXYZ` | reproduced (mechanics) | BTCSEED string |
| `HINT-2023` | 161 | see 04 | reverse-bit decode of message 8446 | reproduced | master hint, "reverse binary" |
| `OUT-chain1` | 79 | `1449a2178eea7c0e3fabac8c1ad2afa294be4fc1800c594a025a056e88c626bf` | `salph_inner` under EVP-MD5, raw password `matrixsumlistenterlastwordsbeforearchichoicethispasswordmatrixsumlist` | reproduced (mechanics); significance unverified | "chain 1", K_C1||K_C2||E_C, `salphaseion_plain_79.bin` (listed in A PR93 file listing; bytes not held) |
| `OUT-chain2` | 79 | `b40fce72ef5638e4f79b3233e653f8a5dbdb0d4ae2009d2d3da2c98b70f4d004` | `p32_trailing` under EVP-MD5, password = uncompressed WIF of `OUT-chain1[0:32]` | reproduced (mechanics); significance unverified | "chain 2", K_S1||K_S2||E_S. **Not** the 1,151-byte `chain2_decrypted.bin` of B PR#15's Drive folder |
| `OUT-cosmic` | 1,327 | `4f7a1e4efe4bf6c5581e32505c019657cb7b030e90232d33f011aca6a5e9c081` | `cosmic` under EVP-MD5 with the 32 raw bytes XOR(SHA-256 of 7 tokens) | reproduced (mechanics); significance unverified | "chain 3", `cosmic_1327b_decrypted.bin`, `cosmic_decrypted_verified.bin`, K_B1||K_B2||E_B||K_H1||K_H2||E_H + 1,169 "mystery" bytes |
| `OUT-cosmic-A` | 1,327 | `cd3fea3d697a7fbfb2e6e4c1fd79316a1a8635be225a07539d4cc56a3f6d3002` | a different padding-valid `cosmic` decrypt (recipe unknown) | reported (file held) | `cosmic_A.bin` [B:_pr15/unverified/drive-2026-05/@1e913fd] |
| `ENV-chain4` | 1,168 | -- | `OUT-cosmic[158:-1]` XOR repeating `b657264f2f6e6921` -> `Salted__`, salt `5bbd88ac32481bca` | reproduced; header **forced** by the mask (see 03) | masked nested envelope |
| `OUT-chain4` | 1,151 | `e4269ed5fbb202a81e5e1aa6b5190fdd1ea126b2c8547ea7cdbdf45387ea135b` | `ENV-chain4` under EVP-MD5, password `E_C||E_S||E_B[:2]` | reproduced (mechanics) | "Chain4", `chain4_final.bin` |
| `ENV-ca158` | 1,169 | `d895da1ba96e924ca928e54fc8c2299f3d5383539922083b5d18378d758c8298` | `OUT-cosmic-A[158:]` XOR repeating `e264c342fc04995b`; salt `0391bdb016191c9d` | reproduced (crib control) | `ca158_hidden_blob.bin` |
| `chain4.bin (A#84)` | 1,168 | `a80a399af1221bd62538594141bee1064e1b071b547d60729f13c0224041a0f7` | as cited in [A#84]; generator not held | reported | "1168-byte chain4" |

Field names: `K_C1`=`OUT-chain1[0:32]`, `K_C2`=`[32:64]`, `E_C`=`[64:79]`; `K_S1`/`K_S2`/`E_S` likewise for `OUT-chain2`; `K_B1`, `K_B2`, `E_B`, `K_H1`, `K_H2`, `E_H` are the six fields of `OUT-cosmic[0:158]` (32+32+15+32+32+15). These partitions are an analyst's choice, not a format.

## 3. Stages, pages and labels

| Canonical stage name | Means | Other names |
|---|---|---|
| **Phase 0 -- opening image** | `puzzle.png`, 14x14 grid -> `gsmg.io/theseedisplanted` | bunny image, genesis grid, `follow_the_white_rabbit.png`, "Phase 1" (A PR68) |
| **Phase 1 -- form** | `/theseedisplanted` page; POST to `/phase1verification`; answer `theflowerblossomsthroughwhatseemstobeaconcretesurface` | "The Warning", "phase-2 flower password" (A PR93, mislabel) |
| **Phase 2** | `/choiceisanillusion...myself` page; `ENV-phase2`; parts 1-4 (2.1) and 5-7 (2.2) | "Mr Robot", "Phase 3" (A PR68) |
| **Phase 3** | `PT-phase2` riddles -> three answers -> opens `ENV-phase32`... | "Free Will", "Phase 3.1/3.2" in PR68 numbering -- numbering differs across sources; use container names |
| **Phase 3.2** | `PT-phase32`: speech region, `VIC-DIGITS`, riddle, `p32_trailing` | "The Architect"; A sub-labels 3.2.1 (Beaufort) / 3.2.2 (VIC) |
| **Decentraland** | parcel -41,-17 ("GSMG.io Puzzle piece"), `puzzlepiece.mp3` -> `HASHTHETEXT` | -- |
| **SalPhaseIon** | page `https://gsmg.io/89727c598b9cd1cf8873f27cb7057f050645ddb6a7a157a110239ac0152f6a32` holding `SOUP` and `cosmic` | SalPhaselon, salph, "salphation" (creator spelling), "salvation part" (solver), "final page", Phase 3.2.2 (some sources) |
| **Cosmic Duality** | the `cosmic` container and the book-cover hint of 2022-12-10 | Dualite |

Soup section names: `agda` -> `lastwordsbeforearchichoice`; `cfob` -> `thispassword`; a/b blocks -> `matrixsumlist` (104 bits) and `enter` (40 bits); `shabef` (read as "sha256"/"sha before"); `anstoo` ("answer too").

## 4. People and handles (display names are not authenticated accounts)

| Name used here | Other renderings | Role / note |
|---|---|---|
| **@SoWut** (creator-attributed handle) | display name `Jrk Bgrt` in the PR93 transcript (411/411 text messages match); "Jrk Bgrk" in [B:README.md@9e61693] (screenshot transcription); Jrk, JRK, "Jrk (Discord #4105)" | messages under this handle are treated as **creator-attributed**, never authenticated; when asked "are you creator?" the handle replied "Rumour has it I'm an admin at least." [A:_pr93/_work/chat_transcript.txt@2c97f44 L14079] |
| Janusz Baran | @janusz_baran, Telegram id 394589394 | solver; author of the 104/FEFEFE/101010 text and the {2,3,5,7} question (2021-03-01) |
| Detective Froz | @AndyFroz | solver; coined "encrypted private key stored online" (2021-08) |
| k1ng | -- | solver; critiqued the 2025-08-23 Cosmic claim as a padding false positive |
| Mauro Etrade | links `jackdevs66/GSMG5_CDuality` | announced Cosmic "decryption" 2025-08-23 |
| GalloClaudio64 | -- | [A#68 comment 3704010992] chain 1-4 recipes (2026-01-01) |
| dz17ghost-create | -- | opened [B#17] (2026-10-05) |
| Naddiseo | -- | B maintainer; A PR #3/#8/#16 author |
| Hosterjack | HosterjackAGV, @DaneelOlivaw | C maintainer |
| Sycorax | -- | first BTCSEED post in the transcript (2025-06-11) |
| RB | @rb_6969 | solver cited by A PR93 (checkerboard theory) |
| Deleted Account | many accounts | Telegram merge label (>=3 distinct numeric ids seen); never one person |
| consigcody94 / halbgott29a / wayzeek / pgurido / biawalid | -- | authors of A PRs #68 / #93 / #101-#102 / #30 / #11 |

## 5. Addresses and keys (public)

| Object | Value | Note |
|---|---|---|
| Prize address | `1GSMG1JC9wtdSwfwApgj2xcmJPAwx7prBe` | uncompressed P2PKH of the prize point (reproduced) |
| Prize public key | `04f4d1bbd91e65e2a019566a17574e97dae908b784b388891848007e4f55d5a4649c73d25fc5ed8fd7227cab0be4e576c0c6404db5aa546286563e4be12bf33559` | on curve; appears 3x in the 2020 halving spend tx hex (reproduced) |
| Compressed form | `1cc6xayvqpeetixmuXDRsGug7GKyoRdxP` | not the prize address |
| Halving recipient | `17ucy1K9ZUAaoY6JVtM932W9jUp5LXfyHa` | received 2.5 BTC (2020-05-11) and 1.25 BTC (2024-04-24) from the prize key [A:_pr101/README.md@68d09aa] (reported) |
| `3GSMG24TujqfMJG1kQoBX18DzJHQLeJYMK` | -- | sent OP_RETURN "Halving" dust spent alongside the prize key in 2020 (reported, B PR#15) |
| Donation addresses | A `1JK27jtvE1wS4VG9k7Zpo8wBufMbYwy3r8`; B `bc1qla7lmz3guzz3cezhfl72r0w546a4gyacpu530r`; C `bc1qh065fgqmxwt5d65g4r07dvlntryjdnxwkaws87` | repository maintainers' own; **not puzzle addresses** |

## 6. Terms

- **reproduced / reported / interpreted** -- see [00_INDEX.md](00_INDEX.md) section 3.
- **EVP-SHA256 / EVP-MD5** -- OpenSSL `EVP_BytesToKey`, one iteration, with that digest.
- **1-byte-pad** -- a decryption whose last byte is `0x01`; the typical shape of a wrong-key "valid padding" event (~1/256 of random keys).
- **SPA shell** -- the generic ~36 KB page gsmg.io served for any unknown path from 2024 on; a capture of such a URL is not a puzzle page.
- **E054** -- a pointer in the prior brief to an unavailable private experiment register; not held.
