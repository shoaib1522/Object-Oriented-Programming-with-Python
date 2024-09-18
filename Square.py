from Shape import Shape
from math import sqrt
class Square(Shape):
    def __init__(self, name, outline, outline_color, Background, Type, Location,length):
        super().__init__(name, outline, outline_color, Background, Type, Location)
        self.__length=length
    @property
    def length(self):
        return self.__length
    @length.setter
    def length(self,length):
        self.__length=length
        return self.__length
    def __str__(self):
        return super().__str__() + "\n Length: {}".format(self.__length)
    def area(self):
        return self.__length**2
    def perimeter(self):
        return self.__length**4
    def length_of_diagonal_square(self):
        return self.__length*sqrt(2)
# def main():
#     s=Square('sh',True,'rED',"WHITE",'GD','JS',5)
#     print(s)
# main()