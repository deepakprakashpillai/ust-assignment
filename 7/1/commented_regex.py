import re

manuscript_text = """
𐎟𐎚𐎗𐎂 𐎚𐎟𐎗𐎚 𐎟𐎚𐎗𐎂
𐎚𐎚𐎗𐎟 𐎚𐎟𐎗𐎚 𐎚𐎗𐎂𐎟
𐎗𐎂𐎟𐎚 𐎚𐎗𐎂𐎟 𐎚𐎗𐎂𐎟
"""

output_file = 'commented_regex_results.txt'

pattern = r'𐎚𐎗𐎂'

matches = re.findall(pattern, manuscript_text)

with open(output_file, 'w', encoding='utf-8') as file:
    file.write(f"Pattern '{pattern}' found:\n{matches}\n")

print(f"Regex pattern matching results have been written to {output_file}")
