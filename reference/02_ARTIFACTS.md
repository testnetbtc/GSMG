# 02 -- Artifacts

One canonical byte-copy of every puzzle artifact is in `reference/artifacts/`. `reference/data/ARTIFACT_FILES.csv` maps each copy to its canonical source path, upstream citation, SHA-256 and every byte-identical duplicate in `sources/`. `reference/data/ARTIFACT_REGISTRY.csv` is the object registry: the prior report's rows (ids `PR-...`) are preserved, and new objects have ids `NEW-...`. Object names follow [08_GLOSSARY.md](08_GLOSSARY.md).

## 1. What counts as a puzzle artifact here

| Class | Folder | Provenance basis |
|---|---|---|
| Opening image, page images, chess position | `artifacts/images/` | puzzle pages; byte-identical across A, B and C where present |
| Encrypted envelopes (7) | `artifacts/envelopes/` | page text or decrypted stage text; see section 2 |
| Decrypted stage texts (3) | `artifacts/plaintexts/` | B's files; byte-identical to this archive's reproduction |
| SalPhaseIon soup + archived pages | `artifacts/pages/` | as supplied in B PR #15 (a user-uploaded Wayback dump); not refetched by this build |
| Decentraland audio + screenshots | `artifacts/audio/`, `artifacts/images/` | B's assets, content id `QmeRy5MjmEZ2W6J3DwhQfht5HKBKXBFpoGzSkzmjeGKiDK` |
| Hint screenshots (34) | `artifacts/hints/` | B's `hints/` folder (C vendors the same bytes); dated by filename only |
| Creator-posted media (4) | `artifacts/creator_media/` | C's `assets/sowut/` (message ids in filename) |

Derived research objects (chain outputs, Bifid output, speech) are **not** puzzle artifacts. They are kept in `reproduction/results/` with their recipes.

## 2. Containers and where each one really comes from

| Container | Placement evidence | Assessment |
|---|---|---|
| `ENV-phase2`, `ENV-phase3` | Both base64 heads are present on the archived Phase-2 page, 2020-11-12 capture [B:_pr15/neo/materials/wayback/pages/choiceisanillusion_2020-11-12.html@1e913fd]; A prints both [A:README.md@fb92dd1] | puzzle containers (reproduced placement in held capture; stage solved) |
| `ENV-phase32` | inside `PT-phase3` (reproduced) | puzzle container (solved) |
| `p32_trailing` | final 128 base64 characters of `PT-phase32` (reproduced; equals [C:ciphertexts/p32_trailing.txt@caaa77a] and [B:_pr15/neo/materials/inner96.b64@1e913fd]) | **embedded in a creator-encrypted plaintext** -- strongest provenance of the open containers |
| `salph_inner` | `SOUP` minus the `enter` a/b insertion (reproduced; equals [C:ciphertexts/salph_inner.txt@caaa77a]) | on the SalPhaseIon page (reproduced against the held captures) |
| `cosmic` | second textarea of the SalPhaseIon page under `<h1> Cosmic Duality </h1>`; byte-equal to [C:ciphertexts/cosmic.txt@caaa77a] in both held captures (reproduced) | on the SalPhaseIon page |
| `urlblob` | its first 53 bytes equal the hex path of two Wayback captures (2026-01-05, 2026-02-07) that returned the generic 36,627-byte SPA shell [B:_pr15/neo/materials/wayback/INDEX.tsv@1e913fd]; bytes 53-111 have no stated source [C:docs/ENDGAME-ANALYSIS.md@caaa77a section 8c] | **community URL artifact**; it must not share the provenance status of page-embedded containers (reported + interpreted) |

**SalPhaseIon page captures.** The page is `https://gsmg.io/89727c598b9cd1cf8873f27cb7057f050645ddb6a7a157a110239ac0152f6a32`. B PR #15's index lists captures 2023-11-27 (4,556 B, held only as a hash), 2024-11-23 (4,588 B, held), 2025-10-31 (5,092 B, held; adds a Cloudflare beacon) and 2026-04-05 (hash only) [B:_pr15/neo/materials/wayback/INDEX.tsv@1e913fd]. C cites a 2023-06-01 capture (4,592 B) containing both texts [C:content/attempts.js@caaa77a L3142] [C:docs/ENDGAME-ANALYSIS.md@caaa77a section 8c]; that capture is not held. Markup of the held captures (reproduced): `<title>GSMG Puzzle</title>`, `<H1> SalPhaseIon </H1>` + textarea, `<h1> Cosmic Duality </h1>` + textarea. There are no comments, hidden inputs or other text. **No verification value or checkpoint is published on the page.** The word "Dualite" [A:_pr102/README.md@7656174] does not occur in either held capture.

