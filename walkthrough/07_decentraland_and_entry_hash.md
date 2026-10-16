# Decentraland -- the audio says HASHTHETEXT, the "Roses" hint says which text

Status: SOLVED (hash reproduced; the audio reading is visual)
Where: Decentraland parcel -41,-17 ("GSMG.io Puzzle piece"); then https://gsmg.io/puzzle
Previous: [06_phase3_2_speech_and_vic.md](06_phase3_2_speech_and_vic.md) --
Next: [08_salphaseion_soup.md](08_salphaseion_soup.md)

## 1. Data (what you are given)

Two creator-attributed posts and one audio file:

| Date | What | Where kept |
|---|---|---|
| 2020-01-14 | the "Roses" hint (typed text, below) | `reference/artifacts/hints/2020-01-14-roses-are-red.png`; C dataset id 1710 |
| 2020-02-20 | a Decentraland screenshot at parcel -41,-17; on 2020-02-22: "Only -41,-17 matters" | `reference/artifacts/hints/2020-02-20-decentraland.jpg`, `creator_media/1743.jpg`; ids 1743, 1837 |
| (in-world) | the parcel "GSMG.io Puzzle piece" plays a sound file | `reference/artifacts/audio/puzzlepiece.mp3` (content id `QmeRy5MjmEZ2W6J3DwhQfht5HKBKXBFpoGzSkzmjeGKiDK`; SHA-256 `ef17a96dce37b4dd7cbf79f210c5cbaf37fcae60e5faf8004de4e0832bd0dfee`) |

The "Roses" hint, verbatim:

```
Roses are White but often Red.
Yellow has a number and so does Blue.
Go back to the first puzzle piece without further ado.

It might have shown you only one door, beware that the rabbits nest may
contain a whole lot more.

Hush hush.
```

## 2. Clues that apply

- "Go back to the first puzzle piece" = the opening image of Phase 0.
- "may contain a whole lot more" = the first image hides more than the URL.
- The audio (next section) literally says what to do with it.

## 3. Workings out

**The audio.**

1. Decode `puzzlepiece.mp3` to stereo PCM (ffmpeg, 44.1 kHz, 229,248
   samples).
2. Subtract the right channel from the left. The music that is identical in
   both channels cancels (the signal's RMS drops from about 4,637 to about
   495) and the hidden part remains.
3. Draw a spectrogram of the difference signal (NFFT 2048, overlap 1536):
   `reproduction/results/audio_LminusR_spectrogram.png`. Hexadecimal
   numerals are drawn into the time-frequency plane:

   ```
   48 41 53 48 54 48 45 54 45 58 54
   ```

4. Read them as ASCII: `H A S H T H E T E X T` = **HASHTHETEXT**.

**Which text?** The Roses hint points back to the first puzzle piece. Its
printed text, taking letters and digits only (the dot in `GSMG.IO` and the
spaces are dropped), is 59 characters:

```
GSMGIO5BTCPUZZLECHALLENGE1GSMG1JC9wtdSwfwApgj2xcmJPAwx7prBe
```

SHA-256 of that text (UTF-8, no trailing newline):

```
89727c598b9cd1cf8873f27cb7057f050645ddb6a7a157a110239ac0152f6a32
```

and `https://gsmg.io/89727c598b9cd1cf8873f27cb7057f050645ddb6a7a157a110239ac0152f6a32`
is a real page: SalPhaseIon (next file).

## 4. Solution

- `HASHTHETEXT`
- the page `https://gsmg.io/89727c598b9cd1cf8873f27cb7057f050645ddb6a7a157a110239ac0152f6a32`

## 5. Verification

| Check | Result |
|---|---|
| `reproduce.py` step `audio_LminusR_spectrogram` | confirmed. Read by eye from the rendered PNG. The eighth group sits under a broadband transient near 3.4 s and is only partly legible; "54" there rests on a partial glyph plus context (every other reading of the word is clear). |
| `reproduce.py` step `salphaseion_entry_hash` | confirmed |
| `verify.py` | text length 59, hash as above, mp3 hash as above |
| the page exists | two archived captures of it are held (2024-11-23, 2025-10-31) and contain the SalPhaseIon soup and the Cosmic Duality envelope (reproduced against the captures as supplied in B PR #15; not refetched by this archive) |

## 6. Extra findings and notes

- Who said to hash exactly that text: the instruction ("hash the text on the
  puzzle image") was posted in Telegram on 2021-05-06 by a **Deleted
  Account**, not by the creator-attributed handle. B and C call it
  "revealed" / "official"; it is community knowledge whose result happens to
  be a real page. A solver added at the time: "We did say to hash the text..".
- Appending a newline to the text gives `8784851d...` instead -- a common
  mistake.
- B's README once spells the domain `gmsg.io` (a typo).
- Reported by a contributor (A PR #30): the in-world sound was broken in some
  desktop/browser clients, a nearby "door" does nothing, and the original
  files are no longer downloadable from the world. The mp3 is preserved in
  B's assets and here.
- B's `invert_data` function multiplies one channel by -1 and sums, which is
  the same as left minus right.
- The creator-attributed handle later said "a few might not require the
  internet anymore" (2021-01-21) and, to "Given the available knowledge, is
  internet still required to solve it?", answered "Nope" (2023-11-24).
- "Yellow has a number and so does Blue" has never been given a confirmed
  meaning beyond the LSB observation of Phase 0; see 10 and 11.

Sources: `reference/01_SOLVED_CHAIN.md` sections 3.7-3.8; `reference/04_CREATOR_CLUES.md`
(ids 1710, 1743, 1837, 5717, 16624); `reference/02_ARTIFACTS.md`; A's README
"Additional hints"; B's `decentraland.ipynb`.
