from math import sqrt
import math
class Canvas(object):
    # __shapes={"Triangle","Rectangle","Circle","Square","Oval"}
    def __init__(self,name,outline,Background):
        self.name=name
        self.outline=outline
        self.background=Background
    def __str__(self):
        return " Name: {} , Outline: {} , Background: {}".format(self.name,self.outline,self.background)
class Shape(Canvas):
    def __init__(self,name,outline,outline_color,Background,Type,Location):
        super().__init__(name, outline, Background)
        self.location=Location
        self.type=Type
        self.color=outline_color
    def __str__(self):
        return "Type: {} Outline Color: {}".format(self.type,self.color) + super().__str__() + " Location: {}".format(self.location)
class Point(object):
    def __init__(self, Location):
        self.location = Location

    def __str__(self):
        return "Location: {}".format(self.location)

class Outline(object):
    def __init__(self, outline):
        self.outline = outline 

    def __str__(self):
        return "Outline: {}".format(self.outline)

class Square(Shape):
    def __init__(self, name, outline, outline_color, Background, Type, Location,length):
        super().__init__(name, outline, outline_color, Background, Type, Location)
        self.length=length
    def __str__(self):
        return super().__str__() + "\n Length: {}".format(self.length)
    def area(self):
        return self.length**2
    def perimeter(self):
        return self.length**4
    def length_of_diagonal_square(self):
        return self.length*sqrt(2)
class Circle(Shape):
    def __init__(self, name, outline, outline_color, Background, Type, Location ,radius):
        super().__init__(name, outline, outline_color, Background, Type, Location)
        self.radius=radius
    def __str__(self):
        return super().__str__() + '\n Radius: {}'.format(self.radius)
    def area(self):
        return math.pi*self.radius*self.radius
    def circumference(self):
        return 2*(math.pi)*self.radius
    def diameter(self):
        return self.radius*2
class Rectangle(Square):
    def __init__(self, name, outline, outline_color, Background, Type, Location, length,width):
        super().__init__(name, outline, outline_color, Background, Type, Location, length)
        self.width=width
    def __str__(self):
        return super().__str__() + "Width : {}".format(self.width)
    def area(self):
        return self.width*self.length
    def perimeter(self):
        return 2*(self.length+self.width)
    def length_of_diagonal_rectangle(self):
        return sqrt((self.length**2)+(self.width**2))
    
def main():
    # # SHAPE 1:
    Sq_1_outline=Outline(True) 
    Sq_1_point=Point("Center")
    Sq_1=Rectangle("Shape 1",Sq_1_outline,"Red","White",'Square',Sq_1_point,5,3)
    print(Sq_1)
    # Sq_1_outline=Outline(True) 
    # Sq_1_point=Point("Center")
    # Sq_1=Square("Shape 1",Sq_1_outline,"Red","White",'Square',Sq_1_point,5)
    # print(Sq_1)

main()