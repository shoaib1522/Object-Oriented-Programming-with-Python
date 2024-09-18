class human(object):
    def __init__(self, nam, ag):
        self.name = nam
        self.age = ag
    def __str__(self):
        return self.name + ", " + str(self.age)
        
class student(human):
    def __init__(self, rno, dep):
        self.rollno = rno
        self.dept = dep
    def __str__(self):
        return self.rollno + ", " + self.dept

class employee(human):
    def __init__(self, nam, ag, grd, sal):
        super().__init__(nam, ag)
        self.grade = grd
        self.salary = sal
    def __str__(self):
        # base class data member are directly available here through self
        return self.name +", " + str(self.age) + "\n" +self.grade +", " + str(self.salary)
        
        
def main():
    j = human('jameel', 25)
    print(j)
    e = employee('rasheed', 23, '3', 25000)
    print(e)
    
main()     