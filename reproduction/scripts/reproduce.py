#!/usr/bin/env python3
"""Fresh, independent reproduction of the GSMG solved chain and the published
fixed community recipes (brief §8.1). Writes reproduction/results/.

Inputs are read only from sources/ (the raw upstream imports); every input is
recorded with its repo@commit:path. Two implementations are used where the
operation allows it (Python vs. OpenSSL CLI / iconv / Python cp273 codec).

No keyspace or candidate search is performed: each step evaluates one
published recipe (the Cosmic step evaluates the four password/digest
encodings of the single published key, to pin down which one the prior
report meant by "raw-password/MD5").

Run from anywhere:  python3 reproduction/scripts/reproduce.py
"""
import collections, hashlib, json, os, re, subprocess, sys, tempfile

import numpy as np
from PIL import Image

sys.path.insert(0, os.path.dirname(__file__))
import gsmglib as g  # noqa: E402

A, B, C = "fb92dd15487c6e2d275adb8c923698b7166c328e", "9e61693404ef74e8e681598116d371924f399ffa", "caaa77a8c218e97f9fdaae8908d580e51118edec"
CIT = {"puzzlehunt": f"A@{A[:7]}", "naddiseo": f"B@{B[:7]}", "hosterjack": f"C@{C[:7]}"}
OUT = os.path.join(g.REPO, "reproduction", "results")
os.makedirs(OUT, exist_ok=True)
RESULTS = []


def cite(path):
    repo = path.split("/", 1)[0]
    return f"{CIT.get(repo, repo)}:{path.split('/', 1)[1]}"


def rec(step, *, inputs, params, outputs, prior=None, impls=None, note=""):
    """Append one result record; status = confirmed / discrepancy / new (no prior value)."""
    status = "new"
    if prior is not None:
        status = "confirmed" if all(outputs.get(k) == v for k, v in prior.items()) else "discrepancy"
    if impls is not None and not all(impls.values()):
        status = "discrepancy"
    r = dict(step=step, status=status, inputs=inputs, params=params, outputs=outputs,
             prior_report=prior, implementations_agree=impls, note=note)
    RESULTS.append(r)
    print(f"[{status:11}] {step}")
    return r


def save(name, data):
    p = os.path.join(OUT, name)
    open(p, "wb").write(data if isinstance(data, bytes) else data.encode())
    return f"reproduction/results/{name}"


# ======================================================================== 1. grid
def step_grid():
    path = "puzzlehunt/puzzle.png"
    im = np.array(Image.open(g.src(path)).convert("RGB"))
    cells, counts = [], collections.Counter()
    for r in range(14):
        row = []
        for c in range(14):
            blk = im[r * 75:min(r * 75 + 75, 1048), c * 75:min(c * 75 + 75, im.shape[1])].reshape(-1, 3)
            col = collections.Counter(map(tuple, blk)).most_common(1)[0][0]
            row.append(col); counts[col] += 1
        cells.append(row)
    names = {(0, 0, 0): "black", (255, 255, 255): "white", (63, 72, 204): "blue", (255, 242, 0): "yellow", (254, 254, 254): "FEFEFE"}
    bit = {"black": 1, "blue": 1, "white": 0, "yellow": 0, "FEFEFE": 0}
    grid = [[bit[names[x]] for x in row] for row in cells]
    # counter-clockwise spiral from top-left, first move down
    seen = [[False] * 14 for _ in range(14)]; order = []; r = c = 0; dr, dc = 1, 0
    for _ in range(196):
        order.append((r, c)); seen[r][c] = True
        nr, nc = r + dr, c + dc
        if not (0 <= nr < 14 and 0 <= nc < 14 and not seen[nr][nc]):
            dr, dc = -dc, dr; nr, nc = r + dr, c + dc
        r, c = nr, nc
    bits = "".join(str(grid[r][c]) for r, c in order)
    text = bytes(int(bits[i:i + 8], 2) for i in range(0, 192, 8)).decode()
    fe = [(r, c) for r in range(14) for c in range(14) if names[cells[r][c]] == "FEFEFE"]
    sp = {rc: i for i, rc in enumerate(order)}
    colored = sorted(sp[(r, c)] for r in range(14) for c in range(14) if names[cells[r][c]] in ("blue", "yellow"))
    color_bits = "".join("1" if names[cells[order[i][0]][order[i][1]]] == "blue" else "0" for i in colored)
    lsb = "".join(str(ord(ch) & 1) for ch in text)
    rec("grid_14x14_to_url",
        inputs={"image": cite(path), "image_sha256": g.sha256(open(g.src(path), "rb").read())},
        params={"cell_px": 75, "cell_value": "modal RGB", "1": "black,blue", "0": "white,yellow,FEFEFE",
                "spiral": "start top-left, first move down, counter-clockwise", "bit_order": "MSB-first"},
        outputs={"url": text, "residual_bits": bits[192:], "ones": sum(map(sum, grid)),
                 "row_sums": [sum(r) for r in grid], "col_sums": [sum(grid[r][c] for r in range(14)) for c in range(14)],
                 "palette_counts": {names[k]: v for k, v in counts.items()},
                 "FEFEFE_cell_rc_zero_based": fe, "FEFEFE_spiral_index_zero_based": [sp[x] for x in fe],
                 "FEFEFE_rowmajor_index_zero_based": [r * 14 + c for r, c in fe],
                 "colored_spiral_idx_all_7_mod_8": all(i % 8 == 7 for i in colored),
                 "colored_bits_equal_url_lsbs": color_bits == lsb, "n_colored": len(colored)},
        prior={"url": "gsmg.io/theseedisplanted", "residual_bits": "0000", "ones": 101,
               "row_sums": [6, 10, 8, 7, 6, 6, 5, 4, 9, 9, 7, 8, 7, 9],
               "col_sums": [8, 10, 8, 10, 8, 7, 3, 6, 7, 5, 9, 6, 6, 8],
               "palette_counts": {"black": 86, "white": 85, "blue": 15, "yellow": 9, "FEFEFE": 1},
               "FEFEFE_cell_rc_zero_based": [(7, 4)]},
        note="Prior report §5.2 gives spiral index 163 (zero-based) for FEFEFE.")
    return text


