# Clues index -- every creator-attributed clue, dated, and what it does and does not establish

Previous: [10_frontier_dbbi_faed_btcseed.md](10_frontier_dbbi_faed_btcseed.md) --
Next: [12_verification.md](12_verification.md)

**Attribution.** "Creator-attributed" means posted under the Telegram handle
@SoWut (display name Jrk Bgrt) in the "GSMG Puzzle Solvers" group. Nothing
authenticates that handle as the author; asked "are you creator?" it
answered "Rumour has it I'm an admin at least." Its first-person statements
about writing and testing the puzzle are strong circumstantial support. Two
corpora hold these messages: C's dataset `sowut-data.js` (510 records,
2019-04-20 to 2026-09-01; `id` below) and the full group transcript shipped
in A PR #93 (51,177 messages to 2026-06-12). Every text message in the
dataset's window is also in the transcript (checked message by message).
Dates are UTC. Full raw context for every row:
`reference/04_CREATOR_CLUES.md` and `reference/data/CREATOR_CLUES.jsonl`.

## 1. Clues embedded in the puzzle itself

| Where | Text | Bears on |
|---|---|---|
| Phase-2 page | `(aaa, connected enf)`, `(aBa, connected enf)`, `(aBa, connected not enf)` | answer formatting: case and spaces (03, 04) |
| Phase-2 page | "--> parts 1..7 --> sha-256 -> dgst is the password" | the password convention (04) |
| PT-phase3 | "just add giveit in front of the answer"; "Phase 3.2 is ciphered with aes-256-cbc base64 and a sha256 pw, yet again" | 05 |
| PT-phase32 | "... am I here? Wake up, you... a beautiful strategic position. One for one, four for one." | key `thematrixhasyou`, Beaufort, code page 1141 (06) |
| the speech | "reinserting the prime basics after which you will be required to select from over twenty-three ciphers sixteen encryptions and or seven intertwined passwords to find the actual private key note that also brute forcing might be required" | the endgame (09, 10) |
| the speech | "what a wise man above hinted at is worth hundred fourty of the investment" | unknown; a "104" reading was called a typo by the creator |
| the speech | "please if you find a way to complete the last part of the puzzle take the private key youve earned it" | the target is a private key |
| PT-phase32 | "A fubcd-king & oracle-queen, thingky mvps, on a sad board but as wide as the first one seen." | the checkerboard alphabet (06) |
| VIC sentence | "in case you manage to crack this the private keys belong to half and better half and they also need funds to live" | two keys; "half" (06, 09) |
| the soup | `shabefourfirsthintisyourlastcommand`, `shabefanstoo` ("sha256 ...") | readings only (08) |
| Decentraland audio | `HASHTHETEXT` | 07 |

## 2. Creator-attributed messages (chronological)

