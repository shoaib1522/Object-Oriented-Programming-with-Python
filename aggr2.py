class Student:
    def __init__(self, ..., dept):
        self.departmentJoined = dept
        print("student initialized")
 
    def setDepartment(self, dept):
        self.departmentJoined = dept
 
    def __del__(self):
        print("student deleted") 

def main() 
    print("... creating department object")
    obj_dept = Department(...)
    print("... creating student object")
    obj_stud = Student(..., obj_dept)
    print("... deleting student object")
    del obj_stud
    print("... deleting department object")
    del obj_dept
    print("end of main program")
