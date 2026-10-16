# The frontier, part 2 -- DBBI, FAED, the Bifid decode that begins BTCSEED, and what has been tested

Status: OPEN. The Bifid decode is reproduced; what to do with its output is unknown.
Previous: [09_frontier_containers.md](09_frontier_containers.md) --
Next: [11_clues_index.md](11_clues_index.md)

## 1. The two letter blocks

Both come from the SalPhaseIon soup (08). Both use only the letters a-i,
and -- unlike the soup's solved number fields, which use `o` for 0 --
neither contains an `o`.

**DBBI** (soup offset 0, 91 letters):

```
dbbibfbhccbegbihabebeihbeggegebebbgehhebhhfbabfdhbeffcdbbfcccgbfbeeggecbedcibfbffgigbeeeabe
```

| Fact | Value |
|---|---|
| SHA-256 | `71fe46259e270c113529dfaded4b59c59a9dffd826a7202ab07fc498b6a2c5ca` |
| letter counts | b 25, e 18, f 10, g 10, c 8, h 8, i 5, d 4, a 3 |
| first-occurrence order | `D B I F H C E G A` |
| length | 91 = 7 x 13 (also the 13th triangular number) |
| index of coincidence | 0.151 (English is about 0.066; a-i letters only) |
| `b` sits at positions 2, 3, 5, 7, 11, 31, 79 (counting from 1); the first ten letters `dbbibfbhcc` have `b` at exactly 2, 3, 5, 7 | descriptive only |

**FAED** (soup offset 195, 570 letters; shown wrapped):

```
faedggeedfcbdabhhggcadcfeddgfdgbgigaaedggiafaecghggcdaihehahbahigceifgbfgefgaifabifagaegeacgbbeagfgg
eeggafbacgfcdbeiffaafcidahgdeefghhcggaegdebhhegeghcegadfbdiagefcicggifdcgaaggfbigaicfbhecaecbceiaice
bgbgiecdeggfgegaedggfiiciiififhggcgfgdcdggefcbeeigefibgibggghhfbcgifdehedfdagicdbhicgaiedaehahghhcih
dghfhbiicecbiichihiiigiddgehhdfdchcbafgfbhaheagegecafehgcfggggcagfhhghbaihidiehhfdeggdgcihggggghadah
igigbgecgedfcdggaccdehiicigfbffhggaeidbbeibbeiifdgfdhieeeieeecifdgdahdiggfhegfiaffiggbcbcehceabfbedb
iibfbfdedeehgigfaaiggagbeiichiedifbehgbccahhbiibibbibdcbahaidhfahiihic
```

| Fact | Value |
|---|---|
| SHA-256 | `066191b4aafc114fbca7f0d168382f40129c4ff18490375b689741081d5ef3c2` |
| letter counts | a 54, b 49, c 52, d 49, e 69, f 57, g 107, h 58, i 75 |
| length | 570 = 2 x 3 x 5 x 19 |
| index of coincidence | about 0.118 |

## 2. Clues that apply

- Creator-attributed, 2021-12-26 ("a mini mini hint"): "We've seen prime
  numbers being mentioned; well, that is definitely an aspect which is
  required to proceed. Furthermore, along the way, some characters need to
  be 'zeroed out'." Also 2023-01-09: "At least prime number is very
  important to get any further." And 2021-03-01: "You are at the prime part
  already??? ... That might have been a hint."
- The 2023-02-23 hint (full decode in 11): four labels
  `yellowblueprimes | matrixsumlist | lastwordsbeforearchichoice | yinyang`,
  followed by "we wont give away the password its in front of your eyes but
  youre not seeing it very last step is a true giveaway promised".
- "yin yang": "Once you hit a 'ying yang', you'll be able to solve it the
  same day" (2023-08-06); "It's the next phase, but I await the day someone
  finally gets there" (2025-04-28).
- The target: "Regular Bitcoin Private key" (2024-01-26); "a private key"
  (2020-08-09, to "private key or seed phrase or brain wallet?").
- The Architect speech (06): "reinserting the prime basics after which you
  will be required to select from over twenty-three ciphers, sixteen
  encryptions and or seven intertwined passwords to find the actual private
  key, note that also brute forcing might be required".

## 3. Workings out -- the Bifid decode

**Step 1 -- DBBI gives a key square.** Write DBBI's letters in order of first
appearance, `DBIFHCEGA`, then the rest of the alphabet with J left out
(the usual 25-letter Polybius convention):

```
        col 0  1  2  3  4
row 0       D  B  I  F  H
row 1       C  E  G  A  K
row 2       L  M  N  O  P
row 3       Q  R  S  T  U
row 4       V  W  X  Y  Z
```

Every letter that occurs in FAED (a-i) sits in rows 0 and 1.

