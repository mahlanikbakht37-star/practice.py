from abc import ABC, abstractmethod
import math

class Shape(ABC):

    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass

class Rectangle(Shape):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2

    def calculate_perimeter(self):
        return 2 * math.pi * self.radius


# کد اصلی
shapes = []

rect = Rectangle(2, 3)
circle = Circle(2)

shapes.append(rect)
shapes.append(circle)

for shape in shapes:
    print("Area:", shape.calculate_area())
    print("Perimeter:", shape.calculate_perimeter())
    print("-------------------")
