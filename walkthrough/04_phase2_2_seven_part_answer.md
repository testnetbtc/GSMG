# Phase 2.2 -- JFK, the genesis block and a chess problem give parts 5, 6, 7; all seven open the second envelope

Status: SOLVED (reproduced; Python and OpenSSL agree byte for byte)
Where: the same Phase-2 page as 03 (its lower half)
Previous: [03_phase2_causality_and_riddles.md](03_phase2_causality_and_riddles.md) --
Next: [05_phase3_three_part_answer.md](05_phase3_three_part_answer.md)

## 1. Data (what you are given)

The page text below the first envelope (verbatim from the 2020-11-12 capture):

```
There's a guy who theorised the idea that 'Any linear electrical network with
voltage and current sources and only resistances can be replaced at terminals
A-B by an equivalent current source Ino in parallel connection with an
equivalent resistance Rno'. He might have been insecure. His competition might
have been that as well. However, after enough belikins this competition tried
to become a ruler of a piece of land that's technically the poorest of the
entire planet. 4 rulers have shared the first name of the competition. 2 had
the firstname in the surname. One of the rulers had a number, and dirty too.
Another had a resemblance to Carrey, James Gates, also Simulacra and
Simulation. Another ruler was at some point a floating zerg house while being
under control of the dirty one.. too. The one after died too soon. Moral:
never execute an order that revokes the highest power or you might suddenly
get killed. The 5binary code is a part of the piece of this puzzle.

Years later the idea of this _green_ came _back_. Looking at the current
state of nature not quickly enough. Afraid for random magic pieces of metal,
that moved in directions that science couldn't and still can't explain,
coming from places where inspiring papers used to be deposited, a chancellor
awaiting banks to be bailed out decided to write an anarchist digital answer
to this worlds' misery. Its' raw data after 4 on row 1616 to be one of the
last pieces of this part required in order to continue this riddle.
/(aBa, connected enf)

B5KR/1r5B/6R1/2b1p1p1/2P1k1P1/1p2P2p/1P2P2P/3N1N2 w - - 0 1
And now a buddhist is forced to move. What will be the next situation?
/(aBa, connected not enf)

--> parts 1..7 --> sha-256 -> dgst is the password to enter Phase 3.
```

and the second envelope:

| Envelope | File | Decoded size | Salt | SHA-256 of the decoded envelope |
|---|---|---:|---|---|
| `ENV-phase3` | `reference/artifacts/envelopes/phase3.b64.txt` | 4,112 bytes (16 + 4,096 ciphertext) | `9fbc451d13d071f4` | `9163a38d8c49038d01005bc468d9c677183b49b14d7a88fdf3bade75d1443f30` |

The chess position (`reference/artifacts/images/chess.png` shows it on a
board): White has bishops a8 and h7, king g8, rooks h8 and g6, knights d1 and
f1, pawns b2 c4 e2 e3 g4 h2; Black has rook b7, bishop c5, king e4, pawns b3
e5 g5 h3. White to move.

## 2. Clues that apply

- The numbers written into words (`5binary`) are part numbers, as in 03.
- `/(aBa, connected enf)` after the two paragraphs: keep case, no spaces,
  for parts 5 and 6. `/(aBa, connected not enf)` after the chess line: keep
  case AND keep the spaces, for part 7.
- "came _back_" (reversed) and "row 1616" (a source-code line number) are
  the pointers for part 6.

## 3. Workings out

**Part 5 -- the executive order.** The quoted theorem is Norton's theorem.
The "competition" of Norton whose first name four US presidents shared is
John (Adams, Quincy Adams, Tyler, Kennedy); two more had it in the surname
(Andrew Johnson, Lyndon Johnson); "the one after died too soon" and "never
execute an order that revokes the highest power or you might suddenly get
killed" point at John F. Kennedy and the popular theory around his
Executive Order 11110 (1963, on silver certificates and the Federal Reserve).
"The 5binary code" = part 5 looks like a five-digit binary number:

```
11110
```

The community itself calls this reading "a bit of a stretch"; B's notebook
records that the value was settled by trying the eight JFK executive orders
that look binary against the next envelope. It is confirmed by the decrypt
in step "all seven" below, not by the riddle alone.

