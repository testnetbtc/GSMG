#!/usr/bin/env python3
"""Copy one canonical byte-copy of each puzzle artifact into reference/artifacts/ and write
reference/data/ARTIFACT_FILES.csv (artifact path, source path, repo@commit, bytes, sha256, kind, note).
Canonical source = the canonical row of the byte-identical group in SOURCE_LINEAGE.csv when one exists."""
import csv, hashlib, os, shutil

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
S = "sources/"
B, A, C, B15 = S + "naddiseo/", S + "puzzlehunt/", S + "hosterjack/", S + "naddiseo/_pr15/"
ITEMS = [  # (dest, source, kind, note)
    ("images/puzzle.png", A + "puzzle.png", "puzzle image", "opening 14x14 grid + banner + QR + address"),
    ("images/theseedisplanted.png", A + "theseedisplanted.png", "puzzle page image", "Phase-1 page image"),
    ("images/phase2_page.png", A + "phase2.png", "puzzle page screenshot", "A's phase2.png (differs from B phase2-assets/phase2.png)"),
    ("images/phase3_page.png", A + "phase3.png", "puzzle page screenshot", ""),
    ("images/SalPhaselonCosmicDuality.png", A + "SalPhaselonCosmicDuality.png", "puzzle page screenshot", "SalPhaseIon + Cosmic Duality page screenshot"),
    ("images/decentraland_photo_2020-04-26_09-24-30.jpg", A + "photo_2020-04-26_09-24-30.jpg", "creator hint image", "Decentraland screenshot (save-date filename)"),
    ("images/phase1-source.png", B + "phase1-assets/phase1-source.png", "puzzle page screenshot", ""),
    ("images/warning-logic.png", B + "phase1-assets/warning-logic.png", "puzzle page image", ""),
    ("images/phase2_page_B.png", B + "phase2-assets/phase2.png", "puzzle page screenshot", ""),
    ("images/chess.png", B + "phase2-assets/chess.png", "puzzle image", "Phase-2 part-7 chess position"),
    ("envelopes/phase2.b64.txt", B + "phase2-assets/phase2_aes.txt", "AES envelope", "salt 06286612d43ed7ed"),
    ("envelopes/phase3.b64.txt", B + "phase2-assets/phase3_aes.txt", "AES envelope", "salt 9fbc451d13d071f4"),
    ("envelopes/phase32.b64.txt", B + "phase3-assets/phase3.2-aes.txt", "AES envelope", "salt eefc4c5befc1656a"),
    ("envelopes/salph_inner.b64.txt", C + "ciphertexts/salph_inner.txt", "AES envelope", "salt 3ab585348552415d; reconstructed from soup"),
    ("envelopes/p32_trailing.b64.txt", C + "ciphertexts/p32_trailing.txt", "AES envelope", "salt b45a5e3d827593ca; tail of phase32 plaintext"),
    ("envelopes/cosmic.b64.txt", C + "ciphertexts/cosmic.txt", "AES envelope", "salt 2d3f6fe06dc950e6; = archived page textarea 2"),
    ("envelopes/urlblob.b64.txt", C + "ciphertexts/urlblob.txt", "AES envelope (community URL artifact)", "salt 74c974e3f92e64b5; NOT a page-embedded container"),
    ("plaintexts/phase2_plaintext.txt", B + "phase2-assets/phase2.1.txt", "decrypted stage text", "= reproduced aes_phase2 output (CRLF)"),
    ("plaintexts/phase3_plaintext.txt", B + "phase2-assets/phase3.txt", "decrypted stage text", "= reproduced aes_phase3 output"),
    ("plaintexts/phase32_plaintext.bin", B + "phase3-assets/phase3.2.txt", "decrypted stage bytes", "= reproduced aes_phase32 output"),
    ("pages/salphaseion_soup.txt", B15 + "neo/materials/primary/salphaseion_soup_space_separated.txt", "page text", "SalPhaseIon textarea 1 (space separated)"),
    ("pages/salphaseion_page_2024-11-23.html", B15 + "neo/materials/wayback/pages/salphaseion_2024-11-23.html", "archived page", "Wayback 20241123015038 as supplied in B PR#15"),
    ("pages/salphaseion_page_2025-10-31.html", B15 + "neo/materials/wayback/pages/salphaseion_2025-10-31.html", "archived page", "Wayback 20251031153559 as supplied in B PR#15"),
    ("pages/choiceisanillusion_2020-11-12.html", B15 + "neo/materials/wayback/pages/choiceisanillusion_2020-11-12.html", "archived page", "Phase-2 page"),
    ("pages/choiceisanillusion_2026-04-05.html", B15 + "neo/materials/wayback/pages/choiceisanillusion_2026-04-05.html", "archived page", "adds 'little bunny hunter' HTML comment"),
    ("pages/root_2026-08-19_finale.html", B15 + "neo/materials/wayback/pages/root_2026-08-19_finale.html", "archived page", "post-parking 'finale' page; authorship unverified"),
    ("audio/puzzlepiece.mp3", B + "decentraland-assets/puzzlepiece.mp3", "audio", "Decentraland -41,-17; content id QmeRy5MjmEZ2W6J3DwhQfht5HKBKXBFpoGzSkzmjeGKiDK"),
    ("images/decentraland-01-show-interactive.png", B + "decentraland-assets/01-show-interactive.png", "screenshot", ""),
    ("images/decentraland-02-dcl-info.png", B + "decentraland-assets/02-dcl-info.png", "screenshot", ""),
    ("creator_media/1537.jpg", C + "assets/sowut/1537.jpg", "creator-posted media", "lossy JPEG of the puzzle image (msg 1537)"),
    ("creator_media/1647.jpg", C + "assets/sowut/1647.jpg", "creator-posted media", "Matrix cake still (msg 1647)"),
    ("creator_media/1743.jpg", C + "assets/sowut/1743.jpg", "creator-posted media", "Decentraland -41,-17 (msg 1743)"),
    ("creator_media/66964.jpg", C + "assets/sowut/66964.jpg", "creator-posted media", "banter screenshot (msg 66964)"),
]
for f in sorted(os.listdir(os.path.join(ROOT, B, "hints"))):
    ITEMS.append(("hints/" + f.replace(" ", "_"), B + "hints/" + f, "hint screenshot", "dated filename; display names not authenticated"))

lin = {}
with open(os.path.join(ROOT, "reference/data/SOURCE_LINEAGE.csv")) as fh:
    for r in csv.DictReader(fh):
        lin[r["path"]] = r
rows = []
for dest, srcp, kind, note in ITEMS:
    r = lin.get(srcp)
    canon = r["canonical_path"] if r and r["role"] == "duplicate" else srcp
    data = open(os.path.join(ROOT, canon), "rb").read()
    out = os.path.join(ROOT, "reference/artifacts", dest)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, "wb").write(data)
    cr = lin.get(canon, {})
    rows.append(dict(artifact=f"reference/artifacts/{dest}", canonical_source=canon,
                     citation=f"{ {'puzzlehunt':'A','naddiseo':'B','hosterjack':'C'}[canon.split('/')[1]] }:{cr.get('upstream_path','')}@{cr.get('commit','')[:7]}",
                     bytes=len(data), sha256=hashlib.sha256(data).hexdigest(), kind=kind,
                     duplicates=";".join(x["path"] for x in lin.values() if x.get("group_id") == cr.get("group_id") and x["path"] != canon), note=note))
with open(os.path.join(ROOT, "reference/data/ARTIFACT_FILES.csv"), "w", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
print(len(rows), "artifacts copied")
