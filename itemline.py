class Itemline(object):
    def __init__(self,item_name,item_price):
        self.__item=item_name
        self.__itemprice=item_price
    @property
    def item(self):
        return self.__item
    @item.setter
    def item(self,it):
        self.__item=it
        return self.__item
    @property
    def itemprice(self):
        return self.__itemprice
    @itemprice.setter
    def itemprice(self,it):
        self.__itemprice=it
        return self.__itemprice
    def calculating_price(self,qty):
        Calculated=self.__itemprice*qty
        return f"{self.__item}           {self.itemprice}      {qty}      {Calculated}"
    def total(self,other=[]):
        total_price=self.__itemprice
        for i in range(len(other)):
            total_price+=other[i].__itemprice
        return total_price
    
    










        







