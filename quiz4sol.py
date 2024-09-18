class Author:
    
    def __init__(self,name,email,gender):
        self.setName(name)
        self.setEmail(email)
        self.setGender(gender)
    
    def setName(self,name):
        self.__name=name
    def getName(self):
        return self.__name
    
    def setEmail(self,email):
        self.__email=email
    def getEmail(self):
        return self.__email
    
    def setGender(self,gender):
        if gender.upper() =="F" or gender.upper()=="M":
            self.__gender=gender.upper()
        else:
             raise Exception("Sorry, no available options entered")
    def getGender(self):
        return self.__gender
    
    def __str__(self):
        s="Name: {}\nEmail: {}\nGender: {}".format(self.__name,self.__email,self.__gender)
        return s


class Book:
    
    def __init__(self,name,author,price,qty=0):
        self.setName(name)
        self.setPrice(price)
        self.setQtyInStock(qty)
        self.setAuthor(author)
   
    def setName(self,name):
        self.__name=name
    def getName(self):
        return self.__name
    def setAuthor(self,author):
        self.__author=author 
    def getAuthor(self):
        return self.__author
    def getAuthorName(self):
        return self.__author.getName()
 
    def setPrice(self,price):
        self.__price=price
   
    def getPrice(self):
        return self.__price
    def setQtyInStock(self,qty=0):
        if qty>=0:
            self.__qtyInStock=qty  
    def getQtyInStock(self):
        return self.__qtyInStock
    
    def print(self):
         print(f"'{self.__name}' by {self.getAuthorName()} ({self.__author.getGender()}) {self.__author.getEmail()}")

def main():
    A1=Author("Julie Smith","mail@doctorjuliesmith.com","f")
    b1=Book("Why Has Nobody Told Me This Before",A1,2000.789,5)
    print(b1.getAuthorName())
    b1.print()
    print(b1.getAuthor())

main()