| Date / id | Exact text (trimmed) | Context | What follows / what does not |
|---|---|---|---|
| 2019-04-22 / 225 | `5ac407837447fba24ba2802e4d1e9aecb4580aa29fef1088cc387c180b746f75` | then 226 "just try hit your options against that hash."; 257: released because "the website was giving a lot of token errors" | SHA-256 of the Phase-1 answer (02). The only creator-published checkpoint in the whole puzzle |
| 2019-05-17/18 / 866-875 | "...unless you'd know where to add 1 extra character between the 3 answers..."; "giveit = givetit"; "The issue is within the 3th phase."; "I've tested the entire puzzle 3 times with the same string which had the typo in it" | Phase 3 | one acknowledged typo; the string with `giveit` is the one that works (05) |
| 2019-05-18 / 881 | "In case the private key hasn't been found in 2019 we'll release a tiny hint at the start of 2020, that will be the final hint. Can the private key be retrieved without that hint? Yes." | -- | the 2020 hint is not a dependency |
| 2019-09-22/26 / 1465, 1487 | "7 parts right?" / "There may indeed a piece be found outside the main puzzle." | -- | an outside piece (Decentraland fits) |
| 2020-01-14 / 1710 | "Roses are White but often Red. / Yellow has a number and so does Blue. / Go back to the first puzzle piece without further ado. / It might have shown you only one door, beware that the rabbits nest may contain a whole lot more. / Hush hush." | typed text; re-pointed by 4096 "This one" | hash the opening image's text (07); "more doors" in the first piece; no values given |
| 2020-01-27 / 1726 | "Might have been fixed fyi"; "Would be nice, not required" | on garbled Phase-3.2 text | spelling fixes not required |
| 2020-02-20/22 / 1743, 1837, 1806 | Decentraland screenshot; "Only -41,-17 matters"; "Typos: Horrible mistakes due to rushed work... No clues to be found in those typos" | -- | the parcel (07); typos are not clues |
| 2020-02-25 / 2013, 2026 | "3.2 is a thing btw" / "Don't know but most see 3.2 as the last part." | -- | 3.2 matters; the creator does NOT say it is last |
| 2020-03-25 / 2910, 2918 | "Answering that would be too much of a hint." / "There must at least be something hidden in there." | to "the PK is in the last cipher of 3.2 decoded" | weak support that 3.2 hides something (`p32_trailing`?); not a confirmation |
| 2020-05-11 / 3902, 3923 | "Well spotted" (to "the half of prize went to better half"); "...who knows what you'll find after opening the 2nd door. The price is in half, but what does it mean" | first halving | links the prize split to "better half"; ambiguous |
| 2020-05-20/21 / 4102, 4105 | "answer is there" / "First or zero" | no preserved question | unspecified |
| 2020-08-02 / 4589, 4590 | "Or the same puzzle, or just not at all." / "Really nobody managed to find the extra door..." | after a SOLVER wrote "the second half will probably be used for another puzzle" | the "another puzzle" sentence is the solver's, not the creator's |
| 2020-08-09 / 4624 | "a private key" | to "What to find private key or seed phrase or phrase for brain wallet?" | the target is a private key |
| 2021-01-21 / 5717 | "Not to give any hints but a few might not require the internet anymore." | -- | -- |
| 2021-03-01 / 5960 | "Ancient spelling. One of the many many typos." | a REPLY to a solver's "FORTY but hundred FOUR = 104 is the fefefe square" | evidence AGAINST the 104 / FEFEFE numerology |
| 2021-03-01 / 5966, 5969 | "You are at the prime part already???" / "Oh wait, shouldn't have said that. That might have been a hint" | after a solver asked "which primes 2,3,5,7" | a "prime part" exists; the set {2,3,5,7} is the solver's |
| 2021-03-14 / 6497, 6509 | "...Breaking salphation, should be giving the feeling of the phase's name..."; "I gave an unforseen hint already" | -- | the SalPhaseIon page name is meaningful; the unforeseen hint is unidentified |
| 2021-04-01 / 6884, 6913, 7529 | "Hint: another door might be found on {1},{4},{21}"; "R=18 A=1 B=2 Could also be 21 or 1812 bit"; (2021-04-18) "Do you know what usually happens on the first of april?" | April 1 | probably a joke |
| 2021-08-10/11 / 7830-7834 | "Technically we do" -> "The one to be found by solving the puzzle yes" -> "And the solver will find a way to 'decrypt' it." | to a SOLVER's "Puzzle creators do not store the private key online" / "the encrypted private key stored online?" | assent to the solver's wording; no container named; 'decrypt' in quotes |
| 2021-12-03 / 7914 | "There is / Another / D / O / O / R" | -- | another door |
| 2021-12-26 / 7998, 8000 | "A mini mini hint. Ready?" / "The previous 'there is another door hint' is still a thing. We're not sure if anyone has found another door so far, and we can't check that... We've seen prime numbers being mentioned; well, that is definitely an aspect which is required to proceed. Furthermore, along the way, some characters need to be 'zeroed out'.. Best of luck and happy holidays!" | 20:18 UTC (some sources date it 12-25) | PRIMES required; some characters ZEROED OUT; no set, index or rule given |
| 2022-12-11 / 8311, 8315 | ".... That is very specific" / "If the puzzle is solved you'll see how scary specific that is" | to a media post not held | the "specific" thing is unknown (the Cosmic Duality book cover is an inference) |
| 2023-01-09/12 / 8330, 8352-8360 | "At least prime number is very important to get any further."; "I checked a certain GitHub yesterday... You guys are really getting close."; "Focussing on the theory of everything is also still a valid path to reaching the private key."; "At least higher than sqrt(-1)."; "...the remaining 2.5 btc is well deserved... Or 5, who knows." | -- | primes again; "theory of everything" unexplained |
| 2023-02-23 / 8446 | 161 groups of 8 bits (decode below) | first public decode next day by a Deleted Account; creator's only reaction "shrug" | the four labels (10) |
| 2023-08-03 / 8774, 8787, 8796 | "Are you really looking for just the btc...?" / "Might be. Wish I had said nothing though." / "Actually, the hardest part is done." | -- | -- |
| 2023-08-06 / 9550-9639 | "...if I suddenly can't answer you guys anymore, it was nice knowing you all."; "The puzzle talks for me."; "Technically my friends and family can get to all my data if they'd work together. In that scenario, don't expect a halving of the price."; "Probably the last hint: Once you hit a 'ying yang', you'll be able to solve it the same day."; "No need. You have all the info."; "Partly." (to "Has anyone passed the salvation part?"); "...you'll need the internet to claim the prize in the end" | the friends/family line answers "if you need to disappear, is there someone else who knows the solutions" | YIN YANG is a milestone; "you have all the info"; the friends line is about succession, not about deriving the answer |
| 2023-08-29 / 12653 | "Correct" | to "Jrk has stated that the blockchain messages are not his and are not part of the puzzle" | on-chain OP_RETURN messages are NOT puzzle material |
| 2023-11-24 / 16624 | "'Given the available knowledge, is internet still required to solve it?' Nope" | -- | -- |
| 2024-01-26 / 20223 | "Regular Bitcoin Private key" | to "what format key we are all searching?" | format: a regular private key (WIF/hex/compression unspecified) |
| 2024-04-10/20 / 24627 | "1357 blocks to go"; "...A private key, some 'obscure' intel, or ... hold on to Bitcoin" | halving countdown | -- |
| 2024-11-29 / 32579, 32613, 32671 | "...If you guys got 1 microstep further, the puzzle will likely be solved the same day..."; "I think I'll be going for ASCII 127 myself."; "You only need the last number of pi and it might get you somewhere." | joking threads | one microstep away (again); DEL / pi links are solvers' |
| 2025-04-28 / 39224, 39237 | "Did anyone found yingyang? ... when yingyang is reached, 2 hours max." / "It's the next phase, but I await the day someone finally gets there." | to "is yinyang found after decoding an AES ciphertext?" | yin yang = the next phase; the AES part not affirmed |
| 2026-01-01 / 53335-53342 | five dot messages, then 77 binary groups: "Happy new year! Make the best of everything. Oh, and here's a 'tiny hint' <3." | -- | decode reproduced (plain ASCII); the "tiny hint" referent unknown |
| 2026-03-04 / 60302-60314 | "...Jacque was quite an inspiring lad I'd say."; "Bingo"; "I only need to look at the address. If any of you reaches the next phase, the price is taken in no-time." | "Bingo" context survives only in a user screenshot | unresolved what "Bingo" confirms |
| 2026-05-28 / 63957 | "Ah, ofcourse. The puzzle is still valid!" | to "The sites are down..." | -- |
| 2026-07-13 / 66549-66606 | "I might me drunk, or worse..."; "...I have a hidden laptop which I haven't touched in years. On that thing... is the actual answer...."; "My close friends have the best chance of solving it (a few tried). But they don't have the skills some of you do." "NOTE: that is a hint."; "...it's all still solvable with a few stable qubits."; "The '5' btc was never the actual prize. That was only a tiny fraction."; "Some already found it. And understood not to risk it..." | self-declared intoxicated session; only in C's dataset (after the transcript ends) | explicitly marked a hint; suggests personal knowledge helps; no book, password or generator named |

