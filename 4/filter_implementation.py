import itertools
species_observations = [
    {"species": "sparrow", "habitat": "forest"},
    {"species": "eagle", "habitat": "mountain"},
    {"species": "wolf", "habitat": "forest"}
]

forest_observations = filter(lambda x: x["habitat"] == "forest", species_observations)
mountain_observations = itertools.filterfalse(lambda x: x["habitat"] == "forest", species_observations)

mask = [True, False, True, False]
filtered_by_mask = itertools.compress(species_observations, mask)

print("Forest Observations:", list(forest_observations))
print("Mountain Observations:", list(mountain_observations))
print("Filtered by Mask:", list(filtered_by_mask))
