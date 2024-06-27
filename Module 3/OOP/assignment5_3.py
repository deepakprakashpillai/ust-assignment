from PIL import Image

image = Image.open("image.png")
print(f"Image width: {image.width}")
print(f"Image height: {image.height}")
print(f"Image format: {image.format}")
