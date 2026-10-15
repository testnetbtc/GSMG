#!/usr/bin/env python3
"""Hash every file under sources/ and build the inventory, byte-identical lineage
and near-identical variant tables (brief §6.1–6.2).

Outputs (reference/data/):
  SOURCE_INVENTORY.csv  one row per file: path, repo, origin ref, commit, bytes, sha256, first_seen_date
  SOURCE_LINEAGE.csv    one row per file: group_id, sha256, bytes, repo, path, commit, first_seen_date,
                        role (canonical|duplicate|variant), canonical_path, variant_group
  VARIANT_GROUPS.csv    near-identical text groups: canonical + members, normalisation that equates them,
                        similarity, and the diff file
  variants/<id>.diff    unified diff canonical -> member (only for non-byte-identical variants)

Canonical choice for a byte-identical group (brief §6.1): upstream repo in fork history first
(A puzzlehunt > B naddiseo [GitHub fork of A] > C hosterjack [vendors B, per its NOTICE.md]),
then default branch before PR/branch extras, then earliest first_seen_date, then shortest path.
"""
import csv, difflib, hashlib, os, re, subprocess, sys
from collections import defaultdict

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
SRC = os.path.join(ROOT, "sources")
DATA = os.path.join(ROOT, "reference", "data")
os.makedirs(os.path.join(DATA, "variants"), exist_ok=True)

KEY = {"puzzlehunt": "A", "naddiseo": "B", "hosterjack": "C", "discussions": "D"}
DEFAULT = {"A": "src-A/master", "B": "src-B/master", "C": "src-C/main"}
REFS = {}
with open(os.path.join(SRC, "REFS.tsv")) as fh:
    for row in csv.DictReader(fh, delimiter="\t"):
        REFS[(row["key"], row["kind"], row["ref"])] = row["head_commit"]


def git(*a):
    return subprocess.run(["git", "-C", ROOT, *a], capture_output=True, text=True).stdout


def origin(rel):
    """(repo key, origin ref label, commit, path inside upstream repo)."""
    parts = rel.split("/")
    top = parts[1]
    k = KEY.get(top, "?")
    if k == "D":
        return k, "github-api", "", "/".join(parts[2:])
    if len(parts) > 2 and parts[2].startswith("_pr"):
        n = parts[2][3:]
        return k, f"pr-{n}", REFS[(k, "pr", n)], "/".join(parts[3:])
    if len(parts) > 3 and parts[2] == "_branches":
        # branch names may contain '/', match the longest known branch
        rest = "/".join(parts[3:])
        for (kk, kind, ref), sha in sorted(REFS.items(), key=lambda x: -len(x[0][2])):
            if kk == k and kind == "branch" and rest.startswith(ref + "/"):
                return k, f"branch-{ref}", sha, rest[len(ref) + 1:]
    return k, "default", REFS[(k, "branch", {"A": "master", "B": "master", "C": "main"}[k])], "/".join(parts[2:])


_first_cache = {}


def first_seen(commit, blob):
    """Earliest committer date at which `blob` exists in history reachable from `commit`."""
    key = (commit, blob)
    if key not in _first_cache:
        out = git("log", "--reverse", "--format=%cI", f"--find-object={blob}", commit).split()
        _first_cache[key] = out[0] if out else ""
    return _first_cache[key]


