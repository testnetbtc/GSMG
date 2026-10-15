# GSMG — consolidated 5 BTC puzzle archive

A single, auditable repository for the GSMG.IO 5 BTC puzzle (prize address `1GSMG1JC9wtdSwfwApgj2xcmJPAwx7prBe`). It is built from three community repositories:

| Key | Source | Frozen commit |
|---|---|---|
| **A** | [puzzlehunt/gsmgio-5btc-puzzle](https://github.com/puzzlehunt/gsmgio-5btc-puzzle) | `fb92dd1` |
| **B** | [Naddiseo/gsmgio-5btc-puzzle](https://github.com/Naddiseo/gsmgio-5btc-puzzle) (fork of A) | `9e61693` |
| **C** | [HosterjackAGV/gsmg-5btc-puzzle](https://github.com/HosterjackAGV/gsmg-5btc-puzzle) | `caaa77a` |

Built 2026-10-15 per [BRIEF.md](BRIEF.md). Every judgement call is in [DECISIONS.md](DECISIONS.md), and the build log is in [PROGRESS.md](PROGRESS.md).

**What it is:** every file, git commit, branch, PR head, issue, PR, comment, review and reachable attachment from A, B and C, preserved once with provenance, plus a deduplicated, source-linked reference and an independent reproduction of the solved chain.
**What it is not:** a solution. Nothing here is a key. Mechanically reproducible community "openings" of the unsolved containers are documented with their unverified significance.

## Layout

```
README.md  BRIEF.md  DECISIONS.md  PROGRESS.md
MANIFEST.md            completeness proof: imports, discussions, dedup, coverage-check output, known gaps
sources/               raw archive (evidence of record)
  puzzlehunt/ naddiseo/ hosterjack/    git subtrees with history; _pr<N>/ and _branches/<b>/ hold files unique to PR heads and branches
  discussions/<repo>/  raw/ (API JSON + headers), issues/NNN.md, pulls/NNN.md (lossless renders), COUNTS.json
  discussions/attachments/             downloaded attachments + ATTACHMENTS.tsv (status per URL)
  REFS.tsv             every advertised ref, head commit, archive tag
reference/             curated, deduplicated knowledge base — start at reference/00_INDEX.md
  00_INDEX … 08_GLOSSARY.md
  artifacts/           one canonical copy of each puzzle artifact
  data/                SOURCE_INVENTORY, SOURCE_LINEAGE, VARIANT_GROUPS (+ variants/*.diff), ARTIFACT_REGISTRY,
                       ARTIFACT_FILES, CLAIMS, CREATOR_CLUES, EXPERIMENT_COVERAGE, CONTRADICTIONS, INJECTIONS, extraction/
reproduction/          independent code + recorded outputs (see reproduction/README.md)
reports/
  MASTER_REASONING_REPORT.md    prior report (14 Oct 2026), verbatim under a dated header
  REASONING_REPORT_v2.md        this build's auditable reasoning report
```

Every non-default ref of every source is also kept as a git tag `archive/<A|B|C>/<pr-N | branch/name>`, so no commit object is lost.

## How to run

Requirements: Python 3.10+, `pycryptodome`, `numpy`, `Pillow`, `matplotlib`, the `openssl`, `iconv` and `ffmpeg` CLIs.

```bash
# completeness check: zero orphans expected
python3 reproduction/scripts/check_manifest.py

# independent reproduction of the solved chain and the published fixed recipes
python3 reproduction/scripts/reproduce.py      # writes reproduction/results/

# rebuild derived tables (deterministic from sources/)
python3 reproduction/scripts/build_inventory.py    # inventory, lineage, variants
python3 reproduction/scripts/build_artifacts.py    # reference/artifacts + ARTIFACT_FILES.csv
python3 reproduction/scripts/build_registers.py    # CLAIMS, CREATOR_CLUES, EXPERIMENT_COVERAGE, …
python3 reproduction/scripts/build_manifest.py     # MANIFEST.md (embeds check_manifest output)
```

`reproduction/scripts/collect_discussions.py` and `render_discussions.py` re-collect and re-render the GitHub discussions. They need network access and pace themselves under the unauthenticated API rate limit.

## Citation legend

| Form | Meaning |
|---|---|
| `[A:path@fb92dd1]` | file in source A at that commit (`_prN/…` = only in PR head N; commit = that head) |
| `[B#17]`, `[B#17 body]` | issue or PR #17 of source B |
| `[A#68 comment 3704010992]` | GitHub comment id in A |
| `[T L13992]` | line of the Telegram transcript `[A:_pr93/_work/chat_transcript.txt@2c97f44]` |
| `[C:content/sowut-data.js@caaa77a id 8000]` | record in C's creator-message dataset |
| status **reproduced / reported / interpreted** | re-run here / a source says so / someone's reading |

Creator attribution in this archive is by Telegram handle and display name (`@SoWut` / `Jrk Bgrt`). It is **never** treated as an authenticated identity.

## Licences and notices

Upstream material keeps its owners' rights. A and B carry no licence (all rights reserved by their authors). C's own contributions are CC0 per [sources/hosterjack/LICENSE](sources/hosterjack/LICENSE) and [NOTICE.md](sources/hosterjack/NOTICE.md), both preserved verbatim. Puzzle artifacts belong to the puzzle's creator. This archive relabels nothing as original work: its own contributions are the `reference/`, `reproduction/` and `reports/REASONING_REPORT_v2.md` layers and the build metadata.