# ======================================================================== 2. AES stages
SEVEN = ("causality" "Safenet" "Luna" "HSM" "11110"
         "0x" + "The Times 03/Jan/2009 Chancellor on brink of second bailout for banks"[::-1].encode().hex().upper()
         + "B5KR/1r5B/2R5/2b1p1p1/2P1k1P1/1p2P2p/1P2P2P/3N1N2 b - - 0 1")
STAGES = [
    ("phase2", "naddiseo/phase2-assets/phase2_aes.txt", "causality",
     "eb3efb5151e6255994711fe8f2264427ceeebf88109e1d7fad5b0a8b6d07e5bf", "e2f9dd65604a3231f8b3301724e8d713a88fffc4b6c7c4aeeb20f58a582b593a", 648),
    ("phase3", "naddiseo/phase2-assets/phase3_aes.txt", SEVEN,
     "1a57c572caf3cf722e41f5f9cf99ffacff06728a43032dd44c481c77d2ec30d5", "c4ad94559a44a927c1032cc0e024515f9510a0806a2d14458dbf4a360af9865f", 4090),
    ("phase32", "naddiseo/phase3-assets/phase3.2-aes.txt", "jacquefrescogiveitjustonesecondheisenbergsuncertaintyprinciple",
     "250f37726d6862939f723edc4f993fde9d33c6004aab4f2203d9ee489d61ce4c", "b82afeb86f9e50848220f9b64b744b821400308aea273a1c949b9d2d0e408a34", 2422),
]


def step_aes():
    pts = {}
    for name, path, ans, pw_prior, out_prior, n_prior in STAGES:
        b64 = open(g.src(path)).read()
        raw, salt, ct = g.parse_envelope(b64)
        pw = g.sha256(ans.encode())
        py = g.aes_decrypt(b64, pw.encode(), "sha256")
        ossl = g.openssl_decrypt(b64, pw.encode(), "sha256")
        wrong_md5 = g.aes_decrypt(b64, pw.encode(), "md5")
        wrong_raw = g.aes_decrypt(b64, bytes.fromhex(pw), "sha256")
        pts[name] = py
        rec(f"aes_{name}",
            inputs={"envelope": cite(path), "envelope_sha256": g.sha256(raw), "answer": ans, "answer_chars": len(ans)},
            params={"password": "lowercase hex of SHA-256(UTF-8 answer)", "kdf": "EVP_BytesToKey, 1 iteration, SHA-256",
                    "cipher": "AES-256-CBC", "padding": "strict PKCS#7", "salt": salt.hex(), "ciphertext_bytes": len(ct)},
            outputs={"password_hex": pw, "plaintext_bytes": len(py), "plaintext_sha256": g.sha256(py),
                     "plaintext_file": save(f"{name}_plaintext.bin", py),
                     "control_md5_kdf_valid_padding": wrong_md5 is not None,
                     "control_raw_digest_password_valid_padding": wrong_raw is not None},
            prior={"password_hex": pw_prior, "plaintext_sha256": out_prior, "plaintext_bytes": n_prior},
            impls={"python": True, "openssl_cli_equal": ossl == py})
    # upstream plaintext files vs our output
    for name, path in [("phase2", "naddiseo/phase2-assets/phase2.1.txt"), ("phase3", "naddiseo/phase2-assets/phase3.txt"),
                       ("phase32", "naddiseo/phase3-assets/phase3.2.txt"), ("phase2", "hosterjack/assets/walkthrough/phase2-assets/phase2.1.txt"),
                       ("phase3", "hosterjack/assets/walkthrough/phase2-assets/phase3.txt"), ("phase32", "hosterjack/assets/walkthrough/phase3-assets/phase3.2.txt")]:
        up = open(g.src(path), "rb").read()
        rec(f"upstream_plaintext_check:{path}", inputs={"file": cite(path), "sha256": g.sha256(up), "bytes": len(up)},
            params={"compare_to": f"aes_{name} output"},
            outputs={"byte_identical": up == pts[name],
                     "identical_after_CRLF_to_LF": up == pts[name].replace(b"\r\n", b"\n"),
                     "identical_after_CRLF_to_LF_and_strip": up.strip() == pts[name].replace(b"\r\n", b"\n").strip()})
    # ciphertext copies in Hosterjack
    for name, path in [("phase2", "hosterjack/ciphertexts/phase2.txt"), ("phase3", "hosterjack/ciphertexts/phase3.txt"), ("phase32", "hosterjack/ciphertexts/phase32.txt")]:
        ref = [s for s in STAGES if s[0] == name][0][1]
        same = g.parse_envelope(open(g.src(path)).read())[0] == g.parse_envelope(open(g.src(ref)).read())[0]
        rec(f"envelope_copy_check:{path}", inputs={"file": cite(path), "reference": cite(ref)}, params={},
            outputs={"decoded_envelope_identical": same})
    return pts


