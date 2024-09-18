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
    def __init__(self, grd, sal):
        self.grade = grd
        self.salary = sal
    def __str__(self): 
        # ERROR BELOW
        return self.name +", " + self.age + "\n" +self.grade +", " + str(self.salary)
        
        
def main():
    j = human('jameel', 25)
    print(j)
    e = employee('3', 25000)
    print(e)   # results in error
    
main()     