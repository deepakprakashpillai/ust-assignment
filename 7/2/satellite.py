class Spacecraft:
    def __init__(self, name, fuel):
        self.name = name
        self.fuel = fuel

    def __str__(self):
        return f"Spacecraft: {self.name}, Fuel: {self.fuel}"

class Satellite:
    def __init__(self, name, data_collected):
        self.name = name
        self.data_collected = data_collected

    def __str__(self):
        return f"Satellite: {self.name}, Data Collected: {self.data_collected}"

    def __add__(self, other):
        return Satellite(self.name, self.data_collected + other.data_collected)

if __name__ == "__main__":
    sat1 = Satellite("Sat-1", 100)
    sat2 = Satellite("Sat-2", 150)
    combined_sat = sat1 + sat2
    print(combined_sat)
