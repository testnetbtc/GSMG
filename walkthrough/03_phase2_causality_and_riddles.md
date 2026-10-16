# Phase 2 -- "causality" opens the first envelope; Mr Robot gives parts 2, 3, 4

Status: SOLVED (reproduced; Python and OpenSSL agree byte for byte)
Where: https://gsmg.io/choiceisanillusioncreatedbetweenthosewithpowerandthosewithoutaveryspecialdessertiwroteitmyself
Previous: [02_phase1_the_form.md](02_phase1_the_form.md) --
Next: [04_phase2_2_seven_part_answer.md](04_phase2_2_seven_part_answer.md)

## 1. Data (what you are given)

The Phase-2 page (archived copies: `reference/artifacts/pages/choiceisanillusion_2020-11-12.html`
and `..._2026-04-05.html`; screenshots `images/phase2_page.png`,
`images/phase3_page.png`). Its visible text, top to bottom:

```
PHASE 2

"1... are you looking for the private keymaker?" You come to me, without it.
Come to me with it and you'll have the power to continue. It'll grant the
first part.  /(aaa, connected enf)

Ciphered with aes-256-cbc /w base64 sha-256(password)

<ENV-phase2: 14 lines of base64 beginning U2FsdGVkX18GKGYS...>

<two paragraphs of riddles and a chess line: parts 5, 6, 7 -- quoted in 04>

--> parts 1..7 --> sha-256 -> dgst is the password to enter Phase 3.
Phase 3 is also ciphered with aes-256-cbc /w base64.

PHASE 3

<ENV-phase3: base64 beginning U2FsdGVkX1+fvEUd...>
```

So this one page holds TWO encrypted envelopes. This file covers the first
one; the second is handled in 04.

| Envelope | File | Decoded size | Salt | SHA-256 of the decoded envelope |
|---|---|---:|---|---|
| `ENV-phase2` | `reference/artifacts/envelopes/phase2.b64.txt` | 672 bytes (8 header + 8 salt + 656 ciphertext) | `06286612d43ed7ed` | `a089144531c666e59770c799427c05d1ea4ae074857b97d61b8d3924ff14c7e7` |

## 2. Clues that apply

- The URL is a line of the Merovingian in *The Matrix Reloaded*: "Choice is
  an illusion created between those with power and those without", followed
  by his remark about the cake, "a very special dessert, I wrote it myself".
  In the same scene he says: "there is only one constant, one universal ...
  **causality** -- cause and effect." The "keymaker" is the character the
  heroes come to him for.
- Formatting markers used throughout the puzzle: `aaa` = all lowercase,
  `aBa` = keep the case as written; `connected enf` = remove the spaces,
  `connected not enf` = keep them.
- The page states the cipher outright: AES-256-CBC, base64, password =
  SHA-256 of the answer.

## 3. Workings out

**Part 1.** The answer is `causality`.

**Opening ENV-phase2.** Apply the convention (see the README): the password
is the 64 lowercase hex characters of SHA-256("causality"):

```
eb3efb5151e6255994711fe8f2264427ceeebf88109e1d7fad5b0a8b6d07e5bf
```

Then AES-256-CBC with key and IV from OpenSSL's `EVP_BytesToKey` (SHA-256,
one round, the salt from the envelope):

```
openssl enc -d -aes-256-cbc -md sha256 -a -in phase2.b64.txt \
   -pass pass:eb3efb5151e6255994711fe8f2264427ceeebf88109e1d7fad5b0a8b6d07e5bf
```

The plaintext `PT-phase2` is 648 bytes:

