from Shape import Shape
class Triangle(Shape):
    def __init__(self, name, outline, outline_color, Background, Type, Location,base,height,length1,length2,length3):
        super().__init__(name, outline, outline_color, Background, Type, Location)
        self.__base=base
        self.__height=height
        self.__len1=length1
        self.__len2=length2
        self.__len3=length3
    @property
    def base(self):
        return self.__base
    @base.setter
    def base(self,b):
        self.__base=b
        return self.__base
    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self,h):
        self.__height=h
        return self.__height
    @property
    def len1(self):
        return self.__len1
    @len1.setter
    def len1(self,l):
        self.__len1=l
        return self.__len1
    @property
    def len2(self):
        return self.__len2
    @len2.setter
    def len2(self,l):
        self.__len2=l
        return self.__len2
    @property
    def len3(self):
        return self.__len3
    @len3.setter
    def len3(self,l):
        self.__len3=l
        return self.__len3
    def __str__(self):
        return super().__str__() + '\n Base: {} , Height : {} , S1: {} - S2: {} - S3: {}'.format(self.__base,self.__height,self.__len1,self.__len2,self.__len3)
    def area(self):
        return 0.5*self.__base*self.__height
    def perimeter(self):
        return self.__len1+self.__len2+self.__len3
    


    