# ======================================================================== 3. EBCDIC + Beaufort, checkerboard
def step_phase32(pt):
    seg = pt[447:1986]
    # implementation 1: GNU iconv LATIN1 -> IBM1141
    with tempfile.NamedTemporaryFile() as f:
        f.write(seg); f.flush()
        r = subprocess.run(["iconv", "-f", "LATIN1", "-t", "IBM1141", f.name], capture_output=True)
    e1 = r.stdout if r.returncode == 0 else None
    # implementation 2: Python cp273 codec (CP1141 = CP273 + euro; no euro sign occurs in Latin-1 input)
    e2 = seg.decode("latin1").encode("cp273")
    letters = e1.decode("latin1")
    key = "thematrixhasyou"
    plain = "".join(chr(97 + (ord(key[i % 15]) - ord(ch)) % 26) for i, ch in enumerate(letters))
    rec("phase32_ebcdic1141_beaufort",
        inputs={"plaintext": "aes_phase32 output", "slice": "[447:1986]"},
        params={"step1": "bytes as Latin-1 characters, encode to CP1141", "step2": "Beaufort p=(k-c) mod 26", "key": key},
        outputs={"ebcdic_all_lowercase": bool(re.fullmatch(r"[a-z]+", letters)), "letters": len(letters),
                 "speech_sha256": g.sha256(plain.encode()), "speech_head": plain[:40], "speech_tail": plain[-20:],
                 "speech_file": save("phase32_speech.txt", plain)},
        prior={"letters": 1539}, impls={"iconv_IBM1141": e1 is not None, "python_cp273_equal": e1 == e2})
    # straddling checkerboard
    txt = pt.decode("latin1")
    digits = max(re.findall(r"\d{100,}", txt), key=len)
    alpha = "fubcdora/lethingkymvpszjqwx."
    top = dict(zip([0, 2, 3, 5, 6, 7, 8, 9], alpha[:8]))
    rows = {1: alpha[8:18], 4: alpha[18:28]}
    out, i = [], 0
    while i < len(digits):
        d = int(digits[i])
        if d in rows:
            out.append(rows[d][int(digits[i + 1])]); i += 2
        else:
            out.append(top[d]); i += 1
    sentence = "".join(out)
    rec("phase32_straddling_checkerboard",
        inputs={"plaintext": "aes_phase32 output", "digits": digits, "n_digits": len(digits)},
        params={"alphabet": alpha, "blank_top_row_columns": [1, 4], "top_row": top, "row1": rows[1], "row4": rows[4]},
        outputs={"sentence": sentence, "letters": len(sentence)},
        prior={"letters": 91})
    RESULTS[-1]["prior_report"]["n_digits"] = 149
    if len(digits) != 149: RESULTS[-1]["status"] = "discrepancy"
    trailing = txt[txt.index("U2FsdGVkX1"):]
    return trailing


# ======================================================================== 4. audio
def step_audio():
    path = "naddiseo/decentraland-assets/puzzlepiece.mp3"
    with tempfile.TemporaryDirectory() as td:
        wav = os.path.join(td, "a.raw")
        subprocess.run(["ffmpeg", "-loglevel", "error", "-i", g.src(path), "-f", "s16le", "-ac", "2", "-ar", "44100", wav], check=True)
        x = np.frombuffer(open(wav, "rb").read(), dtype="<i2").reshape(-1, 2).astype(float)
    d = x[:, 0] - x[:, 1]
    import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
    fig, ax = plt.subplots(figsize=(24, 6), dpi=100)
    ax.specgram(d, NFFT=2048, Fs=44100, noverlap=1536, cmap="gray_r"); ax.set_ylim(0, 22050)
    fig.savefig(os.path.join(OUT, "audio_LminusR_spectrogram.png"), bbox_inches="tight"); plt.close(fig)
    hexs = "48 41 53 48 54 48 45 54 45 58 54"
    rec("audio_LminusR_spectrogram",
        inputs={"audio": cite(path), "sha256": g.sha256(open(g.src(path), "rb").read())},
        params={"decode": "ffmpeg -> s16le 44.1 kHz stereo", "signal": "left - right", "spectrogram": "NFFT 2048, overlap 1536"},
        outputs={"samples": int(len(d)), "rms_L": float(np.sqrt((x[:, 0] ** 2).mean())), "rms_LminusR": float(np.sqrt((d ** 2).mean())),
                 "spectrogram_png": "reproduction/results/audio_LminusR_spectrogram.png",
                 "visual_reading_hex": hexs, "visual_reading_ascii": bytes.fromhex(hexs.replace(" ", "")).decode()},
        prior={"visual_reading_ascii": "HASHTHETEXT"},
        note="Read by eye from the rendered PNG on 2026-10-15: 48 41 53 48 54 48 45 5? 4 45 58 54. The 8th group sits under a broadband transient at ~3.4 s; its first digit is only partly visible, so '54' there rests on a partial glyph plus context. Visual, not programmatic, check.")


# ======================================================================== 5. SalPhaseIon
def soup_text():
    path = "naddiseo/salphaseion.ipynb"
    nb = json.load(open(g.src(path)))
    cell = "".join(nb["cells"][0]["source"])
    body = cell.split("```")[1].strip()
    return path, body.replace(" ", "").replace("\n", "")


def ab(s):
    bits = s.replace("a", "0").replace("b", "1")
    return bytes(int(bits[i:i + 8], 2) for i in range(0, len(bits), 8)).decode()


