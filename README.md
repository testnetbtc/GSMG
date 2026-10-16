# GSMG -- consolidated 5 BTC puzzle archive

A single, auditable repository for the GSMG.IO 5 BTC puzzle (prize address `1GSMG1JC9wtdSwfwApgj2xcmJPAwx7prBe`). It is built from three community repositories:

| Key | Source | Frozen commit |
|---|---|---|
| **A** | [puzzlehunt/gsmgio-5btc-puzzle](https://github.com/puzzlehunt/gsmgio-5btc-puzzle) | `fb92dd1` |
| **B** | [Naddiseo/gsmgio-5btc-puzzle](https://github.com/Naddiseo/gsmgio-5btc-puzzle) (fork of A) | `9e61693` |
| **C** | [HosterjackAGV/gsmg-5btc-puzzle](https://github.com/HosterjackAGV/gsmg-5btc-puzzle) | `caaa77a` |

Built 2026-10-15 per [BRIEF.md](BRIEF.md); re-verified 2026-10-16. Every judgement call is in [DECISIONS.md](DECISIONS.md), and the build log is in [PROGRESS.md](PROGRESS.md).

## Start here

**[walkthrough/README.md](walkthrough/README.md)** -- the readable account of the whole puzzle, phase by phase: for each phase the data you are given, the clues that apply, the workings out, the solution, how it is verified, and the extra findings -- from the opening image through the solved chain to the community frontier (the open containers, DBBI, FAED and the Bifid decode that begins `BTCSEED`), with a dated index of every creator clue. Every value on those pages is re-derived by an independent second implementation (`walkthrough/verify.py`) and every hash printed there is audited against the held bytes.

**What this archive is:** every file, git commit, branch, PR head, issue, PR, comment, review and reachable attachment from A, B and C, preserved once with provenance; a deduplicated, source-linked reference; an independent reproduction of the solved chain; the walkthrough; and this archive's own experiments on the unsolved parts.
**What it is not:** a solution. Nothing here is a key. Mechanically reproducible community "openings" of the unsolved containers are documented with their unverified significance.

## Layout

```
README.md  BRIEF.md  DECISIONS.md  PROGRESS.md
MANIFEST.md            completeness proof: imports, discussions, dedup, coverage-check output, known gaps
walkthrough/           START HERE -- phase-by-phase account (data, clues, workings, solution, verification, extras)
  README.md 01 ... 12  index, Phase 0 .. SalPhaseIon, the frontier (containers; DBBI/FAED/BTCSEED), clues index, verification
  verify.py            independent re-derivation of every value + audit of every hash quoted in the pages
  check_ascii.py       the "no strange fonts" guard (walkthrough is pure ASCII; other docs free of odd typography)
sources/               raw archive (evidence of record; never edited)
  puzzlehunt/ naddiseo/ hosterjack/    git subtrees with history; _pr<N>/ and _branches/<b>/ hold files unique to PR heads and branches
  discussions/<repo>/  raw/ (API JSON + headers), issues/NNN.md, pulls/NNN.md (lossless renders), COUNTS.json
  discussions/attachments/             downloaded attachments + ATTACHMENTS.tsv (status per URL)
  REFS.tsv             every advertised ref, head commit, archive tag
reference/             curated, deduplicated knowledge base -- start at reference/00_INDEX.md
  00_INDEX ... 08_GLOSSARY.md
  artifacts/           one canonical copy of each puzzle artifact
  data/                SOURCE_INVENTORY, SOURCE_LINEAGE, VARIANT_GROUPS (+ variants/*.diff), ARTIFACT_REGISTRY,
                       ARTIFACT_FILES, CLAIMS, CREATOR_CLUES, EXPERIMENT_COVERAGE, CONTRADICTIONS, INJECTIONS, extraction/
reproduction/          independent code + recorded outputs (see reproduction/README.md)
  results/             outputs; README.md explains each file; every .bin has a readable .hex twin
research/              this archive's own experiments on the unsolved parts (dated folders; see 2026-10-15_SESSION_JOURNAL.md)
reports/
  MASTER_REASONING_REPORT.md    prior report (14 Oct 2026), kept byte-for-byte under a dated header
  REASONING_REPORT_v2.md        this build's auditable reasoning report
```

Every non-default ref of every source is also kept as a git tag `archive/<A|B|C>/<pr-N | branch/name>` on the remote (22 tags), so no commit object is lost. (`git fetch --tags` if your clone did not fetch them.)

## Reading on GitHub: typography and binary files

- All documents written by this archive are plain 7-bit ASCII typography (no arrows, ellipsis, box-drawing or math symbols that GitHub renders in a fallback font). `walkthrough/check_ascii.py` enforces it; `reproduction/scripts/ascii_sanitize.py` applies it. Upstream content under `sources/` is untouched, as is the verbatim prior report.
- Files ending in `.bin` under `reproduction/results/` are binary outputs. GitHub cannot show them as text (it used to display them as garbled characters). `.gitattributes` marks them binary and each one has a `.hex` twin you can read; `reproduction/results/README.md` says what each file is and whether readable text is expected in it (for the community "chain" outputs it is not -- see `walkthrough/09_frontier_containers.md`).

## How to run

Requirements: Python 3.10+, `pycryptodome`, `numpy`, `Pillow`, `matplotlib`, the `openssl`, `iconv` and `ffmpeg` CLIs; `chess` (python-chess) is optional for one extra check.

```bash
# the walkthrough's own checks
python3 walkthrough/verify.py                     # independent re-derivation + hash audit of the pages
python3 walkthrough/check_ascii.py                # typography guard
python3 walkthrough/build_verification_page.py    # regenerates walkthrough/12_verification.md from live results

# completeness check: zero orphans expected
python3 reproduction/scripts/check_manifest.py

# independent reproduction of the solved chain and the published fixed recipes
python3 reproduction/scripts/reproduce.py         # writes reproduction/results/
python3 reproduction/scripts/render_results_hex.py  # .hex twins of the .bin outputs

# rebuild derived tables (deterministic from sources/)
python3 reproduction/scripts/build_inventory.py    # inventory, lineage, variants
python3 reproduction/scripts/build_artifacts.py    # reference/artifacts + ARTIFACT_FILES.csv
python3 reproduction/scripts/build_registers.py    # CLAIMS, CREATOR_CLUES, EXPERIMENT_COVERAGE, ...
python3 reproduction/scripts/build_manifest.py     # MANIFEST.md (embeds check_manifest output)
```

`reproduction/scripts/collect_discussions.py` and `render_discussions.py` re-collect and re-render the GitHub discussions. They need network access and pace themselves under the unauthenticated API rate limit.

## Citation legend

| Form | Meaning |
|---|---|
| `[A:path@fb92dd1]` | file in source A at that commit (`_prN/...` = only in PR head N; commit = that head) |
| `[B#17]`, `[B#17 body]` | issue or PR #17 of source B |
| `[A#68 comment 3704010992]` | GitHub comment id in A |
| `[T L13992]` | line of the Telegram transcript `[A:_pr93/_work/chat_transcript.txt@2c97f44]` |
| `[C:content/sowut-data.js@caaa77a id 8000]` | record in C's creator-message dataset |
| status **reproduced / reported / interpreted** | re-run here / a source says so / someone's reading |

Creator attribution in this archive is by Telegram handle and display name (`@SoWut` / `Jrk Bgrt`). It is **never** treated as an authenticated identity.

## Licences and notices

Upstream material keeps its owners' rights. A and B carry no licence (all rights reserved by their authors). C's own contributions are CC0 per [sources/hosterjack/LICENSE](sources/hosterjack/LICENSE) and [NOTICE.md](sources/hosterjack/NOTICE.md), both preserved verbatim. Puzzle artifacts belong to the puzzle's creator. This archive relabels nothing as original work: its own contributions are the `walkthrough/`, `reference/`, `reproduction/`, `research/` and `reports/REASONING_REPORT_v2.md` layers and the build metadata.
