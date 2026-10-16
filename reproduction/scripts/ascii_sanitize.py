#!/usr/bin/env python3
"""Normalise typography to plain ASCII in the archive's OWN documents.

GitHub renders arrows, ellipses, box-drawing characters, math symbols,
superscripts, section signs and typographic quotes in a fallback font that
looks wrong, especially inside code spans. This script rewrites those
characters to ASCII equivalents. It never touches sources/ (upstream content
is preserved verbatim), and it leaves accented letters and emoji alone (they
render normally and occur inside quoted creator messages).

Idempotent. Usage:
    python3 reproduction/scripts/ascii_sanitize.py            # default file set
    python3 reproduction/scripts/ascii_sanitize.py FILE...    # specific files
"""
import os, re, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

SINGLE = {
    "…": "...",            # ellipsis
    "—": "--",             # em dash
    "–": "-", "‒": "-", "‑": "-", "‐": "-",   # en/figure/nb/plain hyphen
    "−": "-",              # minus sign
    "→": "->", "←": "<-", "↔": "<->", "↑": "^", "↓": "v",
    "⇒": "=>", "⇐": "<==", "⇔": "<=>", "⟶": "-->",
    "×": "x", "÷": "/", "±": "+/-", "≈": "~", "≠": "!=",
    "≡": "==", "≤": "<=", "≥": ">=", "∞": "inf",
    "∈": " in ", "∉": " not in ", "⊕": " XOR ", "⊗": " x ",
    "√": "sqrt", "∑": "sum", "∏": "prod",
    "‖": "||", "∥": "||", "′": "'", "″": '"', "°": " deg",
    "·": "-",
    "“": '"', "”": '"', "„": '"', "‘": "'", "’": "'", "‚": "'",
    "«": '"', "»": '"',
    "─": "-", "│": "|", "┌": "+", "┐": "+", "└": "+", "┘": "+",
    "├": "+", "┤": "+", "┬": "+", "┴": "+", "┼": "+",
    "═": "=", "║": "|", "╔": "+", "╗": "+", "╚": "+", "╝": "+", "╬": "+",
    "▶": ">", "◀": "<", "▲": "^", "▼": "v", "●": "*", "○": "o",
    "■": "#", "□": "[ ]", "⬤": "*",
    "✓": "[ok]", "✔": "[ok]", "✗": "[x]", "✘": "[x]", "✅": "[OK]",
    "❌": "[X]", "⚠": "[!]",
    "χ": "chi", "π": "pi", "α": "alpha", "β": "beta", "λ": "lambda",
    "μ": "mu", "σ": "sigma",
    " ": " ", " ": " ", " ": " ", " ": " ", "⁠": "", "​": "", "﻿": "",
}
SUP = {"⁰": "0", "¹": "1", "²": "2", "³": "3", "⁴": "4", "⁵": "5",
       "⁶": "6", "⁷": "7", "⁸": "8", "⁹": "9", "⁺": "+", "⁻": "-"}
SUB = {chr(0x2080 + i): str(i) for i in range(10)}

SUP_RUN = re.compile("[" + "".join(map(re.escape, SUP)) + "]+")
SUB_RUN = re.compile("[" + "".join(map(re.escape, SUB)) + "]+")


def sanitize(text: str) -> str:
    text = SUP_RUN.sub(lambda m: "^" + "".join(SUP[c] for c in m.group(0)), text)
    text = SUB_RUN.sub(lambda m: "_" + "".join(SUB[c] for c in m.group(0)), text)
    # section sign -> "section " (with a space before it unless at line start / after '(')
    text = re.sub(r"(?<=[^\s(])§\s*", " section ", text)
    text = re.sub(r"§\s*", "section ", text)
    for k, v in SINGLE.items():
        text = text.replace(k, v)
    text = text.replace("prior_reportsection", "prior_report section")
    return text


def default_targets():
    out = []
    for top in ["README.md", "BRIEF.md", "DECISIONS.md", "MANIFEST.md", "PROGRESS.md"]:
        p = os.path.join(ROOT, top)
        if os.path.exists(p): out.append(p)
    # reports/MASTER_REASONING_REPORT.md is a verbatim record (header states its
    # body hash) and is deliberately left untouched.
    exempt = {os.path.join(ROOT, "reports", "MASTER_REASONING_REPORT.md")}
    for sub in ["reference", "reports", "research", "reproduction"]:
        for dp, dn, fn in os.walk(os.path.join(ROOT, sub)):
            for f in fn:
                p = os.path.join(dp, f)
                if f.endswith(".md") and p not in exempt:
                    out.append(p)
    # generator scripts whose string literals end up in generated documents
    for f in ["reproduce.py", "build_manifest.py", "build_inventory.py", "build_registers.py", "check_manifest.py"]:
        out.append(os.path.join(ROOT, "reproduction", "scripts", f))
    return out


def main(argv):
    targets = [os.path.abspath(a) for a in argv] or default_targets()
    changed = 0
    for path in targets:
        rel = os.path.relpath(path, ROOT)
        if rel.startswith("sources" + os.sep):
            print(f"skip (upstream, verbatim): {rel}"); continue
        raw = open(path, encoding="utf-8").read()
        new = sanitize(raw)
        if new != raw:
            n = sum(1 for a, b in zip(raw, new) if a != b) + abs(len(raw) - len(new))
            open(path, "w", encoding="utf-8").write(new)
            changed += 1
            print(f"rewrote {rel}")
    print(f"{changed} file(s) changed of {len(targets)}")


if __name__ == "__main__":
    main(sys.argv[1:])
