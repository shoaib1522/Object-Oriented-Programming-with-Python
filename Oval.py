from Circle import Circle
import math
class Oval(Circle):
    def __init__(self, name, outline, outline_color, Background, Type, Location, radius, radius2):
        super().__init__(name, outline, outline_color, Background, Type, Location, radius)
        self.__radius2=radius2
    @property
    def radius2(self):
        return self.__radius
    @radius2.setter
    def radius(self,rad):
        self.__radius2=rad
        return self.__radius
    def __str__(self):
        return super().__str__() + " Another Radius : {} ".format(self.__radius2)
    def area(self):
        return math.pi * self.__radius * self.__radius2
    def perimeter(self):
        return math.sqrt(((self.__radius**2)+(self.__radius2**2))/2)
    