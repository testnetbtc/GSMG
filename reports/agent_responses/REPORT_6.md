# GSMG 5 BTC puzzle: why it's unsolved, and how it could be solved
Independent analysis, 22 Oct 2026.

**Sources:**
- Telegram: both groups, Apr 2018 → 10 Oct 2026.
- Every prior agent report on the VPS.
- Your repo testnetbtc/GSMG (commit d4db275) and the community repo.
- Our test rounds 1–4.
- The blockchain.

**Checked by me today:**
- all 61 creator quotes below, against the raw Telegram data (times UTC);
- the SalPhaseIon decode;
- the on-chain balances;
- our test totals.

**Tags:** [drinking] = the creator said they were drinking at the time. "Judgement" = my opinion, not evidence.

## Where it stands
- **Prize.**
  - `1GSMG1JC9…` holds **1.2565 BTC** (block 972,614).
  - Half moves to `17ucy…` at every halving, as announced on 21 Apr 2019 (COM-28876). `17ucy…` holds 3.7506 BTC and has never been spent from.
  - Next halving: block 1,050,000, around April 2028 (estimate).
- **Solved in public: 8 steps, ending at the SalPhaseIon page.**
  - By the creator's count, a team got past the second route by Aug 2020 but was "stuck in the next phase" (SOL-4694). By 22 Mar 2021 there were five in SalPhaseIon (SOL-6712).
  - The page has been public since 16 Apr 2021.
- **Never opened:**
  - the page's two letter blocks, dbbi (91 letters) and faed (570 letters);
  - four sealed blobs: cosmic (1,328 B), salph_inner (80 B), p32_trailing (80 B), and urlblob (96 B, origin disputed).
- **Nobody has reached the next phase, "yinyang"** (SOL-39237, Apr 2025, [drinking]; SOL-60314, Mar 2026).
- **Effort so far:**
  - all agents' runs: about 10⁹ password guesses (EXHAUSTED.md);
  - our tests: 44.8 M guesses;
  - validated openings: **0**.

## 1. Why has nobody solved it?
1. **The last part was designed to take a long time, and what's missing is an interpretation, not computing power.**
   - In 2019 the creator said: "The 'last' part of the puzzle will ensure that there's quite some time" (SOL-879).
   - The 2023 hint names four ingredients, *yellowblueprimes, matrixsumlist, lastwordsbeforearchichoice, yinyang* (SOL-8446). None comes with a value:
     - **yellowblueprimes:** no agreed meaning.
     - **matrixsumlist:** no agreed format. The creator: "I gave an unforseen hint already" (SOL-6509).
     - **lastwordsbeforearchichoice:** what it refers to is disputed.
     - **yinyang:** a stage, not a value. "It's the next phase" (SOL-39237).
   - How the four combine is never stated.
   - The creator's only specific clues for this stage:
     - "prime numbers… required to proceed" (SOL-8000; also SOL-5966/5969, SOL-8330);
     - "some characters need to be 'zeroed out'" (SOL-8000).
   - Those clues fit dbbi and faed. Both use the same a–i letters as the page's decoded labels but contain **no "o", which is the zero digit**. Neither has ever been decoded.
   - I checked the literal readings. Zeroing or deleting the prime positions gives random bytes.
