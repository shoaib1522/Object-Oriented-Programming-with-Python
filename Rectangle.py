from Square import Square
from math import sqrt
class Rectangle(Square):
    def __init__(self, name, outline, outline_color, Background, Type, Location, length,width):
        super().__init__(name, outline, outline_color, Background, Type, Location, length)
        self.__width=width
    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self,width):
        self.__width=width
        return self.__width
    def __str__(self):
        return super().__str__() + "Width : {}".format(self.__width)
    def area(self):
        return self.__width*self.__length
    def perimeter(self):
        return 2*(self.__length+self.__width)
    def length_of_diagonal_rectangle(self):
        return sqrt((self.__length**2)+(self.__width**2))
    
