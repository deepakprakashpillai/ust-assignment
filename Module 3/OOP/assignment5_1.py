class MagicNumber:
    def __init__(self, number):
        self.number = number

    def __call__(self):
        return self.number ** 2

num = MagicNumber(5)

print(num()) 