2. **The lock gives no partial credit.**
   - One wrong character produces garbage.
   - About 1 in 255 wrong guesses passes the padding check by chance. That chance pass has fed years of false "solutions": the md5 chain (republished as the community repo's issue #17 on 5 Oct 2026), btcseed, and message 74724.
   - So you can't get warmer; you can only be exactly right. 10⁹ failed guesses show the community's interpretations were wrong, not the puzzle.
3. **It was built fast, and the creator's own testing can't catch a mismatch between a clue and the stored answer.**
   - The build took "two sloppy days" or a "couple hours" (COM-67741, SOL-70336). "I rushed (t)it" (SOL-70311).
   - In 2019 a typo blocked Phase 3 until solvers reported it. The creator had "tested the entire puzzle 3 times with the same string which had the typo in it" (SOL-871).
   - Since then the creator has said "I forgot the last details on how to solve it exactly but it's possible" (2021, known from a member's forward, SOL-24156). Also "Most of you know the puzzle WAAAY better than me" (SOL-66568, [drinking]).
4. **The hints are few and unreliable.**
   - Many came while the creator was drinking.
   - One was a joke: {1},{4},{21}, disowned as April Fools (SOL-7529).
   - Many are emoji or one-word replies with no reply link.
   - "high likely no hints anymore" (SOL-9621, 2023). "without giving any hints" (COM-67742, 2026).
5. **A piece may lie outside the page.**
   - For: "My close friends have the best chance of solving it (a few tried). But they don't have the skills some of you do." / "NOTE: that is a hint." (SOL-66573/4, Jul 2026, [drinking]).
   - Against, sober and in direct reply: "You have all the info" (SOL-9607, 2023) and no internet needed (SOL-16624).
   - This is unresolved. If such a piece is needed, that alone explains six years.
6. **The community works against itself.**
   - The prize rewards secrecy. Early teams reported progress to the creator by private message (SOL-6497).
   - Scams and impersonators: 470 scam records.
   - Noise: 18,452 Solvers messages in 2026 alone.
   - Coincidences get recycled.
   - Tool blind spots: graders that looked only for printable text, and the biggest grammar sweep never ran on cosmic.
7. **Brute force can't replace insight.**
   - The prize address is a vanity address ("few seconds… Only 4 chars", COM-28526/7), so the key is effectively random.
   - Its public key has been exposed since 2020, but reversing it takes about 2¹²⁸ work.

**Judgement:**
- About 60 %: intact, and solvable from the public material by an interpretation nobody has found.
- About 25 %: needs something outside the page.
- About 15 %: broken by a build error that only the creator could fix.

## 2. What is required, and why
1. **The exact answer strings, built from the SalPhaseIon page.**
   - You need three things:
     - a rule for dbbi and faed (or the image's yellow and blue cells) that uses primes and zeroing;
     - the exact value of each named ingredient;
     - the way they are joined.
   - *Why:* the 2023 hint says "it's in front of your eyes" (SOL-8446), and the creator said "You have all the info" (SOL-9607).
   - Every solved lock used one convention: lowercase answer → sha256 hex → `openssl aes-256-cbc` with sha256 key derivation, 1 iteration. Our self-test confirmed it again; md5 and sha1 fail.
2. **An opening you can prove.**
   - Accept only one of these:
     - readable text;
     - a full 16-byte block of 0x10 padding, meaning an 80-byte blob that holds a 64-hex value;
     - a nested `Salted__` header;
     - a key whose address matches the prize.
   - Valid padding alone has fooled people for years.
3. **Yinyang, then the last step.**
   - After yinyang the creator says it's "the same day" or "2 hours max" (SOL-9599; SOL-39224, [drinking]).
   - The end product is a "Regular Bitcoin Private key" (SOL-20223), stored encrypted online (SOL-7830/7832/7834).
   - *Inference:* cosmic (~1.3 KB) is page-sized like the solved pages, so it is probably the yinyang page. The 80-byte blobs are exactly a 64-hex key plus padding.
4. **Possibly, knowledge that people close to the creator have** (see 1.5).
5. **Skill and discipline.** The creator has used Beaufort, VIC, code pages, bit reversal, Caesar and base64. Every result needs rigorous checking.

## 3. How a solver can solve it
1. **Use primary material only.** That means the page bytes, the image, the solved plaintexts, and the creator's sober replies that answer a specific message.
   - Drop btcseed, the md5 chain, 3GSMG24 and {1},{4},{21}.
   - Drop YOUWON too. "Pfff. Coincidence." (SOL-70307) most likely answered that morning's YOUWON/VIC post.
2. **Model the creator from the 8 solved steps.**
   - Answers are English phrases, or joins of pieces you found.
   - Instructions sit inside the plaintext.
   - A new idea should look like something the creator has already done.
3. **Treat the hints as a checklist that any correct reading must pass:**
   - primes;
   - zeroing;
   - "in front of your eyes";
   - the last step is "a true giveaway";
   - no internet needed;
   - the result is a regular private key.
4. **Decode before you decrypt.**
   - Make dbbi or faed into readable text first. A correct decode proves itself; a password guess doesn't.
   - Prefer one rule that explains several clues at once: the missing "o", primes, zeroing, yellow/blue, "Go back to the first puzzle piece" and "First or zero".
5. **One idea = one small, pre-registered test.**
   - Use the solved locks as controls.
   - Keep every output that passes the padding check, and grade the full bytes.
6. **Work in a small, trusted team.** Never post keys, and expect scams.

## 4. Every route to the key, whatever the answer turns out to be

| Route | Possible? | Evidence |
|---|---|---|
| Intended: SalPhaseIon → blob → yinyang → key | Yes, if the puzzle is intact | "it might appear unsolvable, but it's not" (SOL-8360, sober); "salphaseion is 100% solveable?" → "Yes" (SOL-66588, [drinking]); "still valid" (SOL-63957) |
| The creator posts a giveaway hint | Uncertain | 2023: might add one if unsolved "in the next few years", and it "would probably be a give away" (SOL-9621). 2026: "without giving any hints" (COM-67742) |
| The creator fixes a build error | Has happened once | The Phase 3 typo was fixed after a report (SOL-866/867). Contacting the creator is your call; agents make no contact |
| Personal knowledge of the creator | Hinted (SOL-66573/4) | Privacy-sensitive: no digging into anyone's private life |
| Brute-forcing the key | No | The vanity key is random |
| Brute-forcing passwords | Only once the right reading is known | About 10⁹ tried, none opened |
| Quantum computer | Not today | The creator raised it: "solvable with a few stable qubits" and BIP-360 (SOL-66589, SOL-66555). They may move the funds first |

## 5. Other useful questions
- **Has someone solved it quietly?** Not to the point of taking the key.
  - The prize is unspent. The creator: "If wallet != empty, puzzle not solved (Most likely)" (SOL-32535).
  - "Some already found it…" (SOL-66600, [drinking]) replied to a challenge of the line 'The "5" btc was never the actual prize' (SOL-66593). So "it" probably means that "actual prize", a secret the creator wanted to share, not the key.
- **Can the creator still verify an answer?** Not reliably. The creator "forgot the last details" (2021), and the answer sits on "a hidden laptop which I haven't touched in years" (SOL-66568).
- **Why did the early stages fall in days?**
  - Each clue there had one recognisable target and came with an instruction.
  - Here the clues name ingredients without values, several must be combined, and nothing shows until the combination is exactly right.
- **What single result would change everything?** dbbi or faed decoding to readable text, or an 80-byte blob opening to a 64-hex value.
- **Is it a scam?** The evidence says no.
  - The prize is real and moves by the announced rule, and every solved stage was genuine.
  - The creator: "I couldn't happily live with the idea that some would think that this was a scam" (SOL-9621).
- **Could the site vanish?** It went down in May 2026 (SOL-63942) and is back up. On 21 Oct its content matched the April 2026 copy, and we hold local copies.

## 6. Way forward (ranked by evidence per unit of cost)
1. **Decode-first tests on dbbi and faed, judged by readability.** Cost: minutes. A hit proves itself.
   - Selectors from the image's yellow and blue cells (planned by an earlier agent, never run).
   - The 2023 words read as operations, not values (your repo's top recommendation).
   - Prime selection combined with zeroing (SOL-8000).
2. **Reading only, no compute.**
   - Find the "unforseen hint" for matrixsumlist (given before 14 Mar 2021). Best lead: "You are at the prime part already???… That might have been a hint" (SOL-5966/5969, 1 Mar 2021).
   - Pin down "our first hint". Candidates: the "First external hint" (COM-26065, the 1 Apr 2019 rickroll puzzle) or "Follow the white rabbit." (COM-28522, launch night).
3. **Cheap closures of known blind spots.** These turn "probably covered" into real negatives.
   - Run the existing 245.9 M recipe grammar on cosmic, with sha256 and md5.
   - Regrade everything that passed the padding check, using a grader that also catches binary plaintext.
   - Audit the p32 padding excess: 185 passes vs 148.5 expected.
   - Try "we won't" in the lastwords slot.
   - Solve the 14×14 grid as a yin-yang logic puzzle.
4. **Stop doing these:**
   - big guess lists that don't come from a new interpretation;
   - chasing coincidences;
   - treating valid padding as success;
   - treating drunk or April Fools replies as instructions.
5. **Your decisions:**
   - whether to use public facts the creator has posted about themselves (the close-friends route);
   - whether to report a suspected build error to the creator, if an interpretation fits perfectly but the lock doesn't open.

## 7. What our own tests (21–22 Oct) ruled out

| Test | Idea | Candidates | Result |
|---|---|---|---|
| A + A2 | Image numbers ("First or zero") joined with the recipe and hint words | 359,575 | 0 hits |
| B + B2 | Primes → delete/zero → matrix sums → list | 642,369 | 0 hits |
| D + D2 | lastwords = a 1–12-word window of the Architect scene (8 spellings) | 241,597 | 0 hits |
| E + markers | FAED minus each 570-letter window of the scene | 11,100 strings | noise |

- **Scale:** 44,767,476 decrypt trials on salph_inner, p32_trailing and cosmic.
- **Padding passes:** 176,187, against 175,559 expected by chance.
- **Caveat on the cosmic results.** Our grader flagged only plaintext at least 90 % printable or containing a key, and kept nothing else.
  - The solved Phase 3.2 page is only ~60 % printable, so a correct plaintext that is partly binary would have been missed.
  - So the cosmic negatives are weaker than "0 hits" sounds.
- **Caveat on Test E.** It rested on YOUWON and {1},{4},{21}, which the record treats as a coincidence and an April Fools joke.

**Corrections found in this pass:**
- Several 2026 messages under the creator's name are members forwarding old posts: "Equivalent of 25 btc", "The puzzle talks for me", and the Dutch lines.
- "Friends and family can get to all my data" (SOL-9595) is about succession ("don't expect a halving of the price"). It is not a solving hint.
- "Bingo" (SOL-60312) followed a member quoting the Cartman line the creator had just mentioned. It is not a puzzle confirmation.
