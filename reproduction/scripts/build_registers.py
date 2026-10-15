#!/usr/bin/env python3
"""Build the machine-readable registers in reference/data/ (brief §6.3):

  CLAIMS.jsonl            every claim: prior-report rows (source "prior_report§N"), this build's
                          reproduction records (status "reproduced"), and extraction rows
  CREATOR_CLUES.jsonl     prior-report §5 rows + extracted creator-attributed statements
  EXPERIMENT_COVERAGE.csv prior-report §7 rows + extracted experiment/attempt rows
  CONTRADICTIONS.jsonl    extracted contradiction rows (the reasoned register is 07_CONTRADICTIONS.md)
  INJECTIONS.jsonl        repository text addressed to readers/AIs that was recorded and not acted on

Every row has `source` and `status`. Extraction rows come from reference/data/extraction/*.jsonl,
written by read-only sub-agents (see reference/data/extraction/README.md); their statuses are
`reported` / `interpreted` / `source-reproduced` and are never upgraded here. Only rows produced
from reproduction/results/reproduction_results.json carry status `reproduced`.
"""
import csv, glob, json, os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
D = os.path.join(ROOT, "reference", "data")
EX = os.path.join(D, "extraction")

PRIOR_CLAIMS = [
    ("3.1", "AES convention: sha256hex(answer) password, EVP_BytesToKey SHA-256 one round, AES-256-CBC, strict PKCS#7, for phase2/phase3/phase32"),
    ("3.1", "Opening grid -> gsmg.io/theseedisplanted followed by four zero bits"),
    ("3.1", "Phase-1 answer sha256 equals released checkpoint 5ac40783…0b746f75"),
    ("3.1", "phase2 answer causality -> 648-byte plaintext sha256 e2f9dd65…593a"),
    ("3.1", "phase3 227-char answer -> 4090-byte plaintext sha256 c4ad9455…865f"),
    ("3.1", "phase32 62-char answer -> 2422-byte plaintext sha256 b82afeb8…8a34"),
    ("3.1", "speech = PT-phase32[447:1986] Latin-1 -> CP1141 -> Beaufort thematrixhasyou, 1539 letters"),
    ("3.1", "149-digit region -> straddling checkerboard (blank cols 1,4; alphabet fubcdora/lethingkymvpszjqwx.) -> 91-letter sentence"),
    ("3.1", "audio L-R spectrogram hex 48 41 53 48 54 48 45 54 45 58 54 -> HASHTHETEXT"),
    ("3.1", "entry hash SHA256(GSMGIO5BTCPUZZLECHALLENGE1GSMG1JC9wtdSwfwApgj2xcmJPAwx7prBe)=89727c59…6a32"),
    ("3.1", "soup a/b -> matrixsumlist; z-sections -> lastwordsbeforearchichoice, thispassword; inner a/b -> enter"),
    ("3.2", "salphaseion.txt and salph_inner.txt are byte-identical aliases"),
    ("4.1", "80-byte CBC ciphertext permits 64-79 bytes of unpadded plaintext"),
    ("4.2", "DBBI is 91 letters over a-i, no o, first-occurrence DBIFHCEGA, b/c expansion 169"),
    ("4.3", "FAED is 570 letters, counts a54 b49 c52 d49 e69 f57 g107 h58 i75, b/c expansion 1225"),
    ("4.4", "full-period Bifid of FAED with square DBIFHCEGAKLMNOPQRSTUVWXYZ -> 570 letters sha256 0c5d984f…, head BTCSEED, single Z at index 97"),
    ("4.4", "even output positions use {B,C,D,E}; odd positions minus I,O = 256 letters over 23 symbols; period-2 interleaved identity holds"),
    ("4.5", "chain1 79 bytes 1449a217…; chain2 79 bytes b40fce72…; Cosmic 1327 bytes 4f7a1e4e…; chain4 1151 bytes e4269ed5…"),
    ("5.2", "grid: 101 ones; palette 86 black/85 white/15 blue (63,72,204)/9 yellow (255,242,0)/1 FEFEFE at (7,4)"),
    ("5.2", "24 blue/yellow cells at URL last-bit positions"),
    ("6", "XOR of seven digests with two identical matrixsumlist digests reduces to XOR of five"),
    ("8", "address balance at collection 125,649,674 sat (1.25649674 BTC); spending tx input pubkeys match uncompressed prize key"),
    ("10.2", "chain1 password raw literal matrixsumlistenterlastwordsbeforearchichoicethispasswordmatrixsumlist, EVP-MD5; WIF 5K2byJMssxFKuTgnk9YQjpBz5FhkwwF2LaZoAyTus8HjGEpz8AT opens p32_trailing to 79 bytes"),
    ("10.3", "earliest exact E_S publication located: A PR#68 comment 3704010992, 2026-01-01T19:07:36Z"),
    ("10.4", "random-key valid PKCS#7 probability ≈1/255; one-byte padding is ~99.6% of valid cases"),
    ("11", "uncompressed prize point -> 1GSMG1JC9wtdSwfwApgj2xcmJPAwx7prBe; compressed -> 1cc6xayvqpeetixmuXDRsGug7GKyoRdxP"),
    ("11", "no interval bound, seed generator or stopping rule is supplied by any source"),
]
PRIOR_CLUES = [
    ("2019-04-22", "dataset message 225: released 64-hex checkpoint", "a usable answer checkpoint; does not authenticate all dataset messages"),
    ("2019-05", "messages 866–875 giveit/givetit correction", "historical spelling defect; no general licence to treat typos as clues"),
    ("2020-01-14", "yellow and blue have numbers; return to first piece; more than one door", "colours and extra-path interpretation supported; no values/operation"),
    ("2021-03-01", "primes screenshot: Janusz asks about 2,3,5,7; Jrk on the prime part", "the set {2,3,5,7} is supplied by the solver"),
    ("2021-03-01", "spelling screenshot: Janusz 104/FEFEFE/101010; Jrk ancient spelling", "arithmetic is community text; not explicit confirmation"),
    ("2021-05-06", "entry screenshot from Deleted Account", "community-published entry recipe; not creator authorship"),
    ("2021-12-25", "primes required; characters zeroed out; another door still relevant", "no string, index convention or zeroing semantics fixed [date corrected to 2021-12-26 by this build]"),
    ("2022-12-10", "Cosmic Duality book-cover images", "book hashing/edition/normalisation unspecified"),
    ("2023-02-23", "dataset 8446: 161 binary bytes", "reversal yields exact concatenated words; boundaries/grammar interpretive"),
    ("2023-08-03/06", "harder parts done; ying yang milestone; salvation partly solved", "does not establish output must be literally yinyang"),
    ("2026-01-01", "New Year binary", "conventional ASCII; operation interpretive"),
    ("2026-07-12", "close friends have best chance", "no book/password/generator identified [UTC date 2026-07-13]"),
    ("dataset 9595", "friends/family could get to the author's data", "backup/data-recovery scenario, not derivability"),
    ("dataset 7830/7832/7834", "encrypted online key; solver finds a way to decrypt", "identifying the object as Cosmic is an extra inference"),
]
PRIOR_EXP = [
    ("floflo777 letter-bit masks / spatial reads", "~335 million submissions; injected controls; two implementations", "reported; generator and logs unavailable"),
    ("floflo777 16+7 alphabet partitions", "245,157 partitions, both polarities", "finite claimed model; not replayed"),
    ("Base58 / substrings / direct blob windows", "explicit window lengths/steps in tested.md", "excludes only documented representations"),
    ("fixed taijitu antisymmetry model", "analytical argument", "not a proof against all yin-yang interpretations"),
    ("prior small-blob oracle sweeps", "MD5 version; later SHA-256 rerun; later both-digest tools", "coverage must retain the actual digest"),
    ("word-window / joined-answer / matrices / planted-address families", "named counts and synthetic witnesses", "scoped negatives; need frozen manifests"),
    ("Hosterjack field / binary / grid / cipher families", "many printable-text scoring checks", "a readability negative is not a binary-key negative"),
    ("Naddiseo#13 permutation/null experiments", "9! keys, prefix analysis, corrections, direct-key checks", "prefix/substring nulls differ"),
    ("Naddiseo#17 continuation attempts", "named WIF, digest/KDF/mode families, ~2,400 ingredient candidates", "no full parameter manifest"),
    ("E054 / earlier operation-capped searches", "mentioned only in brief", "no coverage inherited; cap is not exhaustiveness"),
]