Earlier, indirect evidence that the soup existed: the 2021-04-16 Telegram "leak" (transcribed with errors) [C:docs/WALKTHROUGH.md@caaa77a#L2449-L2497], the 2021-05-06 entry recipe, A's README soup section (most plausibly added by Naddiseo's PR #8, merged 2021-05-25 -- interpreted from A#3's head, which still says the entry text was "not currently public knowledge") [A:README.md@fb92dd1#L371-L373], and B's undated `SalPhaselonCosmicDuality.png` screenshot.

**Phase-2 page change.** A 2026-04-05 capture adds `<!-- You made it to the next step! Good luck little bunny hunter ;) -->` after `<body>`. The comment is absent at 2020-11-12 and 2022-12-23 (reported; presence/absence checked in the two held captures by agent N4) [B:_pr15/neo/materials/wayback/pages/choiceisanillusion_2026-04-05.html@1e913fd#L19]. Who added it, and when, is unknown.

**gsmg.io after mid-2026.** Parked/for-sale from 2026-07-07; a "finale" root page appears 2026-08-19 ("2017 -- 2026", "Nine years of chaos ended. One mystery remains.") [B:_pr15/neo/materials/wayback/README.md@1e913fd]. Authorship after the parking is unverified. C names a community mirror `gsmg-archive.org` [C:docs/WALKTHROUGH.md@caaa77a#L3]. A 2020 source map gives the page title `GSMG MEGANIGMA || 5 BTC`, with no secrets in the client code (reported) [C:docs/WALKTHROUGH.md@caaa77a#L41-L46].

## 3. Hint screenshots (artifacts/hints/)

Dates come from B's filenames and README timeline [B:README.md@9e61693]. B's labels are B's own judgement ("Official", "Semi-Official", "not official"); they are not provenance. Where the C dataset holds the typed text, the clue is stated in [04_CREATOR_CLUES.md](04_CREATOR_CLUES.md) with its message id. Corrections: `2021-12-25-hint.png` shows a message posted **2021-12-26** (20:18 UTC). `2026-07-12-official-hint.png` is 2026-07-13 00:51 UTC (19:51 local UTC-5). `2021-05-06-salph instructions.png` shows a **Deleted Account**, not the creator-attributed handle.

| File | B label | Note |
|---|---|---|
| 2020-01-14-roses-are-red.png | Official | text = C id 1710 |
| 2020-02-20-decentraland.jpg, decentraland-tg.png | Official | parcel -41,-17 |
| 2020-04-08.png | "not official ... could be Jrk trolling" | creator adds "(not a hint btw, just fooling around)" [C:docs/WALKTHROUGH.md@caaa77a#L2298] |
| 2020-05-11.png | Bitcoin halving | |
| 2020-06-07-salph-discord.png | first SalPhaseIon mention | Discord user VrsN, not creator |
| 2020-08-02.png, 2021-01-21.png, 2021-02-12-salph-mention.png, 2021-03-14.png | -- | |
| 2021-03-01-primes.png, 2021-03-01-spelling-hint.png | "Spelling and primes" | see 04 for raw context |
| 2021-04-01-april fool.png | "might not be a real hint" | |
| 2021-04-16-salph.png | soup "leak" | user "Hii" |
| 2021-05-06-salph instructions.png | "finally revealed" | poster: Deleted Account |
| 2021-12-02-another-door-hint.png, 2021-12-25-hint.png | Official | dates 12-03 / 12-26 UTC |
| 2022-12-10-cosmic.png, cosmic-duality-book.png | book cover | Time-Life *Mysteries of the Unknown: Cosmic Duality* |
| 2023-01-09-prime-number.png, 2023-01-12-theory of everything.png | Semi-official | |
| 2023-02-23.png | Official | binary; OCR equals dataset 8446 (prior report) |
| 2023-08-03-1/2.png, 2023-08-06-1...4.png | Official | |
| 2024-04-10.png, 2024-04-19-1/2.png | halving | |
| 2026-01-01-new-year-hint.png | New Year | binary, plain ASCII |
| 2026-07-12-official-hint.png, 2026-07-12-other-msg.png | Official | handle shown as "@Jrk Bgrk" |

## 4. Other repository-held materials that are *not* puzzle artifacts

- `architect_span.txt` (501 uppercase letters, no origin note) [B:_pr15/neo/materials/primary/architect_span.txt@1e913fd]: unattributed; kept in `sources/` only.
- B PR #15 Drive files (`cosmic_A.bin`, `ca158_hidden_blob.bin`, `chain2_decrypted.bin`, `chain4_final.bin`, `cosmic_1327b_decrypted.bin`): derived by unknown solvers, described as "not primary" [B:_pr15/unverified/drive-2026-05/README.md@1e913fd]. Registered as `NEW-06`, `NEW-07`, `NEW-09` and under `PR-4.5-*`.
- The PR93 file listing names Telegram attachments (`salphaseion_plain_79.bin`, `cosmic_decrypted_verified.bin`, `Jrk Bgrt Chat History.txt`, `Cosmic Duality (Mysteries of the Unknown).pdf`, ...) whose bytes are **not** in any repo [A:_pr93/_work/files_listing.txt@2c97f44].
- On-chain transactions (raw hex in B PR #15) are evidence about the prize key, not puzzle steps; see [03_UNRESOLVED.md](03_UNRESOLVED.md) section 6.
