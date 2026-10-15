"""
Render the BTCSEED output's 256-symbol payload (odd stream minus I/O) as 16x16
bitmaps under several yin/yang binarizations (PIL only). The "yin yang"
milestone may be VISUAL (a QR / glyph / word / literal yin-yang), not numeric.
Produces one montage PNG of all binarizations, upscaled nearest-neighbour.
"""
import numpy as np
from PIL import Image, ImageDraw

S = open('../../reproduction/results/bifid_full.txt').read().strip()
SQUARE = "DBIFHCEGAKLMNOPQRSTUVWXYZ"
POS = {c: i for i, c in enumerate(SQUARE)}
ROW = {c: POS[c] // 5 for c in SQUARE}
COL = {c: POS[c] % 5 for c in SQUARE}

odd = S[1::2]
payload = ''.join(c for c in odd if c not in "IO")
assert len(payload) == 256

CLASS = {
    "rowpar": lambda c: ROW[c] & 1,
    "colpar": lambda c: COL[c] & 1,
    "sqidx>=12": lambda c: 1 if POS[c] >= 12 else 0,
    "alpha>=N": lambda c: 1 if c >= 'N' else 0,
    "rows01v24": lambda c: 0 if ROW[c] <= 1 else 1,
    "vowel": lambda c: 1 if c in "AEIOUY" else 0,
}
VIEWS = [("rowmaj", 0), ("rowmaj", 1), ("colmaj", 0), ("colmaj", 1)]

CELL = 10              # px per bit
PAD = 18              # label strip
cols, rows = len(VIEWS), len(CLASS)
tilew = 16 * CELL
tileh = 16 * CELL + PAD
montage = Image.new("RGB", (cols * tilew, rows * tileh), "white")
draw = ImageDraw.Draw(montage)

for r, (cname, fn) in enumerate(CLASS.items()):
    bits = np.array([fn(c) for c in payload])
    for c, (fill, pol) in enumerate(VIEWS):
        b = bits ^ pol
        g = b.reshape(16, 16) if fill == "rowmaj" else b.reshape(16, 16).T
        img = Image.fromarray((255 - g * 255).astype(np.uint8), "L").resize(
            (tilew, 16 * CELL), Image.NEAREST).convert("RGB")
        ox, oy = c * tilew, r * tileh
        draw.rectangle([ox, oy, ox + tilew - 1, oy + PAD - 1], fill="black")
        draw.text((ox + 2, oy + 4), f"{cname}/{fill}/p{pol}", fill="white")
        montage.paste(img, (ox, oy + PAD))

montage.save("grid_payload_binar.png")

# even stream {D,B,C,E}->0..3 as a 4-level image (15x20 padded)
even = S[0::2]
val = {"D": 0, "B": 1, "C": 2, "E": 3}
ev = np.array([val[c] for c in even] + [0] * (300 - len(even))).reshape(15, 20)
Image.fromarray((ev * 85).astype(np.uint8), "L").resize((20 * 16, 15 * 16),
    Image.NEAREST).save("grid_even_2bit.png")

print("wrote grid_payload_binar.png and grid_even_2bit.png")
