import board
import neopixel
import digitalio
import time
import random

# Matrix Konfiguration
PIXEL_PIN = board.D10
WIDTH = 16
HEIGHT = 16
pixels = neopixel.NeoPixel(PIXEL_PIN, WIDTH * HEIGHT, brightness=0.1, auto_write=False)

# Eingabe Konfiguration
# Mapping laut README: Oben=D0, Unten=D1, Links=D4, Rechts=D5
up = digitalio.DigitalInOut(board.D0)
down = digitalio.DigitalInOut(board.D1)
left = digitalio.DigitalInOut(board.D4)
right = digitalio.DigitalInOut(board.D5)

for pin in [up, down, left, right]:
    pin.direction = digitalio.Direction.INPUT
    pin.pull = digitalio.Pull.UP

# Spiel-Variablen
player_x = WIDTH // 2
player_y = HEIGHT // 2
target_x = random.randint(0, WIDTH - 1)
target_y = random.randint(0, HEIGHT - 1)
score = 0

def get_index(x, y):
    return y * WIDTH + x

print("Mini-Game: Fang das Pixel!")

while True:
    pixels.fill((0, 0, 0))

    # Joystick
    if not up.value and player_y > 0:
        player_y -= 1
    if not down.value and player_y < HEIGHT - 1:
        player_y += 1
    if not left.value and player_x > 0:
        player_x -= 1
    if not right.value and player_x < WIDTH - 1:
        player_x += 1

    # Kollisionserkennung
    if player_x == target_x and player_y == target_y:
        score += 1
        print(f"Gefangen! Score: {score}")
        # Neues Ziel
        target_x = random.randint(0, WIDTH - 1)
        target_y = random.randint(0, HEIGHT - 1)
        # Kurzes visuelles Feedback
        pixels.fill((0, 255, 0))
        pixels.show()
        time.sleep(0.1)

    # Zeichnen
    pixels[get_index(target_x, target_y)] = (255, 0, 0) # Ziel: Rot
    pixels[get_index(player_x, player_y)] = (0, 0, 255) # Spieler: Blau
    pixels.show()

    time.sleep(0.05)
