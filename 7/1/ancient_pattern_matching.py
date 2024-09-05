
manuscript_text = """
𐎟𐎚𐎗𐎂 𐎚𐎟𐎗𐎚 𐎟𐎚𐎗𐎂
𐎚𐎚𐎗𐎟 𐎚𐎟𐎗𐎚 𐎚𐎗𐎂𐎟
𐎗𐎂𐎟𐎚 𐎚𐎗𐎂𐎟 𐎚𐎗𐎂𐎟
"""

def naive_pattern_search(text, pattern):
    matches = []
    pattern_length = len(pattern)
    for i in range(len(text) - pattern_length + 1):
        if text[i:i + pattern_length] == pattern:
            matches.append(i)
    return matches

pattern = "𐎚𐎗𐎂"
matches = naive_pattern_search(manuscript_text, pattern)

with open("pattern_matches.txt", "w", encoding="utf-8") as file:
    file.write(f"Pattern '{pattern}' found at positions: {matches}\n")

print("Pattern matching results have been written to pattern_matches.txt")
