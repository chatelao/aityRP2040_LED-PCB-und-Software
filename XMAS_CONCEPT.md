# Konzept: Xmas PCB (Weihnachts-Leiterplatte)

Dieses Dokument beschreibt das Hardware- und Softwarekonzept für die interaktive Weihnachts-Leiterplatte (Xmas PCB) auf Basis des **Seeed Studio XIAO ESP32-C6** mit **CircuitPython**.

---

## 1. Übersicht & Zielsetzung

Das Xmas PCB ist als interaktives Schulungs- und Dekorationsobjekt gestaltet (z. B. in Form eines Weihnachtsbaums). Es kombiniert visuelle Effekte mit kapazitiver Berührungssensorik und bietet Erweiterungsmöglichkeiten für eigene Elektronikprojekte.

### Hauptmerkmale
- **Mikrocontroller**: Seeed Studio XIAO ESP32-C6
- **Laufzeitumgebung**: CircuitPython
- **Beleuchtung**: 64 serielle RGB-LEDs (Neopixel / WS2812B oder SK6812)
- **Interaktion**: 4 kapazitive Touch-Ornamente ("Weihnachtskugeln" / Bulbs) sowie ein kapazitiver Slider (Schieberegler) als feierliches Ornament (z. B. als Girlande oder Baumschmuck-Band)
- **Erweiterbarkeit**: Alle weiteren verfügbaren GPIO-Pins sind als Lötpads mit mechanischer Zugentlastung herausgeführt.

---

## 2. Hardware-Architektur

### 2.1 Mikrocontroller (XIAO ESP32-C6)
Der Seeed Studio XIAO ESP32-C6 bietet moderne drahtlose Konnektivität (Wi-Fi 6, Bluetooth 5, Zigbee/Thread) sowie ausreichend Rechenleistung für komplexe Lichtmuster und Interaktionen in CircuitPython.

### 2.2 Serielle RGB-LEDs (64x)
- **Typ**: WS2812B-Mini (3528/2020) oder SK6812.
- **Anordnung**: In einer dekorativen Matrix oder entlang der Kontur/Äste des Weihnachtsbaums verschaltet.
- **Ansteuerung**: Alle 64 LEDs sind seriell hintereinander geschaltet (Daisy Chain) und werden über einen einzelnen Datenpin angesteuert.
- **Datenpin**: Verbunden mit **D10** (GPIO18).

### 2.3 Kapazitive Touch-Ornamente & Kapazitiver Slider
- **Weihnachtskugeln (4x Touch-Pads)**:
  - **Funktion**: 4 grossflächige Kupferflächen auf der Platinenoberfläche, geformt als Weihnachtsbaumkugeln.
  - **Sensorik**: Werden über die kapazitive Touch-Funktion von CircuitPython (`touchio.TouchIn`) eingelesen.
  - **Pin-Zuordnung**:
    - **Touch 1 (Ornament A)**: **D0** (GPIO0)
    - **Touch 2 (Ornament B)**: **D1** (GPIO1)
    - **Touch 3 (Ornament C)**: **D2** (GPIO2)
    - **Touch 4 (Ornament D)**: **D3** (GPIO21)
- **Kapazitiver Slider (Girlanden-Schieberegler)**:
  - **Funktion**: Ein als dekorative Lametta-Girlande oder Schmuckband geformter kapazitiver Schieberegler quer über den Weihnachtsbaum.
  - **Funktionsweise**: Besteht aus nebeneinander angeordneten kapazitiven Kupfersegmenten (Interdigital- oder Keilstruktur). Die Pins des Sliders nutzen die Touch-Kanäle (z. B. **D0** bis **D3**), um durch interpolation der Berührungssignale eine kontinuierliche Position (z. B. Helligkeit, Farbauswahl oder Scroll-Effekt) zu berechnen.

### 2.4 Lötpads mit Zugentlastung (Strain Relieved Solder Pads)
Alle verbleibenden freien Ausgänge und Schnittstellen des XIAO ESP32-C6 sowie Stromversorgungs-Piping werden auf dedizierte Lötpads herausgeführt.
- **Zugentlastung**: Jedes Lötpad besitzt mindestens zwei benachbarte, unbeschichtete Durchkontaktierungen (Stanzlöcher/Bohrungen), durch die das Anschlusskabel gefädelt werden kann, bevor es auf das Lötpad gelötet wird. Dies verhindert das Ausreissen der Lötstelle bei mechanischer Belastung.
- **Herausgeführte Pins**:
  - **D4** (GPIO22 / I2C SDA)
  - **D5** (GPIO23 / I2C SCL)
  - **D6** (GPIO16 / UART TX)
  - **D7** (GPIO17 / UART RX)
  - **D8** (GPIO19 / SPI SCK)
  - **D9** (GPIO20 / SPI MISO)
  - **VBUS** (5V USB-Versorgung)
  - **3V3** (3.3V Regler-Ausgang)
  - **GND** (Masseanschlüsse)

---

## 3. Pin-Belegung (Pin Mapping)

