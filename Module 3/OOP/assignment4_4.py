from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, color):
        self.color = color 

    @abstractmethod
    def area(self):
        raise NotImplementedError("Subclasses must implement this method")

    @abstractmethod
    def get_color(self):

        raise NotImplementedError("Subclasses must implement this method")

class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)  
        self.width = width 
        self.height = height  

    def area(self):
        return self.width * self.height

    def get_color(self):
        return self.color

rectangle = Rectangle(color="Blue", width=5, height=10)

print(f"Color: {rectangle.get_color()}")
print(f"Area: {rectangle.area()}")
