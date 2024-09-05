observations = [
    {"species": "sparrow", "habitat": "forest"},
    {"species": "eagle", "habitat": "mountain"},
    {"species": "wolf", "habitat": "forest"},
    {"species": "wolf", "habitat": "mountain"},
]

filtered_observations = [
    {"species": o["species"], "habitat": o["habitat"].upper() if o["species"] != "sparrow" else "unknown"}
    for o in observations
]

unique_species = {o["species"] for o in filtered_observations}
species_habitats = {o["species"]: o["habitat"] for o in filtered_observations}

print(filtered_observations)
print(unique_species)
print(species_habitats)
