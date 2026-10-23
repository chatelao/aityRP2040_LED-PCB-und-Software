import board
import neopixel
import digitalio
import time

# Matrix Konfiguration
PIXEL_PIN = board.D10
WIDTH = 16
HEIGHT = 16
pixels = neopixel.NeoPixel(PIXEL_PIN, WIDTH * HEIGHT, brightness=0.1, auto_write=False)

# Joystick Konfiguration
# Mapping laut README: Oben=D0, Unten=D1, Links=D4, Rechts=D5
up = digitalio.DigitalInOut(board.D0)
down = digitalio.DigitalInOut(board.D1)
left = digitalio.DigitalInOut(board.D4)
right = digitalio.DigitalInOut(board.D5)

for pin in [up, down, left, right]:
    pin.direction = digitalio.Direction.INPUT
    pin.pull = digitalio.Pull.UP

# Startposition des Pixels
x = WIDTH // 2
y = HEIGHT // 2

def get_index(x, y):
    # Einfaches progressives Layout (wie in code.py definiert)
    return y * WIDTH + x

print("Pixel-Steuerung")
print("Nutze den Joystick, um den Pixel zu bewegen!")

while True:
    # Aktuellen Pixel loeschen
    pixels.fill((0, 0, 0))

    # Joystick abfragen
    if not up.value and y > 0:
        y -= 1
    if not down.value and y < HEIGHT - 1:
        y += 1
    if not left.value and x > 0:
        x -= 1
    if not right.value and x < WIDTH - 1:
        x += 1

    # Neuen Pixel zeichnen
    pixels[get_index(x, y)] = (255, 255, 255) # Weiss
    pixels.show()

    time.sleep(0.05)