def zdec(s):
    n = int(s.translate(str.maketrans("abcdefghio", "1234567890")))
    return n.to_bytes((n.bit_length() + 7) // 8, "big").decode()


def step_salphaseion():
    entry = "GSMGIO5BTCPUZZLECHALLENGE1GSMG1JC9wtdSwfwApgj2xcmJPAwx7prBe"
    rec("salphaseion_entry_hash", inputs={"text": entry, "chars": len(entry)}, params={"hash": "SHA-256 of UTF-8"},
        outputs={"sha256": g.sha256(entry.encode())},
        prior={"sha256": "89727c598b9cd1cf8873f27cb7057f050645ddb6a7a157a110239ac0152f6a32"})
    path, s = soup_text()
    m = re.match(r"([a-i]+?)((?:[ab]){104})([a-i]+)z([a-io]+)z([a-io]+)z(shabef.*?)(U2Fsd.*)$", s)
    dbbi, abblk, faed, z1, z2, z3, rest = m.groups()
    enter = re.search(r"abbaababab.{30}", rest).group(0)
    b64a, b64b = rest.split(enter)
    tail_marker = re.search(r"shabefanstoo$", b64b).group(0)
    inner_b64 = b64a + b64b[:-len(tail_marker)]
    hj = g.parse_envelope(open(g.src("hosterjack/ciphertexts/salph_inner.txt")).read())[0]
    rec("salphaseion_soup_sections",
        inputs={"soup": cite(path) + " cell 0", "soup_chars_no_spaces": len(s), "soup_sha256": g.sha256(s.encode())},
        params={"split": "regex: a-i run | 104-char a/b block | a-i run | z | z | z | shabef… | base64"},
        outputs={"dbbi_len": len(dbbi), "dbbi_offsets": [0, len(dbbi)], "dbbi_sha256": g.sha256(dbbi.encode()),
                 "ab_block_offsets": [len(dbbi), len(dbbi) + 104], "matrixsumlist": ab(abblk),
                 "faed_len": len(faed), "faed_offsets": [195, 195 + len(faed)], "faed_sha256": g.sha256(faed.encode()),
                 "faed_counts": dict(sorted(collections.Counter(faed).items())),
                 "dbbi_has_o": "o" in dbbi, "dbbi_first_occurrence": "".join(dict.fromkeys(dbbi)).upper(),
                 "z1": zdec(z1), "z2": zdec(z2), "z3_text": z3, "inner_insertion": ab(enter),
                 "inner_b64_halves": [len(b64a), len(b64b) - len(tail_marker)], "trailing_text": tail_marker,
                 "inner_envelope_equals_hosterjack_salph_inner": g.parse_envelope(inner_b64)[0] == hj,
                 "inner_salt": g.parse_envelope(inner_b64)[1].hex(), "inner_ct_bytes": len(g.parse_envelope(inner_b64)[2]),
                 "dbbi_file": save("dbbi.txt", dbbi), "faed_file": save("faed.txt", faed)},
        prior={"dbbi_len": 91, "faed_len": 570, "matrixsumlist": "matrixsumlist", "z1": "lastwordsbeforearchichoice",
               "z2": "thispassword", "inner_insertion": "enter", "dbbi_first_occurrence": "DBIFHCEGA", "dbbi_has_o": False,
               "faed_counts": {"a": 54, "b": 49, "c": 52, "d": 49, "e": 69, "f": 57, "g": 107, "h": 58, "i": 75},
               "inner_salt": "3ab585348552415d", "inner_ct_bytes": 80})
    return dbbi, faed, inner_b64


# ======================================================================== 6. 2023 hint
def step_hint2023():
    path = "hosterjack/content/sowut-data.js"
    js = open(g.src(path), encoding="utf-8").read()
    data = json.loads(js[js.index("{"):js.rindex("}") + 1])
    msg = [m for m in data["messages"] if m["id"] == 8446][0]
    groups = msg["text"].split()
    bits = "".join(groups)[::-1]
    out = bytes(int(bits[i:i + 8], 2) for i in range(0, len(bits), 8)).decode()
    alt = bytes(int(gp[::-1], 2) for gp in reversed(groups)).decode()
    rec("hint_2023_reverse_binary",
        inputs={"dataset": cite(path) + " message id 8446", "date": msg["date"], "groups": len(groups)},
        params={"rule": "reverse the entire bit string, group by 8, ASCII"},
        outputs={"text": out, "bytes": len(out), "sha256": g.sha256(out.encode()), "equivalent_rule_agrees": alt == out},
        prior={"text": "yellowblueprimesmatrixsumlistlastwordsbeforearchichoiceyinyangwewontgiveawaythepassworditsinfrontofyoureyesbutyourenotseeingitverylaststepisatruegiveawaypromised", "bytes": 161})
    nyb = None
    # 2026 New Year hint (transcription in Naddiseo README)
    rd = open(g.src("naddiseo/README.md"), encoding="utf-8").read()
    mm = re.search(r"Copyable:\n> ([01 ]+)", rd)
    if mm:
        nyb = bytes(int(x, 2) for x in mm.group(1).split()).decode()
        rec("hint_2026_new_year_binary", inputs={"transcription": cite("naddiseo/README.md") + " §2026-01-01"},
            params={"rule": "8-bit groups, MSB-first ASCII (no reversal)"}, outputs={"text": nyb},
            prior=None, note="prior report: 'decode is conventional ASCII'")


# ======================================================================== 7. Naddiseo #17 chain
def step_chain12(inner_b64, trailing_b64):
    pw1 = "matrixsumlistenterlastwordsbeforearchichoicethispasswordmatrixsumlist"
    c1 = g.aes_decrypt(inner_b64, pw1.encode(), "md5")
    c1o = g.openssl_decrypt(inner_b64, pw1.encode(), "md5")
    wif = g.wif_uncompressed(c1[:32])
    hj = g.parse_envelope(open(g.src("hosterjack/ciphertexts/p32_trailing.txt")).read())[0]
    c2 = g.aes_decrypt(trailing_b64, wif.encode(), "md5")
    c2o = g.openssl_decrypt(trailing_b64, wif.encode(), "md5")
    a1 = g.p2pkh(g.ser(g.point_mul(int.from_bytes(c2[:32], "big")), False))
    a2 = g.p2pkh(g.ser(g.point_mul(int.from_bytes(c2[32:64], "big")), False))
    rec("naddiseo17_chain1_salph_inner",
        inputs={"envelope": "salph_inner reconstructed from soup (== C:ciphertexts/salph_inner.txt)", "password": pw1},
        params={"password": "raw UTF-8 literal", "kdf": "EVP_BytesToKey MD5", "cipher": "AES-256-CBC", "padding": "strict PKCS#7"},
        outputs={"bytes": len(c1), "sha256": g.sha256(c1), "E_C": c1[64:79].hex(), "file": save("chain1.bin", c1)},
        prior={"bytes": 79, "sha256": "1449a2178eea7c0e3fabac8c1ad2afa294be4fc1800c594a025a056e88c626bf", "E_C": "38d4f4c90cb45fdfc8cff50d0ed1c5"},
        impls={"python": True, "openssl_cli_equal": c1 == c1o})
    rec("naddiseo17_chain2_p32_trailing",
        inputs={"envelope": "tail of aes_phase32 plaintext", "envelope_equals_hosterjack_p32_trailing": g.parse_envelope(trailing_b64)[0] == hj,
                "password": "WIF text derived from chain1[0:32]"},
        params={"wif": "mainnet 0x80 prefix, no compression flag, Base58Check", "kdf": "EVP_BytesToKey MD5", "cipher": "AES-256-CBC"},
        outputs={"wif_password": wif, "bytes": len(c2), "sha256": g.sha256(c2), "K_S1": c2[:32].hex(), "K_S2": c2[32:64].hex(),
                 "E_S": c2[64:79].hex(), "addr_K_S1_uncompressed": a1, "addr_K_S2_uncompressed": a2, "file": save("chain2.bin", c2)},
        prior={"wif_password": "5K2byJMssxFKuTgnk9YQjpBz5FhkwwF2LaZoAyTus8HjGEpz8AT", "bytes": 79,
               "sha256": "b40fce72ef5638e4f79b3233e653f8a5dbdb0d4ae2009d2d3da2c98b70f4d004",
               "K_S1": "b06fa6f20561756c865dac7190f063480a371e4a13206e529ee7e9078f309c4b",
               "K_S2": "b11d211ca0a17cd68c580308f3e6f21d3f935c8da3c4373b6f73ab5ccfaea597",
               "E_S": "740a25de4b8e946d0a5ae2667a23a2",
               "addr_K_S1_uncompressed": "1MixpoELBvfkFSRUQtDCGXbdG53cjqknZT", "addr_K_S2_uncompressed": "176ysPe7FdevdQjZWaFCK2nnVbzX9Tgydy"},
        impls={"python": True, "openssl_cli_equal": c2 == c2o},
        note="The WIF is a published puzzle intermediate (A#68 comment 3704010992; B#17) used only as an AES password string; it is not imported into any wallet.")
    return c1, c2


# ======================================================================== 8. Cosmic + chain 4
def step_cosmic(c1, c2):
    path = "hosterjack/ciphertexts/cosmic.txt"
    b64 = open(g.src(path)).read()
    raw, salt, ct = g.parse_envelope(b64)
    toks = ["matrixsumlist", "enter", "lastwordsbeforearchichoice", "thispassword", "matrixsumlist", "yourlastcommand", "secondanswer"]
    x = bytes(32)
    for t in toks:
        x = bytes(a ^ b for a, b in zip(x, hashlib.sha256(t.encode()).digest()))
    x5 = bytes(32)
    for t in toks[1:4] + toks[5:]:
        x5 = bytes(a ^ b for a, b in zip(x5, hashlib.sha256(t.encode()).digest()))
    variants = {}
    for pwname, pw in [("raw32", x), ("hex64", x.hex().encode())]:
        for md in ("md5", "sha256"):
            o = g.aes_decrypt(b64, pw, md)
            variants[f"{pwname}/{md}"] = None if o is None else [len(o), g.sha256(o)]
    out = g.aes_decrypt(b64, x, "md5")
    outo = g.openssl_decrypt(b64, x, "md5")
    rec("cosmic_seven_token_xor",
        inputs={"envelope": cite(path), "envelope_sha256": g.sha256(raw), "tokens": toks,
                "recipe_source": "A#68 comment 3704010992; A:_pr68/GAP_ANALYSIS.md@27ea50e"},
        params={"key": "XOR of SHA-256 digests of the seven tokens", "password": "the 32 raw XOR bytes", "kdf": "EVP_BytesToKey MD5",
                "salt": salt.hex(), "ciphertext_bytes": len(ct)},
        outputs={"xor_key_hex": x.hex(), "xor_of_five_without_matrixsumlist_equal": x5 == x,
                 "encoding_variants": variants, "bytes": None if out is None else len(out),
                 "sha256": None if out is None else g.sha256(out), "first32": None if out is None else out[:32].hex(),
                 "file": None if out is None else save("cosmic_output.bin", out)},
        prior={"xor_key_hex": "a795de117e472590e572dc193130c763e3fb555ee5db9d34494e156152e50735", "bytes": 1327,
               "sha256": "4f7a1e4efe4bf6c5581e32505c019657cb7b030e90232d33f011aca6a5e9c081"},
        impls={"python": out is not None, "openssl_cli_equal": out == outo})
    # chain 4
    mystery = out[158:]
    body = mystery[:-1]
    mask = bytes.fromhex("b657264f2f6e6921")
    env = bytes(b ^ mask[i % 8] for i, b in enumerate(body))
    E_C, E_S, E_B = c1[64:79], c2[64:79], out[64:79]
    pw = E_C + E_S + E_B[:2]
    key, iv = g.evp_bytes_to_key(pw, env[8:16], "md5")
    from Crypto.Cipher import AES
    c4 = g.strict_unpad(AES.new(key, AES.MODE_CBC, iv).decrypt(env[16:])) if env[:8] == b"Salted__" else None
    import base64
    c4o = g.openssl_decrypt(base64.b64encode(env).decode(), pw, "md5")
    rec("chain4_masked_nested_envelope",
        inputs={"cosmic_output": "cosmic_seven_token_xor output", "offset": 158, "trim_last_byte": True, "mask": mask.hex(),
                "recipe_source": "A#68 comment 3704010992"},
        params={"password": "E_C || E_S || E_B[:2] (raw 32 bytes)", "kdf": "EVP_BytesToKey MD5"},
        outputs={"mystery_bytes": len(mystery), "unmasked_header": env[:8].decode("latin1"), "salt": env[8:16].hex(),
                 "masked_envelope_sha256": g.sha256(env), "masked_envelope_bytes": len(env),
                 "literal_Salted___in_cosmic_output": b"Salted__" in out, "password_hex": pw.hex(),
                 "bytes": None if c4 is None else len(c4), "sha256": None if c4 is None else g.sha256(c4),
                 "file": None if c4 is None else save("chain4.bin", c4),
                 "mask_equals_header_xor": bytes(a ^ b for a, b in zip(body[:8], b"Salted__")).hex() == mask.hex()},
        prior={"mystery_bytes": 1169, "unmasked_header": "Salted__", "salt": "5bbd88ac32481bca", "bytes": 1151,
               "password_hex": "38d4f4c90cb45fdfc8cff50d0ed1c5740a25de4b8e946d0a5ae2667a23a259cc",
               "sha256": "e4269ed5fbb202a81e5e1aa6b5190fdd1ea126b2c8547ea7cdbdf45387ea135b"},
        impls={"python": c4 is not None, "openssl_cli_equal": c4 == c4o},
        note="mask_equals_header_xor=True shows the 8-byte mask is exactly cosmic_output[158:166] XOR 'Salted__' — the header is forced by the mask choice.")


# ======================================================================== 9. Bifid
def step_bifid(dbbi, faed):
    sq = "".join(dict.fromkeys(dbbi.upper())) + "".join(ch for ch in "ABCDEFGHIKLMNOPQRSTUVWXYZ" if ch not in dbbi.upper())
    pos = {ch: divmod(i, 5) for i, ch in enumerate(sq)}
    q = [v for ch in faed.upper() for v in pos[ch]]
    n = len(faed)
    outp = "".join(sq[q[i] * 5 + q[i + n]] for i in range(n))
    inter = "".join(a + b for a, b in zip(faed[:285].upper(), faed[285:].upper()))
    q2 = []
    for i in range(0, len(inter), 2):
        pr = [v for ch in inter[i:i + 2] for v in pos[ch]]
        q2.append(sq[pr[0] * 5 + pr[2]] + sq[pr[1] * 5 + pr[3]])
    per2 = "".join(q2)
    even, odd = outp[0::2], outp[1::2]
    rec("bifid_full_period_faed",
        inputs={"faed": "soup FAED (570 letters)", "square_from": "first-occurrence order of DBBI + remaining alphabet, J omitted"},
        params={"square": sq, "direction": "decrypt", "coordinate_order": "row then column", "period": n},
        outputs={"square": sq, "bytes": len(outp), "sha256": g.sha256(outp.encode()), "head": outp[:7], "z_index_zero_based": [i for i, ch in enumerate(outp) if ch == "Z"],
                 "even_positions_alphabet": "".join(sorted(set(even))), "odd_positions_symbols_after_removing_I_O": len(set(odd) - {"I", "O"}),
                 "odd_positions_len_after_removing_I_O": len(odd.replace("I", "").replace("O", "")),
                 "period2_interleaved_identity": per2 == outp, "file": save("bifid_full.txt", outp)},
        prior={"square": "DBIFHCEGAKLMNOPQRSTUVWXYZ", "bytes": 570, "head": "BTCSEED",
               "sha256": "0c5d984f90e9baefc09f1d3888e62acbd101f9b0194887e2ae88fc6c9967745e", "z_index_zero_based": [97],
               "even_positions_alphabet": "BCDE", "odd_positions_symbols_after_removing_I_O": 23, "odd_positions_len_after_removing_I_O": 256,
               "period2_interleaved_identity": True})
    # b/c expansion lengths (Naddiseo#14 model)
    sub = {"a": "a", "b": "b", "c": "c", "d": "bb", "e": "bc", "f": "cc", "g": "bbc", "h": "bcc", "i": "ccc"}
    rec("bc_expansion_lengths", inputs={"dbbi": "soup DBBI", "faed": "soup FAED"}, params={"substitution": sub},
        outputs={"dbbi_expanded": len("".join(sub[c] for c in dbbi)), "faed_expanded": len("".join(sub[c] for c in faed))},
        prior={"dbbi_expanded": 169, "faed_expanded": 1225})


# ======================================================================== 10. prize key
def step_prize():
    pub = "04f4d1bbd91e65e2a019566a17574e97dae908b784b388891848007e4f55d5a4649c73d25fc5ed8fd7227cab0be4e576c0c6404db5aa546286563e4be12bf33559"
    b = bytes.fromhex(pub); pt = (int.from_bytes(b[1:33], "big"), int.from_bytes(b[33:], "big"))
    # ground the point in a spend transaction stored in the sources (Naddiseo PR #15 materials)
    txp = "naddiseo/_pr15/neo/materials/chain/tx_halving_spend.hex"
    tx = open(g.src(txp)).read().strip().lower()
    rec("prize_pubkey_to_address",
        inputs={"pubkey_uncompressed": pub, "pubkey_source": "prior report §11; also present in " + cite(txp)},
        params={"address": "HASH160 -> version 0x00 -> Base58Check"},
        outputs={"on_curve": g.on_curve(pt), "address_uncompressed": g.p2pkh(b), "address_compressed": g.p2pkh(g.ser(pt, True)),
                 "occurrences_in_spend_tx_hex": tx.count(pub)},
        prior={"on_curve": True, "address_uncompressed": "1GSMG1JC9wtdSwfwApgj2xcmJPAwx7prBe", "address_compressed": "1cc6xayvqpeetixmuXDRsGug7GKyoRdxP"})


def step_crib_control():
    """Is the chain-4 mask a clue-derived rule or a crib fit? Apply the same offset-158 'Salted__' crib
    to an unrelated 1-byte-pad Cosmic decrypt shipped in B PR #15 and compare with the shipped file."""
    d = "naddiseo/_pr15/unverified/drive-2026-05/"
    ca = open(g.src(d + "cosmic_A.bin"), "rb").read()
    hid = open(g.src(d + "ca158_hidden_blob.bin"), "rb").read()
    c4f = open(g.src(d + "chain4_final.bin"), "rb").read()
    mask = bytes(a ^ b for a, b in zip(ca[158:166], b"Salted__"))
    unmasked = bytes(b ^ mask[i % 8] for i, b in enumerate(ca[158:158 + len(hid)]))
    rec("chain4_crib_control_cosmic_A",
        inputs={"cosmic_A": cite(d + "cosmic_A.bin"), "cosmic_A_sha256": g.sha256(ca), "cosmic_A_bytes": len(ca),
                "ca158_hidden_blob": cite(d + "ca158_hidden_blob.bin"), "chain4_final": cite(d + "chain4_final.bin")},
        params={"rule": "mask = X[158:166] XOR 'Salted__', applied repeating to X[158:]"},
        outputs={"crib_mask_hex": mask.hex(), "ca158_equals_masked_cosmic_A": unmasked == hid, "ca158_bytes": len(hid),
                 "ca158_header": hid[:8].decode("latin1"), "ca158_salt": hid[8:16].hex(),
                 "chain4_final_sha256": g.sha256(c4f)},
        prior=None,
        note="Same crib recipe on a different padding-valid Cosmic decrypt yields a different well-formed 'Salted__' envelope; the header is manufactured by the mask choice. Observation first reported by extraction agent N4 from B PR #15 files; verified here.")


def step_page_provenance():
    """Do the notebook soup, the PR #15 primary soup and the archived SalPhaseIon pages agree, and does the
    page's Cosmic textarea equal C:ciphertexts/cosmic.txt? (byte comparisons only)"""
    import html as _html
    _, nb = soup_text()
    prim = open(g.src("naddiseo/_pr15/neo/materials/primary/salphaseion_soup_space_separated.txt"), encoding="utf-8").read()
    cos = g.parse_envelope(open(g.src("hosterjack/ciphertexts/cosmic.txt")).read())[0]
    out = {"primary_soup_sha256": g.sha256(prim.encode()), "primary_equals_notebook_after_space_strip": "".join(prim.split()) == nb}
    for name in ("salphaseion_2024-11-23.html", "salphaseion_2025-10-31.html"):
        page = open(g.src("naddiseo/_pr15/neo/materials/wayback/pages/" + name), encoding="utf-8", errors="replace").read()
        tas = [_html.unescape(t) for t in re.findall(r"<textarea[^>]*>(.*?)</textarea>", page, re.S | re.I)]
        out[name] = {"textareas": len(tas),
                     "soup_textarea_equals_primary": any(t == prim or t.strip() == prim.strip() for t in tas),
                     "soup_textarea_equals_notebook_after_space_strip": any("".join(t.split()) == nb for t in tas),
                     "cosmic_textarea_equals_cosmic_txt": any(t.strip().startswith("U2Fsd") and g.parse_envelope(t)[0] == cos for t in tas),
                     "h1": re.findall(r"<h1[^>]*>(.*?)</h1>", page, re.S | re.I)}
    rec("salphaseion_page_provenance",
        inputs={"notebook_soup": cite("naddiseo/salphaseion.ipynb"), "primary_soup": cite("naddiseo/_pr15/neo/materials/primary/salphaseion_soup_space_separated.txt"),
                "wayback_pages": cite("naddiseo/_pr15/neo/materials/wayback/pages/") + " (captures 20241123015038, 20251031153559 per INDEX.tsv)",
                "cosmic": cite("hosterjack/ciphertexts/cosmic.txt")},
        params={"comparison": "exact bytes after HTML unescape; soup also compared with all whitespace removed"},
        outputs=out, prior=None,
        note="Captures are as supplied in B PR #15 (user-uploaded Wayback dump); this archive did not refetch them from archive.org.")


def step_cosmic_set_a():
    """A#62/A#69 publish a different seven-token set ('Set A') and claim the same Cosmic output."""
    path = "hosterjack/ciphertexts/cosmic.txt"
    b64 = open(g.src(path)).read()
    toks = ["matrixsumlist", "enter", "lastwordsbeforearchichoice", "thispassword", "matrixsumlist", "sha256", "theone"]
    x = bytes(32)
    for t in toks:
        x = bytes(a ^ b for a, b in zip(x, hashlib.sha256(t.encode()).digest()))
    variants = {}
    for pwname, pw in [("raw32", x), ("hex64", x.hex().encode())]:
        for md in ("md5", "sha256"):
            o = g.aes_decrypt(b64, pw, md)
            variants[f"{pwname}/{md}"] = None if o is None else [len(o), g.sha256(o)]
    rec("cosmic_seven_token_xor_set_A",
        inputs={"envelope": cite(path), "tokens": toks, "recipe_source": "A#62 comment 3432403162; A#69 body"},
        params={"key": "XOR of SHA-256 digests", "encodings_tested": ["raw32", "hex64"], "kdfs_tested": ["md5", "sha256"]},
        outputs={"xor_key_hex": x.hex(), "encoding_variants": variants,
                 "any_variant_gives_4f7a1e4e": any(v and v[1].startswith("4f7a1e4e") for v in variants.values())},
        prior={"xor_key_hex": "818af53daa3028449f125a2e4f47259ddf9b9d86e59ce6c4993a67ffd76bb402"},
        note="Prior value = key published in A#69. A null entry means invalid padding.")


def step_a15_controls(inner_b64):
    """A#15 (eazytest, Aug 2023): two published passwords that open salph_inner and cosmic with valid padding.
    A control showing padding-valid outputs of the same lengths arise from unrelated recipes."""
    cos_b64 = open(g.src("hosterjack/ciphertexts/cosmic.txt")).read()
    out = {}
    for name, b64, pw in [("salph_inner", inner_b64, "26770c535632f626daefc0736dd4f85fd6126f647e6a160a2b58c51c0693d40f"),
                          ("cosmic", cos_b64, "93de0175aa3d0a6a2768ba650009a35a36530fa31898da6f3c46757a693f108f")]:
        for md in ("sha256", "md5"):
            o = g.aes_decrypt(b64, pw.encode(), md)
            out[f"{name}/{md}"] = None if o is None else {"bytes": len(o), "sha256": g.sha256(o), "head16": o[:16].hex(), "pad": 80 - len(o) if name == "salph_inner" else 1328 - len(o)}
    rec("a15_padding_controls",
        inputs={"recipe_source": "A#15 comments 1674478225 (2023-08-11), 1668268853 (2023-08-07)",
                "salph_inner_password": "26770c535632f626daefc0736dd4f85fd6126f647e6a160a2b58c51c0693d40f (stated = SHA-256 of 'MatrixSumlist AnsToo')",
                "cosmic_password": "93de0175aa3d0a6a2768ba650009a35a36530fa31898da6f3c46757a693f108f (stated = SHA-256 of reversed printable salph_inner output)"},
        params={"password": "64-char hex string as typed into openssl -pass pass:", "kdfs_tested": ["sha256", "md5"]},
        outputs=out, prior=None,
        note="Source states the cosmic output begins 5d2ec2af4c2f9dfb191fce6a70e4a75a. Neither prior report nor any later recipe treats these as stages; they are recorded as independent padding-valid controls.")


def step_103x103(cos):
    """A#72/A#79/A#81: 103x103 bit matrix of the Cosmic output -> shifted row+col sums -> base-38 -> 68 bytes."""
    bits = "".join(f"{b:08b}" for b in cos)[:103 * 103]
    m = [[int(bits[r * 103 + c]) for c in range(103)] for r in range(103)]
    rs = [sum(r) for r in m]; cs = [sum(m[r][c] for r in range(103)) for c in range(103)]
    sec = [rs[i] + cs[(i + 7) % 103] for i in range(103)]
    n = 0
    for v in sec:
        n = n * 38 + (v - 80)
    out = n.to_bytes((n.bit_length() + 7) // 8, "big")
    half, better, trail = out[:32], out[32:64], out[64:]
    addrs = {}
    for nm, k in (("half", half), ("better_half", better)):
        P = g.point_mul(int.from_bytes(k, "big"))
        addrs[nm] = {"uncompressed": g.p2pkh(g.ser(P, False)), "compressed": g.p2pkh(g.ser(P, True))}
    rec("cosmic_103x103_base38",
        inputs={"cosmic_output": "cosmic_seven_token_xor output (4f7a1e4e…)", "recipe_source": "A#72 body; A#79 body; A#81 body"},
        params={"bits": "first 10,609 bits MSB-first, row-major 103x103", "secondary": "row_sum[i] + col_sum[(i+7) mod 103]",
                "digit": "value - 80", "base": 38, "split": "32 + 32 + rest"},
        outputs={"secondary_string": "".join(chr(v) for v in sec), "secondary_min_max": [min(sec), max(sec)], "bytes": len(out),
                 "half_prefix": half[:4].hex(), "better_half_prefix": better[:4].hex(), "trail": trail.hex(),
                 "addresses": addrs, "prize_address_match": any(a == "1GSMG1JC9wtdSwfwApgj2xcmJPAwx7prBe" for d in addrs.values() for a in d.values())},
        prior=None,
        note="Prior report §6 listed this as not reproduced. Published values to compare: half 0423d911…, better half 48cc46e6…, trail fc0c1b02, addresses 1JG648ya…/15E3pcDD…/1FhbJnrd…/145ZQ9si… (A#72, A#79). The 32-byte values are already public; addresses are derived only for comparison with the published ones and the prize address. Shift 7, offset 80, base 38 and the split are discretionary choices made after inspecting the bytes.")


if __name__ == "__main__":
    step_grid()
    pts = step_aes()
    trailing = step_phase32(pts["phase32"])
    step_audio()
    dbbi, faed, inner = step_salphaseion()
    step_hint2023()
    c1, c2 = step_chain12(inner, trailing)
    step_cosmic(c1, c2)
    step_bifid(dbbi, faed)
    step_prize()
    step_crib_control()
    step_page_provenance()
    step_cosmic_set_a()
    step_a15_controls(inner)
    step_103x103(open(os.path.join(OUT, "cosmic_output.bin"), "rb").read())
    summary = collections.Counter(r["status"] for r in RESULTS)
    doc = {"generated_utc": __import__("datetime").datetime.now(__import__("datetime").timezone.utc).isoformat(timespec="seconds"),
           "script": "reproduction/scripts/reproduce.py", "source_commits": {"A": A, "B": B, "C": C},
           "summary": dict(summary), "results": RESULTS}
    json.dump(doc, open(os.path.join(OUT, "reproduction_results.json"), "w"), indent=1, ensure_ascii=False, default=list)
    print(dict(summary))
