# reproduction/

Fresh, independent code that re-derives the GSMG solved chain and every published *fixed* recipe that bears on the unsolved containers. It was written for this archive after reading, not reusing, the upstream notebooks and harnesses.

## Scripts

| Script | Purpose |
|---|---|
| `scripts/gsmglib.py` | helpers: OpenSSL envelope parsing, EVP_BytesToKey (any digest), AES-256-CBC with strict PKCS#7, an OpenSSL-CLI second implementation, pure-Python secp256k1, Base58Check, P2PKH, WIF text |
| `scripts/reproduce.py` | every reproduction step → `results/reproduction_results.json` plus output files |
| `scripts/collect_discussions.py`, `render_discussions.py` | GitHub discussions collection (paced, resumable) and lossless rendering + attachment download |
| `scripts/build_inventory.py`, `build_artifacts.py`, `build_registers.py`, `build_manifest.py`, `check_manifest.py` | the archive's derived tables and the completeness proof |

Run `python3 reproduction/scripts/reproduce.py` from any directory (about 5 s). Inputs are read only from `sources/`; every input is recorded with `repo@commit:path`.

## Independence and second implementations

- AES stages: Python (pycryptodome AES primitive, our own EVP_BytesToKey and PKCS#7 check) **and** the OpenSSL CLI (`openssl enc -d -aes-256-cbc -md <digest> -pass file:`; for binary passwords, `openssl dgst` computes EVP and `-K/-iv` is used). The CLI output must equal the Python output byte-for-byte (`implementations_agree`).
- CP1141: GNU `iconv -t IBM1141` **and** Python `cp273` (CP1141 = CP273 + euro sign; no euro occurs in the input).
- secp256k1/addresses: pure Python, sanity-checked against the known address of k = 1.
- Audio: ffmpeg decode → L − R → matplotlib spectrogram, read **by eye** (`results/audio_LminusR_spectrogram.png`).

## Status of each step

`confirmed` = equals the prior report's recorded value; `new` = no prior value (or a new control); `discrepancy` would mean a mismatch (none occurred). `implementations agree` = the second implementation returned identical bytes.

| Step | Status | Implementations agree |
|---|---|---|
| `grid_14x14_to_url` | confirmed | — |
| `aes_phase2` | confirmed | yes |
| `aes_phase3` | confirmed | yes |
| `aes_phase32` | confirmed | yes |
| `upstream_plaintext_check:naddiseo/phase2-assets/phase2.1.txt` | new | — |
| `upstream_plaintext_check:naddiseo/phase2-assets/phase3.txt` | new | — |
| `upstream_plaintext_check:naddiseo/phase3-assets/phase3.2.txt` | new | — |
| `upstream_plaintext_check:hosterjack/assets/walkthrough/phase2-assets/phase2.1.txt` | new | — |
| `upstream_plaintext_check:hosterjack/assets/walkthrough/phase2-assets/phase3.txt` | new | — |
| `upstream_plaintext_check:hosterjack/assets/walkthrough/phase3-assets/phase3.2.txt` | new | — |
| `envelope_copy_check:hosterjack/ciphertexts/phase2.txt` | new | — |
| `envelope_copy_check:hosterjack/ciphertexts/phase3.txt` | new | — |
| `envelope_copy_check:hosterjack/ciphertexts/phase32.txt` | new | — |
| `phase32_ebcdic1141_beaufort` | confirmed | yes |
| `phase32_straddling_checkerboard` | confirmed | — |
| `audio_LminusR_spectrogram` | confirmed | — |
| `salphaseion_entry_hash` | confirmed | — |
| `salphaseion_soup_sections` | confirmed | — |
| `hint_2023_reverse_binary` | confirmed | — |
| `hint_2026_new_year_binary` | new | — |
| `naddiseo17_chain1_salph_inner` | confirmed | yes |
| `naddiseo17_chain2_p32_trailing` | confirmed | yes |
| `cosmic_seven_token_xor` | confirmed | yes |
| `chain4_masked_nested_envelope` | confirmed | yes |
| `bifid_full_period_faed` | confirmed | — |
| `bc_expansion_lengths` | confirmed | — |
| `prize_pubkey_to_address` | confirmed | — |
| `chain4_crib_control_cosmic_A` | new | — |
| `salphaseion_page_provenance` | new | — |
| `cosmic_seven_token_xor_set_A` | confirmed | — |
| `a15_padding_controls` | new | — |
| `cosmic_103x103_base38` | new | — |

## Safety scope

No keyspace or candidate sweep is performed. Each step evaluates one published recipe; the Cosmic steps try the four encodings (raw/hex × MD5/SHA-256) of one published key, to pin down which convention a source meant. Public 32-byte values published in issues are turned into addresses only to compare with the published addresses and the prize address. No key is imported into any wallet, nothing is signed or broadcast, and no live gsmg.io endpoint is contacted.
