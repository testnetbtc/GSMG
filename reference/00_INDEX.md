# 00 -- Index and citation legend

This is the curated, deduplicated reference layer of the GSMG archive. The raw evidence of record is `sources/`; this layer states each fact once, cites every source that carries it, and tags every mechanical claim with a status. `MANIFEST.md` (repo root) proves that every file in `sources/` is either canonical here or a recorded duplicate/variant of one that is.

## 1. Files

| File | Contents |
|---|---|
| [01_SOLVED_CHAIN.md](01_SOLVED_CHAIN.md) | every solved stage: inputs, rules, exact answers, outputs |
| [02_ARTIFACTS.md](02_ARTIFACTS.md) | the puzzle artifacts, where each container really comes from, hint images |
| [03_UNRESOLVED.md](03_UNRESOLVED.md) | open containers, DBBI, FAED, Bifid, labels, seed/interval, on-chain facts |
| [04_CREATOR_CLUES.md](04_CREATOR_CLUES.md) | creator-attributed statements with raw context, the 2023 hint, label values |
| [05_COMMUNITY_MECHANISMS.md](05_COMMUNITY_MECHANISMS.md) | community proposals, lineage, first unsupported transitions |
| [06_EXPERIMENT_COVERAGE.md](06_EXPERIMENT_COVERAGE.md) | what published negatives cover and do not cover |
| [07_CONTRADICTIONS.md](07_CONTRADICTIONS.md) | disagreements with the prior report; source-vs-source conflicts |
| [08_GLOSSARY.md](08_GLOSSARY.md) | **canonical object names** (by envelope hash and salt), aliases, people, addresses |
| `artifacts/` | one canonical byte-copy of each puzzle artifact (map: `data/ARTIFACT_FILES.csv`) |
| `data/` | registers -- see section 4 |

## 2. Citation keys

| Key | Repository | Frozen default commit | Local path |
|---|---|---|---|
| **A** | https://github.com/puzzlehunt/gsmgio-5btc-puzzle (`master`) | `fb92dd15487c6e2d275adb8c923698b7166c328e` | `sources/puzzlehunt/` |
| **B** | https://github.com/Naddiseo/gsmgio-5btc-puzzle (`master`; GitHub fork of A) | `9e61693404ef74e8e681598116d371924f399ffa` | `sources/naddiseo/` |
| **C** | https://github.com/HosterjackAGV/gsmg-5btc-puzzle (`main`; vendors B per its NOTICE) | `caaa77a8c218e97f9fdaae8908d580e51118edec` | `sources/hosterjack/` |

Forms:

- `[A:README.md@fb92dd1]` -- file on a default branch, at the frozen commit; `#L12-L20` or ` section 3` narrows it.
- `[A:_pr93/FINDINGS.md@2c97f44]` -- file that exists only in a PR head (or `_branches/<name>/`), at that head commit. Heads are listed in `sources/REFS.tsv`; local copies live in `sources/<repo>/_pr<N>/` and `sources/<repo>/_branches/`.
- `[A#68]`, `[A#68 body]` -- issue or pull request #68 (issues and PRs share one number space). Rendered losslessly at `sources/discussions/<repo>/issues/068.md` or `pulls/068.md`.
- `[A#68 comment 3704010992]` -- a GitHub comment id (URL `...#issuecomment-3704010992`).
- `[T L13992]` -- shorthand for `[A:_pr93/_work/chat_transcript.txt@2c97f44 L13992]`, the Telegram transcript shipped in puzzlehunt PR #93 (line of the message header).
- `[C:content/sowut-data.js@caaa77a id 8000]` -- record id in C's creator-message dataset (Telegram message id per C).
- `prior_report section N` -- `reports/MASTER_REASONING_REPORT.md` section N (14 Oct 2026).
- `reproduction` / step names -- `reproduction/results/reproduction_results.json`.

## 3. Status vocabulary (never blurred)

| Status | Meaning |
|---|---|
| **reproduced** | re-run from fresh code in `reproduction/scripts/` on bytes from `sources/`; outputs and hashes recorded. Used only for mechanics. |
| **reported** | a source says so; not verified here. |
| **interpreted** | a reading someone places on evidence (including this archive's own readings, which are labelled as such). |
| **source-reproduced** | the source shows code and output, but this archive did not re-run it (used in extraction rows). |

Two separate verdicts are kept for every proposed stage: **mechanics** (do the bytes reproduce?) and **significance** (is it an intended puzzle step?). Creator attribution is handle/display-name based (`@SoWut` / `Jrk Bgrt`) and is never treated as authenticated.

## 4. Data registers (`reference/data/`)

| File | Rows | Purpose |
|---|---|---|
| `SOURCE_INVENTORY.csv` | every file under `sources/` | path, repo, origin ref, commit, upstream path, bytes, SHA-256, first-seen date |
| `SOURCE_LINEAGE.csv` | every file under `sources/` | byte-identical `group_id`, `role` (canonical / duplicate / variant), canonical path, variant group |
| `VARIANT_GROUPS.csv` + `variants/*.diff` | near-identical text groups | normalisation rule, similarity, unified diff, unique-fact review result |
| `ARTIFACT_REGISTRY.csv` | puzzle and derived objects | prior-report rows (`PR-...`) preserved + new rows (`NEW-...`); `source`, `status` |
| `ARTIFACT_FILES.csv` | `artifacts/` copies | canonical source, duplicates, hashes |
| `CLAIMS.jsonl` | claims | prior-report rows, every reproduction record, extracted claims; `source`, `status` |
| `CREATOR_CLUES.jsonl` | creator-attributed statements | prior section 5 rows + extracted register |
| `EXPERIMENT_COVERAGE.csv` | attempts and negatives | prior section 7 rows + extracted rows |
| `CONTRADICTIONS.jsonl`, `INJECTIONS.jsonl`, `GLOSSARY_RAW.jsonl` | extracted rows | inputs to 07, the injection log, 08 |
| `extraction/` | raw agent notes | read-only sub-agent extraction, one file per scope (see its README) |

## 5. Reading order

For the puzzle: 01 -> 03 -> 04 -> 05. For auditing a claim: find the object in 08, its registry row, then its source citation. Every claim here can be traced to a `sources/` path or a discussion URL.
