#!/usr/bin/env python3
"""Render collected GitHub discussions losslessly to Markdown and download attachments.

Reads sources/discussions/<repo>/raw/ (written by collect_discussions.py) and writes:
  sources/discussions/<repo>/issues/NNN.md and pulls/NNN.md  — full body, every comment in
      chronological order (author, created/updated timestamps, URL, full body), PR reviews,
      review comments (with path/line/diff_hunk) and changed-file list
  sources/discussions/<repo>/COUNTS.json — issues/PRs/comments expected vs fetched, reviews
  sources/discussions/attachments/<repo>/<sha8>_<name> — every attachment URL found in bodies
  sources/discussions/attachments/ATTACHMENTS.tsv — url, repo, locator, status, bytes, sha256, local path
Usage: render_discussions.py [--no-download]
"""
import glob, hashlib, json, os, re, sys, time, urllib.request, urllib.error
from collections import defaultdict

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
D = os.path.join(ROOT, "sources", "discussions")
REPOS = {"puzzlehunt": "puzzlehunt/gsmgio-5btc-puzzle", "naddiseo": "Naddiseo/gsmgio-5btc-puzzle",
         "hosterjack": "HosterjackAGV/gsmg-5btc-puzzle"}
ATT_RE = re.compile(r"https://(?:user-images\.githubusercontent\.com/[^\s)\]\"'<>]+|github\.com/user-attachments/(?:assets|files)/[^\s)\]\"'<>]+"
                    r"|private-user-images\.githubusercontent\.com/[^\s)\]\"'<>]+|github\.com/[^/\s]+/[^/\s]+/files/\d+/[^\s)\]\"'<>]+)")


def load(pattern):
    out = []
    for f in sorted(glob.glob(pattern)):
        if f.endswith(".headers.json"):
            continue
        b = json.load(open(f))
        if isinstance(b, dict) and "_error_status" in b:
            continue
        out.extend(b if isinstance(b, list) else [b])
    return out


def block(title, user, created, updated, url, body, extra=""):
    s = f"### {title}\n\n- author: `{user}`\n- created: {created}\n- updated: {updated}\n- url: {url}\n{extra}\n"
    s += "\n<!-- body verbatim below -->\n\n" + (body if body is not None else "*(empty body)*") + "\n\n---\n\n"
    return s


