# Lektion 5: Halloween & Herbst Matrix Engine & Animationen

Willkommen zu Lektion 5! In dieser Lektion wird die 16x16 NeoPixel LED-Matrix zum Leben erweckt. Wir steuern 32 verschiedene Halloween- und Herbst-Klassiker mit flüssigen 4-Frame-Animationen an. Ausserdem zeigt die Lektion, wie Grafiken über eine strukturierte JSON-Datei geladen und entweder automatisch abgespielt oder interaktiv mit dem Arcade Joystick gesteuert werden.

## Übersicht der Dateien

- **`images.json`**: Enthält die Farbpalette sowie alle 32 Motive mit jeweils 4 Animationsframes im ASCII-Art-Raster-Format (16x16).
- **`code.py`**: Automatische Wiedergabe-Engine. Das Skript lädt `images.json` und spielt thematisch passende Motiv-Gruppen in einer Endlosschleife auf der LED-Matrix ab.
- **`code.joystick.py`**: Interaktive Steuerung. Erlaubt das Wechseln zwischen Motiven und einzelnen Frames über den angeschlossenen Arcade Joystick.
- **`pixel.py`**: Beispielsammeldatei für Koordinaten- und Positionslogik von Pixel-Objekten.
- **`render_images.py`**: Hilfsskript zum automatischen Rendern aller 32 Motive in PNG-Einzelbilder (128 Frames) und animierte GIFs (32 Dateien).

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

## Galerie der 32 Motive

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
| **17** | **Autumn Maple Leaf** | Color Shift & Morning Dew | ![Autumn Maple Leaf](./images/17_autumn_maple_leaf_anim.gif) |
| **18** | **Haunted House** | Lightning Strike & Flickering Windows | ![Haunted House](./images/18_haunted_house_anim.gif) |
| **19** | **Wise Owl** | Head Tilt, Blink & Hoot | ![Wise Owl](./images/19_wise_owl_anim.gif) |
| **20** | **Toadstool Mushroom** | Glowing Spores | ![Toadstool Mushroom](./images/20_toadstool_mushroom_anim.gif) |
| **21** | **Scarecrow** | Blinking Eyes & Waving Straw | ![Scarecrow](./images/21_scarecrow_anim.gif) |
| **22** | **Poison Apple** | Dripping Green Skull Poison | ![Poison Apple](./images/22_poison_apple_anim.gif) |
| **23** | **Flickering Candle** | Dancing Flame & Melting Wax | ![Flickering Candle](./images/23_flickering_candle_anim.gif) |
| **24** | **Falling Acorn** | Swaying Oak Nut & Leaf | ![Falling Acorn](./images/24_falling_acorn_anim.gif) |
| **25** | **Spellbook** | Floating Pentagram & Magic Sparks | ![Spellbook](./images/25_spellbook_anim.gif) |
| **26** | **Campfire** | Crackling Flames & Rising Embers | ![Campfire](./images/26_campfire_anim.gif) |
| **27** | **Frankenstein's Bride** | Electric Hair Streaks | ![Frankenstein's Bride](./images/27_frankensteins_bride_anim.gif) |
| **28** | **Werewolf** | Howling at the Moon | ![Werewolf](./images/28_werewolf_anim.gif) |
| **29** | **Spiderweb** | Dew Glint & Caught Fly | ![Spiderweb](./images/29_spiderweb_anim.gif) |
| **30** | **Magic Potion** | Swirling Color-Changing Elixir | ![Magic Potion](./images/30_magic_potion_anim.gif) |
| **31** | **Grim Reaper** | Glowing Eyes & Gleaming Scythe | ![Grim Reaper](./images/31_grim_reaper_anim.gif) |
| **32** | **Harvest Cornucopia** | Bountiful Autumn Shimmer | ![Harvest Cornucopia](./images/32_harvest_cornucopia_anim.gif) |

Viel Spass beim Ausprobieren und Programmieren eigener Animationsmuster!
