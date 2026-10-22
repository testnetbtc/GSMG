# FUNNEL -- Task 1, Stages C and D: ten ideas, scored, cut to one

Section 0 (the five laws) was re-read before writing the cards. Clue IDs are from `CLUES.md`;
pool IDs (P-nn) and report ways (R?-W?) are from `REPORT_ANALYSIS.md`. No experiment was run in
this stage: every number below is a specification, a count of candidates, or a held hash.

Uniqueness: each idea differs in what is acted on, the operation, or how success is recognised.
Four come from the reports' pool (W-02, W-03, W-05, W-08's neighbour R6-W2 is *not* used; see
W-08's origin); six are new or reworked from the shared blind spots (`REPORT_ANALYSIS.md` B.3).
Four are non-computational (W-04, W-05, W-09, W-10). A planned eleventh, "the 24 colour bits as
a selector/zero mask over DBBI/FAED" (R5-W1a), was dropped before carding: B PR#15 campaigns 13
and 19 ran exactly that (409,920 trials, selection and zeroing by colour bit, both index bases,
on the FAED remainder, DBBI's 24 prime positions and the 7x13 matrices) with a gate that accepts
readable text; no flaw found -> `GRAVEYARD.md`.

Held inputs cited by hash (SHA-256, bytes):

| Path | SHA-256 | Bytes |
|---|---|---|
| `reference/artifacts/images/puzzle.png` | `38125bbdf1ea58b9b30b075bc6bf71e4089d04bba37098317e47097e2f2a1830` | 29,931 |
| `reference/artifacts/pages/salphaseion_soup.txt` | `d39d10b1e1902d2620eb19ebcad4215e23c048de639466cca9a26bdc9303330c` | 2,149 |
| `reference/artifacts/envelopes/salph_inner.b64.txt` | `f8b89da595f868906e14d254d8079d70033153f1dfaa603821dcc641987836d0` | 128 |
| `reference/artifacts/envelopes/cosmic.b64.txt` | `92f9dddfdf5cb8722727c95e0120782af3c4fb4c3c78490923e83758760604c5` | 1,792 |
| `reference/artifacts/envelopes/p32_trailing.b64.txt` | `b2e3f02fd7b79b9a0a85b9286d2b1f4e0e749171b3107d34ffc6b0b6fc2bdf5e` | 128 |
| `reference/artifacts/audio/puzzlepiece.mp3` | `ef17a96dce37b4dd7cbf79f210c5cbaf37fcae60e5faf8004de4e0832bd0dfee` | 212,031 |
| `reproduction/results/chain1.bin` | `1449a2178eea7c0e3fabac8c1ad2afa294be4fc1800c594a025a056e88c626bf` | 79 |
| `reproduction/results/chain2.bin` | `b40fce72ef5638e4f79b3233e653f8a5dbdb0d4ae2009d2d3da2c98b70f4d004` | 79 |
| `reproduction/results/cosmic_output.bin` | `4f7a1e4efe4bf6c5581e32505c019657cb7b030e90232d33f011aca6a5e9c081` | 1,327 |
| `reproduction/results/chain4.bin` | `e4269ed5fbb202a81e5e1aa6b5190fdd1ea126b2c8547ea7cdbdf45387ea135b` | 1,151 |
| `sources/naddiseo/_pr15/unverified/drive-2026-05/cosmic_A.bin` | `cd3fea3d697a7fbf...` (full hash in `reference/data/SOURCE_LINEAGE.csv`) | 1,327 |
| `sources/naddiseo/_pr15/unverified/drive-2026-05/ca158_hidden_blob.bin` | `d895da1ba96e924c...` | 1,169 |
| `sources/naddiseo/_pr15/unverified/drive-2026-05/chain2_decrypted.bin` | `74f0e46cdb463748...` | 1,151 |
| `reproduction/results/bifid_full.txt` | `0c5d984f90e9baefc09f1d3888e62acbd101f9b0194887e2ae88fc6c9967745e` | 570 |
| `reproduction/results/dbbi.txt` / `faed.txt` | `71fe4625...c5ca` / `066191b4...f3c2` | 91 / 570 |
| `reproduction/results/phase32_speech.txt` | `90829b510c3697569da47d2817f545f1e2a1cddd78e45f821dafcdab3dc0c281` | 1,539 |
| `research/2026-10-15_btcseed_bits/btclib.py` | `9a3848423c2cc5e5c6429ea205621963ebf33ef1cb1bac4ddc1f216be01f1755` | 6,054 |

Common success test used by the container ideas (W-01, W-03, W-06; written once here):
**S1** valid PKCS#7 and a plaintext that is >= 95% printable ASCII and contains >= 3 words of a
fixed English word list (every solved plaintext meets this); or **S2** a plaintext containing a
64-hex or WIF string whose secp256k1 point equals the prize point, or whose hash160 (either
compression) equals the prize's or `17ucy1...`'s, via `btclib.py`; or **S3** a nested
`Salted__` header at offset 0. Padding validity alone is never success.

---

## Stage C -- the ten cards

### W-01  Clear the marked bit (prime-position LSB zeroing of the first piece)
Origin: new (blind spot B.3-1), narrowed after finding character-level zeroing in the records.
One-paragraph description: The opening image marks the least significant bit of each of the 24
URL bytes in colour (A-10: blue = 1, yellow = 0; reproduced). Read C-25 literally on that
object: "characters" = the 24 URL characters; "zeroed out" = set the marked bit to 0; "prime
numbers ... required to proceed" = do it at the characters whose position is prime. The result
is a modified string S. By the solved-stage convention the next answer is used as sha256hex(S),
tried as the password of each held container. (A would-be URL `gsmg.io/<sha256hex(S)>` is
recorded for the user but cannot be fetched: the site is parked, and C-17/C-32 say the rest is
offline anyway, so the door's content must be a password or key, not a page.)
Stage acted on and exact inputs: the "another door" of the first piece (C-14, C-24, C-25) ->
the next container. Inputs: `puzzle.png` (hash above) and its derived URL + coloured-cell
indices (`reproduce.py` step `grid_14x14_to_url`); the three containers (hashes above).
Clues used -> how:
  C-25 "some characters need to be 'zeroed out'" / "prime numbers ... required to proceed" -> the operation (clear the bit) and the selector (prime positions)
  C-06 "Yellow has a number and so does Blue. Go back to the first puzzle piece" / "rabbits nest may contain a whole lot more" -> the object (the coloured bits of the opening image) and the promise of a second door there
  C-13 "answer is there" / "First or zero" -> the first piece is Phase 0; "zero" names the operation
  C-28 `yellowblueprimes` (first label) / "its in front of your eyes but youre not seeing it" -> the label names exactly {yellow, blue, primes}; the bits are literally visible
  C-14, C-24 "extra door" unfound 2020-08 and 2021-12 -> the door is not the SalPhaseIon route
  C-17, C-32 offline -> the door yields a password, not a URL
  A-01 "parts -> sha-256 -> dgst is the password", aes-256-cbc -> the test convention
  A-10 the LSB structure (reproduced) -> the bit to clear
Clues it contradicts: none.
Prior attempts and why flawed / why missed: C `EXT-E0098` (attempts.js L862-872): "URL chars at
prime / small-prime positions, URL with non-prime (or prime) positions zeroed out" tested alone
and inside the Cosmic recipe -- scripts not shipped (`reference/06` section 1), zeroing
semantics unstated; its DBBI sibling (attempts.js L1738-1748) defines "zeroed out" as forcing
the digit 0, deleting, or inserting '0'; validator printable > 0.92 or >= 2 words; KDF SHA-256.
B PR#15 campaign_06: one `zero:url-yellow->0` candidate (yellow characters -> '0').
B campaigns 13/19: zeroing by colour bit on the FAED remainder and DBBI's prime positions, not
the URL. The gap: no record clears the *bit the colour marks*; every record replaces or deletes
characters. Why missed: solvers held that the colours "just mark the LSB ... no more information
to extract" [T L21871, L31809], and "zeroed out" was read through the soup's `o` = 0 digit
(B campaigns 06/08; C's DBBI entry).
Every parameter and its source: polarity blue = 1 <- A-10 (reproduced); operation = clear the
marked bit <- C-25 + A-10; prime positions <- C-25; index convention <- FREE: {spiral index of
the coloured cell: primes 7, 23, 31, 47, 71, 79, 103, 127, 151, 167, 191; 1-based character
index: 2, 3, 5, 7, 11, 13, 17, 19, 23; 0-based character index} (3 values); password =
sha256hex(S) <- A-01; KDF EVP SHA-256 one round <- A-01; targets = `salph_inner`, `cosmic`,
`p32_trailing` <- A-07, A-08, A-09.
Count of FREE parameters: 1 (3 values, fully enumerated). Candidate strings (computed from the
held URL, nothing decrypted): spiral -> `fslf.ho/thesdedhsplanted`; 1-based ->
`grlg.in/thdsdedirplantdd`; 0-based -> ``gslf.ho.thereddispl`nted``. 3 x 3 = 9 decrypts.
Success test: S1 / S2 / S3 above. Negative criterion: none of the 9 decrypts meets S1-S3.
Cost / bounds / stop: < 1 s; exactly 9 decrypts; stop after them.
Inputs not held: none.
Why hasn't someone already done this? The bit-level reading was never applied; the
character-level readings were, and are unauditable.

### W-02  Exact-oracle sweep over the held "openings"
Origin: taken from R6-W1 / R5-W3b (pool P-18).
One-paragraph description: Every community "opening" is a padding-valid byte string that was
only ever inspected through imposed field layouts (32/32/15; 103x103) or text gates. Slide an
exact key oracle over all of them: for every byte-aligned 32-byte window, derive the secp256k1
point of the scalar and of its byte-reversal, double and half (A-06 "half and better half"),
and compare with the prize point; compare hash160 of both encodings with the prize's and
`17ucy1...`'s hash160; also regex-scan each file for ASCII hex-64 and WIF substrings. Run it
on the chain outputs, the Cosmic outputs, the drive files and, as controls, the 2023 A#15
outputs. A match is a solve; a clean negative retires "the key sits in these bytes" for good.
Stage acted on and exact inputs: the M5/M6/M8/M15 outputs (`reference/05`). Inputs:
`chain1.bin`, `chain2.bin`, `cosmic_output.bin`, `chain4.bin`, `cosmic_A.bin`,
`ca158_hidden_blob.bin`, `chain2_decrypted.bin` (hashes above); the two A#15 control outputs
recomputed by `reproduce.py` (`a15_padding_controls`: 79 B `c27ea25d...`, 1,327 B); the two
103x103 32-byte values (`0423d911...`, `48cc46e6...`). Targets: the prize public key
`04f4d1bb...3559` (held in `sources/naddiseo/_pr15/neo/materials/chain/tx_halving_spend.hex`,
reproduced), its hash160, and the hash160 of `17ucy1K9ZUAaoY6JVtM932W9jUp5LXfyHa`.
Clues used -> how:
  C-33 "Regular Bitcoin Private key" -> the object sought is a 256-bit scalar; both encodings tested
  C-23 "The one to be found by solving the puzzle yes" / "the solver will find a way to 'decrypt' it" -> the key may sit raw in a decrypted container
  C-10 "There must at least be something hidden in there" (Phase 3.2) -> `p32_trailing`'s claimed output (chain2) is in scope
  A-06 "the private keys belong to half and better half" / C-12 "Well spotted" (half -> better half) -> the second target `17ucy1...` and the x2 / /2 transforms
Clues it contradicts: none (it is a closure test; a positive would make the MD5 recipes intended, which A-01's convention does not predict).
Prior attempts and why flawed / why missed: `reference/03` section 1.1 compared K_S1/K_S2 as
uncompressed addresses only; `EXT-E0087` (C) checked posted keys, dbbi/faed bytes and split
halves; B LEDGER L1349: "No sliding windows, no substrings"; `research/2026-10-15` used the
exact oracle on BTCSEED-derived scalars only; C's "universal inspector" (2026-07-13) used
"fixed readings" and its scripts are not shipped. Why missed: the proposers imposed layouts
and checked only those fields; everyone else used text gates.
Every parameter and its source: window = 32 bytes <- C-33; offsets = every byte offset (exhaustive,
no choice); transforms = {identity, byte-reversal <- solved-stage convention (Phase 2.2 part 6
reversal; the 2023 binary reversal), x2 mod n and /2 mod n <- A-06/C-12}; encodings = both <-
C-33 leaves compression unspecified; targets <- A-06/C-12.
Count of FREE parameters: 0.
Success test: exact equality of a derived point with the prize point, or of a derived hash160
with the prize's or `17ucy1...`'s. Negative criterion: no equality for any window, transform
or encoding in any file.
Cost / bounds / stop: ~7,900 windows x 4 transforms, ~32k point multiplications in pure-Python
`btclib.py`: about 1-3 minutes; stop when every file is scanned.
Inputs not held: none.
Why hasn't someone already done this? Layout-first thinking and text validators; the exact
oracle only arrived in `research/2026-10-15` and was pointed at BTCSEED.

### W-03  "The judgement": the song's third part under the solved-stage lock
Origin: taken from R6-W3 (pool P-23).
One-paragraph description: Phase 0's URL and Phase 1's answer are the song's "phase one" and
"phase two" lines (A-01 precedent; [T L32947]). The song's "phase three" ("The judgement ... The
red rose or the black? ... no in-between", S-12) was never used. Try its lines, formatted by the
puzzle's own markers, as sha256hex passwords on the three containers.
Stage acted on and exact inputs: the next container; inputs: the lines as quoted in the
transcript [T L7943-L7947], [T L1069]; the three containers.
Clues used -> how:
  C-06 "Roses are White but often Red" -> a rose choice is the creator's own first image in the poem
  A-01 formatting markers and sha-256 password convention; the Phase-1 precedent (a song line is an answer) -> the test
Clues it contradicts: C-30(b) weakly ("you have all the info": the lyric is outside the artifacts, though the song is identified by Phase 1).
Prior attempts and why flawed / why missed: `EXT-E0295` posted 15 lyric lines x normalisations
to the Phase-1 *form* only; `EXT-E0182` harvested phrases from plaintexts, speech and VIC, not
the song; no CSV row for "judgement"; discussed in chat 2019-04-24, 2020-05-21, 2023-08-20 and
answered "Maybe we're not there yet" [T L25685-L25686]. Why missed: the song was considered
spent after Phase 1.
Every parameter and its source: lines <- FREE (7 enumerated: `thejudgement`,
`ifitweretofalluponyoutodaywhichflowerwouldyoube`, `theredroseortheblack`,
`redroseorblackrosenoinbetween`, `blackroseorredrosenothinginbetween`, `thisisthewarning`,
`phasethree`); case/space forms <- A-01 (`aaa connected enf` plus the two other markers);
password = sha256hex <- A-01; KDF and targets <- A-01, A-07..A-09.
Count of FREE parameters: 1 (plus the exact lyric wording, which the repo does not hold).
Success test: S1 / S2 / S3. Negative criterion: none of 63 decrypts meets them.
Cost / bounds / stop: seconds; 63 decrypts.
Inputs not held: the official lyric text (to confirm the chat quotation).
Why hasn't someone already done this? Probably somebody has, informally; there is no record,
and the 2023 suggestion was waved off.

### W-04  The rabbit's nest: the parcel beyond one mp3
Origin: new (blind spot B.3-3). Non-computational (retrieval + a held-file scan).
One-paragraph description: The outside piece (C-05, C-08) is held as one mp3 and two
screenshots. (a) Scan the held mp3 as a container: ID3 frames (text, APIC, GEOB), bytes after
the last MPEG frame, embedded file signatures (`Salted__`, PNG, ZIP, PDF), and a full-band
spectrogram of L, R and L+R over the whole clip (only L-R has ever been read). (b) Retrieve the
parcel's complete 2020 deployment (scene manifest, models, textures, other audio) from the
Decentraland content servers that served `QmeRy5...` in 2020, and catalogue every asset; A PR #30
reports an in-world "door" that "does nothing".
Stage acted on and exact inputs: the outside piece. Inputs: `puzzlepiece.mp3` (hash above);
parcel -41,-17; content id `QmeRy5MjmEZ2W6J3DwhQfht5HKBKXBFpoGzSkzmjeGKiDK`.
Clues used -> how:
  C-05 "There may indeed a piece be found outside the main puzzle." -> the parcel is puzzle material
  C-08 "Only -41,-17 matters" -> the exact object
  C-06 "the rabbits nest may contain a whole lot more" -> more than one thing hides in a piece
  C-24, C-25 "another door" -> the in-world door reported by A PR #30
Clues it contradicts: C-17/C-32 (offline) only if the result were a new online dependency; a file is not one.
Prior attempts and why flawed / why missed: `EXT-E0200` (L-R spectrogram -> HASHTHETEXT); A PR #30
(sound broken in some clients; files no longer downloadable from the world); B
`decentraland.ipynb` (`dcl status -41,-17`, not run). No record of ID3/appended-data/full-band
analysis or of an asset catalogue. Why missed: the parcel was treated as consumed once
HASHTHETEXT opened SalPhaseIon; the links died. (S-06 "blobs in mp3 didnt recovered" is a
solver's remark, context only.)
Every parameter and its source: none (a scan and a listing).
Count of FREE parameters: 0.
Success test: (a) any non-audio payload in the mp3 that is readable text or a well-formed
container, or glyphs beyond HASHTHETEXT in the full-band spectrograms; (b) any asset beyond the
known mp3/screenshots that carries text, an image or a file. Negative criterion: a clean mp3
(no tags, no appendix, no extra glyphs) and a deployment that lists only known assets or cannot
be reached.
Cost / bounds / stop: (a) minutes, held; (b) network to Decentraland content servers, one attempt.
Inputs not held: the parcel's deployment (may no longer exist).
Why hasn't someone already done this? The 2021 solver summary says the mp3 blobs were "not
recovered" and nobody returned to it after the entry hash worked.

### W-05  Reply targets: the Telegram JSON export and the PR93 attachments
Origin: taken from R1-W1 / R3-W5 / R5-W4 / R6-W4 (pool P-02, P-11). Non-computational.
One-paragraph description: Every unresolved ruling in `REPORT_ANALYSIS.md` B.2 turns on a
missing reply target or a missing attachment. Obtain the raw export of the "GSMG Puzzle
Solvers" group (id `1166734859`; ChatExport 2026-07-26, ~57,729 messages) and the attachments
listed in A PR #93 (`salphaseion_plain_79.bin`, `cosmic_decrypted_verified.bin`, `Jrk Bgrt Chat
History.txt`), then run pre-registered lookups.
Stage acted on and exact inputs: the clue record itself. Inputs not held: the export and the
three attachments; held: `sources/puzzlehunt/_pr93/_work/files_listing.txt` (names, sizes).
Clues used -> how (LAW 1 read per proposal PR-4: a retrieval is anchored on the clue whose context it recovers):
  C-13 the questions behind "answer is there" / "First or zero" -> `reply_to` of 4102, 4105
  C-26 the media behind "That is very specific" -> the file of message 8310
  C-40 "Bingo" -> `reply_to` of 60312 (D-01)
  C-46 "Pfff. Coincidence." -> `reply_to` of 70307 (D-02)
  C-11 "one team managed to find something" -> the solver posts of 2020-03-24..04-10 with ids
  C-10 / C-23 -> the date and context of the 79-byte attachment
Clues it contradicts: none.
Prior attempts and why flawed / why missed: A#114 asked publicly (2026); unanswered in the
archive; the held transcript was built from an HTML export without ids or reply targets
(`reference/04` section 1). Why not done: nobody holding the export has shared it.
Every parameter and its source: none.
Count of FREE parameters: 0.
Success test: the files in hand and the six lookups answered. Negative criterion: not
obtainable; nothing is retired.
Cost / bounds / stop: human effort; one request to the PR93 author and the group admins.
Inputs not held: all of them.
Why hasn't someone already done this? It has been asked; it depends on other people.

### W-06  Prime sums: `matrixsumlist` as the prime-masked sum list of the first piece
Origin: new (blind spot B.3-4).
One-paragraph description: C-21 ("I gave an unforseen hint already") is a Telegram reply to a
request for a `matrixsumlist` hint, and the only unplanned hint before it is C-19 ("You are at
the prime part already???"). So `matrixsumlist` is the prime part. With C-25 ("zeroed out",
primes), read on the first piece: zero every cell of the 14x14 bit grid whose spiral position
is not prime, then take the row and column sums (the circulating reading of "matrix sum list",
`reference/04` section 4) -> a value V; password = sha256hex(V).
Stage acted on and exact inputs: the next container. Inputs: `puzzle.png`; the 14x14 bit grid
and spiral of A-10 (unmasked row sums `[6,10,8,7,6,6,5,4,9,9,7,8,7,9]`, column sums
`[8,10,8,10,8,7,3,6,7,5,9,6,6,8]`, reproduced); the three containers.
Clues used -> how:
  C-21 + C-19 (reply link) -> `matrixsumlist` involves the prime part
  C-25 "prime numbers ... required" / "characters ... 'zeroed out'" -> keep prime positions, zero the rest, then sum
  C-28 label order (`yellowblueprimes` then `matrixsumlist`) -> the sums follow a prime selection on the image object
  C-06, C-13 -> the object is the first piece (Phase 0)
  A-07 `matrixsumlist` is a literal token -> it is a value to compute
  A-01 -> the test convention
Clues it contradicts: none.
Prior attempts and why flawed / why missed: unmasked sums `610876654997879` /
`8108108736759668` tested in hundreds of recipes (`EXT-E0098`, `EXT-E0099`, `EXT-E0157`);
`EXT-E0078` (sums from the FEFEFE cell with four zeros); C "prime-filtered index subsets and
their sums" (sums of coloured-cell indices, not masked grid sums); B PR#15 tick 10 adopted the
model "zero at prime-derived positions, then sum" and ran it in campaigns 12-19 on the soup's
7x13 matrices (`m7:*`) and the FAED remainder / DBBI prime positions (`p24:*`); its tick 32
says "broader matrixsumlist readings on the 14x14 grid were already closed (campaigns 12-19)",
but no campaign record shows a prime-masked 14x14 row/column-sum family. The gap is that
family. Why missed: the reply link of C-21 is invisible in the transcript; the sums were taken
as given.
Every parameter and its source: order = the A-10 spiral <- solved-stage convention; mask =
prime positions <- C-25; index base <- FREE {0, 1}; zeroing = set non-prime cells to 0 <- C-25;
sums = row sums then column sums <- the circulating reading (community convention), serialisation
<- FREE {rows||cols decimal concatenation, rows only, cols only, comma-separated rows||cols};
password = sha256hex(V) <- A-01; KDF, targets <- A-01, A-07..A-09.
Count of FREE parameters: 2 (2 x 4 = 8 values, fully enumerated); 24 decrypts.
Success test: S1 / S2 / S3. Negative criterion: none of 24.
Cost / bounds / stop: < 1 s; 24 decrypts.
Inputs not held: none.
Why hasn't someone already done this? B's ledger believes it has (tick 32) but logged it on the
wrong object; C summed indices, not masked cells.

### W-07  Better-half relation: is `17ucy1...`'s key an arithmetic image of the prize key?
Origin: new (blind spot B.3-7; A-06 unused by all six).
One-paragraph description: A-06 says there are two private keys, "half and better half", that
"need funds to live"; C-12 greeted "the half of prize went to better half" with "Well spotted".
The prize public point P is known; `17ucy1...` has only a hash160 (never spent). If the second
key is an arithmetic image of the first (double, half, negation, a small additive or
multiplicative offset), its public point is computable from P without any private key:
f(P) for a fixed relation family, compared by hash160 (both encodings) with `17ucy1...`.
A match reveals the two-key structure (not the prize key).
Stage acted on and exact inputs: the two-key model of A-06. Inputs: the prize public key
`04f4d1bb...3559` (tx hex, reproduced); `17ucy1K9ZUAaoY6JVtM932W9jUp5LXfyHa` (hash160 via Base58);
`btclib.py`.
Clues used -> how:
  A-06 "the private keys belong to half and better half and they also need funds to live" -> two keys, one a "half" of the other; funds = the halving payments
  C-12 "Well spotted" / "The price is in half, but what does it mean" -> the halving address is "better half"
  C-33 -> a regular key, so both encodings are tested
Clues it contradicts: none.
Prior attempts and why flawed / why missed: the 2021-07-18 "neighbors, half and double" dust
paid P-G, P/2, 2P, P+G (`reference/03` section 5; B tick 38) -- four points, sender unknown, not
compared with `17ucy1...` in any record; B campaign_29 derived 42 one-rule keys from the two
hash160s (not points); B tick 37 MITM targeted the prize key, not `17ucy1...`. Why missed: the
second address was treated as an independent wallet.
Every parameter and its source: relation family <- FREE: {2^i P, 2^-i P (i = 1..256), -P, -2P,
-P/2, P + mG and P - mG (m = 1..2^20), mP (m = 2..2^16)}; encodings both <- C-33.
Count of FREE parameters: 1 (the family bound), fully enumerated: ~2.2M hash160 comparisons.
Success test: exact hash160 equality with `17ucy1...` under either encoding. Negative criterion:
none in the family.
Cost / bounds / stop: ~2.2M point additions/doublings + hash160 in pure Python: ~10-20 minutes.
Inputs not held: none.
Why hasn't someone already done this? The four obvious neighbours were sent dust by someone in
2021; nobody enumerated beyond them against the second address.

### W-08  The speech as a recipe: a cipher battery over the Bifid output
Origin: reworked from the archive's own next-look list (`walkthrough/10` section 6 item 1;
`research/2026-10-15_SESSION_JOURNAL.md`), adjacent to R6-W2 but not taken from it.
One-paragraph description: A-03 instructs: "reinserting the prime basics after which you will
be required to select from over twenty-three ciphers sixteen encryptions and or seven
intertwined passwords ... brute forcing might be required". The only held object that was ever
produced *from* the soup by a cipher is the Bifid output `BTCSEED...` (S-10; mechanics
reproduced). Apply a fixed list of 23 classical ciphers, keyed only by puzzle material, to
the output's four natural payloads, and recognise success by English or by an exact key hit.
Stage acted on and exact inputs: the Bifid output. Inputs: `bifid_full.txt` (hash above),
`dbbi.txt`, `phase32_speech.txt`, the VIC checkerboard alphabet (`walkthrough/06`).
Clues used -> how:
  A-03 "select from over twenty-three ciphers ..." / "brute forcing might be required" -> a bounded cipher enumeration is the creator's own instruction
  C-25, C-27 primes required -> "reinserting the prime basics" is tested as the I/O-stripped (prime-count) payloads of `walkthrough/10`
  C-33 -> an exact key test on any hex/WIF that appears
Clues it contradicts: none; but its input S-10 is a solver construction whose significance is unverified (and C-46 may target it).
Prior attempts and why flawed / why missed: C's substitution/transposition/Vigenere/Beaufort sweeps
(`reference/06` section 2) and B campaign_07 mod-26 decodes acted on the raw blocks, not the
Bifid output; `research/2026-10-15` tested bits and keys of the output, not ciphers over it.
Why missed: the output became public only in 2025-06 and was read as a seed, not as ciphertext.
Every parameter and its source: payloads <- FREE {full 570; odd 285; odd minus I/O 256; even
285} (4, from `walkthrough/10`); cipher list <- A-03 says "select from over twenty-three", the
membership of the list is FREE (fixed in advance: Caesar, Atbash, Vigenere, Beaufort, variant
Beaufort, Gronsfeld, Porta, Autokey, running-key, Playfair, two-square, four-square, Bifid
(periods 5..30), Trifid, Polybius, Nihilist, ADFGX, columnar transposition, rail fence,
scytale, route, straddling checkerboard, Baconian); keys <- the solved chain (`DBIFHCEGA` square,
`dbifhceg`, `thematrixhasyou`, the VIC alphabet).
Count of FREE parameters: 2 (payload; list membership), fully enumerated: ~4 x 23 x 4 = 368 decodes.
Success test: >= 95% letters forming >= 3 dictionary words in a row (strong), or S2 on any
hex/WIF substring (exact). Negative criterion: neither in any decode.
Cost / bounds / stop: seconds; 368 decodes plus Bifid period range.
Inputs not held: none.
Why hasn't someone already done this? Because the output's significance is disputed; the
battery was never run on it.

### W-09  Which GitHub was "really getting close"? (C-27 archaeology)
Origin: new (blind spot B.3-10). Non-computational.
One-paragraph description: On 2023-01-11 the creator wrote "I checked a certain GitHub
yesterday, for whoever set that up, nicely done. You guys are really getting close." That is
a creator statement about the proximity of a specific public write-up at a known date. Identify
the repository (the held ones had no commits between 2022-10 and 2023-02: A's master is unchanged
since 2021-05-25 and A issues #1-#7 are from 2020-2021; so the candidate is either A's 2021
README plus seven issues, or an external repository -- the prior report's fourth source,
floflo777/open-crypto-puzzles, is public and clonable), freeze its content at 2023-01-10, and
list the endgame constructions it contained, each re-checked against the coverage register.
Stage acted on and exact inputs: the public record at a date. Inputs: tags
`archive/A/branch/master` (fb92dd1), `archive/B/branch/master`, A issues 001-007
(`sources/discussions/puzzlehunt/issues/`), transcript lines ~19980-20330 (2023-01-05..14); not
held: external repositories' history.
Clues used -> how:
  C-27 "I checked a certain GitHub yesterday ... You guys are really getting close." -> the object and the date
  C-27 same week: "prime number is very important" (01-09), "theory of everything ... valid path" (01-12) -> what "close" is near
  C-30(c) "Partly." (2023-08) -> a bound on how close
Clues it contradicts: none.
Prior attempts and why flawed / why missed: none of the six; B PR#15's "corpus exhausted" covers
creator messages, not dated external repositories. Why missed: the transcript gives no link
in that window (checked) and the held repos were static, so the question looked empty.
Every parameter and its source: none.
Count of FREE parameters: 0.
Success test: a dated artifact (commit <= 2023-01-10) whose content is a specific endgame
construction, with the creator's "close" attached to it; output = a short list for LAW 2
re-checks. Negative criterion: no candidate repository identifiable -> nothing retired.
Cost / bounds / stop: an hour of reading; one anonymous public clone.
Inputs not held: the identity of the repository, if external.
Why hasn't someone already done this? The remark reads as praise, not as a dated pointer.

### W-10  The April-2020 window: what did "one team ... find"? (C-11 transcript read)
Origin: new (blind spot B.3-2). Non-computational.
One-paragraph description: On 2020-04-08 the creator said one team had found "something others
haven't yet found", and on 2020-08-12 that "1 club ... passed but they are stuck in the next
phase". Read the solver side of the transcript for 2020-03-20 -> 2020-04-12 and 2020-05-18 -> 22
(the days of C-11, C-13 and the on-chain dust of D-05) and list every candidate object posted
(strings, URLs, keys, images) that the creator reacted to, for LAW 2 re-checks.
Stage acted on and exact inputs: the dated chat record. Inputs: `chat_transcript.txt` lines
~7,600-8,100 and ~9,800-9,950 (2020-03-20..04-12; 2020-05-18..22), held.
Clues used -> how:
  C-11 "one team managed to find something... something others haven't yet found" -> there was a find, and a date
  C-16 "1 club that passed but they are stuck in the next phase" -> the find was a stage
  C-13 "answer is there" / "First or zero" -> the May window's missing questions
  C-14 "Really nobody managed to find the extra door" (2020-08) -> the April find was not the extra door
Clues it contradicts: none.
Prior attempts and why flawed / why missed: B PR#15 ticks 39 and 63 read the on-chain side of
those days and withdrew the "unpublished stage" lead (the "Good job, Neo!" recipients are the
Phase-0 seed used as a raw key); nobody read the chat side for what the team posted. Why
missed: extraction agents summarised creator messages, not solver posts.
Every parameter and its source: none.
Count of FREE parameters: 0.
Success test: a dated solver post that identifies the find (an object not already in `CLUES.md`
or the graveyard). Negative criterion: the window shows only known material (Decentraland
audio, the seed-as-key) -> retires "the April-2020 find is an unpublished object".
Cost / bounds / stop: ~1 hour of reading.
Inputs not held: none.
Why hasn't someone already done this? The find was assumed to be the Decentraland piece.

---

## Score table (section 4 scale; any 0 rejects)

| Idea | Clue anchoring | Novelty | Parameter freedom | Success test | Cost | Total |
|---|---|---|---|---|---|---|
| W-01 Clear the marked bit | 3 | 2 (variant; prior semantics differ and are unauditable) | 2 (1 FREE) | 2 | 3 | **12** |
| W-02 Exact-oracle sweep | 3 | 3 | 3 (0 FREE) | 3 (exact) | 3 | **15** |
| W-03 The judgement | 1 | 2 | 2 (1 FREE + unheld wording) | 2 | 2 | **9** |
| W-04 The rabbit's nest | 2 | 2 | 3 | 2 | 2 | **11** |
| W-05 Reply targets | 2 | 2 | 3 | 2 | 1 | **10** |
| W-06 Prime sums | 3 | 2 (B claims closed; gap shown) | 1 (2 FREE) | 2 | 3 | **11** |
| W-07 Better-half relation | 2 | 3 | 2 (1 FREE) | 3 (exact) | 3 | **13** |
| W-08 Speech cipher battery | 2 | 2 | 1 (2 FREE) | 2 | 3 | **10** |
| W-09 Which GitHub | 2 | 3 | 3 | 1 | 2 | **11** |
| W-10 April-2020 window | 2 | 3 | 3 | 1 | 3 | **12** |

Tie-break rule, fixed before cutting: fewer FREE parameters, then the stronger success test,
then the lower cost.

---

## Stage D -- the funnel

### Round 1 (10 -> 5): laws pass
Section 0 re-read before this round: yes.
Outright failures: none (every card names CORE creator clues, has a stated flaw or reason for
every prior attempt, declares <= 2 FREE parameters, and has a pre-registered success test).
More than five survive, so the lowest totals are cut. Ranking: W-02 15, W-07 13, W-01 12,
W-10 12, then W-04 / W-06 / W-09 at 11, W-05 10, W-08 10, W-03 9. The fifth place goes to
W-04 by the tie-break (0 FREE and a strong success test, against W-06's 2 FREE and W-09's weak
success test).

Kill notes:
- **W-03** (9): lowest total; one loose clue; the lyric wording is not held. -> GRAVEYARD.
- **W-05** (10): cost 1 (an input we may never get); it remains a standing *request* to the
  user (see `SELECTED.md` section 7), not a funnel idea. -> GRAVEYARD (as "not pursued").
- **W-08** (10): 2 FREE parameters including the membership of the cipher list; input is a
  disputed solver construction. -> GRAVEYARD.
- **W-06** (11): lost the tie on FREE parameters (2) and a success test weaker than W-04's
  exact-shape criteria. The gap it names (no logged prime-masked 14x14 sum family) is real and
  is recorded in the graveyard as "not pursued", not as "done". -> GRAVEYARD.
- **W-09** (11): lost the tie on the weak success test; the held repos were static in 2023-01,
  so the question probably points outside the archive. -> GRAVEYARD.

Survivors: W-02, W-07, W-01, W-10, W-04.

### Round 2 (5 -> 3): adversarial attack
Section 0 re-read before this round: yes. Transcript re-searched for prior attempts with the
terms: "lsb", "least significant", "zero" x {"url", "theseedisplanted"}, "half and double",
"17ucy", "id3", "mp3", "scene", "dcl", "github" (2023-01 window), "stuck in the next phase".

- **W-02, strongest case against:** "You are dignifying noise: the archive itself calls these
  outputs chance padding events, so the prior that a key sits in them is tiny; the x2 and /2
  transforms stretch A-06; a negative only re-states what everyone already believes." Hidden
  fitted choices: none (every offset, both encodings, four sourced transforms). Could the
  success test fire falsely? No: an exact point match has no false positives. Prior attempt
  missed? C's "universal inspector" is unaudited and described as fixed readings. Verdict:
  the attack is about expected value, not validity; it survives.
- **W-07, strongest case against:** "The relation family is open-ended and its bound (2^20,
  2^16) is a fitted choice dressed as enumeration; 'half and better half' may be nothing more
  than a joke about the halving; the four obvious neighbours were already dust-probed by
  someone in 2021 and are not `17ucy1...`; and a positive does not open anything -- it confirms
  a structure." Hidden fitted choice: the family bound (admitted). Verdict: suffers the most on
  LAW 4 among the five. -> cut.
- **W-01, strongest case against:** "'Characters' in C-25 most naturally means the soup letters
  solvers were discussing in December 2021; C claims to have tried 'URL with prime positions
  zeroed out'; the three index conventions are a menu; and why would a string derived from the
  2019 image open a container written for 2021?" Replies: the soup's letter blocks have no
  zeroable digit and were exhaustively zero-tested (`zero_merge`, `EXT-E0042`); C's test is
  unauditable and its own definition of "zeroed out" is character-level; the three conventions
  are all the conventions there are; the creator built the puzzle at once (C-02, C-47) and
  C-06 (2020-01) already pointed back at the image. Verdict: survives.
- **W-10, strongest case against:** "A reading task with a subjective success; the April-2020
  find is most simply the Decentraland piece (hinted 2020-02-20) or the seed-as-key stamps B
  already explained; the 'club stuck in the next phase' is the first team to reach SalPhaseIon
  (five were in it by 2021-03-22, C id 6712)." Verdict: the simplest explanation covers it;
  the output could not open anything. -> cut.
- **W-04, strongest case against:** "The retrieval half is almost certainly dead (A PR #30:
  files no longer downloadable; Decentraland redeploys); the forensic half is a five-minute
  scan with a low prior -- the creator's hiding method was the L-R trick, not steganography;
  'blobs in mp3' is a solver's words; success (b) is vague." Verdict: the forensic half has
  0 FREE parameters and a crisp criterion; it survives this round on that half.

Survivors: W-02, W-01, W-04.

### Round 3 (3 -> 2): explains the creator
Section 0 re-read before this round: yes. Each survivor against the test statements:

| Statement | W-01 | W-02 | W-04 |
|---|---|---|---|
| "once you hit yinyang you'll solve it the same day" (C-30a, C-38) | consistent: opening a container is the next phase | consistent: one check away | -- |
| "the hardest part is done" (C-29) | yes: one small operation on known material | yes | -- |
| "1 microstep further" (C-35) | yes | yes | -- |
| "you have all the info" (C-30b) | yes: image, hint, container all held | yes | no: needs an external server |
| "it's in front of your eyes but you're not seeing it" (C-28) | yes, literally: the coloured bits | partly: the outputs are public | -- |
| primes required (C-19, C-25, C-27) | yes | no | no |
| characters "zeroed out" (C-25) | yes | no | no |
| "Breaking salphation should be giving the feeling of the phase's name" (C-20) | -- | -- | -- |
| "regular Bitcoin private key" (C-33) | downstream | yes, exactly | -- |
| CORE clues made true if right (count) | C-06, C-13, C-14, C-17, C-24, C-25, C-28, C-30b, C-32, C-35, A-10 (11) | C-10, C-23, C-33, A-06, C-12, C-35 (6) | C-05, C-06, C-08, C-24 (4) |
| Contradictions if right | none | a positive would make the MD5/duplicate-token recipes intended, against A-01's convention and C-28/C-25's vocabulary | none |

W-04 explains the fewest and is cut. W-02 explains fewer CORE clues than W-01 and its positive
would contradict the convention; it stays only because the round cuts one.
-> **W-04 cut.** GRAVEYARD (as "not pursued"); its forensic half is recorded in `IDEAS_INBOX.md`
as a five-minute side check for a later session.

Survivors: W-01, W-02.

### Round 4 (2 -> 1): decisiveness per cost
Section 0 re-read before this round: yes.

| | W-01 Clear the marked bit | W-02 Exact-oracle sweep |
|---|---|---|
| Clean positive? | yes: readable text or a key (S1-S3) | yes: an exact point/hash160 match -- a solve |
| Negative retires a branch? | one literal reading of C-25 on the first piece (narrow) | "the key sits raw, reversed, doubled or halved in any held community output" -- the branch still pushed in [B#17] (2026-10-05) and [A#108]; no held sweep ever closed it |
| Cost | < 1 s, 9 decrypts | 1-3 minutes, ~32k point multiplications |
| Missing inputs | none | none |
| FREE parameters | 1 | 0 |

Both are cheap and complete. Run once, W-02 gives the clearer answer either way: its positive
is exact and its negative closes a branch that the community keeps reopening, whereas W-01's
negative closes only one reading. It also has the fewer FREE parameters. **W-02 is selected;
W-01 is the runner-up and becomes ACTIVE as soon as W-02 has run** (a negative is expected;
the whole run costs minutes). This is not a judgement that W-02 is the likelier solve -- W-01
explains more of the creator (round 3) and is the project's first real hypothesis; W-02 is the
decisive closure that the rules put first.

Kill note for **W-01** (this round): not killed on merit; ranked second on decisiveness per
cost. It goes to `PLAN.md` as the next ACTIVE item, not to the graveyard.
