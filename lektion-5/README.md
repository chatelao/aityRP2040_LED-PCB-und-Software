# Lektion 5: Halloween Matrix Engine & Animationen

Willkommen zu Lektion 5! In dieser Lektion wird die 16x16 NeoPixel LED-Matrix zum Leben erweckt. Wir steuern 16 verschiedene Halloween-Klassiker mit flüssigen 4-Frame-Animationen an. Ausserdem zeigt die Lektion, wie Grafiken über eine strukturierte JSON-Datei geladen und entweder automatisch abgespielt oder interaktiv mit dem Arcade Joystick gesteuert werden.

## Übersicht der Dateien

- **`images.json`**: Enthält die Farbpalette sowie alle 16 Motive mit jeweils 4 Animationsframes im ASCII-Art-Raster-Format (16x16).
- **`code.py`**: Automatische Wiedergabe-Engine. Das Skript lädt `images.json` und spielt thematisch passende Motiv-Gruppen in einer Endlosschleife auf der LED-Matrix ab.
- **`code.joystick.py`**: Interaktive Steuerung. Erlaubt das Wechseln zwischen Motiven und einzelnen Frames über den angeschlossenen Arcade Joystick.
- **`pixel.py`**: Beispielsammeldatei für Koordinaten- und Positionslogik von Pixel-Objekten.

## Hardware & Joystick-Steuerung

Falls du die interaktive Version (`code.joystick.py`) wählst, verwende die folgende Belegung für deinen Arcade Joystick am Seeed Studio XIAO RP2040:

| Joystick-Richtung | Anschluss (Pin) | GP-Nummer | Funktion |
| :--- | :---: | :---: | :--- |
| **Oben** | **D4** | GP06 | Vorheriges Motiv wählen |
| **Unten** | **D5** | GP07 | Nächstes Motiv wählen |
| **Links** | **D0** | GP26 | Vorherigen Animationsframe anzeigen |
| **Rechts** | **D1** | GP27 | Nächsten Animationsframe anzeigen |

> **Hinweis**: Vergiss nicht, `code.joystick.py` in `code.py` umzubennen und zusammen mit `images.json` auf das `CIRCUITPY`-Laufwerk deines Microcontrollers zu kopieren.

---

## Galerie der 16 Halloween-Motive

Jedes Motiv besteht aus einer 16x16 Matrix und 4 Animationsframes. Hier ist die Übersicht aller verfügbaren Motive:

| ID | Motivname | Beschreibung der Animation | Vorschau (Animation) |
| :-: | :--- | :--- | :-: |
| **1** | **Jack-o'-Lantern** | Candle Flicker & Laugh | ![Jack-o'-Lantern](./images/01_jack_o_lantern_anim.gif) |
| **2** | **Classic Ghost** | Floating & Waving Tail | ![Classic Ghost](./images/02_classic_ghost_anim.gif) |
| **3** | **Skull** | Chattering Jaw & Glowing Eyes | ![Skull](./images/03_skull_anim.gif) |
| **4** | **Vampire Bat** | Flapping Wings | ![Vampire Bat](./images/04_vampire_bat_anim.gif) |
| **5** | **Black Cat** | Looking Around & Blinking | ![Black Cat](./images/05_black_cat_anim.gif) |
| **6** | **Witch Hat** | Wagging Tip & Sparkling Buckle | ![Witch Hat](./images/06_witch_hat_anim.gif) |
| **7** | **Candy Corn** | Magical Sparkles & Shine | ![Candy Corn](./images/07_candy_corn_anim.gif) |
| **8** | **Frankenstein** | High Voltage Neck Bolts | ![Frankenstein](./images/08_frankenstein_anim.gif) |
| **9** | **Bubbling Cauldron** | Rising & Popping Potion Bubbles | ![Bubbling Cauldron](./images/09_bubbling_cauldron_anim.gif) |
| **10** | **Descending Spider** | Dropping Down on Web | ![Descending Spider](./images/10_descending_spider_anim.gif) |
| **11** | **Bloodshot Eyeball** | Darting Pupil Left & Right | ![Bloodshot Eyeball](./images/11_bloodshot_eyeball_anim.gif) |
| **12** | **RIP Tombstone** | Zombie Hand Emerging | ![RIP Tombstone](./images/12_rip_tombstone_anim.gif) |
| **13** | **Vampire** | Baring Fangs & Dripping Blood | ![Vampire](./images/13_vampire_anim.gif) |
| **14** | **Mummy** | Glowing Eyes & Shifting Eyes | ![Mummy](./images/14_mummy_anim.gif) |
| **15** | **Witch's Broom** | Sweeping & Magic Trail | ![Witch's Broom](./images/15_witchs_broom_anim.gif) |
| **16** | **Crescent Moon** | Passing Night Clouds | ![Crescent Moon](./images/16_crescent_moon_anim.gif) |

Viel Spass beim Ausprobieren und Programmieren eigener Animationsmuster!
