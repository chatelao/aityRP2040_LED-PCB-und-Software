# Aity Kids 4-LED Board

Dieses Projekt bietet ein einfaches 4-LED-Board an, das mit einem Seeed Studio XIAO RP2040 (oder einem kompatiblen XIAO-Modul) betrieben wird. Es enthält Beispiele sowohl für CircuitPython als auch für den Microsoft MakeCode Maker.

## Hardware-Konfiguration

- **Mikrocontroller**: Seeed Studio XIAO RP2040.
- **NeoPixel-Datenpin**: Verbunden mit **D10** (entspricht **GP3** auf dem RP2040).
- **LED-Matrix**: In den bereitgestellten Beispielen für eine 16x16-Matrix (256 LEDs) konfiguriert.

<img width="616" height="432" alt="image" src="https://github.com/user-attachments/assets/f364a9d5-ba34-4fb9-b765-a625a0828113" />

## Lektionen

1. [Lektion 1: Erste Schritte](./lektion-1/Lektionserläuterung.md)
2. [Lektion 2: Arcade Controller](./lektion-2/README.md)
3. [Lektion 5: Halloween Matrix Engine & Animationen](./lektion-5/README.md)

## Vorbereitung des XIAO RP2040

Um eine neue Firmware (CircuitPython oder MakeCode) auf den XIAO RP2040 zu laden, müssen Sie zuerst in den **Bootloader-Modus** wechseln:

1. Verbinden Sie den XIAO RP2040 über USB mit Ihrem Computer.
2. Drücken und halten Sie die **BOOT**-Taste (beschriftet mit 'B').
3. Während Sie die **BOOT**-Taste gedrückt halten, drücken Sie einmal kurz die **RESET**-Taste (beschriftet mit 'R') oder stecken Sie das USB-Kabel ein.
4. Lassen Sie die **BOOT**-Taste los.
5. Ein neues Laufwerk mit dem Namen `RPI-RP2` sollte auf Ihrem Computer erscheinen.

---

## CircuitPython (CPy) Installation

### 1. CircuitPython-Firmware installieren
1. Laden Sie die neueste CircuitPython-UF2-Datei für den **Seeeduino XIAO RP2040** von [circuitpython.org](https://circuitpython.org/board/seeeduino_xiao_rp2040/) herunter.
2. Wechseln Sie in den Bootloader-Modus (siehe oben), damit das Laufwerk `RPI-RP2` erscheint.
3. Ziehen Sie die heruntergeladene UF2-Datei per Drag-and-Drop auf das Laufwerk `RPI-RP2`.
4. Das Board startet neu und ein neues Laufwerk mit dem Namen `CIRCUITPY` erscheint.

### 2. Bibliotheken installieren
CircuitPython benötigt externe Bibliotheken, um das Beispiel auszuführen.
1. Laden Sie das [CircuitPython Library Bundle](https://circuitpython.org/libraries) herunter.
2. Erstellen Sie einen Ordner namens `lib` auf Ihrem `CIRCUITPY`-Laufwerk, falls dieser noch nicht existiert.
3. Kopieren Sie die folgenden Ordner/Dateien aus dem Bundle in den `lib`-Ordner:
   - `adafruit_neopixel.mpy` (oder den Ordner)
   - `adafruit_imageload` (Ordner)
   - `adafruit_display_text` (falls für zukünftige Erweiterungen benötigt)

### 3. Code bereitstellen
1. Kopieren Sie die Datei `code.py` aus dem Stammverzeichnis dieses Repositories auf das `CIRCUITPY`-Laufwerk.
2. Falls der Code ein Bild benötigt, kopieren Sie `image.png` in das Stammverzeichnis des `CIRCUITPY`-Laufwerks.
3. Das Board lädt den Code automatisch neu und beginnt mit der Ausführung des Skripts.

---

## MakeCode-Installation

Der Microsoft MakeCode Maker bietet einen blockbasierten Editor sowie einen TypeScript-Editor für den RP2040.

### 1. Projekt öffnen
1. Gehen Sie auf [Microsoft MakeCode Maker](https://maker.makecode.com).
2. Klicken Sie auf **Import** und wählen Sie dann **Import File...** aus.
3. Wählen Sie die Datei `makecode/pxt.json` oder `makecode/main.ts` aus diesem Repository aus.
4. Wenn Sie dazu aufgefordert werden, wählen Sie **Seeed Studio XIAO RP2040** als Ihr Board aus.

### 2. Herunterladen und Flashen
1. Klicken Sie auf die Schaltfläche **Download** im MakeCode-Editor.
2. Es wird eine `.uf2`-Datei generiert.
3. Wechseln Sie in den Bootloader-Modus (siehe oben) auf Ihrem XIAO RP2040.
4. Ziehen Sie die heruntergeladene UF2-Datei per Drag-and-Drop auf das Laufwerk `RPI-RP2`.
5. Das Board startet neu und beginnt sofort mit der Ausführung Ihres MakeCode-Programms.