## 3. The two binary hints, decoded

**2023-02-23 (id 8446).** 161 groups of 8 bits. Rule: reverse the ENTIRE bit
string, then read 8-bit ASCII (equivalently: reverse the byte order and the
bits inside each byte). Output, 161 bytes, no spaces, SHA-256
`d13afe77dd6969a438e2020cc3df22e0e7d589ae88196caa9162c9168e25a018`:

```
yellowblueprimesmatrixsumlistlastwordsbeforearchichoiceyinyangwewontgiveawaythepassworditsinfrontofyoureyesbutyourenotseeingitverylaststepisatruegiveawaypromised
```

Readable: "yellowblueprimes | matrixsumlist | lastwordsbeforearchichoice |
yinyang | we wont give away the password / its in front of your eyes but
youre not seeing it / very last step is a true giveaway promised". The four
labels occupy bytes 0-61; the sentence bytes 62-160. Any spaces you see in
other write-ups are interpretation.

**2026-01-01 (ids 53340-53342).** 77 groups, plain 8-bit ASCII, no reversal:
`Happy new year! Make the best of everything. Oh, and here's a "tiny hint" <3.`
The five preceding posts were ".", "..", "...", "....", "....." one minute
apart (a solver read them as Morse).

## 4. Things the creator-attributed handle has never said

Searching both corpora: no use of `E_S`, checksum, "verification", WIF,
seed, mnemonic, vanity, `matrixsumlist` (as a value), `yellowblueprimes`,
`cosmic`, `BTCSEED`, `dbbi`, `faed`, offset 158, the chain-4 mask,
`secondanswer` or `yourlastcommand`. Several "creator rules" in circulation
are in fact solver text: FEFEFE/104, the prime set {2,3,5,7}, "encrypted
private key stored online", "second half for another puzzle", and the
2021-05-06 "hash the text" instruction.

Sources: `reference/04_CREATOR_CLUES.md` (with the raw context of every
row), `reference/07_CONTRADICTIONS.md` section 2.3.