def main(download=True):
    att_rows = []
    for key, full in REPOS.items():
        raw = os.path.join(D, key, "raw")
        if not os.path.exists(os.path.join(raw, "repo.json")):
            print(key, "not collected yet; skipped"); continue
        issues = load(os.path.join(raw, "issues_p*.json"))
        comments = load(os.path.join(raw, "issue_comments_p*.json"))
        pulls = {p["number"]: p for p in load(os.path.join(raw, "pulls_p*.json"))}
        refetch = defaultdict(list)
        for f in sorted(glob.glob(os.path.join(raw, "refetch", "*_comments_p*.json"))):
            if f.endswith(".headers.json"): continue
            n = int(os.path.basename(f).split("_")[0]); b = json.load(open(f))
            if isinstance(b, list): refetch[n].extend(b)
        by_issue = defaultdict(dict)
        for c in comments + [c for v in refetch.values() for c in v]:
            by_issue[int(c["issue_url"].rsplit("/", 1)[1])][c["id"]] = c
        counts = {"issues": 0, "pulls": 0, "comments_expected": 0, "comments_fetched": 0, "reviews": 0,
                  "review_comments": 0, "mismatches": []}
        for it in issues:
            n = it["number"]; is_pr = "pull_request" in it
            kind = "pulls" if is_pr else "issues"
            counts[kind] += 1
            cs = sorted(by_issue.get(n, {}).values(), key=lambda c: (c["created_at"], c["id"]))
            counts["comments_expected"] += it["comments"]; counts["comments_fetched"] += len(cs)
            if it["comments"] != len(cs):
                counts["mismatches"].append({"number": n, "counter": it["comments"], "fetched": len(cs),
                                             "refetched": len(refetch.get(n, [])) if n in refetch else None})
            labels = ", ".join(l["name"] for l in it.get("labels", [])) or "—"
            md = [f"# {key} {'PR' if is_pr else 'issue'} #{n}: {it['title']}\n",
                  f"- repository: {full}\n- url: {it['html_url']}\n- state: {it['state']}"
                  f"{' (' + it['state_reason'] + ')' if it.get('state_reason') else ''}\n- labels: {labels}\n"
                  f"- comments counter: {it['comments']} · fetched: {len(cs)}\n- closed_at: {it.get('closed_at')}\n"
                  f"- raw JSON: `sources/discussions/{key}/raw/` (issues_p*.json, issue_comments_p*.json)\n\n"]
            md.append(block("Opening post", it["user"]["login"] if it.get("user") else "ghost", it["created_at"], it["updated_at"], it["html_url"], it.get("body")))
            if is_pr:
                p = pulls.get(n, {})
                if p:
                    md.insert(1, f"- head: `{p['head'].get('label')}` @ `{p['head']['sha']}` · base: `{p['base']['ref']}` · merged_at: {p.get('merged_at')}\n")
                reviews = load(os.path.join(raw, "pr", f"{n:04d}_reviews_p*.json"))
                rcs = load(os.path.join(raw, "pr", f"{n:04d}_review_comments_p*.json"))
                files = load(os.path.join(raw, "pr", f"{n:04d}_files_p*.json"))
                commits = load(os.path.join(raw, "pr", f"{n:04d}_commits_p*.json"))
                counts["reviews"] += len(reviews); counts["review_comments"] += len(rcs)
                md.append(f"## Changed files ({len(files)})\n\n" + "".join(
                    f"- `{f['filename']}` — {f['status']}, +{f['additions']}/-{f['deletions']}, blob `{f.get('sha')}`\n" for f in files) + "\n")
                md.append(f"## Commits ({len(commits)})\n\n" + "".join(
                    f"- `{c['sha']}` {c['commit']['author']['date']} {c['commit']['author']['name']}: {c['commit']['message'].splitlines()[0] if c['commit']['message'] else ''}\n" for c in commits) + "\n")
                md.append(f"## Reviews ({len(reviews)})\n\n")
                for r in reviews:
                    md.append(block(f"Review {r['id']} — {r['state']}", (r.get("user") or {}).get("login", "ghost"), r.get("submitted_at"), r.get("submitted_at"), r["html_url"], r.get("body")))
                md.append(f"## Review comments ({len(rcs)})\n\n")
                for r in rcs:
                    ex = f"- path: `{r['path']}` line {r.get('line') or r.get('original_line')}\n- in_reply_to: {r.get('in_reply_to_id')}\n\n```diff\n{r.get('diff_hunk','')}\n```\n"
                    md.append(block(f"Review comment {r['id']}", (r.get("user") or {}).get("login", "ghost"), r["created_at"], r["updated_at"], r["html_url"], r.get("body"), ex))
            md.append(f"## Comments ({len(cs)})\n\n")
            for i, c in enumerate(cs, 1):
                md.append(block(f"Comment {i} — id {c['id']}", (c.get("user") or {}).get("login", "ghost"), c["created_at"], c["updated_at"], c["html_url"], c.get("body")))
            os.makedirs(os.path.join(D, key, kind), exist_ok=True)
            open(os.path.join(D, key, kind, f"{n:03d}.md"), "w").write("".join(md))
            # attachments
            texts = [(it["html_url"] + " body", it.get("body") or "")] + [(c["html_url"], c.get("body") or "") for c in cs]
            if is_pr:
                texts += [(r["html_url"], r.get("body") or "") for r in load(os.path.join(raw, "pr", f"{n:04d}_review*_p*.json"))]
            for loc, t in texts:
                for u in dict.fromkeys(ATT_RE.findall(t)):
                    att_rows.append([u.rstrip(".,;"), key, loc])
        counts["unique_comment_ids"] = len({c["id"] for c in comments})
        json.dump(counts, open(os.path.join(D, key, "COUNTS.json"), "w"), indent=1)
        print(key, {k: v for k, v in counts.items() if k != "mismatches"}, "mismatches:", counts["mismatches"])
    # download attachments (dedup by URL)
    adir = os.path.join(D, "attachments"); os.makedirs(adir, exist_ok=True)
    seen = {}
    tsv = ["url\trepo\tlocator\tstatus\tbytes\tsha256\tlocal_path"]
    for u, key, loc in att_rows:
        if u not in seen:
            st, size, sha, lp = "not-attempted", "", "", ""
            if download:
                try:
                    req = urllib.request.Request(u, headers={"User-Agent": "gsmg-archive-collector"})
                    with urllib.request.urlopen(req, timeout=60) as r:
                        data = r.read(); st = str(r.status)
                        ctype = r.headers.get("Content-Type", "")
                    sha = hashlib.sha256(data).hexdigest(); size = str(len(data))
                    name = re.sub(r"[^A-Za-z0-9._-]", "_", u.rsplit("/", 1)[-1])[:80]
                    if "." not in name:
                        ext = {"image/png": ".png", "image/jpeg": ".jpg", "image/gif": ".gif", "video/mp4": ".mp4",
                               "application/pdf": ".pdf", "text/plain": ".txt", "application/zip": ".zip"}.get(ctype.split(";")[0], ".bin")
                        name += ext
                    os.makedirs(os.path.join(adir, key), exist_ok=True)
                    lp = f"sources/discussions/attachments/{key}/{sha[:8]}_{name}"
                    open(os.path.join(ROOT, lp), "wb").write(data)
                except urllib.error.HTTPError as e:
                    st = f"HTTP {e.code}"
                except Exception as e:
                    st = f"ERROR {type(e).__name__}: {e}"
                time.sleep(0.5)
            seen[u] = (st, size, sha, lp)
        st, size, sha, lp = seen[u]
        tsv.append("\t".join([u, key, loc, st, size, sha, lp]))
    open(os.path.join(adir, "ATTACHMENTS.tsv"), "w").write("\n".join(tsv) + "\n")
    from collections import Counter
    print("attachment occurrences", len(att_rows), "distinct", len(seen), Counter(v[0] for v in seen.values()))


if __name__ == "__main__":
    main(download="--no-download" not in sys.argv)