def main():
    rows = []
    disc_dates = {}
    for dp, dn, fn in os.walk(SRC):
        dn.sort()
        for f in sorted(fn):
            ap = os.path.join(dp, f); rel = os.path.relpath(ap, ROOT)
            if rel == "sources/REFS.tsv":
                k, ref, commit, up = "M", "build", "", "REFS.tsv"
            else:
                k, ref, commit, up = origin(rel)
            data = open(ap, "rb").read()
            sha = hashlib.sha256(data).hexdigest()
            if k in ("A", "B", "C"):
                blob = git("hash-object", ap).strip()
                fs = first_seen(commit, blob)
            else:
                fs = ""
            rows.append(dict(path=rel, repo=k, origin_ref=ref, commit=commit, upstream_path=up,
                             bytes=len(data), sha256=sha, first_seen_date=fs))
    # discussion files: first_seen = fetch time from requests.log is not per file; use mtime date of raw
    for r in rows:
        if r["repo"] == "D":
            r["first_seen_date"] = "fetched-2026-10-15"
    with open(os.path.join(DATA, "SOURCE_INVENTORY.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)

    # ---------------- byte-identical groups
    rank = {"A": 0, "B": 1, "C": 2, "D": 3, "M": 4}
    groups = defaultdict(list)
    for r in rows:
        groups[r["sha256"]].append(r)

    def prefkey(r):
        return (rank[r["repo"]], r["origin_ref"] != "default", r["first_seen_date"] or "9999", len(r["path"]), r["path"])

    gid = {}
    for i, (sha, members) in enumerate(sorted(groups.items(), key=lambda x: min(prefkey(m) for m in x[1]))):
        members.sort(key=prefkey)
        gid[sha] = f"G{i + 1:04d}"
        for j, m in enumerate(members):
            m["group_id"] = gid[sha]
            m["role"] = "canonical" if j == 0 else "duplicate"
            m["canonical_path"] = members[0]["path"]
            m["variant_group"] = ""

    # ---------------- near-identical text variants (among group canonicals)
    def text(path):
        b = open(os.path.join(ROOT, path), "rb").read()
        if len(b) > 3_000_000 or b"\0" in b[:4096]:
            return None
        try:
            return b.decode("utf-8")
        except UnicodeDecodeError:
            return None

    def norm(t):
        t = t.replace("\r\n", "\n").replace("\r", "\n")
        return "\n".join(l.rstrip() for l in t.split("\n")).strip()

    canon = [r for r in rows if r["role"] == "canonical" and r["repo"] in "ABC"]
    bynorm = defaultdict(list)
    texts = {}
    for r in canon:
        t = text(r["path"])
        if t is not None:
            texts[r["path"]] = t
            bynorm[hashlib.sha256(norm(t).encode()).hexdigest()].append(r)
    vgroups = []
    used = set()
    for h, ms in bynorm.items():
        if len(ms) > 1:
            ms.sort(key=lambda r: (rank[r["repo"]], -r["bytes"]))
            vgroups.append((ms, "CRLF->LF + trailing-space + outer-strip normalisation equal"))
            used.update(m["path"] for m in ms)
    # same basename across different repos/refs, similarity >= 0.80
    byname = defaultdict(list)
    for r in canon:
        if r["path"] in texts and r["path"] not in used:
            byname[os.path.basename(r["path"])].append(r)
    for name, ms in byname.items():
        if len(ms) < 2 or name in ("README.md",) and False:
            continue
        ms.sort(key=lambda r: (rank[r["repo"]], r["origin_ref"] != "default", -r["bytes"]))
        base = ms[0]; cluster = [base]
        for m in ms[1:]:
            a, b = norm(texts[base["path"]]), norm(texts[m["path"]])
            if max(len(a), len(b)) > 400_000:
                ratio = difflib.SequenceMatcher(None, a.splitlines(), b.splitlines(), autojunk=False).quick_ratio()
            else:
                ratio = difflib.SequenceMatcher(None, a.splitlines(), b.splitlines(), autojunk=False).ratio()
            if ratio >= 0.80:
                m["_ratio"] = ratio; cluster.append(m)
        if len(cluster) > 1:
            vgroups.append((cluster, "same file name, line-similarity >= 0.80"))
    vrows = []
    for i, (ms, why) in enumerate(vgroups):
        vid = f"V{i + 1:03d}"
        # canonical = most complete (most lines after normalisation), tie -> upstream order
        ms.sort(key=lambda r: (r["origin_ref"] != "default", -len(norm(texts[r["path"]]).splitlines()), rank[r["repo"]]))
        c = ms[0]
        c["variant_group"] = vid
        for m in ms[1:]:
            a, b = norm(texts[c["path"]]).splitlines(), norm(texts[m["path"]]).splitlines()
            diff = list(difflib.unified_diff(a, b, c["path"], m["path"], lineterm="", n=1))
            dfile = f"reference/data/variants/{vid}_{len(vrows) + 1:03d}.diff"
            open(os.path.join(ROOT, dfile), "w").write("\n".join(diff) + "\n")
            only_member = sum(1 for l in diff if l.startswith("+") and not l.startswith("+++"))
            only_canon = sum(1 for l in diff if l.startswith("-") and not l.startswith("---"))
            ratio = m.get("_ratio") or difflib.SequenceMatcher(None, a, b, autojunk=False).quick_ratio()
            # every byte-duplicate of m follows m into the variant role
            for r in rows:
                if r["group_id"] == m["group_id"]:
                    r["role"] = "variant"; r["canonical_path"] = c["path"]; r["variant_group"] = vid
            vrows.append(dict(variant_group=vid, canonical_path=c["path"], member_path=m["path"], rule=why,
                              line_similarity=f"{ratio:.3f}", lines_only_in_member=only_member,
                              lines_only_in_canonical=only_canon, diff_file=dfile if (only_member or only_canon) else "",
                              unique_fact_review="pending"))
    with open(os.path.join(DATA, "VARIANT_GROUPS.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(vrows[0].keys()) if vrows else ["variant_group"]); w.writeheader(); w.writerows(vrows)

    cols = ["group_id", "sha256", "bytes", "repo", "path", "commit", "first_seen_date", "role", "canonical_path", "variant_group", "origin_ref", "upstream_path"]
    with open(os.path.join(DATA, "SOURCE_LINEAGE.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=cols, extrasaction="ignore"); w.writeheader()
        w.writerows(sorted(rows, key=lambda r: (r["group_id"], r["role"] != "canonical", r["path"])))
    from collections import Counter
    print("files", len(rows), "groups", len(groups), "multi-member groups", sum(1 for g in groups.values() if len(g) > 1),
          "variant groups", len(vgroups), "roles", dict(Counter(r["role"] for r in rows)))


if __name__ == "__main__":
    main()