```
The ironic 2name of the keymakers trying to protect the current digital
powers which are still in severe danger due to the keymaker's way of
security by hiding, nearly unprotected, in plain sight. {eps3.4_[in one of
the valleys of Phillip]runtime-error.r00., where daughters hit magic keypads}
When this fails.. Crypto finally to the latin 3Moon? Tell me, 4How so mate?
# X 2 S H 4 Y 0 Q B 15 #
Q -> extend the name of a hackers' swordless fish, the I and W are below.
B -> ((BV80605001911AP)- (sqrt(-1)))^2
H -> (Answer to only this puzzle but nothing else) * -1
S -> cha' + (vagh * jav)
Ok kid, on the highway, let put it in the worst gear.
```

**Parts 2, 3, 4 (the numbers `2name`, `3Moon`, `4How so mate` are the part
numbers).** `{eps3.4_ ... runtime-error.r00}` is the title of *Mr. Robot*
season 3 episode 4, "eps3.4_runtime-error.r00" (the series names episodes
like file names). In that episode a hardware security module -- a SafeNet
Luna HSM -- is attacked by hand ("daughters hit magic keypads"), and HSMs are
"keymakers" that protect keys by sitting in plain sight on a network.

- part 2, "the ironic name of the keymakers": **Safenet**
- part 3, "the latin Moon": **Luna**
- part 4, "How so mate" = H S M: **HSM**

(The case is kept as the community found it worked: `Safenet`, `Luna`, `HSM`.)

**The `# X 2 S H 4 Y 0 Q B 15 #` line** is not needed to go on, and no
reading of it is confirmed:

- `S = cha' + (vagh * jav)` is Klingon arithmetic: 2 + (5 x 6) = 32.
- `BV80605001911AP` is the Intel "S-spec" code of a Core i5 processor, so A
  reads `B = ((i5) - i)^2 = (4i)^2 = -16`. B's notebook instead solves
  Q = 82, H = 42 and B = 25 and reads the whole row as the coordinates
  51 52 28.0 N, 4 24 23.2 E, "very close" to SafeNet Technologies (single
  source; reported; checked only by B's own screenshot).
- A second-hand relay of a creator remark says "#...# wasn't used."

## 4. Solution

- part 1: `causality`
- parts 2-4: `Safenet`, `Luna`, `HSM`
- `PT-phase2` (648 bytes, `e2f9dd65604a3231f8b3301724e8d713a88fffc4b6c7c4aeeb20f58a582b593a`),
  kept as `reproduction/results/phase2_plaintext.bin` and
  `reference/artifacts/plaintexts/phase2_plaintext.txt`.

## 5. Verification

| Check | Result |
|---|---|
| `reproduce.py` step `aes_phase2` | confirmed; Python and the OpenSSL CLI produce identical bytes |
| `verify.py` | envelope hash, salt, password hash, decrypt, plaintext length 648 and hash all pass |
| negative controls | the same password with an MD5 key derivation does NOT open it; the raw 32-byte digest as password does NOT open it |
| upstream copies | B's `phase2.1.txt` is byte-identical to the decrypt; C's copy is identical after CRLF -> LF |

## 6. Extra findings and notes

- OpenSSL versions: from OpenSSL 1.1.0 on, `-md sha256` is the default, so
  A's command (which omits `-md`) works there; OpenSSL 1.0.2 and earlier
  defaulted to MD5 and need `-md sha256` spelled out. The key-derivation
  digest for every solved stage is SHA-256 (reproduced; MD5 fails as a
  control). Some write-ups state this the other way round.
- Two issue comments misquote SHA-256("causality") as `...5a0b8b...`; the
  correct value ends `...5b0a8b6d07e5bf` as above.
- Both envelopes are on this one page: the 2020-11-12 capture holds both
  base64 blocks (placement reproduced).
- `PT-phase2` and `PT-phase3` plaintexts are text files and render normally
  on GitHub; `PT-phase32` (next phases) does not, because it contains a
  1,539-byte block of non-ASCII bytes by design.

Sources: `reference/01_SOLVED_CHAIN.md` section 3.3; `reference/07_CONTRADICTIONS.md`;
A's README section 3; B's `phase2.ipynb`.
