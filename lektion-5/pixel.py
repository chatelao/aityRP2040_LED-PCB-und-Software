# --- PIXEL STATE (COMPOSITE VARIABLES) ---
pixel1 = {"x": 0, "y": 0}
pixel2 = {"x": 15, "y": 15}

# --- MOVEMENT FUNCTIONS ---
def moveRight(pixel):
    pixel["x"] = min(15, pixel["x"] + 1)

def moveLeft(pixel):
    pixel["x"] = max(0, pixel["x"] - 1)

def moveUp(pixel):
    pixel["y"] = min(15, pixel["y"] + 1)

def moveDown(pixel):
    pixel["y"] = max(0, pixel["y"] - 1)