**Step 2 -- Bifid-decrypt FAED with the whole text as one block (period
570).** In Bifid every letter is a (row, column) pair. To decrypt, write the
570 pairs of FAED one after another as a single stream of 1,140 digits:
`r1 c1 r2 c2 ... r570 c570`. The first 570 digits of that stream are the
ROWS of the plaintext letters, the last 570 are their COLUMNS; plaintext
letter number i is the square entry at (rows[i], cols[i]).

**Step 3 -- the output** (`reproduction/results/bifid_full.txt`, 570
letters, SHA-256
`0c5d984f90e9baefc09f1d3888e62acbd101f9b0194887e2ae88fc6c9967745e`):

```
BTCSEEDDEOEMCKEADHBSCHDKBDCSDKDVBXCPCOCHCRDICIBQEEBDDBCNDSBDCPDGCPDNCNCSESCGDDCLENBMCUDUCQCACDELDZELCMEFDFESDODWCKBYCUBWBAESBWBNEMEDEADOBRCPBGBQCOEGBSENESBLBTESDADPDUESCPCREACNCKCSCDCNBEDKCKCTCLBRENENCCEGELCNCUBSBGESEIENDUEFDDBACKDNBSDSESCRBSEBBLBIERDVCOBDCCEGBSEOBVBVCDEMCPCSCGELDIEGDADWDYCACPEGENBYEBCGCLCRDBBRDGDBDMERCNCGDTCDBNCFCLCPDNBRBBEBCNEREREMELDSDADLENCQBOCHDQDGBXEGCFCUEEEIDACIEADOCTDNEIEGDEELDEELBMCKEDBBEACMCODREMCCCMCSCGDBCOCMDTDLBMCDBMBMDPBSDNBSDYEOEOCIENBSEOBICBBBCNCNECDUCIBECCCGDOCMEEDUBNDEELBLBACPCPCMDXDXDRDGCBCMDNDRDDECDWEADHBTDICQCPDOEFDHDGDXDPCIEL
```

It begins with the word **BTCSEED**. Getting a meaningful English word out of
a Bifid decode by accident is not realistic, so the square and the method are
almost certainly intended. What the remaining 563 letters mean is unknown.

**Structure of the output (all confirmed by `verify.py`):**

| Fact | Value |
|---|---|
| letters at EVEN positions (0, 2, 4, ...) | 285 letters, only ever `B`, `C`, `D`, `E` |
| letters at ODD positions (1, 3, 5, ...) | 285 letters, any of the 25 letters; they include 13 `I` and 16 `O` |
| odd letters with `I` and `O` removed | exactly 256 letters, over 23 distinct symbols |
| the single `Z` | at position 97 (zero-based) |

**An honest note on that structure.** The even/odd pattern is a mathematical
consequence of the construction, not an extra message: because every FAED
letter lies in rows 0-1, the stream of digits alternates row, column, row,
column of the first 285 FAED letters, so every even output position gets a
row AND a column that are both 0 or 1 -- the top-left 2 x 2 square `D B / C E`.
Odd positions get a column coordinate (0-4) in both slots and can be any
letter. So only the exact counts (256 non-I/O odd letters; 23 distinct
symbols; 16 `O`) are candidates for being meaningful, and those may be
chance. They do, number for number, match the speech's "twenty-three
ciphers, sixteen encryptions and or seven intertwined passwords" (`BTCSEED`
has 7 letters), which is why they are worth recording.

**Lineage.** First posted in Telegram by "Sycorax" on 2025-06-11 (keyword
`dbifhceg`, period 570), independently of the square derivation above; B
PR #8 (2026-06-12, credits a Telegram user "X" and a CyberChef Bifid decode
with key `dbifhceg`); B issue #13 (2026-08-24) with the output file that
matches ours byte for byte; A #112 cites "BTCSEED, sha256 15d62c82..."
without saying what was hashed. C modelled Bifid with 3 x 3 squares, could
not reproduce it, and called it coincidental -- that is not a negative for
the 5 x 5 construction.

## 4. What BTCSEED is NOT (tests run in this archive, 2026-10-15/16)

All of these used an exact, fully offline oracle: a candidate 32-byte scalar
is turned into its secp256k1 public point and compared with the prize's
public key (which is public: it is in the 2020 spending transaction). A
wrong candidate fails with probability about 1 - 2^-160, so these negatives
cannot be false positives, unlike the padding tests of 09. Code and results:
`research/2026-10-15_btcseed_bits/` and `research/2026-10-15_yinyang_ops/`;
summary in `research/2026-10-15_SESSION_JOURNAL.md`.