| XIAO Pin | ESP32-C6 GPIO | Funktion auf Xmas PCB | Beschreibung |
| :--- | :--- | :--- | :--- |
| **D0** | GPIO0 | Touch Ornament 1 / Slider Segment 1 | Kapazitives Touchpad "Kugel 1" & Slider Position 1 |
| **D1** | GPIO1 | Touch Ornament 2 / Slider Segment 2 | Kapazitives Touchpad "Kugel 2" & Slider Position 2 |
| **D2** | GPIO2 | Touch Ornament 3 / Slider Segment 3 | Kapazitives Touchpad "Kugel 3" & Slider Position 3 |
| **D3** | GPIO21 | Touch Ornament 4 / Slider Segment 4 | Kapazitives Touchpad "Kugel 4" & Slider Position 4 |
| **D4** | GPIO22 | Lötpad D4 (SDA) | Mit Zugentlastung herausgeführt |
| **D5** | GPIO23 | Lötpad D5 (SCL) | Mit Zugentlastung herausgeführt |
| **D6** | GPIO16 | Lötpad D6 (TX) | Mit Zugentlastung herausgeführt |
| **D7** | GPIO17 | Lötpad D7 (RX) | Mit Zugentlastung herausgeführt |
| **D8** | GPIO19 | Lötpad D8 (SCK) | Mit Zugentlastung herausgeführt |
| **D9** | GPIO20 | Lötpad D9 (MISO) | Mit Zugentlastung herausgeführt |
| **D10** | GPIO18 | NeoPixel Data | Datenleitung für 64x RGB-LEDs |

---

## 4. Stromversorgung & Leistungsbudget

- **Maximaler Stromverbrauch**:
  - 64 RGB-LEDs bei voller Helligkeit (Weiss): $64 \times 60\text{ mA} \approx 3.84\text{ A}$.
  - Im normalen Betrieb (gemischte Farben, dynamische Effekte, Helligkeit begrenzt auf ca. 20-30%): $\approx 500\text{ mA} - 1.0\text{ A}$.
- **Stromzuführung**:
  - Die Stromversorgung erfolgt primär über den USB-C Anschluss des XIAO ESP32-C6 oder über externe 5V-Lötpads mit Zugentlastung.
  - Auf der Platine sind ausreichend Pufferkondensatoren (z. B. $100\ \mu\text{F}$ Elektrolytkondensator an der 5V-Schiene sowie $100\text{ nF}$ Keramikkondensatoren pro LED) vorgesehen.

---

## 5. Software-Konzept (CircuitPython)

Das Board nutzt CircuitPython für einfache Programmierbarkeit.

### Beispielskelett (`code.py`)

```python
import board
import touchio
import neopixel
import time

# 1. NeoPixel Initialisierung (64 LEDs an D10)
NUM_PIXELS = 64
pixels = neopixel.NeoPixel(board.D10, NUM_PIXELS, brightness=0.2, auto_write=False)

# 2. Touch-Pads & Slider Initialisierung (Segment 1 bis 4 an D0 - D3)
touch_pins = [board.D0, board.D1, board.D2, board.D3]
touch_inputs = [touchio.TouchIn(pin) for pin in touch_pins]

# Farbdefinitionen
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GOLD = (255, 215, 0)
OFF = (0, 0, 0)

print("Xmas PCB bereit!")

def get_slider_position():
    """Liest die Slider-Pads aus und ermittelt die Berührungsposition (0-3) oder None."""
    for idx, touch_in in enumerate(touch_inputs):
        if touch_in.value:
            return idx
    return None

while True:
    # Slider- / Touch-Eingabe auswerten
    slider_pos = get_slider_position()

    if slider_pos is not None:
        # Je nach Slider-Position Helligkeit oder LED-Anzahl anpassen
        active_count = int((slider_pos + 1) * (NUM_PIXELS / len(touch_pins)))
        pixels.fill(OFF)
        for i in range(active_count):
            pixels[i] = GOLD
    else:
        # Standard-Muster
        for i in range(NUM_PIXELS):
            if i % 2 == 0:
                pixels[i] = GREEN
            else:
                pixels[i] = RED

    pixels.show()
    time.sleep(0.05)
```

---

## 6. Mechanisches Layout & PCB-Design

- **Aussenkontur**: Weihnachtsbaumform mit abgerundeten Ecken.
- **Topologie**:
  - Der XIAO ESP32-C6 wird mittig oder im unteren Bereich platziert (männliche/weibliche Stiftleisten oder direkt aufgelötet).
  - Die 64 LEDs sind gleichmässig als "Baumschmuck" und Hintergrundbeleuchtung verteilt.
  - Die 4 Touch-Ornamente sind als exponierte, vergoldete (ENIG) Kupfer-Weihnachtskugeln auf der Vorderseite angeordnet.
  - Der kapazitive Slider zieht sich als geschwungene, vergoldete Girlande waagerecht oder leicht diagonal über die Vorderseite des Weihnachtsbaums.
  - Die Lötpads mit Zugentlastung befinden sich am unteren Rand (Stammbereich) der Leiterplatte.
