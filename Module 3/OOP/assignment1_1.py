class Animal:
    def __init__(self,name,species,age,is_adopted=False) -> None:
        self.name = name
        self.species = species
        self.age = age
        self.is_adopted = is_adopted

    def print_info(self):
        return f"Name : {self.name} Species : {self.species} Age : {self.age} Is Adopted : {self.is_adopted}"

class Dog(Animal):
    def __init__(self, name, species, age, breed,is_adopted=False) -> None:
        super().__init__(name, species, age, is_adopted)
        self.breed = breed

    def print_info(self):
        return super().print_info() + f" Breed : {self.breed}"

class Cat(Animal):
    def __init__(self, name, species, age,color, is_adopted=False) -> None:
        super().__init__(name, species, age, is_adopted)
        self.color = color

    def print_info(self):
        return super().print_info() + f" Color : {self.color}"

arjun = Dog("Arjun","Mammals",4,"Pomeranian",True)

kitty = Cat("Kitty","Mammal",5,"White",False)

print(arjun.print_info())
print(kitty.print_info())