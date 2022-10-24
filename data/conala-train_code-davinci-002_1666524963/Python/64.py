from PIL import Image

im = Image.open("image.png")

if im.mode == "RGBA":
    im = im.convert("RGB")

im.save("image.jpg")