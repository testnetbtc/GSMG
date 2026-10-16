# 01 -- The solved chain

This file is the deduplicated record of every stage that is mechanically solved: the input, the operation, the exact answer string and the output, with sources. Each mechanical claim carries a status (**reproduced** = re-run from fresh code in `reproduction/` with the bytes recorded in `reproduction/results/reproduction_results.json`; **reported**; **interpreted**). Object names follow [08_GLOSSARY.md](08_GLOSSARY.md); citation keys are in [00_INDEX.md](00_INDEX.md).

The A, B and C write-ups ([A:README.md@fb92dd1], [B:README.md@9e61693] with its notebooks, [C:docs/VERIFIED-SOLUTIONS.md@caaa77a] and [C:docs/WALKTHROUGH.md@caaa77a]) describe the same chain. Below, each claim is stated once and cited to every source that makes it. Facts that appear in only one source are marked *(single source)*.

## 1. Overview

```
Phase 0 image --grid--> gsmg.io/theseedisplanted --Phase 1 form--> /choiceisanillusion... (Phase 2 page)
   |                                                                  | ENV-phase2 -causality-> PT-phase2 (riddles, parts 2-7)
   |                                                                  | ENV-phase3 -7-part answer-> PT-phase3 (three riddles + ENV-phase32)
   |                                                                  v
   |                                              ENV-phase32 -3-part answer-> PT-phase32
   |                                                 +- [447:1986] CP1141 -> Beaufort -> SPEECH
   |                                                 +- VIC-DIGITS -checkerboard-> VIC-SENTENCE
   |                                                 +- p32_trailing (unsolved container)
   +- image text --(HASHTHETEXT, from Decentraland audio)--> SHA-256 -> SalPhaseIon page
                                                     +- SOUP: DBBI | matrixsumlist | FAED | z-tokens | salph_inner
                                                     +- cosmic (unsolved container)
```

The diagram records documented navigation, not a proof that every branch belongs to one validated endgame (interpreted; same caution as [reports/MASTER_REASONING_REPORT.md section 3.2]).

## 2. The AES convention (all three solved stages)

1. UTF-8 encode the answer, no trailing newline.
2. Password = the 64 **lowercase hex** characters of SHA-256(answer).
3. Decode base64; check `Salted__`; salt = bytes 8-16.
4. Key||IV = 48 bytes from one-round `EVP_BytesToKey` with **SHA-256** (`D_i = SHA256(D_{i-1} || password || salt)`); key = 32 bytes, IV = next 16.
5. AES-256-CBC; strict PKCS#7.

