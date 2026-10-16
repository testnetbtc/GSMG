# reproduction/results/ -- what each file is, and why some look like garbage on GitHub

Every file here is written by `reproduction/scripts/reproduce.py` from the raw
artifacts in `sources/`. Files ending in `.bin` are **binary**: GitHub cannot
display them as text, and before this note it tried to, producing a screen of
Chinese-looking mojibake. Each `.bin` now has a `.hex` twin (made by
`reproduction/scripts/render_results_hex.py`) that shows the same bytes as a
hex dump with an ASCII column, and `.gitattributes` tells GitHub the `.bin`
files are binary. Open the `.hex` file to look at the bytes.

Important for reading the frontier files: **chain1, chain2, chain4 and
cosmic_output contain no readable text, and that is expected.** They are the
outputs of community-proposed decrypts of the open containers; the bytes
look random because, on current evidence, these are "valid padding by
chance" results, not real plaintexts (see `walkthrough/09_frontier_containers.md`).

| File | Bytes | SHA-256 | What it is | Text expected? |
|---|---:|---|---|---|
| `phase2_plaintext.bin` | 648 | `e2f9dd65604a3231f8b3301724e8d713a88fffc4b6c7c4aeeb20f58a582b593a` | `PT-phase2`: the riddle text behind "causality" (03) | yes -- it is plain text (also in `reference/artifacts/plaintexts/phase2_plaintext.txt`) |
| `phase3_plaintext.bin` | 4,090 | `c4ad94559a44a927c1032cc0e024515f9510a0806a2d14458dbf4a360af9865f` | `PT-phase3`: three riddles + the Phase-3.2 envelope (04, 05) | yes -- plain text (also `phase3_plaintext.txt`) |
| `phase32_plaintext.bin` | 2,422 | `b82afeb86f9e50848220f9b64b744b821400308aea273a1c949b9d2d0e408a34` | `PT-phase32`: Architect text + 1,539 ciphered bytes + digits + riddle + `p32_trailing` (06) | partly -- bytes 447-1985 are non-ASCII BY DESIGN (EBCDIC-coded, Beaufort-ciphered); see `phase32_speech.txt` for the decode |
| `phase32_speech.txt` | 1,539 | `90829b510c3697569da47d2817f545f1e2a1cddd78e45f821dafcdab3dc0c281` | the Architect speech, decoded (06) | yes (no spaces) |
| `dbbi.txt` | 91 | `71fe46259e270c113529dfaded4b59c59a9dffd826a7202ab07fc498b6a2c5ca` | the DBBI block of the soup (08, 10) | letters a-i |
| `faed.txt` | 570 | `066191b4aafc114fbca7f0d168382f40129c4ff18490375b689741081d5ef3c2` | the FAED block of the soup (08, 10) | letters a-i |
| `bifid_full.txt` | 570 | `0c5d984f90e9baefc09f1d3888e62acbd101f9b0194887e2ae88fc6c9967745e` | FAED under the DBBI-square Bifid: begins `BTCSEED` (10) | capital letters |
| `chain1.bin` | 79 | `1449a2178eea7c0e3fabac8c1ad2afa294be4fc1800c594a025a056e88c626bf` | community "chain 1": `salph_inner` opened with five soup tokens + MD5 (09, 3.1) | **no** -- random-looking bytes; significance unverified |
| `chain2.bin` | 79 | `b40fce72ef5638e4f79b3233e653f8a5dbdb0d4ae2009d2d3da2c98b70f4d004` | community "chain 2": `p32_trailing` opened with a WIF string + MD5 (09, 3.2) | **no** |
| `cosmic_output.bin` | 1,327 | `4f7a1e4efe4bf6c5581e32505c019657cb7b030e90232d33f011aca6a5e9c081` | community "Cosmic": seven-token XOR key + MD5 (09, 3.3) | **no** (7.87 bits of entropy per byte) |
| `chain4.bin` | 1,151 | `e4269ed5fbb202a81e5e1aa6b5190fdd1ea126b2c8547ea7cdbdf45387ea135b` | community "chain 4": a masked slice of the Cosmic output decrypted again (09, 3.4) | **no** |
| `audio_LminusR_spectrogram.png` | image | (re-rendered on each run) | spectrogram of left-minus-right of the Decentraland audio; the hex numerals spelling HASHTHETEXT are read from it by eye (07) | image |
| `reproduction_results.json` | -- | -- | every step with inputs, parameters, outputs and status (`confirmed` / `new`; a `discrepancy` would mean a mismatch -- none occurred) | JSON |
| `*.hex` | -- | -- | hex views of the `.bin` files above | yes |

How to regenerate everything (about 6 seconds):

```
python3 reproduction/scripts/reproduce.py
python3 reproduction/scripts/render_results_hex.py
```

Re-running is deterministic: the 2026-10-16 run produced byte-identical
outputs to the 2026-10-15 run (only the timestamp inside the JSON changes,
and the spectrogram PNG re-renders).
