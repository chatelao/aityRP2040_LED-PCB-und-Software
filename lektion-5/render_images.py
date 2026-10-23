import os
import json
import re
from PIL import Image, ImageDraw

def hex_to_rgba(hex_str):
    hex_str = hex_str.lstrip('#')
    r, g, b = tuple(int(hex_str[i:i+2], 16) for i in (0, 2, 4))
    return (r, g, b, 255)

def get_slug(name):
    s = name.replace("'", "")
    s = re.sub(r'[^a-zA-Z0-9]+', '_', s).strip('_').lower()
    return s

def render_frame(frame_data, palette):
    img = Image.new('RGBA', (256, 256), (40, 40, 40, 180))
    draw = ImageDraw.Draw(img)
    for y in range(16):
        for x in range(16):
            char = frame_data[y][x]
            color = palette.get(char, (0, 0, 0, 255))
            box = [x * 16 + 1, y * 16 + 1, (x + 1) * 16 - 1, (y + 1) * 16 - 1]
            draw.rectangle(box, fill=color)
    return img

def render_all(json_path="lektion-5/images.json", output_dir="lektion-5/images"):
    os.makedirs(output_dir, exist_ok=True)
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    palette_raw = data["palette"]
    palette = {k: hex_to_rgba(v) for k, v in palette_raw.items()}

    images_data = data["images"]
    print(f"Loaded {len(images_data)} image definitions from {json_path}.")

    for img_def in images_data:
        idx = img_def["id"]
        slug = get_slug(img_def["name"])
        frames_raw = img_def["frames"]

        rendered_frames = []
        for frame_idx, frame_data in enumerate(frames_raw, start=1):
            frame_img = render_frame(frame_data, palette)
            rendered_frames.append(frame_img)
            png_filename = f"{idx:02d}_{slug}_frame{frame_idx}.png"
            png_path = os.path.join(output_dir, png_filename)
            frame_img.save(png_path, "PNG")

        gif_filename = f"{idx:02d}_{slug}_anim.gif"
        gif_path = os.path.join(output_dir, gif_filename)

        gif_frames = [f.convert("P", palette=Image.ADAPTIVE) for f in rendered_frames]
        gif_frames[0].save(
            gif_path,
            save_all=True,
            append_images=gif_frames[1:],
            duration=300,
            loop=0
        )

    print("Rendering complete!")

if __name__ == "__main__":
    render_all()
