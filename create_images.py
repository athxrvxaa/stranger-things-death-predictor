from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

characters = [
    "Eleven",
    "Max Mayfield",
    "Steve Harrington",
    "Dustin Henderson",
    "Jim Hopper",
    "Mike Wheeler",
    "Lucas Sinclair",
    "Will Byers",
    "Robin Buckley",
    "Nancy Wheeler",
]

img_dir = Path("images")
img_dir.mkdir(exist_ok=True)

for name in characters:
    img = Image.new("RGB", (500, 500), color=(30, 30, 40))
    draw = ImageDraw.Draw(img)

    # Border
    draw.rectangle([10, 10, 490, 490], outline=(0, 180, 255), width=6)

    # Center circle
    draw.ellipse([150, 120, 350, 320], fill=(0, 120, 200))

    # Initials
    initials = "".join([w[0] for w in name.split()][:2]).upper()
    draw.text((250, 220), initials, fill="white", anchor="mm")

    # Name at bottom
    draw.text((250, 400), name, fill="white", anchor="mm")

    filename = name.lower().replace(" ", "_") + ".jpg"
    img.save(img_dir / filename)

    print(f"Created {filename}")
