import time
import json
import board
import digitalio
import neopixel

# 16x16 Matrix = 256 Pixel
NUM_PIXELS = 256
pixels = neopixel.NeoPixel(board.D10, NUM_PIXELS, brightness=0.1, auto_write=False)

# Joystick-Pins für CircuitPython definieren
joystick_pins = {
    "Up": board.D4,
    "Down": board.D5,
    "Left": board.D0,
    "Right": board.D1
}

js_inputs = {}
for key, pin in joystick_pins.items():
    d = digitalio.DigitalInOut(pin)
    d.direction = digitalio.Direction.INPUT
    d.pull = digitalio.Pull.UP
    js_inputs[key] = d

print("CircuitPython Halloween Matrix Engine aktiv!")

# JSON-Datei laden
try:
    with open("images.json", "r") as f:
        data = json.load(f)
    palette = data["palette"]
    images = data["images"]
    print(f"{len(images)} Halloween-Motive erfolgreich geladen.")
except Exception as e:
    print(f"Fehler beim Laden von images.json: {e}")
    images = []

current_image_index = 0
current_frame_index = 0
num_images = len(images) if images else 1

last_up = js_inputs["Up"].value
last_down = js_inputs["Down"].value
last_left = js_inputs["Left"].value
last_right = js_inputs["Right"].value

def hex_to_rgb(hex_str):
    hex_str = hex_str.lstrip('#')
    return tuple(int(hex_str[i:i+2], 16) for i in (0, 2, 4))

def setze_pixel(x, y, color):
    if 0 <= x < 16 and 0 <= y < 16:
        index = y * 16 + x
        pixels[index] = color

while images:
    up_val = js_inputs["Up"].value
    down_val = js_inputs["Down"].value
    left_val = js_inputs["Left"].value
    right_val = js_inputs["Right"].value

    if not up_val and last_up:
        current_image_index = (current_image_index - 1) % num_images
        current_frame_index = 0
    if not down_val and last_down:
        current_image_index = (current_image_index + 1) % num_images
        current_frame_index = 0

    frames = images[current_image_index]["frames"]
    num_frames = len(frames)

    if not left_val and last_left:
        current_frame_index = (current_frame_index - 1) % num_frames
    if not right_val and last_right:
        current_frame_index = (current_frame_index + 1) % num_frames

    last_up = up_val
    last_down = down_val
    last_left = left_val
    last_right = right_val

    pixels.fill((0, 0, 0))

    active_frame = frames[current_frame_index]
    for y, row in enumerate(active_frame):
        for x, char in enumerate(row):
            if char in palette:
                setze_pixel(x, y, hex_to_rgb(palette[char]))

    pixels.show()
    time.sleep(0.05)
