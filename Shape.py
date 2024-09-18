from Square import Square
from Triangle import Triangle
from Circle import Circle
from Rectangle import Rectangle
from Oval import Oval
from Canvas import Canvas
class Shape(Canvas):
    def __init__(self,name,outline,outline_color,Background,Type,Location):
        super().__init__(name, outline, Background)
        self.location=Location
        self.type=Type
        self.color=outline_color
    # @property
    # def location(self):
    #     return self.__location
    # @location.setter
    # def location(self,loc):
    #     self.__location=loc
    #     return self.__location
    # @property
    # def type(self):
    #     return self.__type
    # @type.setter
    # def type(self,ty):
    #     self.__type=ty
    #     return self.__type
    # @property
    # def color(self):
    #     return self.__color
    # @color.setter
    # def color(self,col):
    #     self.__color=col
    #     return self.__color
    def __str__(self):
        return "Type: {} Outline Color: {}".format(self.type,self.color) + super().__str__() + " Location: {}".format(self.location)
    
class Point(object):
    def __init__(self,Location):
        self.location=Location
    # @property
    # def Location(self):
    #     return self.__location
    # @Location.setter
    # def Location(self,loc):
    #     self.__location=loc
    #     return self.__location
class Outline(object):
    def __init__(self,outline):
        self.outline=outline    
# def main():
#     s=Shape('sh',True,'rED',"WHITE",'GD','JS')
#     print(s)
# main()
def main():
    # SHAPE 1:
    Sq_1_outline=Outline(True) 
    Sq_1_point=Point("Center")
    Sq_1=Square("Shape 1",Sq_1_outline,"Red","White",'Square',Sq_1_point,5)
    print(Sq_1)
main()