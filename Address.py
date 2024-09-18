class Address(object):
    def __init__(self,house,street,place,city):
        self.__house=house
        self.__street=street
        self.__place=place
        self.__city=city
    @property
    def house(self):
        return self.__house
    @house.setter
    def house(self,h):
        self.__house=h
        return self.__house
    @property
    def street(self):
        return self.__street
    @street.setter
    def street(self,h):
        self.__street=h
        return self.__street
    @property
    def place(self):
        return self.__place
    @place.setter
    def place(self,h):
        self.__place=h
        return self.__place
    @property
    def city(self):
        return self.__city
    @city.setter
    def city(self,h):
        self.__city=h
        return self.__city
    def __str__(self):
        return f"Customer Address: House no. {self.__house} , Street no. {self.__street} , {self.__place} , {self.__city} "
    
