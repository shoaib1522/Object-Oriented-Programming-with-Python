from Shape import Shape
import math
class Circle(Shape):
    def __init__(self, name, outline, outline_color, Background, Type, Location ,radius):
        super().__init__(name, outline, outline_color, Background, Type, Location)
        self.__radius=radius
    @property
    def radius(self):
        return self.__radius
    @radius.setter
    def radius(self,rad):
        self.__radius=rad
        return self.__radius
    def __str__(self):
        return super().__str__() + '\n Radius: {}'.format(self.__radius)
    def area(self):
        return math.pi*self.__radius*self.__radius
    def circumference(self):
        return 2*(math.pi)*self.__radius
    def diameter(self):
        return self.__radius*2
    
