import itertools

species_observations = [
    {"species": "sparrow", "habitat": "forest"},
    {"species": "eagle", "habitat": "mountain"},
    {"species": "wolf", "habitat": "forest"},
]

species_observations.sort(key=lambda x: x["habitat"])
grouped_by_habitat = itertools.groupby(species_observations, key=lambda x: x["habitat"])

environmental_metrics = [10, 20, 30, 40]
cumulative_metrics = list(itertools.accumulate(environmental_metrics))

for habitat, group in grouped_by_habitat:
    print(habitat, list(group))

print("Cumulative Metrics:", cumulative_metrics)
