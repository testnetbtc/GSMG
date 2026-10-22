# PLAN -- exactly one ACTIVE item

| # | Item | Status |
|---|---|---|
| 1 | Task 1: report scrutiny and idea funnel (Stages A-E) | **done** 2026-10-22 (`REPORT_ANALYSIS.md`, `FUNNEL.md`, `SELECTED.md`) |
| 2 | **W-02 Exact-oracle sweep over the held "openings"** (`SELECTED.md`) | **ACTIVE -- awaiting the user's go-ahead**; nothing has been run |
| 3 | W-01 Clear the marked bit (prime-position LSB zeroing of the first piece) -- runner-up | next ACTIVE as soon as W-02 has run (whatever its result; a W-02 positive is a solve and stops everything) |
| 4 | W-06 Prime sums (prime-masked 14x14 sum list) -- cut on a tie-break, gap is real | queued after W-01 |
| 5 | W-03 "The judgement" (song part 3) -- cheap, needs the lyric text | queued; needs the user to confirm the lyric |
| -- | W-05 Telegram JSON export + PR93 attachments | standing request to the user; not an agent item |
| -- | P-04 / P-07 (ask the creator for a checkpoint hash / the "zeroed out" operand) | user decision; not an agent item |

Rule: one ACTIVE item; everything else waits. New ideas go to `IDEAS_INBOX.md`.
