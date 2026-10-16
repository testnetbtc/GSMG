# Phase 1 -- the form at /theseedisplanted

Status: SOLVED (answer reproduced by hash; form acceptance reported)
Where: https://gsmg.io/theseedisplanted
Previous: [01_phase0_opening_image.md](01_phase0_opening_image.md) --
Next: [03_phase2_causality_and_riddles.md](03_phase2_causality_and_riddles.md)

## 1. Data (what you are given)

The page shows eight coloured tiles and nothing else visible
(`reference/artifacts/images/theseedisplanted.png`; the same tiles rearranged
in `warning-logic.png`; the page source in `phase1-source.png`):

```
[war]   [CA]   [dig i +]   [io]   [crypto gic]   [n you]   [n ing]   [t -]
```

Two of the tiles (`war` and `io`) carry a padlock icon. Hidden in the page
source is an HTML form that POSTs to `/phase1verification` (reported by A's
README; B's notebook `phase1.ipynb` submits to it).

## 2. Clues that apply

- `war` + `n ing` = WARNING. The padlock icon stands for "lock" -> `LO`, and
  `LO` + `gic` (from the `crypto gic` tile) = LOGIC. Together: the song
  "The Warning" by Logic. The remaining tiles are part of the same picture and
  are not needed for the answer.
- In that song a spoken passage announces "Phase two"; the line that follows
  it is the answer.
- The puzzle's own formatting rule, spelled out later on the Phase-2 page as
  `(aaa, connected enf)`: all lowercase, no spaces.

## 3. Workings out

1. Identify the song from the tiles: "The Warning" by Logic.
2. Take the line that follows "Phase two" in the lyrics:
   "the flower blossoms through what seems to be a concrete surface".
3. Lowercase it and remove the spaces.
4. In the browser's developer tools, unhide the form, paste the answer and
   submit. The server redirects to the Phase-2 page.

## 4. Solution

```
theflowerblossomsthroughwhatseemstobeaconcretesurface
```

(53 characters.) The redirect target is

```
https://gsmg.io/choiceisanillusioncreatedbetweenthosewithpowerandthosewithoutaveryspecialdessertiwroteitmyself
```

## 5. Verification

- SHA-256 of the answer is
  `5ac407837447fba24ba2802e4d1e9aecb4580aa29fef1088cc387c180b746f75`.
  On 2019-04-22 the creator-attributed handle posted exactly this hash and
  wrote "just try hit your options against that hash." It is the ONLY
  creator-published checkpoint in the whole puzzle. The equality is
  reproduced (`verify.py`: `phase1`).
- That the form accepted the answer and redirected is reported from B's
  stored notebook output (`FOUND REDIRECT ... /choiceisanillusion...`). This
  archive never contacted the live site; gsmg.io has been parked since
  2026-07.

## 6. Extra findings and notes

- The hash was released because, in the creator's words, "the website was
  giving a lot of token errors" (message id 257) -- it let solvers check an
  answer offline.
- C suggests that "Logic" may be the 1990 house project of Wayne Gardiner and
  Eddie Maduro rather than the rapper (single source, reported). The answer
  is fixed by the hash either way.
- A 2026-04-05 capture of the Phase-2 page carries an HTML comment,
  `You made it to the next step! Good luck little bunny hunter ;)`, that is
  absent from the 2020 and 2022 captures. Who added it is unknown.

Sources: `reference/01_SOLVED_CHAIN.md` section 3.2; `reference/04_CREATOR_CLUES.md`
(ids 225, 226, 257); A's README section 2; B's `phase1.ipynb`.