Status: **reproduced** -- independent Python and the OpenSSL CLI (`openssl enc -d -aes-256-cbc -md sha256 -pass file:`) give identical bytes for all three stages. Negative controls (EVP-MD5, or the raw 32-byte digest as password) fail padding for all three. The convention is documented as source-reproduced in [C:.github/scripts/verify.mjs@caaa77a] and [B:phase2.ipynb@9e61693] (OpenSSL subprocess), and is stated in [A:README.md@fb92dd1] (command without `-md`, which only works on OpenSSL <=1.0.2 per [C:docs/WALKTHROUGH.md@caaa77a#L689]).

Corrections to sources: [C:docs/VERIFIED-SOLUTIONS.md@caaa77a#L266] states "IV = D3[:16]". With SHA-256 the IV is `D2[:16]`. C's own harness does this correctly (reproduced). `Salted__` does **not** fix the KDF; [C:content/attempts.js@caaa77a] (entry at L3626) claims it does -- see [07_CONTRADICTIONS.md](07_CONTRADICTIONS.md).

## 3. Stage by stage

### 3.1 Phase 0 -- opening image -> URL

- Input: `reference/artifacts/images/puzzle.png` (SHA-256 `38125bbd...2a1830`, 1048x1556; byte-identical in A, B, C) [A:puzzle.png@fb92dd1].
- Rule: modal colour per 75-px cell; black/blue = 1, white/yellow (and the single `#FEFEFE` cell) = 0; counter-clockwise spiral from the top-left cell, first move down; MSB-first bytes [A:README.md@fb92dd1#L35-L81] [B:phase0.ipynb@9e61693] [C:.github/scripts/verify.mjs@caaa77a].
- Output (**reproduced**):

```text
gsmg.io/theseedisplanted
```

followed by **four zero bits** (196 = 24x8 + 4). Claims of "no residual bits" or "one null padding byte" [C:docs/verify-findings.json@caaa77a] are wrong.
- The 24 blue/yellow cells sit at spiral indices == 7 (mod 8), and blue=1/yellow=0 equals each URL byte's least-significant bit (**reproduced**). The colours therefore re-encode bits already in the URL [B:phase0.ipynb@9e61693] [A:_pr93/FINDINGS.md@2c97f44#L44-L48] [C:.github/scripts/verify.mjs@caaa77a].
- Palette of the held file (**reproduced**): 86 black, 85 white, 15 blue `(63,72,204)`, 9 yellow `(255,242,0)`, 1 `#FEFEFE` cell at (row 7, col 4) zero-based. That is spiral index 163 (zero-based) and row-major index 102. Matrix: 101 ones; row sums `[6,10,8,7,6,6,5,4,9,9,7,8,7,9]`, column sums `[8,10,8,10,8,7,3,6,7,5,9,6,6,8]`.
- The QR code decodes to `https://www.blockchain.com/btc/address/1GSMG1JC9wtdSwfwApgj2xcmJPAwx7prBe` (reported [B:_pr15/neo/LEDGER.md@1e913fd#L997-1009] [C:docs/WALKTHROUGH.md@caaa77a#L283-L285]; not re-decoded here).

### 3.2 Phase 1 -- the form

- Images and URL point to the song "The Warning" by Logic. The line after "Phase two" is the answer [A:README.md@fb92dd1#L87-L90] [B:README.md@9e61693] [B:phase1.ipynb@9e61693]. C identifies "Logic" as the 1990 Strictly Rhythm house project of Wayne Gardiner and Eddie Maduro, not the rapper *(single source, reported)* [C:docs/VERIFIED-SOLUTIONS.md@caaa77a#L74].

```text
theflowerblossomsthroughwhatseemstobeaconcretesurface
```

- SHA-256 = `5ac407837447fba24ba2802e4d1e9aecb4580aa29fef1088cc387c180b746f75`. This equals the checkpoint posted under the creator-attributed handle on 2019-04-22 (message 225) [C:content/sowut-data.js@caaa77a id 225]. The hash equality is **reproduced**; that the form accepted the answer is **reported** from B's stored notebook output, which shows `FOUND REDIRECT ... http://gsmg.io/choiceisanillusioncreatedbetweenthosewithpowerandthosewithoutaveryspecialdessertiwroteitmyself` [B:phase1.ipynb@9e61693 cell 2]. No live form was contacted for this archive.

### 3.3 Phase 2 -- `ENV-phase2`

```text
causality
```

- SHA-256 password `eb3efb5151e6255994711fe8f2264427ceeebf88109e1d7fad5b0a8b6d07e5bf` -> `PT-phase2`, 648 bytes, SHA-256 `e2f9dd65...593a` (**reproduced**) [A:README.md@fb92dd1#L92-L110] [B:phase2.ipynb@9e61693 cell 1] [C:docs/VERIFIED-SOLUTIONS.md@caaa77a].
- Parts 2-4 `Safenet`, `Luna`, `HSM` (Mr Robot eps3.4 / SafeNet Luna HSM) [A:README.md@fb92dd1] [B:phase2.ipynb@9e61693 cell 3].
- The `X 2 S H 4 Y 0 Q B 15` equation: S = 32 (Klingon cha' + vagh-jav). B resolves Q = 82 and H = 42; with B = 25 it yields coordinates 51 deg52'28.0"N 4 deg24'23.2"E, which B describes as "VERY close" to SafeNet Technologies [B:phase2.ipynb@9e61693 cell 4] *(single source; reported -- checked only by B's image)*. A gives only S = 32 and B = (4i)^2 = -16 [A:README.md@fb92dd1#L122]; A PR #68 lists H, Q, Y as unknown (stale) [A:_pr68/GAP_ANALYSIS.md@27ea50e#L68-L79].
- Part 5 `11110`: B says it was found by brute force over eight JFK executive orders, with no known derivation [B:README.md@9e61693#L115] [B:phase2.ipynb@9e61693 cell 5]. Reading it as EO 11110 is **interpreted** [B:unverified/11110.md@9e61693] [A:README.md@fb92dd1#L148].
- Part 6: `0x` + uppercase hex of the **reversed** genesis-block headline [A:README.md@fb92dd1#L150-L158] [B:README.md@9e61693].
- Part 7: from `B5KR/1r5B/6R1/2b1p1p1/2P1k1P1/1p2P2p/1P2P2P/3N1N2 w - - 0 1` the only non-mating white move is Rc6. The resulting FEN is the answer, **with** its spaces and `0 1` [A:README.md@fb92dd1#L160-L168] [B:phase2.ipynb@9e61693 cell 7] [B:_pr15/neo/LEDGER.md@1e913fd#L1754-1763]. The engine-style `... b - - 1 1` hashes to `53b27a4e9763...` and fails *(single source, reported)* [C:docs/VERIFIED-SOLUTIONS.md@caaa77a#L119].
- Case and spacing markers: `aaa` = lowercase, `aBa` = mixed case, "connected enf" = no spaces, "connected not enf" = keep spaces [B:phase2.ipynb@9e61693 cell 10] [A:README.md@fb92dd1].

### 3.4 Phase 2.2 -- `ENV-phase3` (the seven-part answer)

227 characters (**reproduced**):

```text
causalitySafenetLunaHSM111100x736B6E616220726F662074756F6C69616220646E6F63657320666F206B6E697262206E6F20726F6C6C65636E61684320393030322F6E614A2F33302073656D695420656854B5KR/1r5B/2R5/2b1p1p1/2P1k1P1/1p2P2p/1P2P2P/3N1N2 b - - 0 1
```

- SHA-256 password `1a57c572caf3cf722e41f5f9cf99ffacff06728a43032dd44c481c77d2ec30d5` -> `PT-phase3`, 4,090 bytes, SHA-256 `c4ad9455...865f` (**reproduced**) [A:README.md@fb92dd1#L192] [B:phase2.ipynb@9e61693 cell 11] [C:docs/VERIFIED-SOLUTIONS.md@caaa77a].
- B's README carries the full string. The truncated `...B5KR` rendering survives only in old snapshots [A:_pr16/README.md@f646872#L102] [A:_pr30/README.md@290c334#L104]. C's statement that B's README truncates it is stale (see 07).

### 3.5 Phase 3 -- `ENV-phase32` (the three-part answer)

62 characters (**reproduced**):

```text
jacquefrescogiveitjustonesecondheisenbergsuncertaintyprinciple
```

- Venus Project -> Jacque Fresco; Alice "how long is forever ... sometimes, just one second" -> `giveitjustonesecond`; Heisenberg's uncertainty principle [A:README.md@fb92dd1#L262-L266] [B:phase3.ipynb@9e61693].
- SHA-256 password `250f37726d6862939f723edc4f993fde9d33c6004aab4f2203d9ee489d61ce4c` -> `PT-phase32`, 2,422 bytes, SHA-256 `b82afeb8...8a34` (**reproduced**).
- The creator-attributed handle acknowledged that `giveit` should have been `givetit` and that the puzzle had been tested "3 times with the same string which had the typo". The hint "giveit = givetit" was posted 2019-05-17 [C:content/sowut-data.js@caaa77a ids 866-875] [A:_pr93/_work/chat_transcript.txt@2c97f44 L2069-L2100]. The answer that actually decrypts keeps `giveit` (**reproduced**).
- The spelling `heisenbergs` (with s) is required; C's [C:docs/WALKTHROUGH.md@caaa77a#L2226] typo `heisenberguncertainty...` would fail.

### 3.6 Phase 3.2 -- speech, VIC sentence, trailing container

`PT-phase32` holds a Matrix-Architect preamble, a 1,539-byte high-bit region, `VIC-DIGITS`, a riddle line and the `p32_trailing` base64 [A:README.md@fb92dd1#L275-L287].

**Speech** (**reproduced**; iconv `IBM1141` and Python `cp273` agree): take `PT-phase32[447:1986]` as Latin-1 characters and encode to CP1141 (all lowercase a-z). Then Beaufort `p = (k - c) mod 26` with key `thematrixhasyou`. Output: 1,539 letters, SHA-256 `90829b510c3697569da47d2817f545f1e2a1cddd78e45f821dafcdab3dc0c281`, beginning `yourlifeisthesumofaremainder...` and ending `...ireallyhopeyouretheoneciaobellao`. Full text: `reproduction/results/phase32_speech.txt`. Sources: [A:README.md@fb92dd1#L293-L321] [B:phase3.2.ipynb@9e61693] [C:.github/scripts/verify.mjs@caaa77a#L73-L85]. B's codec scan reports cp273 also gives 100% letters *(single source; consistent with reproduction)* [B:phase3.2.ipynb@9e61693 cell 8]. Speech passages often cited as clues (exact):

```text
...reinsertingtheprimebasicsafterwhichyouwillberequiredtoselectfromovertwentythreecipherssixteenencryptionsandorsevenintertwinedpasswordstofindtheactualprivatekeynotethatalsobruteforcingmightberequired...
...whatawisemanabovehintedatisworthhundredfourtyoftheinvestment...
```

**VIC sentence** (**reproduced**): straddling checkerboard over the 149 digits, with blank top-row columns 1 and 4. Top row `f u b c d o r a` in columns 0,2,3,5,6,7,8,9; row 1 = `/lethingky`; row 4 = `mvpszjqwx.`. Alphabet `fubcdora/lethingkymvpszjqwx.` [B:README.md@9e61693#L140] [B:phase3.2.ipynb@9e61693 cell 16]:

```text
incaseyoumanagetocrackthistheprivatekeysbelongtohalfandbetterhalfandtheyalsoneedfundstolive
```

A gives two alphabet strings, `FUBCDORA.LETHINGKYMVPS/JQZXW` and `FUBCDORA.LETHINGKYMVPS.JQZXW` [A:README.md@fb92dd1#L332-L336]. They differ only in letters absent from this plaintext, so the decode is the same (interpreted from the reproduced decode). B states the alphabet was found by trying "every cipher that can be found in online tools" [B:phase3.2.ipynb@9e61693 cell 16].

**`p32_trailing`**: the final 128 base64 characters (two 64-char CRLF lines). See [02_ARTIFACTS.md](02_ARTIFACTS.md) and [03_UNRESOLVED.md](03_UNRESOLVED.md).

### 3.7 Decentraland audio -> `HASHTHETEXT`

- The creator-attributed handle posted a Decentraland screenshot at parcel -41,-17 on 2020-02-20, then "Only -41,-17 matters" on 2020-02-22 [C:content/sowut-data.js@caaa77a ids 1743, 1837] [B:README.md@9e61693]. The parcel is named "GSMG.io Puzzle piece" (reported) [C:docs/WALKTHROUGH.md@caaa77a#L1580].
- Audio `puzzlepiece.mp3`, content id `QmeRy5MjmEZ2W6J3DwhQfht5HKBKXBFpoGzSkzmjeGKiDK` [B:decentraland.ipynb@9e61693].
- Rule: left - right channel, then spectrogram, then read hex numerals. Output (**reproduced, visual reading**):

```text
48 41 53 48 54 48 45 54 45 58 54  ->  HASHTHETEXT
```

Our rendering is `reproduction/results/audio_LminusR_spectrogram.png`. The eighth group sits under a broadband transient near 3.4 s and is only partly legible; "54" there rests on the partial glyph plus context. B's `invert_data` evaluates `(-1**i)*x` as plain negation, i.e. L-R, not an alternating sign *(N5 code reading)*. Signal band <= ~7.97 kHz (reported) [C:docs/VERIFIED-SOLUTIONS.md@caaa77a#L188]. A notes the same method [A:README.md@fb92dd1#L343-L347]. A PR #30 contributor appended a note to the notebook saying the in-world sound is broken in some desktop/browser clients, a nearby "door" does nothing, and the original files are no longer downloadable *(single source, reported)* [A:_pr30/decentraland.ipynb@290c334 trailing text].

### 3.8 SalPhaseIon entry

Hash the text on the opening image (59 characters, **reproduced**):

```text
GSMGIO5BTCPUZZLECHALLENGE1GSMG1JC9wtdSwfwApgj2xcmJPAwx7prBe
```

```text
89727c598b9cd1cf8873f27cb7057f050645ddb6a7a157a110239ac0152f6a32
```

The page is `https://gsmg.io/89727c598b9cd1cf8873f27cb7057f050645ddb6a7a157a110239ac0152f6a32` [A:README.md@fb92dd1#L361-L363] [B:README.md@9e61693]. B's README once spells it `gmsg.io` (typo). The recipe was **posted by a "Deleted Account" on 2021-05-06**, not by the creator-attributed handle [A:_pr93/_work/chat_transcript.txt@2c97f44 L18392-L18410]. B and C call it "revealed"/"official" -- see 07. A trailing newline gives `8784851d...` instead (reported) [C:docs/VERIFIED-SOLUTIONS.md@caaa77a#L202].

### 3.9 SalPhaseIon soup -- the solved tokens

`SOUP` is 1,075 letters with spaces removed. Three copies agree byte-for-byte after whitespace removal (**reproduced**): B's notebook [B:salphaseion.ipynb@9e61693 cell 0], B PR #15's primary text [B:_pr15/neo/materials/primary/salphaseion_soup_space_separated.txt@1e913fd], and the first textarea of the archived SalPhaseIon page as supplied in B PR #15 (Wayback 2024-11-23 and 2025-10-31). Layout (**reproduced**):

| Offsets / piece | Rule | Output |
|---|---|---|
| `[0:91]` `DBBI` | -- | unsolved (see 03) |
| `[91:195]` a/b block | a=0, b=1, 8-bit MSB-first ASCII | `matrixsumlist` |
| `[195:765]` `FAED` | -- | unsolved (see 03) |
| `z` agda... `z` | a-i = 1-9, o = 0 -> decimal integer -> minimal big-endian bytes | `lastwordsbeforearchichoice` |
| cfob... `z` | same | `thispassword` |
| plain text | -- | `shabefourfirsthintisyourlastcommand` |
| base64 || a/b insertion || base64 | a/b -> ASCII | inserted word `enter`; removing it joins two 64-character halves into `salph_inner` |
| tail | -- | `shabefanstoo` |

Sources: [A:README.md@fb92dd1#L371-L391] [B:salphaseion.ipynb@9e61693 cells 3-12] [C:docs/VERIFIED-SOLUTIONS.md@caaa77a#L210-L213]. The a-i/o fields are **decimal**, not base-9 as [C:docs/WALKTHROUGH.md@caaa77a#L1783] says. The `z` immediately before the `enter` insertion is the 64th base64 character of `salph_inner`, not a separator (reported, [C:docs/VERIFIED-SOLUTIONS.md@caaa77a#L210-L213]; consistent with the reproduced reassembly).

## 4. What is *not* solved

Everything after section 3.9 is open: `DBBI`, `FAED`, `salph_inner`, `p32_trailing`, `cosmic`, `urlblob`, and the meaning of the 2023 hint labels. Community constructions that open `salph_inner`, `p32_trailing` and `cosmic` with valid padding are mechanically reproduced. They are **not** established stages; see [03_UNRESOLVED.md](03_UNRESOLVED.md) and [05_COMMUNITY_MECHANISMS.md](05_COMMUNITY_MECHANISMS.md).
