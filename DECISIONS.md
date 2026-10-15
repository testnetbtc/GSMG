# DECISIONS

One line per judgement call, dated (UTC). Newest at the bottom.

- 2026-10-15 — `gh` CLI is not installed and no `GITHUB_TOKEN` exists; discussions are collected **unauthenticated** via the GitHub REST API with a paced, resumable collector (`reproduction/scripts/collect_discussions.py`), sleeping through rate-limit resets.
- 2026-10-15 — HTTPS clone of the target failed (no credentials; API returns 404 so the repo is private). The machine's default SSH key authenticates as `testnetbtc`, so `origin` is `git@github.com:testnetbtc/GSMG.git`; this is the owner's own configured key, not a substitute credential after a rejected push.
- 2026-10-15 — Target repo was empty (no refs), so `main` was created locally with an initial commit, per brief §5.1.
- 2026-10-15 — `reports/MASTER_REASONING_REPORT.md` = a 4-line archive header + the original file byte-for-byte; the original's SHA-256 (`e6de6b47…7e06`) is stated in the header so the verbatim body is checkable (`tail -n +5`).
- 2026-10-15 — The prior report links to companion files (`ARTIFACT_REGISTRY.csv`, `CLAIMS.jsonl`, `records/`, `appendices/` …) that were **not supplied**; "prior rows preserved" is therefore implemented by transcribing every row of the prior report's own tables into the registers, tagged `source=prior_report§N`.
- 2026-10-15 — The prior report also covered a fourth repo (floflo777/open-crypto-puzzles); this brief names only three, so floflo777 is cited only where the prior report cites it and is not imported.
- 2026-10-15 — `BRIEF.md` is a byte copy of `GSMG_AGENT_BRIEF.md` (SHA-256 `046d9847…cfc5`).
- 2026-10-15 — No source has tags. Every non-default branch and every `refs/pull/*/head` (A: 9 PRs, B: 7 PRs, C: 1 PR + 2 branches) is preserved as a local tag `archive/<A|B|C>/<pr-N|branch/name>` pushed with the repo, so every commit object from every advertised ref is retained.
- 2026-10-15 — For every non-default ref (not only PR #68), files whose blob is absent from all three default-HEAD trees are written to `sources/<repo>/_pr<N>/` or `sources/<repo>/_branches/<branch>/` (paths kept). Reason: the brief's "nothing lost" rule applies to all refs; git stores identical blobs once so cost is ~37 MB of genuinely new bytes (mostly Naddiseo PR #15).
- 2026-10-15 — `sources/REFS.tsv` records each ref, head commit, reachable commit count, tree size and imported-file count. Subtree-merge commit messages read `ingest: sources/<name> from <url> <branch>`; the frozen HEAD commits are in REFS.tsv and MANIFEST.md rather than the message.
- 2026-10-15 — All three default HEADs equal the prior report's frozen commits (A `fb92dd15`, B `9e616934`, C `caaa77a8`): upstream has not moved on default branches. A has gained PR refs #101 and #102 that are absent from the prior report's 9-PR table count check (to be confirmed in discussion collection).
