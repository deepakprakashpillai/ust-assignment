import re

manuscript_text = """
𐎟𐎚𐎗𐎂 𐎚𐎟𐎗𐎚 𐎟𐎚𐎗𐎂
𐎚𐎚𐎗𐎟 𐎚𐎟𐎗𐎚 𐎚𐎗𐎂𐎟
𐎗𐎂𐎟𐎚 𐎚𐎗𐎂𐎟 𐎚𐎗𐎂𐎟
"""

output_file = 'unicode_handling_results.txt'

unicode_pattern = r'[^\x00-\x7F]+' 

matches = re.findall(unicode_pattern, manuscript_text)

with open(output_file, 'w', encoding='utf-8') as file:
    if matches:
        file.write(f"Unicode characters found:\n{matches}\n")
    else:
        file.write("No Unicode characters found.\n")

print(f"Unicode handling results have been written to {output_file}")
