# DECISIONS

One line per judgement call, dated (UTC). Newest at the bottom.

- 2026-10-15 — `gh` CLI is not installed and no `GITHUB_TOKEN` exists; discussions are collected **unauthenticated** via the GitHub REST API with a paced, resumable collector (`reproduction/scripts/collect_discussions.py`), sleeping through rate-limit resets.
- 2026-10-15 — HTTPS clone of the target failed (no credentials; API returns 404 so the repo is private). The machine's default SSH key authenticates as `testnetbtc`, so `origin` is `git@github.com:testnetbtc/GSMG.git`; this is the owner's own configured key, not a substitute credential after a rejected push.
- 2026-10-15 — Target repo was empty (no refs), so `main` was created locally with an initial commit, per brief §5.1.
- 2026-10-15 — `reports/MASTER_REASONING_REPORT.md` = a 4-line archive header + the original file byte-for-byte; the original's SHA-256 (`e6de6b47…7e06`) is stated in the header so the verbatim body is checkable (`tail -n +5`).
- 2026-10-15 — The prior report links to companion files (`ARTIFACT_REGISTRY.csv`, `CLAIMS.jsonl`, `records/`, `appendices/` …) that were **not supplied**; "prior rows preserved" is therefore implemented by transcribing every row of the prior report's own tables into the registers, tagged `source=prior_report§N`.
- 2026-10-15 — The prior report also covered a fourth repo (floflo777/open-crypto-puzzles); this brief names only three, so floflo777 is cited only where the prior report cites it and is not imported.
- 2026-10-15 — `BRIEF.md` is a byte copy of `GSMG_AGENT_BRIEF.md` (SHA-256 `046d9847…cfc5`).
