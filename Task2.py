class Person:
    def __init__(self, name, contact_numbers):
        self.name = name
        self.contact_numbers = contact_numbers
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Contact Numbers:{self.contact_numbers}")
class Student(Person):
    def __init__(self, name, contact_numbers, department, semester):
        Person.__init__(self,name, contact_numbers)
        self.department = department
        self.semester = semester
    def display_info(self):
        Person.display_info(self)
        print(f"Department: {self.department}")
        print(f"Semester: {self.semester}")
class Teacher(Person):
    def __init__(self, name, contact_numbers, course, office_number):
        Person.__init__(self,name, contact_numbers)
        self.course = course
        self.office_number = office_number
    def display_info(self):
        Person.display_info(self)
        print(f"Course: {self.course}")
        print(f"Office Number: {self.office_number}")
class TA(Student, Teacher):
    def __init__(self, name, contact_numbers, department, semester, course, office_number):
        Student.__init__(self, name, contact_numbers, department, semester)
        Teacher.__init__(self, name, contact_numbers, course, office_number)
    def display_info(self):
        print("Information for Teaching Assistant:")
        print("As a Student:")
        Student.display_info(self)
        print("\nAs a Teacher:")
        Teacher.display_info(self)
ta = TA("Shoaib Ahmad", "123-456-7890", "Data Science", 2, "Object Oriented Programming", 254)
ta.display_info()
# print(TA.mro())