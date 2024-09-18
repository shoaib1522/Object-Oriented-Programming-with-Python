class Department:
    #Data members
    __name=None
    __chairman=None
    __id=None
    def __new__(cls,name,chairman,id):
        obj=super().__new__(cls)
        return obj
    def __init__(self,name,chairman,id):
        self.__name=name
        self.__chairman=chairman
        self.__id=id
    def __str__(self):
        return 'Department: {} ,  {} ,  {} '.format(self.__id,self.__name,self.__chairman)
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,n):
        self.__name=n
        return
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self,n):
        self.__id=n
        return
    @property
    def chairman(self):
        return self.__chairman
    @chairman.setter
    def name(self,n):
        self.__chairman=n
        return
    
class Student:
   # Data members
    __name=None
    __rollnum=None
    __sem=None
    __cgpa=None
    __depid=None
    def __new__(cls,name,rollnum,sem,cgpa,depid):
        obj=super().__new__(cls)
        return obj
    def __init__(self,name,rollnum,sem,cgpa,depid):
        self.__name=name
        self.__rollnum=rollnum
        self.__cgpa=cgpa
        self.__sem=sem
        self.__depid=depid
    def __str__(self):
        return '{}     {} \t  {}\t\t{}'.format(self.__rollnum,self.__name,self.__sem,self.__cgpa)
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,n):
        self.__name=n
        return
    @property
    def rollnum(self):
        return self.__rollnum
    @rollnum.setter
    def name(self,n):
        self.__rollnum=n
        return
    @property
    def sem(self):
        return self.__sem
    @sem.setter
    def name(self,n):
        self.__sem=n
        return
    @property
    def cgpa(self):
        return self.__cgpa
    @cgpa.setter
    def name(self,n):
        self.__cgpa=n
        return
    @property
    def depid(self):
        return self.__depid
    @depid.setter
    def depid(self,n):
        self.__depid=n
        return
    
def main():
    
    #list of dep obj
    cs=[]
    it=[]
    se=[]
    ds=[]
    student_lessgrades=[]
    department1=Department('Computer Science','Dr.Khawaja Hasrat','CS')
    print(department1)
    cs.append(Student("Zalaid","BSCSF22A03",2,3.66,"cs"))
    cs.append(Student("Shoaib","BSCSF22A09",1,3.9,"cs"))
    cs.append(Student("Umer","BSCSF22A56",2,2.86,"cs"))
    cs.append(Student("Hazara","BSCSF22A15",2,3.2,"cs"))
    print(f'Roll No.       Name     Semester        CGPA')
    for item in cs:
        if item.cgpa<=1.70:
            student_lessgrades.append(item)
        print(item)
    department2=Department('Data Science','Dr.Iddress ','DS')
    print(department2)
    ds.append(Student("Uzma","BSDSF22A26",2,1.6,"ds"))
    ds.append(Student("Sheraz","BSDSF22B45",2,2.7,"ds"))
    ds.append(Student("Ummama","BSDSF22B25",1,2.86,"ds"))
    ds.append(Student("Hamza","BSDSF22G45",2,3.2,"ds"))
    print(f'Roll No.      Name     Semester        CGPA')
    for item in ds:
        if item.cgpa<=1.70:
            student_lessgrades.append(item)
        print(item)
    department3=Department('Software Engineering','Dr.Hamna Khalid','SE')
    print(department3)
    se.append(Student("Haris","BSSEF21S25",2,3.66,"se"))
    se.append(Student("Jumma","BSSEF21S45",1,1.5,"se"))
    se.append(Student("LubaBA","BSSEF21S15",2,1.2,"se"))
    se.append(Student("Rehaan","BSSEF21S75",2,3.2,"se"))
    print(f'Roll No.       Name     Semester        CGPA')
    for item in se:
        if item.cgpa<=1.70:
            student_lessgrades.append(item)
        print(item)
    department4=Department('Information Technology','Dr.Faizan Ashraf','IT')
    print(department4)
    it.append(Student("Hanzi","BSITF22I78",2,2.1,"it"))
    it.append(Student("Marwa","BSITF22I15",5,1.5,"it"))
    it.append(Student("Fatima","BSITF22I18",2,2.86,"it"))
    it.append(Student("Isha","BSITF22I62",7,3.5,"it"))
    print(f'Roll No.       Name     Semester        CGPA')
    for item in it:
        if item.cgpa<=1.70:
            student_lessgrades.append(item)
        print(item)
    print('The Students with Grades Less than or Equals to 1.70 are: ')
    print(f'Roll No.       Name     Semester        CGPA')
    for students in student_lessgrades:
        print(students)
    
main()