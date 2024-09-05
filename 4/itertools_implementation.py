import itertools

data_cycle = itertools.cycle(["temperature", "humidity", "pressure"])

validation_task = itertools.repeat("validate", 5)

for _ in range(6):
    print(next(data_cycle))

for task in validation_task:
    print(task)
