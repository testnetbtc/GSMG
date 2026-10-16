# PROGRESS

| # | Step | Status | Completed (UTC) | Commit message prefix |
|---|---|---|---|---|
| 1 | Setup + three subtree imports | done | 2026-10-15 13:59 | `init:` / `ingest: sources/*` |
| 2 | Branches/tags/PR68 extras | done (all 17 PR heads + 2 branches; no tags exist) | 2026-10-15 14:01 | `ingest: non-default branches and PR heads` |
| 3 | Discussion collection | done (API paced through one rate-limit reset) | 2026-10-15 15:03 | `ingest: discussions` |
| 4 | Inventory + lineage tables | done | 2026-10-15 15:06 | `reference: SOURCE_INVENTORY...` |
| 5 | Reference files | done (00-08, artifacts, registers) | 2026-10-15 | `reference:` |
| 6 | Reproduction scripts + results | done (18 confirmed, 0 discrepancies; extra controls) | 2026-10-15 | `reproduction:` |
| 7 | Manifest + coverage check | done (zero orphans) | 2026-10-15 | `manifest:` |
| 8 | Reasoning report v2 | done | 2026-10-15 | `report:` |
| 9 | README, final manifest run, push | done (pushed main + 22 archive tags) | 2026-10-15 | `finish:` |
| 10 | Research session on the unsolved parts (offline oracle; BTCSEED, brain-wallet, matrixsumlist, image, stream-combine and vanity-offset tests; yinyang operations) | done (all negative; journal + scripts pushed) | 2026-10-15 | `research:` |
| 11 | `walkthrough/` layer: 12 pages, `verify.py` (102 checks), `check_ascii.py`, generated verification page | done | 2026-10-16 | `walkthrough:` |
| 12 | ASCII typography normalisation; binary results made readable (`.gitattributes`, `.hex`, results README); `CLAUDE.md` restored; results JSON, MANIFEST and registers regenerated | done (all checks PASS) | 2026-10-16 | `docs:` |

Note: work proceeded partly in parallel while the GitHub API rate limit blocked step 3 (steps 5-6 were drafted from repository files first and re-checked after the discussions arrived).
