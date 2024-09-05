import re

manuscript_text = """
𐎟𐎚𐎗𐎂 𐎚𐎟𐎗𐎚 𐎟𐎚𐎗𐎂
𐎚𐎚𐎗𐎟 𐎚𐎟𐎗𐎚 𐎚𐎗𐎂𐎟
𐎗𐎂𐎟𐎚 𐎚𐎗𐎂𐎟 𐎚𐎗𐎂𐎟
"""

segments = re.split(r'𐎟', manuscript_text)

decoded_text = re.sub(r'𐎚', 'A', manuscript_text)
decoded_text = re.sub(r'𐎗', 'B', decoded_text)
decoded_text = re.sub(r'𐎂', 'C', decoded_text)
with open("decoded.txt", "w", encoding="utf-8") as file:
    file.write(f"decoded text : {decoded_text}\n")
