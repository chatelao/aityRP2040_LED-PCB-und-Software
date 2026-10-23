import board
import digitalio
import time

#      XIAO RP2040 Pinout & Joystick Wiring
#
#             +--------------+
# (Oben)   D0 | [ ]      [ ] | 5V
# (Unten)  D1 | [ ]      [ ] | GND <--- Common (GND)
#          D2 | [ ]      [ ] | 3V3
#          D3 | [ ]      [ ] | D10 (NeoPixel Matrix)
# (Links)  D4 | [ ]      [ ] | D9
# (Rechts) D5 | [ ]      [ ] | D8
#          D6 | [ ]      [ ] | D7
#             +-----USB------+

# Pin-Konfiguration für den Arcade-Controller
# Wir verwenden interne Pull-Up Widerstände, daher ist der Wert 'False', wenn gedrückt.
# Mapping laut README: Oben=D0, Unten=D1, Links=D4, Rechts=D5

pins = {
    "Oben": board.D0,
    "Unten": board.D1,
    "Links": board.D4,
    "Rechts": board.D5
}

# Initialisierung der Eingabestifte
inputs = {}
for name, pin in pins.items():
    io = digitalio.DigitalInOut(pin)
    io.direction = digitalio.Direction.INPUT
    io.pull = digitalio.Pull.UP
    inputs[name] = io

print("Arcade-Joystick Test")
print("Bewege den Joystick!")

while True:
    active = []
    for name, io in inputs.items():
        if not io.value: # Signal ist LOW, wenn gedrückt
            active.append(name)

    if active:
        print("Aktiv: " + ", ".join(active))

    time.sleep(0.1)
