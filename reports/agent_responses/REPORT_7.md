# GSMG 5 BTC Puzzle — Why It Remains Unsolved

Oct 22, 2026 · @Jon

## Scope and evidence base

This answers three questions about the GSMG.IO 5 BTC puzzle: why no one has solved it after about seven years, what solving it requires, and how a solver could reach the answer. It is evidence-based and independent of any path we choose next.

It draws on the consolidated community archive (testnetbtc/GSMG), read in full: 116 issues, 17 pull requests and roughly 640 comments, the three source repositories' own documents, plus our own test record and the Telegram transcript of the creator's messages. Key claims were re-checked against those primary sources rather than taken from summaries.

The prize is now about 1.25 BTC at 1GSMG1JC9wtdSwfwApgj2xcmJPAwx7prBe, with a further 3.75 BTC at 17ucy1K9ZUAaoY6JVtM932W9jUp5LXfyHa. The solved chain runs from the opening image through to SalPhaseIon, whose letter "soup" decoded to labels plus two unopened AES envelopes; a third unopened envelope trails phase 3.2. Nothing beyond the soup has a verified opening.

## Why no one has solved it

Seven reasons, ranked by how much the evidence supports each.

1. **No way to tell success from failure after SalPhaseIon.** The creator has published exactly one checkpoint in seven years (the 2019 Phase-1 hash). Past the soup, the only signal is AES padding, which a wrong password passes about 1 time in 256 (measured in the archive at 1 in 243 and 1 in 236). Every claimed "opening" has the wrong-key signature: output exactly one byte short of a block, and random bytes. The "Cosmic Duality" decryption (1,327 bytes) was copied, built on and "verified" by more than ten people over about eight months; two different keys were even claimed to give the same output, which is impossible.
2. **The final step is labelled but never defined.** The soup names ingredients (matrixsumlist, lastwordsbeforearchichoice, thispassword, "our first hint is your last command") but gives no rules for combining them. The creator's hints are themes, not operations: primes, "zeroed out", yin yang. The Phase-2 page spelled out answer formatting; SalPhaseIon gives none.
3. **Every earlier hard gate fell only after a creator hint.** Entry into SalPhaseIon took about two years and needed the Roses hint, Decentraland and the "hash the text" recipe. The current gate has had themes but no operational hint since February 2023. In 2023 the creator said a further hint "would probably be a give away" and that he hopes not to give one.
4. **Noise and misattribution distort the search.** Several widely cited "creator rules" are other people's words: FEFEFE/104 and the prime set {2,3,5,7} came from solvers; "#..# wasn't used / 2nd way wasn't found" is a community summary from February 2021, now quoted as the creator. Real hints are mixed with April-Fool posts and one self-described intoxicated session. From 2025 on, LLM-generated "solutions" dominate, enough that maintainers post notices telling AI agents to ignore whole threads.
5. **Negatives do not add up to coverage.** Most community sweeps used printable-text checks (blind to a binary result) or only one key-derivation setting; one public tool used the wrong one, voiding a 116,000-candidate sweep. There is no shared record of what is ruled out. Our own roughly 240 million trials share the same blind spot: an output that is raw key bytes rather than text would pass a padding check unnoticed.
6. **The two decodes that look non-random lead nowhere yet.** FAED decoded with a key square built from DBBI begins "BTCSEED" (chance of that exact word under that key about 4 in 10 million; if any key ordering counts, the community estimate is about 1 in 15). DBBI minus the puzzle's own last sentence gives "YOUWON", with V-I-C at the hinted positions 1, 4 and 21 (about 1 in 1,400 by chance; the creator's only reaction was "Pfff. Coincidence."). After both words the text is unreadable and the next operation is unknown.
7. **Possible human factors, unquantifiable.** The creator admits rushed work and typos ("A day later I can hardly understand what I have done"), says solvers know the puzzle "WAAAY better than me", and says close friends have "the best chance". He has said both "Some already found it. And understood not to risk it…" and "If wallet != empty, puzzle not solved (Most likely)".

## What solving requires, and why

