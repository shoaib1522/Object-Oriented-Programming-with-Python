class Employee:
    def __init__(self,Employee_number,name,cnic,phone,address):
        self.EmpNum=Employee_number
        self.name=name
        self.cnic=cnic
        self.phone=phone
        self.address=address
    def __str__(self):
        return "Employee Number: {} Name: {} CNIC Number: {} Phone Number: {} Address: {}".format(self.EmpNum,self.name,self.cnic,self.phone,self.address)
class Salaried(Employee):
    def __init__(self,Employee_number,name,cnic,phone,address,Weekly_Salary,Department):
        super().__init__(Employee_number,name,cnic,phone,address)
        self.Weeksalary=Weekly_Salary
        self.department=Department
    def CalculateSalary(self,Number_Of_Weeks):
        Salary=self.Weeksalary*Number_Of_Weeks
        return Salary
    def __str__(self):
        return super().__str__() + "\n Weekly Salary: {} ".format(self.Weeksalary) + "{}".format(self.department)
class Hourly(Employee):
    def __init__(self,Employee_number,name,cnic,phone,address,Hourly_Salary,Department):
        super().__init__(Employee_number,name,cnic,phone,address)
        self.HourlySalary=Hourly_Salary
        self.department=Department
    def CalculateSalary(self,Number_Of_Hours):
        Salary=self.HourlySalary*Number_Of_Hours
        return Salary
    def __str__(self):
        return super().__str__() + "\n Hourly Salary: {}" .format(self.HourlySalary) + " {}".format(self.department)
class Comission(Employee):
    def __init__(self,Employee_number,name,cnic,phone,address,Percentage,Department):
        super().__init__(Employee_number,name,cnic,phone,address)
        self.percentage=Percentage
        self.department=Department
    def CalculatedComission(self,Number_Of_Sales):
        Salary=self.percentage*Number_Of_Sales
        return Salary
    def __str__(self):
        return super().__str__() + "\n Percentage Of Comission: {}" .format(self.percentage) + " {}".format(self.department)

# Class Of Payroll
class Payroll:
    def __init__(self,object1,object2,object3,object4):
        self.list=[]
        self.list.append(object1)
        self.list.append(object2)
        self.list.append(object3)
        self.list.append(object4)
    def list(self):
        return(self.list)  
    
    
class department:
    def __init__(self,name,location):
        self.name=name
        self.location=location
    def __str__(self):
        return 'Department Name: {} , Department Location: {}'.format(self.name,self.location)
        
def main():
    dep1=department('Accounting',"Lahore")
    dep2=department('Sales',"Kasur")
    dep3=department('Seller',"Faislabad")
    dep4=department('Accounting',"Lahore")
    Employee1=(Salaried(1,"Zalaid",35202456841,4454,'House # 5, Street 17 , Shadman',5000,dep1))
    Employee2=(Hourly(2,"Sohaib",35202456841,4454,'House # 5, Street 18 , Shadman',200,dep2))
    Employee3=(Comission(3,"Amnaa",35202456841,4454,'House # 5, Street 216, lahore',0.3,dep3))
    Employee4=(Salaried(4,"Umer",35202456841,4454,'House # 5, Street 78 , GUNJRAWALA',25000,dep4))
    emp=Payroll(Employee1,Employee2,Employee3,Employee4)
    list=Payroll.list(emp)
    for employees in list:
        print(employees)
    
main()
    
        
       
    
    
    
        
        