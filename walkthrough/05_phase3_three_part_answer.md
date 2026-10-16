# Phase 3 -- Jacque Fresco, Alice and Heisenberg open the third envelope

Status: SOLVED (reproduced; Python and OpenSSL agree byte for byte)
Where: inside `PT-phase3`, the plaintext obtained in 04
Previous: [04_phase2_2_seven_part_answer.md](04_phase2_2_seven_part_answer.md) --
Next: [06_phase3_2_speech_and_vic.md](06_phase3_2_speech_and_vic.md)

## 1. Data (what you are given)

`PT-phase3` (4,090 bytes, `reference/artifacts/plaintexts/phase3_plaintext.txt`)
reads, in full apart from the base64 block:

```
What if the merovingian is wrong. What instead of causality something else
could be ours? Therefor, if so, the ...... is ours. The thinker's 1name
behind all of that would grant you access to the next step (of humanity).
Definitely look into his works might you have time. /(aa,connected enf)

I just passed a cheshire cat and I'm getting fed up with this puzzle.. It's
taking forever. But, How long is forever? I don't know, but just add giveit
in front of the answer and you can fall in the keyhole. /(aa,connected enf)

3.The fundamental limit to the precision with which certain pairs of
physical properties are know. /(aa,connected enf)

Phase 3.2 is ciphered with aes-256-cbc base64 and a sha256 pw, yet again.

<ENV-phase32: 38 lines of base64 beginning U2FsdGVkX1/u/Exb...>
```

| Envelope | File | Decoded size | Salt | SHA-256 of the decoded envelope |
|---|---|---:|---|---|
| `ENV-phase32` | `reference/artifacts/envelopes/phase32.b64.txt` | 2,448 bytes (16 + 2,432 ciphertext) | `eefc4c5befc1656a` | `9d172dc017034564b40eb381fa61e31421f509a08430864c77ccf86cfc8fe784` |

## 2. Clues that apply

- `/(aa,connected enf)` after each riddle: lowercase, no spaces.
- "just add giveit in front of the answer" (riddle 2).
- The last line states the convention again: AES-256-CBC, base64, SHA-256
  password.
- Creator, 2019-05-17: "giveit = givetit" -- the author admitted a typo in
  this phase's answer string and confirmed the puzzle had been tested with
  the typo in place (see section 6).

## 3. Workings out

**Riddle 1 -- "the thinker's name".** If not causality, then "the ...... is
ours": "The future is ours to direct" is the closing line of a well-known
quotation by Jacque Fresco, founder of The Venus Project ("The future is
fluid. Each act, each decision, and each development creates new
possibilities and eliminates others. The future is ours to direct.").
Answer 1: `jacquefresco`.

**Riddle 2 -- "How long is forever?"** From *Alice in Wonderland* (the
Cheshire cat is the pointer): "How long is forever?" -- "Sometimes, just one
second." Put `giveit` in front: `giveit` + `justonesecond`.
Answer 2: `giveitjustonesecond`.

**Riddle 3 -- "the fundamental limit to the precision ..."** is the textbook
definition of Heisenberg's uncertainty principle.
Answer 3: `heisenbergsuncertaintyprinciple` (with the `s`).

**Join the three** (lowercase, no spaces) -- 62 characters:

```
jacquefrescogiveitjustonesecondheisenbergsuncertaintyprinciple
```

SHA-256 of that string is the password:

```
250f37726d6862939f723edc4f993fde9d33c6004aab4f2203d9ee489d61ce4c
```

Decrypt `ENV-phase32` with the usual convention. The plaintext `PT-phase32`
is 2,422 bytes and is the subject of the next file.

## 4. Solution

- `jacquefrescogiveitjustonesecondheisenbergsuncertaintyprinciple`
- `PT-phase32` (2,422 bytes, `b82afeb86f9e50848220f9b64b744b821400308aea273a1c949b9d2d0e408a34`),
  kept as `reproduction/results/phase32_plaintext.bin` and
  `reference/artifacts/plaintexts/phase32_plaintext.bin` (a `.bin` because
  it contains a block of non-ASCII bytes on purpose; see 06).

## 5. Verification

| Check | Result |
|---|---|
| `reproduce.py` step `aes_phase32` | confirmed; Python and OpenSSL identical |
| `verify.py` | answer length 62, password hash, decrypt, plaintext length 2,422 and hash pass |
| negative controls | MD5 key derivation and raw-digest password both fail |
| upstream copies | B's `phase3.2.txt` byte-identical; C's identical after CRLF -> LF |

## 6. Extra findings and notes

- The `giveit` typo. On 2019-05-17/18 the creator-attributed handle wrote
  "...unless you'd know where to add 1 extra character between the 3
  answers...", "giveit = givetit", "The issue is within the 3th phase", and
  "I've tested the entire puzzle 3 times with the same string which had the
  typo in it". The string that actually decrypts keeps `giveit` (reproduced).
  The creator also said (2020-02-22) that typos are "horrible mistakes due to
  rushed work" and that "no clues [are] to be found in those typos".
- `heisenbergs` needs its `s`. C's walkthrough misspells it without the `s`;
  that string does not decrypt.
- The three riddles are a Matrix / Alice / physics mix, consistent with the
  puzzle's taste for *The Matrix* quotations throughout.

Sources: `reference/01_SOLVED_CHAIN.md` section 3.5; `reference/04_CREATOR_CLUES.md`
(ids 866-875, 1806); A's README section 3; B's `phase3.ipynb`.
