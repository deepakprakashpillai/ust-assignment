class Animal:
    def __init__(self, species):
        self.species = species
    def display_species(self):
        return f"Species: {self.species}"

class Mammal(Animal):
    def __init__(self, species, warm_blooded=True):
        super().__init__(species) 
        self.warm_blooded = warm_blooded 

    def display_mammal_details(self):
        return f"{self.display_species()}, Warm-blooded: {self.warm_blooded}"

class Dog(Mammal):
    def __init__(self, species, breed, warm_blooded=True):
        super().__init__(species, warm_blooded) 
        self.breed = breed

    def display_dog_details(self):
        return f"{self.display_mammal_details()}, Breed: {self.breed}"

dog = Dog(species="Canine", breed="Pomeranian")

print(dog.display_dog_details())