- **One correct transformation of the soup into "thispassword".** DBBI and FAED are the only undecoded content on the page; everything else on it decoded to labels. The creator calls the gap "1 microstep", says "the hardest part is done", says "no need \[for brute force\], you have all the info", and says the remaining steps are easier than the solved ones.
- **A check that cannot be faked.** Either readable text (every solved stage produced it) or an exact match to the prize public key, which has been public since the 2020 spend. Padding alone will never settle it.
- **Then the chain probably runs itself.** The small envelope's plaintext can only be 64–79 bytes (a key or a short message). "sha256 ans too" plausibly feeds the Cosmic password. The creator says yin yang is "the next phase", reachable "the same day", "2 hours max". The prize address is a vanity address, so its key was ground at random and must be written inside a plaintext, not computed from the puzzle's artifacts.

## How a solver can solve it

- Test small, pre-registered families of readings of the soup, in every spelling the creator has used (lowercase, uppercase, kept case and punctuation, spaced, reversed).
- Check every padding-valid output with both validators above, including raw 32-byte windows tested against the prize public key, not only for printable text.
- Start from the material that is demonstrably non-random: BTCSEED's remaining 563 letters and YOUWON's 64-letter tail, read through the February 2023 ingredient order (yellow, blue, primes, matrixsumlist, lastwordsbeforearchichoice, yinyang).
- Keep a shared ledger of negatives so nothing is repeated.

## However the answer is reached, the only four routes

1. **Find the intended reading** — the transformation the creator built in.
2. **Get information** — the extra hint the creator said in 2023 he might eventually give; the team he said "partly" passed SalPhaseIon; or the full Telegram export, which restores messages cut off in the copies we hold.
3. **The creator ends it.** He holds the key; it spent at both halvings, so whoever ran the puzzle controls it.
4. **Break the key.** Impossible with today's computers (the two spends used distinct ECDSA nonces, so there is no nonce-reuse weakness). It becomes possible with a large quantum computer, because the public key has been exposed since 2020 — a point the creator has raised himself.

## Other questions worth asking

- **How will we know we are right?** Readable text or an exact key match, nothing else.
- **Which "facts" are really the creator's?** Check every rule against the Telegram transcript before using it; the community record repeatedly puts other people's words in his mouth.
- **Did anyone get further?** The creator said one team "managed to find something" (2020) and another passed "partly" (2023). Neither has published anything.
- **What should stop?** Padding-only claims, LLM-built "chains", the Cosmic Duality book as a password source, and unbounded sweeps.

## A way forward grounded in the evidence

1. Fix our own blind spot first: re-check stored padding-valid outputs (and all future ones) for raw key material against the prize public key.
2. Work only the DBBI/FAED → "thispassword" step, starting from BTCSEED and YOUWON.
3. Test one untried lead with real support: the puzzle used the first two parts of Logic's song "The Warning" verbatim (the Phase-0 URL and the Phase-1 form password); its third part, which turns on a choice between two roses, has never been tried in the standard lock, and both the Roses hint and the puzzle's "choice" theme point at it.
4. Request the Telegram JSON export, which would restore cut-off messages and reply threading.

Standing rule: no oracle run until a reading's free checks pass and the test is written down in advance.

## Corrections to my own earlier reasoning

- I had called YOUWON "confirmed". It is suggestive (about 1 in 1,400 by chance, matching the {1},{4},{21} hint), but the hint it matches was posted on 1 April and the creator reacted with "Pfff. Coincidence." It is now weighed as unconfirmed.
- I had dismissed BTCSEED as chance on a test too weak to show that. The exact word under the one key square is about 4 in 10 million; allowing any key ordering, the community estimate is about 1 in 15. Both figures are recorded, and BTCSEED is treated as a probable intended intermediate whose continuation is unknown.

## Sources

- [testnetbtc/GSMG (consolidated archive)](https://github.com/testnetbtc/GSMG)
- [puzzlehunt/gsmgio-5btc-puzzle](https://github.com/puzzlehunt/gsmgio-5btc-puzzle)
- [Naddiseo/gsmgio-5btc-puzzle](https://github.com/Naddiseo/gsmgio-5btc-puzzle)
- [HosterjackAGV/gsmg-5btc-puzzle](https://github.com/HosterjackAGV/gsmg-5btc-puzzle)
- The creator's Telegram messages ("GSMG Puzzle Solvers" group), and our own test record, both cross-checked against the above.
