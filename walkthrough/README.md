# GSMG 5 BTC puzzle -- the walkthrough (start here)

This folder is the readable, phase-by-phase account of the puzzle: for every
phase, the DATA you are given, the CLUES that apply, the WORKINGS OUT, the
SOLUTION, how it is VERIFIED, and the EXTRA findings around it. It runs from
the opening image to the community frontier (the unsolved objects, including
BTCSEED).

Everything stated here is machine-checked: `verify.py` re-derives every value
from the raw artifacts with a second, independent implementation and audits
every SHA-256 printed in these pages. All files in this folder are plain
7-bit ASCII (`check_ascii.py` enforces it), so nothing renders in odd fonts.

## How this folder relates to the rest of the repository

| Layer | What it is | Use it for |
|---|---|---|
| `walkthrough/` (this folder) | the readable account, phase by phase | reading and following the puzzle |
| `reference/` | the deduplicated knowledge base: one statement per fact, each with a pointer to its source | checking where a fact comes from |
| `reproduction/` | independent code that re-derives the whole chain; `results/` holds the outputs | re-running the mechanics yourself |
| `research/` | this archive's own experiments on the unsolved parts (dated folders) | seeing what has been tried and the outcome |
| `sources/` | the three community repositories, preserved byte-for-byte with their history | the evidence of record (never edited) |

The archive was built from three community repositories (keys A, B, C):
A = puzzlehunt/gsmgio-5btc-puzzle, B = Naddiseo/gsmgio-5btc-puzzle (a fork of
A), C = HosterjackAGV/gsmg-5btc-puzzle. `sources/` keeps each one verbatim so
nothing is lost; `reference/` states each fact once; this folder tells the
story in order.

## The map

```
Phase 0    opening image  (puzzle.png, a 14x14 grid)
   |       cells -> bits -> spiral -> ASCII
   v
Phase 1    gsmg.io/theseedisplanted   (hidden form; song "The Warning" by Logic)
   |       answer = theflowerblossomsthroughwhatseemstobeaconcretesurface
   v
Phase 2    gsmg.io/choiceisanillusion...   (page with riddles and TWO AES envelopes)
   |       part 1 "causality" -> AES -> PT-phase2 -> parts 2,3,4 = Safenet, Luna, HSM
   |       page text -> parts 5,6,7 = 11110, 0x7368..., chess FEN after Rc6
   v
Phase 2.2  parts 1..7 joined (227 chars) -> SHA-256 -> AES -> PT-phase3
   v
Phase 3    three riddles -> jacquefresco + giveitjustonesecond + heisenbergsuncertaintyprinciple
   |       -> SHA-256 -> AES -> PT-phase32
   v
Phase 3.2  PT-phase32 =  Architect speech (CP1141 + Beaufort "thematrixhasyou")
                      +  149 digits -> straddling checkerboard -> "half and better half" sentence
                      +  p32_trailing  (an UNSOLVED AES container)

Decentraland   parcel -41,-17 -> audio -> left minus right -> spectrogram -> HASHTHETEXT
   |           + the "Roses" hint -> SHA-256 of the text on the opening image
   v
SalPhaseIon    gsmg.io/89727c59...  =  the letter SOUP  +  the Cosmic Duality envelope
   |           SOUP -> DBBI (open) | matrixsumlist | FAED (open) | z-tokens | salph_inner (open)
   v
Frontier       DBBI gives a 5x5 square; FAED under Bifid -> "BTCSEED..." (open)
               four open containers; community "openings" with no checkpoint
```

## Reading order

| File | Phase | One line |
|---|---|---|
| [01_phase0_opening_image.md](01_phase0_opening_image.md) | 0 | the 14x14 grid is a URL |
| [02_phase1_the_form.md](02_phase1_the_form.md) | 1 | a hidden form and a song lyric |
| [03_phase2_causality_and_riddles.md](03_phase2_causality_and_riddles.md) | 2 | "causality" opens the first envelope; Mr Robot gives parts 2-4 |
| [04_phase2_2_seven_part_answer.md](04_phase2_2_seven_part_answer.md) | 2.2 | JFK, the genesis block and a chess problem give parts 5-7 |
| [05_phase3_three_part_answer.md](05_phase3_three_part_answer.md) | 3 | Jacque Fresco, Alice, Heisenberg |
| [06_phase3_2_speech_and_vic.md](06_phase3_2_speech_and_vic.md) | 3.2 | EBCDIC + Beaufort speech; the checkerboard sentence; the trailing container |
| [07_decentraland_and_entry_hash.md](07_decentraland_and_entry_hash.md) | DCL | the audio says HASHTHETEXT; the "Roses" hint says which text |
| [08_salphaseion_soup.md](08_salphaseion_soup.md) | SalPhaseIon | the soup, its solved tokens, and the two containers it holds |
| [09_frontier_containers.md](09_frontier_containers.md) | frontier | the four open containers and every community "opening", with verdicts |
| [10_frontier_dbbi_faed_btcseed.md](10_frontier_dbbi_faed_btcseed.md) | frontier | DBBI, FAED, the Bifid decode that begins BTCSEED, and what has been tested |
| [11_clues_index.md](11_clues_index.md) | all | every creator clue, dated, and what it does and does not establish |
| [12_verification.md](12_verification.md) | all | how to re-run everything; the hash table; the verifier's output |

## Conventions used in these pages

- **Status words.** `reproduced` = re-derived here from fresh code and the raw
  bytes, with the hash recorded; `reported` = a source says so, not re-run
  here; `interpreted` = someone's reading of the evidence (including ours).
  For the frontier objects two verdicts are always kept apart: *mechanics*
  (do the bytes come out as claimed?) and *significance* (is it a real
  puzzle stage?).
- **Hashes** are SHA-256, lowercase hex. A hash printed in full is one that
  `verify.py` recomputes; `...` never appears inside a hash.
- **Names** follow `reference/08_GLOSSARY.md`: `ENV-phase2` is an encrypted
  envelope, `PT-phase2` its plaintext, `salph_inner` / `p32_trailing` /
  `cosmic` / `urlblob` are the open containers (named by where they live and
  by their salt, because the community uses several conflicting names).
- **The AES convention** that every solved stage follows: UTF-8 encode the
  answer (no newline); the password is the 64 lowercase hex characters of
  SHA-256(answer); base64-decode the envelope; it begins `Salted__` + 8-byte
  salt; derive key+IV with OpenSSL's `EVP_BytesToKey` using SHA-256, one
  round; AES-256-CBC; strict PKCS#7 padding. On the command line:
  `openssl enc -d -aes-256-cbc -md sha256 -a -in envelope.txt -pass pass:<hex>`.
- **Creator attribution** means "posted under the Telegram handle @SoWut
  (display name Jrk Bgrt)". Nothing authenticates that handle as the author;
  it is treated as creator-attributed, never as proven.
- **Nothing here is a key.** The prize address is public; its public key is
  public (it is in the 2020 spending transaction). No private key is derived,
  stored, imported or broadcast anywhere in this repository.

## Verify it yourself

```
python3 walkthrough/verify.py          # independent re-derivation + document hash audit
python3 walkthrough/check_ascii.py     # no non-ASCII typography in the archive's documents
python3 reproduction/scripts/reproduce.py        # the archive's own reproduction (writes results/)
python3 reproduction/scripts/check_manifest.py   # completeness proof of sources/ (zero orphans)
```

Requirements: Python 3.10+, `pycryptodome`, `Pillow`; `numpy`, `matplotlib`
and the `openssl`, `iconv`, `ffmpeg` command-line tools for `reproduce.py`;
`chess` (python-chess) is optional for one extra check.
