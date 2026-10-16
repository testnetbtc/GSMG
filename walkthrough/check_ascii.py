#!/usr/bin/env python3
"""
walkthrough/check_ascii.py -- "no strange fonts" guard.

GitHub renders characters outside the main web font (arrows, ellipsis, box
drawing, math symbols, superscripts, section signs, ...) in a fallback font,
which looks odd -- especially inside code spans. This script fails when such
characters appear in the archive's own documents.

Two levels:
  strict  -- walkthrough/*.md must be pure 7-bit ASCII.
  docs    -- every other archive-authored .md (root, reference/, reports/,
             research/, reproduction/) must not contain the typographic /
             mathematical / box-drawing set below. Accented letters and emoji
             inside verbatim quotations are allowed (they render normally).
sources/ is never checked: it is upstream content preserved verbatim. One
archive document is also exempt: reports/MASTER_REASONING_REPORT.md, the
prior report kept byte-for-byte (its header states the body's SHA-256 so
the verbatim copy stays checkable); its content is superseded by
reports/REASONING_REPORT_v2.md and walkthrough/.

Run:  python3 walkthrough/check_ascii.py        (exit 0 = clean)
"""
import os, sys, unicodedata

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# characters that render in a fallback font on GitHub (or are easily confused)
BANNED = set(
    "…"            # horizontal ellipsis
    "—–‒‑‐−"   # em/en/figure/nb hyphen/hyphen/minus
    "→←↔⇒⇐⇔↑↓⟶"   # arrows
    "§·×÷±≈≠≡≤≥∞∈∉⊕⊗√∑∏"
    "‖∥′″°"
    "²³¹⁰⁴⁵⁶⁷⁸⁹⁻⁺₀₁₂₃₄₅₆₇₈₉"
    "“”‘’„‚«»"
    "─│┌┐└┘├┤┬┴┼═║╔╗╚╝╬"
    "▶◀▲▼●○■□⬤"
    "✓✔✗✘✅❌⚠"
    "χπαβλμσ"
    "    ⁠"   # odd spaces
)

def scan(path, strict):
    bad = {}
    with open(path, encoding="utf-8") as fh:
        for ln, line in enumerate(fh, 1):
            for ch in line:
                if (strict and ord(ch) > 127) or (not strict and ch in BANNED):
                    bad.setdefault(ch, []).append(ln)
    return bad

def main():
    failures = 0
    targets = []
    wt = os.path.join(ROOT, "walkthrough")
    for f in sorted(os.listdir(wt)):
        if f.endswith(".md"):
            targets.append((os.path.join(wt, f), True))
    for top in ["README.md", "BRIEF.md", "DECISIONS.md", "MANIFEST.md", "PROGRESS.md"]:
        p = os.path.join(ROOT, top)
        if os.path.exists(p): targets.append((p, False))
    EXEMPT = {os.path.join(ROOT, "reports", "MASTER_REASONING_REPORT.md")}
    for sub in ["reference", "reports", "research", "reproduction"]:
        for dp, dn, fn in os.walk(os.path.join(ROOT, sub)):
            for f in fn:
                p = os.path.join(dp, f)
                if f.endswith(".md") and p not in EXEMPT:
                    targets.append((p, False))
    for path, strict in targets:
        bad = scan(path, strict)
        if bad:
            failures += 1
            rel = os.path.relpath(path, ROOT)
            for ch, lines in sorted(bad.items(), key=lambda kv: -len(kv[1])):
                try: name = unicodedata.name(ch)
                except ValueError: name = "?"
                print(f"{rel}: U+{ord(ch):04X} {name} x{len(lines)} (first at line {lines[0]})")
    print(f"\nchecked {len(targets)} files; {failures} with disallowed characters")
    sys.exit(1 if failures else 0)

if __name__ == "__main__":
    main()
