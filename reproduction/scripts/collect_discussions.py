#!/usr/bin/env python3
"""Paced, resumable, unauthenticated GitHub REST collector for issues, PRs,
comments, reviews, review comments and PR file lists.

Every response page is saved verbatim (JSON body + response headers) under
sources/discussions/<key>/raw/. Re-running skips pages already saved.
Each request is logged to sources/discussions/requests.log (TSV).
Usage: collect_discussions.py <GSMG repo root>
"""
import json, os, sys, time, urllib.request, urllib.error, re

REPOS = {"puzzlehunt": "puzzlehunt/gsmgio-5btc-puzzle",
         "naddiseo": "Naddiseo/gsmgio-5btc-puzzle",
         "hosterjack": "HosterjackAGV/gsmg-5btc-puzzle"}
API = "https://api.github.com"
ROOT = os.path.join(sys.argv[1], "sources", "discussions")
LOG = os.path.join(ROOT, "requests.log")


def log(*f):
    with open(LOG, "a") as fh:
        fh.write("\t".join(str(x) for x in f) + "\n")


def get(url, dest):
    """Fetch url -> dest (.json + .headers.json). Return parsed body, headers."""
    if os.path.exists(dest):
        with open(dest) as fh:
            body = json.load(fh)
        with open(dest[:-5] + ".headers.json") as fh:
            hdr = json.load(fh)
        return body, hdr
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    while True:
        req = urllib.request.Request(url, headers={
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "gsmg-archive-collector"})
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                raw = r.read(); status = r.status; hdr = dict(r.headers)
        except urllib.error.HTTPError as e:
            hdr = dict(e.headers); status = e.code; raw = e.read()
            if status in (403, 429) and hdr.get("X-RateLimit-Remaining") == "0":
                reset = int(hdr.get("X-RateLimit-Reset", time.time() + 60))
                wait = max(5, reset - time.time() + 10)
                log(time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "RATELIMIT-SLEEP", url, int(wait))
                print(f"rate limited; sleeping {int(wait)}s", flush=True)
                time.sleep(wait); continue
            log(time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), status, url, hdr.get("Link", ""))
            body = {"_error_status": status, "_error_body": raw.decode("utf-8", "replace")}
            with open(dest, "w") as fh: json.dump(body, fh, indent=1)
            with open(dest[:-5] + ".headers.json", "w") as fh: json.dump(hdr, fh, indent=1)
            return body, hdr
        except Exception as e:  # network error: retry
            log(time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "NETERR", url, repr(e))
            time.sleep(30); continue
        body = json.loads(raw)
        with open(dest, "w") as fh: json.dump(body, fh, indent=1, ensure_ascii=False)
        with open(dest[:-5] + ".headers.json", "w") as fh: json.dump(hdr, fh, indent=1)
        log(time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), status, url,
            hdr.get("Link", ""), hdr.get("X-RateLimit-Remaining", ""))
        # gentle pacing: keep within the hourly budget when it gets low
        rem = int(hdr.get("X-RateLimit-Remaining", "60"))
        if rem < 2:
            reset = int(hdr.get("X-RateLimit-Reset", time.time() + 60))
            time.sleep(max(5, reset - time.time() + 10))
        return body, hdr


def paged(base, dest_prefix):
    out, page = [], 1
    while True:
        sep = "&" if "?" in base else "?"
        body, hdr = get(f"{base}{sep}per_page=100&page={page}", f"{dest_prefix}_p{page:03d}.json")
        if isinstance(body, dict) and "_error_status" in body:
            return out, body
        out.extend(body)
        if 'rel="next"' not in (hdr.get("Link") or ""):
            return out, None
        page += 1


def main():
    for key, full in REPOS.items():
        raw = os.path.join(ROOT, key, "raw")
        get(f"{API}/repos/{full}", os.path.join(raw, "repo.json"))
        issues, _ = paged(f"{API}/repos/{full}/issues?state=all&direction=asc", os.path.join(raw, "issues"))
        comments, _ = paged(f"{API}/repos/{full}/issues/comments?direction=asc&sort=created", os.path.join(raw, "issue_comments"))
        pulls, _ = paged(f"{API}/repos/{full}/pulls?state=all&direction=asc", os.path.join(raw, "pulls"))
        prnums = sorted({i["number"] for i in issues if "pull_request" in i} | {p["number"] for p in pulls})
        for n in prnums:
            paged(f"{API}/repos/{full}/pulls/{n}/reviews", os.path.join(raw, "pr", f"{n:04d}_reviews"))
            paged(f"{API}/repos/{full}/pulls/{n}/comments", os.path.join(raw, "pr", f"{n:04d}_review_comments"))
            paged(f"{API}/repos/{full}/pulls/{n}/files", os.path.join(raw, "pr", f"{n:04d}_files"))
            paged(f"{API}/repos/{full}/pulls/{n}/commits", os.path.join(raw, "pr", f"{n:04d}_commits"))
        # per-issue refetch where counter != fetched
        got = {}
        for c in comments:
            n = int(c["issue_url"].rsplit("/", 1)[1]); got[n] = got.get(n, 0) + 1
        for i in issues:
            if i["comments"] != got.get(i["number"], 0):
                paged(f"{API}/repos/{full}/issues/{i['number']}/comments",
                      os.path.join(raw, "refetch", f"{i['number']:04d}_comments"))
        print(f"{key}: issues+prs={len(issues)} comments={len(comments)} pulls={len(pulls)}", flush=True)
    print("DONE", flush=True)


if __name__ == "__main__":
    main()