def load_extraction():
    rows = []
    for f in sorted(glob.glob(os.path.join(EX, "*.jsonl"))):
        agent = os.path.basename(f)[:-6]
        for i, line in enumerate(open(f, encoding="utf-8"), 1):
            line = line.strip()
            if not line:
                continue
            try:
                o = json.loads(line)
            except json.JSONDecodeError:
                continue
            o["_extraction"] = f"reference/data/extraction/{agent}.jsonl#L{i}"
            o["_agent"] = agent
            rows.append(o)
    return rows


def main():
    ex = load_extraction()
    # ---- CLAIMS
    claims = []
    for n, (sec, t) in enumerate(PRIOR_CLAIMS, 1):
        claims.append({"id": f"PRIOR-C{n:03d}", "text": t, "source": f"prior_report§{sec}", "status": "reported (prior report; re-checked where a reproduction row exists)"})
    rr = json.load(open(os.path.join(ROOT, "reproduction", "results", "reproduction_results.json")))
    for r in rr["results"]:
        claims.append({"id": f"REPRO-{r['step']}", "text": r["step"], "source": "reproduction/results/reproduction_results.json",
                       "status": "reproduced", "comparison_with_prior": r["status"], "outputs": r["outputs"], "note": r.get("note", "")})
    k = 0
    for o in ex:
        if o.get("kind") == "claim":
            k += 1
            claims.append({"id": f"EXT-C{k:04d}", "topic": o.get("topic"), "text": o.get("text"), "exact": o.get("exact"),
                           "source": o.get("source"), "status": o.get("status"), "date": o.get("date"), "notes": o.get("notes"),
                           "extracted_by": o["_extraction"]})
    with open(os.path.join(D, "CLAIMS.jsonl"), "w", encoding="utf-8") as fh:
        for c in claims:
            fh.write(json.dumps(c, ensure_ascii=False, default=str) + "\n")
    # ---- CREATOR_CLUES
    clues = []
    for n, (d, t, f) in enumerate(PRIOR_CLUES, 1):
        clues.append({"id": f"PRIOR-K{n:03d}", "date": d, "text": t, "what_follows": f, "source": "prior_report§5",
                      "status": "reported", "attribution": "repository-attributed; not authenticated"})
    k = 0
    for o in ex:
        if o.get("kind") == "creator_clue":
            k += 1
            clues.append({"id": f"EXT-K{k:04d}", "date": o.get("date"), "topic": o.get("topic"), "text": o.get("text"),
                          "exact": o.get("exact"), "source": o.get("source"), "status": o.get("status"), "notes": o.get("notes"),
                          "attribution": "display name / handle only; not authenticated", "extracted_by": o["_extraction"]})
    with open(os.path.join(D, "CREATOR_CLUES.jsonl"), "w", encoding="utf-8") as fh:
        for c in clues:
            fh.write(json.dumps(c, ensure_ascii=False, default=str) + "\n")
    # ---- EXPERIMENT_COVERAGE
    cols = ["id", "family", "target", "inputs_params", "kdf", "validator", "count", "claimed_result", "limits", "date", "who", "source", "status", "extracted_by"]
    exp = []
    for n, (fam, scope, lim) in enumerate(PRIOR_EXP, 1):
        exp.append({"id": f"PRIOR-E{n:03d}", "family": fam, "inputs_params": scope, "limits": lim, "source": "prior_report§7", "status": "reported"})
    k = 0
    for o in ex:
        if o.get("kind") == "experiment":
            k += 1
            notes = o.get("notes")
            notes = json.dumps(notes, ensure_ascii=False) if isinstance(notes, (dict, list)) else (notes or "")
            exp.append({"id": f"EXT-E{k:04d}", "family": o.get("topic") or o.get("category"), "target": ";".join(o.get("heuristic_targets") or []),
                        "inputs_params": (o.get("text") or "") + ((" | exact: " + str(o.get("exact"))) if o.get("exact") else ""),
                        "kdf": ";".join(o.get("heuristic_kdf_mentions") or []), "validator": ";".join(o.get("heuristic_validators") or []),
                        "count": json.dumps(o.get("heuristic_counts"), ensure_ascii=False) if o.get("heuristic_counts") else "",
                        "claimed_result": o.get("outcome") or o.get("claimed_output") or "", "limits": notes,
                        "date": o.get("date") or "", "who": o.get("who") or o.get("author") or "", "source": o.get("source"),
                        "status": o.get("status"), "extracted_by": o["_extraction"]})
    with open(os.path.join(D, "EXPERIMENT_COVERAGE.csv"), "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=cols, extrasaction="ignore"); w.writeheader()
        for e in exp:
            w.writerow({c: ("" if e.get(c) is None else e.get(c)) for c in cols})
    # ---- CONTRADICTIONS / INJECTIONS / GLOSSARY raw
    for kind, name in [("contradiction", "CONTRADICTIONS.jsonl"), ("injection", "INJECTIONS.jsonl"), ("glossary", "GLOSSARY_RAW.jsonl")]:
        with open(os.path.join(D, name), "w", encoding="utf-8") as fh:
            for o in ex:
                if o.get("kind") == kind:
                    fh.write(json.dumps({"topic": o.get("topic"), "text": o.get("text"), "exact": o.get("exact"), "source": o.get("source"),
                                         "status": o.get("status"), "notes": o.get("notes"), "extracted_by": o["_extraction"]},
                                        ensure_ascii=False, default=str) + "\n")
    print(f"claims {len(claims)} clues {len(clues)} experiments {len(exp)}")


if __name__ == "__main__":
    main()
