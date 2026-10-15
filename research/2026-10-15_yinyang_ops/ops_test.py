"""
Pre-registered operations test (report v2, next-check #1).

Question: using only creator-confirmed themes, does an operation on DBBI / FAED
produce a reject-capable milestone word -- the literal "YINYANG"/"YINGYANG"
(the creator's "yin yang" is "the next phase"; "once you hit a yin yang you'll
solve it the same day")? Positive control: the community "YOUWON" finding
(DBBI a=1..i=9  minus  VIC a=1..z=26, mod 26) must reproduce.

Alphabets:
  DBBI/FAED use letters a..i only.
  VIC sentence (91 letters) uses the full alphabet.
Digit maps tried for a..i: linear a=1..i=9; DBBI first-occurrence order
  (D B I F H C E G A -> 0..8); plain a=0..i=8.
Combiners: +, -, reverse-, over the paired letters, reduced mod 26, mapped to
  A..Z under both 0->A and 1->A conventions, both directions.

This is reject-capable: we only report exact occurrences of target words; no
tuning toward them.
"""
import json

DBBI = open('../../reproduction/results/dbbi.txt').read().strip()
FAED = open('../../reproduction/results/faed.txt').read().strip()
VIC = "incaseyoumanagetocrackthistheprivatekeysbelongtohalfandbetterhalfandtheyalsoneedfundstolive"
assert len(DBBI) == len(VIC) == 91

TARGETS = ["YINYANG", "YINGYANG", "YOUWON", "YANG", "YIN", "SEED", "PRIME",
           "PRIVATE", "BTCSEED", "WALLET", "DOOR", "SOLVED", "NEXT"]

def linear(c):          # a=1..i=9
    return ord(c) - ord('a') + 1
def zero_based(c):      # a=0..i=8
    return ord(c) - ord('a')
FIRST_OCC = {c: i for i, c in enumerate("dbifhcega")}
def firstocc(c):
    return FIRST_OCC[c]
def vic_val1(c):        # a=1..z=26
    return ord(c) - ord('a') + 1
def vic_val0(c):        # a=0..z=25
    return ord(c) - ord('a')

DIGIT_MAPS = {"lin": linear, "zero": zero_based, "focc": firstocc}
VIC_MAPS = {"v1": vic_val1, "v0": vic_val0}

def to_letters(vals, base):     # base: 0 -> value 0 is 'A'; 1 -> value 1 is 'A'
    return ''.join(chr(((v - base) % 26) + ord('A')) for v in vals)

def search(name, letters):
    found = []
    for t in TARGETS:
        i = letters.find(t)
        if i >= 0:
            found.append((t, i))
    if found:
        hits.append({"op": name, "found": found, "text": letters})
    allops.append({"op": name, "text": letters})

hits = []
allops = []

for block_name, block in [("DBBI", DBBI), ("FAED_head91", FAED[:91]),
                          ("FAED_tail91", FAED[-91:])]:
    for dmn, dm in DIGIT_MAPS.items():
        for vmn, vm in VIC_MAPS.items():
            dd = [dm(c) for c in block]
            vv = [vm(c) for c in VIC]
            combos = {
                "sub": [a - b for a, b in zip(dd, vv)],
                "rsub": [b - a for a, b in zip(dd, vv)],
                "add": [a + b for a, b in zip(dd, vv)],
            }
            for cn, vals in combos.items():
                for out_base in (0, 1):
                    search(f"{block_name}.{dmn}.{vmn}.{cn}.outbase{out_base}",
                           to_letters(vals, out_base))
                    search(f"{block_name}.{dmn}.{vmn}.{cn}.outbase{out_base}.rev",
                           to_letters(vals[::-1], out_base))

# Also DBBI vs FAED-head (both a..i) against each other
for dmn, dm in DIGIT_MAPS.items():
    dd = [dm(c) for c in DBBI]
    ff = [dm(c) for c in FAED[:91]]
    for cn, vals in {"sub": [a - b for a, b in zip(dd, ff)],
                     "add": [a + b for a, b in zip(dd, ff)]}.items():
        for ob in (0, 1):
            search(f"DBBIxFAED.{dmn}.{cn}.outbase{ob}", to_letters(vals, ob))

print(f"operations evaluated: {len(allops)}")
print(f"operations containing a target word: {len(hits)}")
for h in hits:
    print(json.dumps({"op": h["op"], "found": h["found"]}))
json.dump({"hits": hits, "all": allops}, open("ops_results.json", "w"), indent=0)
