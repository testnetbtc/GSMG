# SalPhaseIon -- the letter soup, its solved tokens, and the two containers it carries

Status: soup layout and five tokens SOLVED (reproduced); DBBI, FAED and both containers are OPEN
Where: https://gsmg.io/89727c598b9cd1cf8873f27cb7057f050645ddb6a7a157a110239ac0152f6a32
Previous: [07_decentraland_and_entry_hash.md](07_decentraland_and_entry_hash.md) --
Next: [09_frontier_containers.md](09_frontier_containers.md)

## 1. Data (what you are given)

The page is tiny (`reference/artifacts/images/SalPhaselonCosmicDuality.png`;
archived markup `reference/artifacts/pages/salphaseion_page_2024-11-23.html`
and `..._2025-10-31.html`, as supplied in B PR #15 from the Wayback Machine):

```
<title>GSMG Puzzle</title>
<H1> SalPhaseIon </H1>      <textarea> the letter soup (1,075 letters, written with spaces) </textarea>
<h1> Cosmic Duality </h1>   <textarea> a base64 OpenSSL envelope </textarea>
```

There are no comments, hidden fields, checkpoints or other text in the page.

| Object | File | Facts |
|---|---|---|
| the soup (`SOUP`) | `reference/artifacts/pages/salphaseion_soup.txt` (2,149 characters with the spaces) | 1,075 letters without spaces; SHA-256 of the no-space form `26e37652067c549c0eee624356be9ffd40a243901197335a41f91fb6c78e6156`; three independent copies (B's notebook, B PR #15's primary text, the archived page) agree byte for byte |
| `cosmic` | `reference/artifacts/envelopes/cosmic.b64.txt` | 1,344-byte envelope (16 + 1,328 ciphertext), salt `2d3f6fe06dc950e6`, SHA-256 `b18950551a4dd0cb8a9378f0906ba18c03a15f0ee83eb98c6bc90165c5f79805`; identical in both captures and in C's `ciphertexts/cosmic.txt` |

The soup, with the spaces removed and broken into its pieces (this is the
whole of it):

```
dbbibfbhccbegbihabebeihbeggegebebbgehhebhhfbabfdhbeffcdbbfcccgbfbeeggecbedcibfbffgigbeeeabe
abbabbababbaaaababbbabaaabbbaabaabbabaababbbbaaaabbbaabbabbbabababbabbababbabbaaabbabaababbbaabbabbbabaa
faedggeedfcbdabhhggcadcfeddgfdgbgigaaedggiafaecghggcdaihehahbahigceifgbfgefgaifabifagaegeacgbbeagfgg
eeggafbacgfcdbeiffaafcidahgdeefghhcggaegdebhhegeghcegadfbdiagefcicggifdcgaaggfbigaicfbhecaecbceiaice
bgbgiecdeggfgegaedggfiiciiififhggcgfgdcdggefcbeeigefibgibggghhfbcgifdehedfdagicdbhicgaiedaehahghhcih
dghfhbiicecbiichihiiigiddgehhdfdchcbafgfbhaheagegecafehgcfggggcagfhhghbaihidiehhfdeggdgcihggggghadah
igigbgecgedfcdggaccdehiicigfbffhggaeidbbeibbeiifdgfdhieeeieeecifdgdahdiggfhegfiaffiggbcbcehceabfbedb
iibfbfdedeehgigfaaiggagbeiichiedifbehgbccahhbiibibbibdcbahaidhfahiihic
z
agdafaoaheiecggchgicbbhcgbehcfcoabicfdhhcdbbcagbdaiobbgbeadedde
z
cfobfdhgdobdgooiigdocdaoofidh
z
shabefourfirsthintisyourlastcommand
U2FsdGVkX186tYU0hVJBXXUnBUO7C0+X4KUWnWkCvoZSxbRD3wNsGWVHefvdrd9z
abbaabababbabbbaabbbabaaabbaabababbbaaba
QvX0t8v3jPB4okpspxebRi6sE1BMl5HI8Rku+KejUqTvdWOX6nQjSpepXwGuN/jJ
shabefanstoo
```

(The first line is 91 letters; the second is 104 letters of only `a` and
`b`; lines 3-8 are 570 letters of `a`..`i` shown wrapped; the rest is as
written. The soup has no line breaks of its own; the pieces are found by
their alphabets, as explained below.)

## 2. Clues that apply

- The page name: "SalPhaseIon" (creator spelling "salphation"; solvers say
  "salvation"). Creator-attributed, 2021-03-14: "Breaking salphation, should
  be giving the feeling of the phase's name."
- `s h a b e f` with a = 1, b = 2, ... reads **sha256** (s, h, a, then
  b = 2, e = 5, f = 6). So `shabefourfirsthintisyourlastcommand` is
  "sha256: our first hint is your last command" and `shabefanstoo` is
  "sha256 ans too" ("answer too"). These are readings, not confirmed
  instructions.
- The 2022-12-10 creator post of a book cover: Time-Life, *Mysteries of the
  Unknown: Cosmic Duality* -- the name of the second heading.
- Every solved stage before this one used SHA-256(answer) as the password.

## 3. Workings out

**Finding the pieces.** The soup uses four alphabets that never mix: runs of
`a`..`i`; runs of only `a`/`b`; the letter `z`; and base64 text. Reading left
to right:

| Offset | Length | Alphabet | Rule applied | Result |
|---:|---:|---|---|---|
| 0 | 91 | a-i | (none known) | **DBBI** -- open |
| 91 | 104 | a, b | a = 0, b = 1; 13 bytes of 8 bits, MSB first | `matrixsumlist` |
| 195 | 570 | a-i | (none known) | **FAED** -- open |
| 765 | 1 | z | separator | |
| 766 | 63 | a-i and o | a = 1 ... i = 9, o = 0; the digits form ONE decimal number; write it in bytes | `lastwordsbeforearchichoice` |
| 829 | 1 | z | separator | |
| 830 | 29 | a-i and o | same rule | `thispassword` |
| 859 | 1 | z | separator | |
| 860 | 35 | plain letters | read as is | `shabefourfirsthintisyourlastcommand` |
| 895 | 64 | base64 | first half of an envelope | (see below) |
| 959 | 40 | a, b | a = 0, b = 1; 5 bytes | `enter` |
| 999 | 64 | base64 | second half of the envelope | (see below) |
| 1063 | 12 | plain letters | read as is | `shabefanstoo` |

Total 1,075. Note that the `z` at offset 958, just before the `enter` block,
is the 64th base64 character of the envelope, not a separator.

**The a/b blocks.** `abbabbab abbaaaab abbbabaa abbbaaba ...` -> `01101101
01100001 01110100 01110010 ...` -> `m a t r ...` -> `matrixsumlist`. The
40-letter block inside the base64 gives `enter`.

**The z-sections (worked for `thispassword`).** Replace a..i by 1..9 and o by 0:

```
letters: c f o b f d h g d o b d g o o i i g d o c d a o o f i d h
digits : 3 6 0 2 6 4 8 7 4 0 2 4 7 0 0 9 9 7 4 0 3 4 1 0 0 6 9 4 8
number : 36026487402470099740341006948
in hex : 7468697370617373776f7264
ASCII  : t h i s p a s s w o r d
```

The 63-letter section gives the number
`174161018595377387932283725836301293648834223172419022725145445`,
hex `6c617374776f7264736265666f7265617263686963686f696365`, ASCII
`lastwordsbeforearchichoice` ("last words before Archi-choice": the
Architect's "choice" scene, i.e. the Phase-3.2 speech ends with the key
words). These fields are decimal numbers; a claim that they are "base 9" is
wrong (reproduced).

**Reassembling the envelope.** Remove the `enter` insertion and join the two
64-character halves: 128 base64 characters = a 96-byte OpenSSL envelope,
`Salted__`, salt `3ab585348552415d`, 80 bytes of ciphertext, SHA-256
`9e2831e1b34b5f34796df47ccaf6530d48d371c61a6bff84d60db1064fa7a258`. This is
the container `salph_inner`. It is byte-identical to C's `salphaseion.txt`.

## 4. Solution (what is solved on this page)

| Token | How |
|---|---|
| `matrixsumlist` | a/b block |
| `lastwordsbeforearchichoice` | z-section 1 |
| `thispassword` | z-section 2 |
| `enter` | a/b insertion inside the base64 |
| "sha256 our first hint is your last command", "sha256 ans too" | readings of the plain-text pieces |

Still open on this page: `DBBI` (91 letters), `FAED` (570 letters), the
container `salph_inner`, the container `cosmic`. `DBBI` and `FAED` are taken
up in [10_frontier_dbbi_faed_btcseed.md](10_frontier_dbbi_faed_btcseed.md);
the containers in [09_frontier_containers.md](09_frontier_containers.md).

## 5. Verification

| Check | Result |
|---|---|
| `reproduce.py` step `salphaseion_soup_sections` | confirmed (offsets, hashes, both a/b decodes, both z decodes, the plain pieces, the envelope) |
| `reproduce.py` step `salphaseion_page_provenance` | the soup textarea of both held captures equals the primary text; the Cosmic textarea equals `cosmic.txt`; headings as shown; nothing else on the page |
| `verify.py` | soup length 1,075 and hash; DBBI and FAED hashes; first-occurrence order of DBBI = `DBIFHCEGA`; `matrixsumlist`; both z decodes; `enter`; the trailing pieces; the reassembled envelope's hash and salt; equality with the envelope artifact; cosmic hash and salt |

## 6. Extra findings and notes

- Earlier signs the soup existed: a garbled Telegram "leak" of it on
  2021-04-16; the instructions of 2021-05-06 (by a Deleted Account); A's
  README section added in 2021.
- "Dualite", a title some write-ups give to the second section, does not
  occur in either held capture (the heading is `Cosmic Duality`). A 2023
  capture cited elsewhere is not held, so earlier markup cannot be excluded.
- The page has never carried a checkpoint value. Everything proposed for the
  open objects therefore has to validate itself some other way -- which is
  exactly the problem described in 09.
- The hosting domain: gsmg.io was parked/for sale from 2026-07-07; a
  "finale" page appeared at the root on 2026-08-19 ("2017 - 2026", "Nine
  years of chaos ended. One mystery remains."). Who published that page is
  not verified.
- Creator-attributed, 2023-08-06, asked "Has anyone passed the salvation
  part?": "Partly."

Sources: `reference/01_SOLVED_CHAIN.md` section 3.9; `reference/02_ARTIFACTS.md`
section 2; `reference/08_GLOSSARY.md`; A's README "Salphaseion"; B's
`salphaseion.ipynb`.
