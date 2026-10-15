#!/usr/bin/env python3
"""Completeness check for the archive (brief §7.4).

Walks sources/ and asserts, for every file on disk, that it is either
  (a) a `canonical` row in reference/data/SOURCE_LINEAGE.csv, or
  (b) a `duplicate`/`variant` row whose canonical_path is itself a canonical row,
and that its current SHA-256 equals the hash recorded in the lineage table.
Anything else is an ORPHAN and is printed with the reason.

It also reports, as a secondary (non-failing) statistic, how many canonical files
are cited by path from the readable reference layer (reference/*.md, reference/data/*
other than the inventory/lineage tables), so the reader can see which canonical
files are carried only by the raw archive + lineage row.

Exit status: 0 when there are zero orphans, 1 otherwise.
Usage: python3 reproduction/scripts/check_manifest.py [--list-uncited]
"""
import csv, glob, hashlib, os, sys
from collections import Counter

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))


def main():
    lin = {}
    with open(os.path.join(ROOT, "reference", "data", "SOURCE_LINEAGE.csv")) as fh:
        for r in csv.DictReader(fh):
            lin[r["path"]] = r
    on_disk = []
    for dp, dn, fn in os.walk(os.path.join(ROOT, "sources")):
        for f in fn:
            on_disk.append(os.path.relpath(os.path.join(dp, f), ROOT))
    orphans, roles = [], Counter()
    for p in sorted(on_disk):
        r = lin.get(p)
        if r is None:
            orphans.append((p, "no lineage row")); continue
        sha = hashlib.sha256(open(os.path.join(ROOT, p), "rb").read()).hexdigest()
        if sha != r["sha256"]:
            orphans.append((p, f"hash drift: disk {sha[:12]} != lineage {r['sha256'][:12]}")); continue
        roles[r["role"]] += 1
        if r["role"] == "canonical":
            continue
        c = lin.get(r["canonical_path"])
        if r["role"] not in ("duplicate", "variant"):
            orphans.append((p, f"unknown role {r['role']}"))
        elif c is None or c["role"] != "canonical":
            orphans.append((p, f"{r['role']} of {r['canonical_path']} which is not a canonical row"))
        elif not os.path.exists(os.path.join(ROOT, r["canonical_path"])):
            orphans.append((p, f"canonical {r['canonical_path']} missing on disk"))
    stale = sorted(set(lin) - set(on_disk))

    # secondary: canonical files cited from the readable reference layer
    corpus = ""
    for f in glob.glob(os.path.join(ROOT, "reference", "*.md")) + glob.glob(os.path.join(ROOT, "reference", "data", "*")):
        if os.path.basename(f) in ("SOURCE_LINEAGE.csv", "SOURCE_INVENTORY.csv") or os.path.isdir(f):
            continue
        corpus += open(f, encoding="utf-8", errors="replace").read()
    canon = [p for p, r in lin.items() if r["role"] == "canonical" and p in set(on_disk)]

    def cited(p):
        rel = p.split("/", 2)[2] if p.count("/") >= 2 else p
        return p in corpus or rel in corpus
    unc = [p for p in canon if not cited(p)]
    cat = Counter(p.split("/")[1] + ("/" + p.split("/")[2] if p.split("/")[2].startswith(("_pr", "_branches", "raw", "issues", "pulls", "attachments")) else "") for p in unc)

    print("=== check_manifest.py ===")
    print(f"files under sources/: {len(on_disk)}")
    print(f"lineage rows: {len(lin)}   stale rows (no file): {len(stale)}")
    print("roles on disk: " + ", ".join(f"{k}={v}" for k, v in sorted(roles.items())))
    print(f"ORPHANS: {len(orphans)}")
    for p, why in orphans:
        print(f"  ORPHAN {p}: {why}")
    for p in stale:
        print(f"  STALE  {p}")
    print(f"canonical files cited by path from reference/: {len(canon) - len(unc)} / {len(canon)}")
    print("canonical files carried by raw archive + lineage row only, by area:")
    for k, v in sorted(cat.items(), key=lambda x: -x[1]):
        print(f"  {v:5d}  {k}")
    if "--list-uncited" in sys.argv:
        for p in unc:
            print("  uncited", p)
    print("RESULT:", "PASS (zero orphans)" if not orphans and not stale else "FAIL")
    return 0 if not orphans and not stale else 1


if __name__ == "__main__":
    sys.exit(main())
