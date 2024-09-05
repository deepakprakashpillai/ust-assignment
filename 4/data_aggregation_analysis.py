import itertools

species_observations = ["sparrow", "eagle", "wolf"]
environmental_metrics = [10, 50, 30]

paired_data = list(enumerate(zip(species_observations, environmental_metrics)))

combinations = list(itertools.combinations(species_observations, 2))
permutations = list(itertools.permutations(species_observations, 2))
products = list(itertools.product(species_observations, environmental_metrics))

print("Paired Data:", paired_data)
print("Combinations:", combinations)
print("Permutations:", permutations)
print("Products:", products)
