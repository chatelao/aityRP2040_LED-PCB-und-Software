import time
import json
import random
import board
import neopixel

# 16x16 Matrix = 256 Pixel
NUM_PIXELS = 256
pixels = neopixel.NeoPixel(board.D10, NUM_PIXELS, brightness=0.1, auto_write=False)

# JSON-Daten laden
with open("images.json", "r") as f:
    data = json.load(f)

# Palette einmalig vorab in RGB-Tupel (Triples) konvertieren
raw_palette = data["palette"]
rgb_palette = {
    k: tuple(int(v.lstrip('#')[i:i+2], 16) for i in (0, 2, 4))
    for k, v in raw_palette.items()
}

images = data["images"]

# Thematisch passende Bild-Dreiergruppen (Triples nach Index 0-15) definieren
triples = [
    (0, 6, 8),    # Jack-o'-Lantern, Candy Corn, Bubbling Cauldron
    (1, 2, 11),   # Classic Ghost, Skull, RIP Tombstone
    (3, 12, 15),  # Vampire Bat, Vampire, Crescent Moon
    (4, 5, 14),   # Black Cat, Witch Hat, Witch's Broom
    (7, 10, 13)   # Frankenstein, Bloodshot Eyeball, Mummy
]

while images:
    # Wähle ein zufälliges Motiv-Triple aus
    active_triple = random.choice(triples)
    
    for img_idx in active_triple:
        if img_idx < len(images):
            frames = images[img_idx]["frames"]
            
            # Zeige die 4-Frame-Animation zweimal pro Motiv an
            for _ in range(2):
                for frame in frames:
                    pixels.fill((0, 0, 0))
                    for y, row in enumerate(frame):
                        for x, char in enumerate(row):
                            if char in rgb_palette:
                                pixels[y * 16 + x] = rgb_palette[char]
                    pixels.show()
                    time.sleep(0.3)
