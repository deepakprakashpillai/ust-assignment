class Shape:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color

class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

class Square(Shape):
    def __init__(self, color, side):
        super().__init__(color) 
        self.side = side

    def area(self):
        return self.side * self.side

circle = Circle(color="Red", radius=5)
square = Square(color="Blue", side=4)

print(f"Circle Color: {circle.get_color()}")
print(f"Circle Area: {circle.area()}")

print(f"Square Color: {square.get_color()}")
print(f"Square Area: {square.area()}")
