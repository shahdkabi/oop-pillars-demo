# Abstraction: Providing a simple interface while hiding implementation details.
from abc import ABC, abstractmethod

class Shape(ABC):  # Abstract base class
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.1416 * self.radius ** 2

# Usage (users don't need to know how area is calculated internally)
rect = Rectangle(5, 3)
print("Rectangle area:", rect.area())
circ = Circle(4)
print("Circle area:", circ.area())
