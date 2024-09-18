class CompanyFooter(object):
    def __init__(self,Signature,Basement,place,city):
        self.__Signature=Signature
        self.__Basement=Basement
        self.__place=place
        self.__city=city
    @property
    def Signature(self):
        return self.__Signature
    @Signature.setter
    def Signature(self,s):
        self.__Signature=s
        return self.__Signature
    @property
    def Basement(self):
        return self.__Basement
    @Basement.setter
    def Basement(self,s):
        self.__Basement=s
        return self.__Basement
    @property
    def place(self):
        return self.__place
    @place.setter
    def place(self,s):
        self.__place=s
        return self.__place
    @property
    def city(self):
        return self.__city
    @city.setter
    def city(self,h):
        self.__city=h
        return self.__city
    def __str__(self):
        return f'Signature: {self.Signature} \n    Basement # {self.__Basement},{self.__place},{self.__city}'
    
    
        
