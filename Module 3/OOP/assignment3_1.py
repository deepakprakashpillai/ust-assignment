class Superhero:
    def __init__(self, name, real_name, powers=None):
        self.name = name 
        self.__real_name = real_name 
        self.__powers = powers if powers is not None else []  # Private attribute

    @property
    def identity(self):
        return self.__real_name

    def add_power(self, power):
        if power and isinstance(power, str):
            self.__powers.append(power)
            print(f"Power '{power}' added.")
        else:
            print("Invalid")

    @property
    def powers(self):
        return self.__powers

    def set_secret_identity(self, real_name):
        if real_name and isinstance(real_name, str):
            self.__real_name = real_name
            print("Secret identity updated successfully.")
        else:
            print("Invalid")

superhero = Superhero(name="Iron Man", real_name="Tony Stark", powers=["Genius", "Suit"])

print(f"Superhero Name: {superhero.name}")

try:
    print(superhero.__real_name)
except AttributeError:
    print("Cannot access private attribute")

print("Powers:", superhero.powers)
superhero.add_power("Flight")
print("Updated Powers:", superhero.powers)

superhero.set_secret_identity("Tony Stark")
print("Real Identity:", superhero.identity)
