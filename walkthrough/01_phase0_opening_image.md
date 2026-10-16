# Phase 0 -- the opening image is a URL

Status: SOLVED (reproduced)
Where: https://gsmg.io/puzzle (the image was published there in 2019)
Next: [02_phase1_the_form.md](02_phase1_the_form.md)

## 1. Data (what you are given)

One image, `puzzle.png`.

| Item | Value |
|---|---|
| Canonical copy | `reference/artifacts/images/puzzle.png` |
| Size | 1048 x 1556 pixels, 29,931 bytes |
| SHA-256 | `38125bbdf1ea58b9b30b075bc6bf71e4089d04bba37098317e47097e2f2a1830` |
| Provenance | byte-identical in all three source repositories (A, B, C) |

What it shows, top to bottom:

- a 14 x 14 grid of 75-pixel squares. Most squares are black or white; 15 are
  blue (RGB 63,72,204) and 9 are yellow (255,242,0). One "white" square is
  actually `#FEFEFE` (row 7, column 4, counting from 0). A small white-rabbit
  outline is drawn over the centre of the grid;
- a red horizontal line;
- the GSMG logo and the words `GSMG.IO 5 BTC PUZZLE CHALLENGE`;
- a QR code (it encodes the blockchain.com page of the prize address --
  reported, not re-decoded here) and the prize address
  `1GSMG1JC9wtdSwfwApgj2xcmJPAwx7prBe`.

## 2. Clues that apply

None are needed to solve this phase. Two later clues point back to it:

- the 2020-01-14 "Roses" hint ("Yellow has a number and so does Blue. Go back
  to the first puzzle piece ...") -- used in
  [07_decentraland_and_entry_hash.md](07_decentraland_and_entry_hash.md);
- the 2023-02-23 hint whose first two labels are `yellowblueprimes` and
  `matrixsumlist` -- discussed in
  [10_frontier_dbbi_faed_btcseed.md](10_frontier_dbbi_faed_btcseed.md).

## 3. Workings out

**Step 1 -- squares are bits.** Black or blue = `1`; white, yellow (and the
`#FEFEFE` square) = `0`. Reading the grid row by row gives this 14 x 14 matrix
(`verify.py` re-reads it from the PNG and checks it against this table):

```
0 0 1 1 0 1 0 0 1 0 1 1 0 0
1 1 1 1 0 0 1 1 1 0 1 0 1 1
1 1 0 1 1 1 0 1 0 0 1 0 0 1
0 1 1 0 1 0 0 0 0 1 1 1 0 1
0 1 1 0 0 0 1 1 0 0 0 1 1 0
1 0 0 1 1 0 0 0 1 0 0 0 1 1
1 0 0 1 1 1 0 0 0 1 0 0 0 0
1 1 1 0 0 0 0 0 0 0 1 0 0 0
0 0 0 1 1 1 0 1 1 1 1 1 0 1
1 1 1 1 1 1 0 0 1 1 0 0 0 1
1 1 0 1 0 0 0 0 0 1 1 0 1 1
1 1 1 1 0 0 1 0 1 0 1 1 0 0
0 1 0 1 1 1 0 1 0 0 0 1 1 0
0 1 1 0 1 1 0 1 1 0 1 0 1 1
```

**Step 2 -- read the bits in a spiral.** Start at the top-left square, move
DOWN the left column to the bottom-left corner, then right along the bottom
row, up the right column, left along the top row, and keep spiralling inward
(counter-clockwise). That visits all 196 squares once.

**Step 3 -- group into bytes, most significant bit first.** The first eight
bits along the spiral are `0 1 1 0 0 1 1 1`:

```
01100111 = 103 = g
01110011 = 115 = s
01101101 = 109 = m
01100111 = 103 = g
00101110 =  46 = .
01101001 = 105 = i
01101111 = 111 = o
00101111 =  47 = /
01110100 = 116 = t
01101000 = 104 = h
01100101 = 101 = e
01110011 = 115 = s
01100101 = 101 = e
01100101 = 101 = e
01100100 = 100 = d
01101001 = 105 = i
01110011 = 115 = s
01110000 = 112 = p
01101100 = 108 = l
01100001 =  97 = a
01101110 = 110 = n
01110100 = 116 = t
01100101 = 101 = e
01100100 = 100 = d
```

196 bits = 24 bytes + 4 bits left over; the four leftover bits are `0000`.

## 4. Solution

```
gsmg.io/theseedisplanted
```

Go to `https://gsmg.io/theseedisplanted`.

## 5. Verification

| Check | Result |
|---|---|
| `reproduction/scripts/reproduce.py` step `grid_14x14_to_url` | confirmed |
| `walkthrough/verify.py` (independent cell classifier + spiral) | matrix equals the table above; text = `gsmg.io/theseedisplanted`; residual bits `0000`; 101 one-cells |
| image hash | `38125bbd...` as above |

## 6. Extra findings and notes

- Palette of the file: 86 black, 85 white, 15 blue, 9 yellow, 1 `#FEFEFE`
  square. The matrix has 101 ones. Row sums (top to bottom):
  `6 10 8 7 6 6 5 4 9 9 7 8 7 9`; column sums (left to right):
  `8 10 8 10 8 7 3 6 7 5 9 6 6 8`. These sums are the community's reading of
  the later label `matrixsumlist`; that reading is not confirmed by the
  creator (see 10).
- The 24 coloured squares (15 blue + 9 yellow) sit exactly at spiral positions
  7, 15, 23, ..., 191 -- that is, every eighth bit, the LAST bit of each byte.
  Reading blue = 1 and yellow = 0 reproduces the least-significant bit of each
  of the 24 URL bytes. In other words the colours re-encode information that
  is already in the URL (reproduced). Whether they also carry something more
  ("Yellow has a number and so does Blue") is an open question.
- The `#FEFEFE` square is at row 7, column 4 (zero-based); that is spiral
  position 163 (zero-based) and row-major position 102. Values of "103/104"
  or "177" that circulate for it are wrong.
- Corrections to claims found in the sources: "no residual bits" and "one null
  padding byte" are both wrong (there are four zero bits); "87 black / 84
  white" is wrong (86 / 85); the large "matrixsumlist" integer posted by one
  solver (`40585734329412479690520338541901772425587069158131163878976`) is
  simply the URL's bytes read as a number and shifted left by four bits -- it
  carries no new information.
- The text on this image is hashed later to reach the SalPhaseIon page
  (see 07). The QR code and the printed address are the prize address.

Sources: `reference/01_SOLVED_CHAIN.md` section 3.1; A's README section 1;
B's `phase0.ipynb`; C's `verify.mjs`.
