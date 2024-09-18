
from math import sqrt
import math

class Canvas(object):
    def __init__(self, name, outline, Background):
        self.name = name
        self.outline = outline
        self.background = Background

    def __str__(self):
        return "Name: {}, Outline: {}, Background: {}".format(self.name, self.outline, self.background)

class Shape(Canvas):
    def __init__(self, name, outline, outline_color, Background, Type, Location):
        super().__init__(name, outline, Background)
        self.location = Location
        self.type = Type
        self.color = outline_color

    def __str__(self):
        return super().__str__() + "\nType: {}, Outline Color: {}, Location: {}".format(self.type, self.color, self.location)

class Square(Shape):
    def __init__(self, name, outline, outline_color, Background, Type, Location, length):
        super().__init__(name, outline, outline_color, Background, Type, Location)
        self.length = length

    def __str__(self):
        return super().__str__() + "\nLength: {}".format(self.length)

    def area(self):
        return self.length**2

    def perimeter(self):
        return self.length * 4

    def length_of_diagonal_square(self):
        return self.length * sqrt(2)

class Point(object):
    def __init__(self, Location):
        self.location = Location

class Outline(object):
    def __init__(self, outline):
        self.outline = outline 

def main():
    # SHAPE 1:
    Sq_1_outline = Outline(True)
    Sq_1_point = Point("Center")
    Sq_1 = Square("Shape 1", Sq_1_outline, "Red", "White", 'Square', Sq_1_point, 5)
    print(Sq_1)

main()
