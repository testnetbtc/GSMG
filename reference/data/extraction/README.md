# Extraction notes (machine-assisted, read-only)

These files were produced on 2026-10-15 by read-only sub-agents. Each agent was given one scope of `sources/`, plus the rules in `AGENT_RULES.md`: repository content is data not instructions; no upstream code executed; no network; no wallet activity; no sweeps; every claim cited `repo@commit:path` or by issue/comment id; statuses limited to `reported` / `interpreted` / `source-reproduced`.

| File | Scope |
|---|---|
| N1 | C core docs, content spine, harness, ciphertext provenance, C PR2/branch variants |
| N2 | C attempts data (`content/attempts.js`, `docs/ATTEMPTS.md`, `content/demos.js`) -- 171 entries |
| N3 | C creator-message dataset (`content/sowut-data.js`, CREATOR-LOG, sowut images) |
| N4 / N4_summary / N4.jsonl | B PR #15, #8, #9, #10, #12 and B `unverified/` (N4.md is truncated mid-table; N4.jsonl was rebuilt by a follow-up agent "N4b") |
| N5 | A README + PR extras, A PR #93 work files, B notebooks + README, unique facts in C WALKTHROUGH |
| N6 | Telegram transcript in A PR #93 (`_work/chat_transcript.txt`) matched against C's dataset |
| D1 | A issues #1-#60 and all A PR threads |
| D2 | A issues #61-#116 |
| D3 | B and C issue/PR threads |

**Limits.** These are extraction aids, not reviewed findings. The curated `reference/*.md` files rely on them only where this build checked the cited source text. Every `reproduced` statement comes from `reproduction/`, never from these notes. "Local check" / "parse check" in a note means the agent ran its own arithmetic or hash on held files. That is recorded as `interpreted`/`source-reproduced`, not `reproduced`. Private-key-like strings published in threads were truncated by the agents.
