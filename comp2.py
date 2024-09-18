class Salary:
    def __init__(self, pay):
        self.pay = pay
        print("salay initialized")
 
    def get_total(self):
        return (self.pay*12)
 
    def __del__(self):
        print("salay deleted") 
 
class Employee:
    def __init__(self, pay, bonus):
        self.pay = Salary(pay)
        self.bonus = bonus
        print("employee initialized")
 
    def annual_salary(self):
        return "Total: " + str(self.pay.get_total() + self.bonus)
 
    def __del__(self):
        print("employee deleted") 
 


print("... creating employee object")
obj_emp = Employee(600, 500)
print(obj_emp.annual_salary())
print("... deleting employee object")
del obj_emp
print("end of main program")