**Part 6 -- the genesis block, backwards.** "This _green_ came _back_" is
the greenback; the "chancellor awaiting banks to be bailed out" is The Times
headline of 3 January 2009 that Satoshi put in Bitcoin's first block; the
"anarchist digital answer" is Bitcoin. "Row 1616" is line 1616 of the
original `main.cpp` in the first public Bitcoin source tree, where the
genesis transaction is built: `... << 486604799 << CBigNum(4) << <the
headline bytes>`. "Raw data after 4" is therefore the headline as bytes --
and "came back" says to write them backwards. Part 6 is `0x` followed by the
uppercase hex of the REVERSED headline:

```
0x736B6E616220726F662074756F6C69616220646E6F63657320666F206B6E697262206E6F20726F6C6C65636E61684320393030322F6E614A2F33302073656D695420656854
```

`verify.py` checks that these bytes, reversed, read exactly
`The Times 03/Jan/2009 Chancellor on brink of second bailout for banks`.

**Part 7 -- the peaceful move.** "A buddhist is forced to move" = the one
move that does not kill. From the given position White has 14 legal moves;
13 of them are checkmate in one. The only move that is not mate is the rook
move `Rc6` (it gives check, but not mate). This is checked by machine in
`verify.py` with python-chess when it is installed. Part 7 is the FEN of the
position after that move, keeping the trailing `b - - 0 1` exactly as the
puzzle wants it:

```
B5KR/1r5B/2R5/2b1p1p1/2P1k1P1/1p2P2p/1P2P2P/3N1N2 b - - 0 1
```

Trap: a chess engine writes the halfmove clock as `1` after a rook move
(`... b - - 1 1`). That string does NOT decrypt the envelope (C reports its
hash, beginning `53b27a4e9763`, fails). Keep `0 1`.

**All seven parts.** Join parts 1..7 with nothing in between (the only spaces
are the ones inside the FEN, which `connected not enf` tells you to keep):

```
causalitySafenetLunaHSM111100x736B6E616220726F662074756F6C69616220646E6F63657320666F206B6E697262206E6F20726F6C6C65636E61684320393030322F6E614A2F33302073656D695420656854B5KR/1r5B/2R5/2b1p1p1/2P1k1P1/1p2P2p/1P2P2P/3N1N2 b - - 0 1
```

That is 227 characters. Its SHA-256 is the password:

```
1a57c572caf3cf722e41f5f9cf99ffacff06728a43032dd44c481c77d2ec30d5
```

Decrypt `ENV-phase3` with the same AES convention as 03. The plaintext
`PT-phase3` is 4,090 bytes: three short riddles and a third envelope (next
file).

## 4. Solution

- parts 5, 6, 7: `11110`; `0x736B6E...656854` (the reversed-headline hex);
  `B5KR/1r5B/2R5/2b1p1p1/2P1k1P1/1p2P2p/1P2P2P/3N1N2 b - - 0 1`
- the 227-character seven-part string above
- `PT-phase3` (4,090 bytes, `c4ad94559a44a927c1032cc0e024515f9510a0806a2d14458dbf4a360af9865f`),
  kept as `reproduction/results/phase3_plaintext.bin` and
  `reference/artifacts/plaintexts/phase3_plaintext.txt`

## 5. Verification

| Check | Result |
|---|---|
| `reproduce.py` step `aes_phase3` | confirmed; Python and OpenSSL identical |
| `verify.py` | answer length 227, password hash, decrypt, plaintext length 4,090 and hash pass; reversed-headline check passes; chess check: 13 of 14 legal moves mate, the exception is `Rc6` |
| negative controls | MD5 key derivation and raw-digest password both fail |
| upstream copies | B's `phase3.txt` byte-identical; C's identical after CRLF -> LF |

## 6. Extra findings and notes

- Old snapshots of A's README (PR #16, PR #30 heads) truncate the seven-part
  string at `...B5KR`; the full string is in B's README and above. A claim in
  C that B's README is truncated is stale.
- The equation line from 03 (`# X 2 S H 4 Y 0 Q B 15 #`) plays no part in
  this answer.
- Part 5 is the one part of the whole solved chain whose derivation from its
  riddle is not fully convincing; it is nevertheless certain, because the
  seven-part string decrypts the envelope with valid padding and readable
  text (the chance of that for a wrong string is about 1 in 256 for padding
  alone and nil for readable text).

Sources: `reference/01_SOLVED_CHAIN.md` section 3.4; `reference/07_CONTRADICTIONS.md`;
A's README section 3; B's `phase2.ipynb` cells 5-11 and `_pr15/neo/LEDGER.md`.
