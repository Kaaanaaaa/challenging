#1
class Apple():
    def __init__(self, name, color, weight, price):
        self.name = name
        self.color = color
        self.weight = weight
        self.price = price

#2
import math
class Circle():
    def __init__(self, length):
        self.length = length
    def area(self):
        return self.length * math.pi
circle = Circle(20)
print(circle.area())

#3
class Triangle():
    def __init__(self, width, length):
        self.width = width
        self.length = length
    def area(self):
        return self.width * self.length / 2
triangle = Triangle(30, 40)
print(triangle.area())

#4
class Hexagon():
    def __init__(self, h1, h2, h3, h4, h5, h6):
        self.h1 = h1
        self.h2 = h2
        self.h3 = h3
        self.h4 = h4
        self.h5 = h5
        self.h6 = h6
    def calcurate_perimeter(self):
        return self.h1 + self.h2 + self.h3 + self.h4 + self.h5 + self.h6
hexagon = Hexagon(10, 10, 10, 20, 40, 40)
print(hexagon.calcurate_perimeter())