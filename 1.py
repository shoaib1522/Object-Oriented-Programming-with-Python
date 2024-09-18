class Person(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    # def agecalc(self):
    #     return self.age
class Heart:
    def __init__(self,name,age,heart):
        obj=Person(name,age)
        self.heart=heart
    def __str__(self):
        return f"Person have {self.heart} present with 4 artriums"

class Bag:
    def __init__(self,name,age,bag):
        self.name=name
        self.age=age
        self.bag=bag
    def __str__(self):
        return f'Person have this brand of bag: {self.bag}'


obj=Person('Shoaib',18)
heart_obj=Heart('Shoaib',18, True)
bag_obj=Bag(obj.name,obj.age,"gUCCI")
print(bag_obj)
                