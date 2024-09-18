class Person:
    def __init__(self, ..., bd):
        print("... creating date object")
        self.BirthDate = Date(bd)   # one of the most important line of code for composition
        print("person initialized")
 
    def setBirthDate(self, bd):
        print("... creating date object")
        self.BirthDate = Date(bd)   # one of the most important line of code for composition
 
    def __del__(self):
        print("... deleting date object")
        del self.BirthDate  # one of the most important line of code for composition
        print("date deleted") 
        print("person deleted") 
 
def main():
    print("... creating person object")
    obj_per = Person(..., bd)    # date object in any form
    print("... deleting person object")
    del obj_per
    print("end of main program")