| Hypothesis | Candidates | Result |
|---|---|---|
| the output IS the 256-bit key: even stream as bits (row, column, 2-bit, all 24 symbol assignments); odd stream minus I/O as 256 bits under six two-colour rules; base-4, base-23, base-25 numbers mod n; 5-bit square indices; prime-position picks; "half + better half" sums of two stream keys; forward and reversed; MSB/LSB/byte-swapped | 640 | 0 prize hits |
| brain wallet: SHA-256 / double SHA-256 / SHA-256 of the hex digest / raw bytes of the exact decoded strings (full output, output after `BTCSEED`, each stream, raw FAED and DBBI, the label words) | 64 | 0 |
| `matrixsumlist` taken literally on the 256 = 16 x 16 payload: 16 row sums + 16 column sums = 32 bytes (five value maps, two fills, two orders, decimal and mod-256 forms) | 80 | 0 |
| "yin yang" as COMBINING the two streams (XOR of parallel bits, packed bytes, sum-merge then SHA-256) | 30 | 0 |
| vanity grind: prize key = seed +/- m for some m below 2^28 (268 million), for every one of the 784 candidate seeds above (baby-step/giant-step) | 784 seeds | 0 |
| the 16 x 16 payload as a picture under six two-colour rules (QR? glyph? a yin-yang?) | 24 images | visual noise |
| operations on DBBI/FAED with the VIC sentence (add/subtract mod 26, three digit maps, forward/reversed) producing the literal milestone word `YINYANG` | 228 | none; the known `YOUWON` (below) reproduces as a control |
| zeros hidden inside one letter or a set of letters of DBBI/FAED under the soup's decimal rule ("zeroed out"), prime-position zero rules, yin-yang folds | exhaustive searches | none (`research/2026-10-15_zero_merge/`) |

So the output is a genuine intermediate, but not the key in any direct,
brain-wallet, matrix-sum, image or small-vanity-offset form, and it does
not come with a generator, a suffix encoding or a checkpoint.

## 5. The 2023 labels and other constructions on DBBI / FAED

| Label or finding | What is known |
|---|---|
| `matrixsumlist` | a literal soup token (08). The community reading "row sums and column sums of the Phase-0 grid" (`610876654997879`, `8108108736759668`) is labelled INFERRED even by its proponents; no creator statement gives its meaning |
| `lastwordsbeforearchichoice` | a literal soup token (08) |
| `yellowblueprimes` | no derivation exists anywhere; a value `7233147103127` circulates only as an undocumented default in one lab script; colour-bit integers and "spiral primes" are solver interpretations. The 2020 "Roses" hint ("Yellow has a number and so does Blue") points at the opening image's 9 yellow and 15 blue squares |
| `yinyang` | no value; the creator calls it "the next phase". Nothing produced the word yet |
| `YOUWON` | subtract the VIC sentence (a = 1 ... z = 26) from DBBI (a = 1 ... i = 9), reduce mod 26, read as letters: `...NBCYOUWONXCP...` -- `YOUWON` at offset 21 (reproduced). 0 of 200,000 shuffles reproduce it, but the layout is forced once the two texts and the digit map are fixed, and the rest of the line is gibberish. Contested |
| b/c expansion | replace d, e, f, g, h, i by bb, bc, cc, bbc, bcc, ccc: DBBI becomes 169 = 13^2 letters, FAED 1,225 = 35^2 (reproduced). The squares are suggestive; no decode follows |
| triangle model (91 = C(14, 2)) | refuted by a random-string control |
| "BYTENPHASE" (A #115) | arithmetic-consistent, with choices its own author calls unjustified |
| capacity | read as a number, FAED is at least 2^1800 (226 bytes) -- it cannot be "seven 32-byte keys" as a plain number |
| the 83/84-token DBBI parses mentioned in an earlier brief | not located in any repository |

## 6. Where to look next (ranked; see the session journal for reasoning)

1. Treat the speech as a literal recipe: "reinsert the prime basics", then
   trial classical ciphers over the output / the 256-letter payload,
   validating ONLY with reject-capable targets (a key whose address is the
   prize; the literal word `yinyang`; readable text) -- never with padding
   or "looks printable".
2. Derive `yellowblueprimes` from the opening image's blue and yellow
   squares at prime positions; no source has tried to define it.
3. A real two-key model ("half and better half"): two scalars that combine
   to the prize scalar, or a second address.
4. DBBI as a transposition key over the output, beyond its first-occurrence
   use.
5. Cross-object "intertwining": the key may need the output together with
   something from the containers in 09.

## 7. Verification pointers

`reproduce.py` steps `salphaseion_soup_sections`, `bifid_full_period_faed`,
`bc_expansion_lengths`; `verify.py` re-implements the Bifid decrypt from
scratch and checks the output, its hash and every structural count above,
and that the DBBI and Bifid strings printed on this page are byte-exact.
The research scripts under `research/2026-10-15_*` are deterministic and
re-runnable.

Sources: `reference/03_UNRESOLVED.md` sections 2-5, `reference/05_COMMUNITY_MECHANISMS.md`,
`reference/04_CREATOR_CLUES.md`, `research/2026-10-15_SESSION_JOURNAL.md`.
