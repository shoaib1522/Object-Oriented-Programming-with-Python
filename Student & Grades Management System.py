import struct
class Student:
    structure = "11s30s2sif11s"
    def __init__(self, roll_no, name, dep_code, semester, gpa, phone_number):
        self.roll_no = roll_no
        self.name = name
        self.dep_code = dep_code
        self.semester = semester
        self.gpa = gpa
        self.phone_number = phone_number
    def __str__(self):
        return f'Roll Number: {self.roll_no}\nName: {self.name}\nSemester: {self.semester}\nGPA: {self.gpa}\nPhone: {self.phone_number}'
    @staticmethod
    def pack(obj):
        return struct.pack(Student.structure, obj.roll_no.encode(), obj.name.encode(),
                           obj.dep_code.encode(), obj.semester, obj.gpa,
                           obj.phone_number.encode())
    @staticmethod
    def unpack(data):
        unpack = struct.unpack(Student.structure, data)
        roll_no, name, department_code, semester, gpa, phone_number = \
            unpack[0].decode(), unpack[1].decode(), unpack[2].decode(), unpack[3], unpack[4], unpack[5].decode()
        return roll_no, name, department_code, semester, gpa, phone_number
    @staticmethod
    def add(student):
        with open("students.dat", 'ab+') as file:
            pack_data = student.pack(student)
            file.write(pack_data)
    @staticmethod
    def search(roll_no):
        size = struct.calcsize(Student.structure)
        with open('students.dat', 'rb') as file:
            while True:
                binary_data = file.read(size)
                if not binary_data:
                    print("Student does not exist")
                    break
                roll_no_file, _, _, _, _, _ = Student.unpack(binary_data)
                if roll_no_file == roll_no:
                    print(Student.unpack(binary_data))
                    break
    @staticmethod
    def edit(roll):
        size = struct.calcsize(Student.structure)
        with open('students.dat', 'rb+') as file:
            checking_line = 0
            while True:
                binary_data = file.read(size)
                if not binary_data:
                    print("Student does not exist")
                    break
                roll_no, _, _, _, _, _ = Student.unpack(binary_data)
                if roll_no == roll:
                    roll_no = input("Enter roll number: ")
                    namee = input("Enter Name: ")
                    department_code = input("Enter Department Code: ")
                    semester = int(input("Enter Semester: "))
                    last_semester_percent = float(input("Enter Last Semester Percentage: "))
                    phone_number = input("Enter Phone Number: ")
                    my_object = Student(roll_no, namee, department_code, semester, last_semester_percent,
                                        phone_number)
                    pack_obj = Student.pack(my_object)
                    file.seek(checking_line * size)
                    file.write(pack_obj)
                    print("The File is Updated")
                    break
                checking_line += 1
    @staticmethod
    def delete(roll_no):
        size = struct.calcsize(Student.structure)
        with open('students.dat', 'rb') as file:
            with open('students_temp.dat', 'ab+') as temp_file:
                while True:
                    binary_data = file.read(size)
                    if not binary_data:
                        print("Student does not exist")
                        break
                    roll_no_file, _, _, _, _, _ = Student.unpack(binary_data)
                    if roll_no_file != roll_no:
                        temp_file.write(binary_data)
                    else:
                        print(f"Student with roll number {roll_no} deleted.")
        with open('students_temp.dat', 'rb') as temp_file:
            with open('students.dat', 'wb') as new_file:
                new_file.write(temp_file.read())
    @staticmethod
    def list_by_semester(semester):
        size = struct.calcsize(Student.structure)
        with open('students.dat', 'rb') as file:
            while True:
                binary_data = file.read(size)
                if not binary_data:
                    break
                _, _, _, student_semester, _, _ = Student.unpack(binary_data)
                if student_semester == semester:
                    print(Student.unpack(binary_data))
    @staticmethod
    def list_by_name(name):
        size = struct.calcsize(Student.structure)
        with open('students.dat', 'rb') as file:
            while True:
                binary_data = file.read(size)
                if not binary_data:
                    break
                roll_no, student_name, _, _, _, _ = Student.unpack(binary_data)
                if student_name.strip('\x00') == name:
                    print(f"Roll Number: {roll_no}\nName: {student_name}")
    @staticmethod
    def print_list():
        size = struct.calcsize(Student.structure)
        with open('students.dat', 'rb') as file:
            while True:
                binary_data = file.read(size)
                if not binary_data:
                    break
                print(Student.unpack(binary_data))
class Grade:
    structure = "20s11sf"
    def __init__(self, course, roll_no, percent_marks):
        self.course = course
        self.roll_no = roll_no
        self.percent_marks = percent_marks
    @staticmethod
    def pack(obj):
        return struct.pack(Grade.structure, obj.course.encode(), obj.roll_no.encode(),
                           obj.percent_marks)
    @staticmethod
    def unpack(data):
        unpack = struct.unpack(Grade.structure, data)
        course, roll_no, percent_marks = unpack[0].decode(), unpack[1].decode(), unpack[2]
        return course, roll_no, percent_marks
    @staticmethod
    def add(grade):
        with open("grades.dat", 'ab+') as file:
            pack_data = grade.pack(grade)
            file.write(pack_data)
    @staticmethod
    def import_grades_from_file(file_name):
        with open(file_name, 'r') as file:
            for line in file:
                data = line.strip().split('\t')
                course, roll_no, percent_marks = data[0], data[1], float(data[2])
                grade = Grade(course, roll_no, percent_marks)
                Grade.add(grade)
    @staticmethod
    def view_student_grades(roll_no):
        size = struct.calcsize(Grade.structure)
        with open('grades.dat', 'rb') as file:
            while True:
                binary_data = file.read(size)
                if not binary_data:
                    break
                _, student_roll_no, percent_marks = Grade.unpack(binary_data)
                if student_roll_no == roll_no:
                    print(f"Course: {_}, Percentage: {percent_marks}")
    @staticmethod
    def edit_student_grades(roll_no, course):
        size = struct.calcsize(Grade.structure)
        with open('grades.dat', 'rb+') as file:
            checking_line = 0
            while True:
                binary_data = file.read(size)
                if not binary_data:
                    break
                _, student_roll_no, _ = Grade.unpack(binary_data)
                if student_roll_no == roll_no:
                    percent_marks = float(input("Enter new percentage: "))
                    my_object = Grade(course, roll_no, percent_marks)
                    pack_obj = Grade.pack(my_object)
                    file.seek(checking_line * size)
                    file.write(pack_obj)
                    print("Grades updated successfully")
                    break
                checking_line += 1
    @staticmethod
    def delete_student_grades(roll_no, course):
        size = struct.calcsize(Grade.structure)
        with open('grades.dat', 'rb') as file:
            with open('grades_temp.dat', 'ab+') as temp_file:
                while True:
                    binary_data = file.read(size)
                    if not binary_data:
                        break
                    _, student_roll_no, _ = Grade.unpack(binary_data)
                    if student_roll_no != roll_no:
                        temp_file.write(binary_data)
                    else:
                        print(f"Grades for course {course} deleted.")
        with open('grades_temp.dat', 'rb') as temp_file:
            with open('grades.dat', 'wb') as new_file:
                new_file.write(temp_file.read())
    @staticmethod
    def list_student_grades(roll_no):
        size = struct.calcsize(Grade.structure)
        with open('grades.dat', 'rb') as file:
            while True:
                binary_data = file.read(size)
                if not binary_data:
                    break
                _, student_roll_no, percent_marks = Grade.unpack(binary_data)
                if student_roll_no == roll_no:
                    print(f"Course: {_}, Percentage: {percent_marks}")
    @staticmethod
    def list_course_grades(course):
        size = struct.calcsize(Grade.structure)
        with open('grades.dat', 'rb') as file:
            while True:
                binary_data = file.read(size)
                if not binary_data:
                    break
                course_name, _, percent_marks = Grade.unpack(binary_data)
                if course_name.strip('\x00') == course:
                    print(f"Roll Number: {_}, Percentage: {percent_marks}")
    @staticmethod
    def award_sheet(course):
        size = struct.calcsize(Grade.structure)
        with open('grades.dat', 'rb') as file:
            while True:
                binary_data = file.read(size)
                if not binary_data:
                    break
                course_name, roll_no, percent_marks = Grade.unpack(binary_data)
                if course_name.strip('\x00') == course:
                    student = Student.search(roll_no)
                    print(f"Course: {course_name}, Roll Number: {roll_no}, "
                          f"Percentage: {percent_marks}, {student}")
    @staticmethod
    def summary_sheet(course):
        size = struct.calcsize(Grade.structure)
        with open('grades.dat', 'rb') as file:
            while True:
                binary_data = file.read(size)
                if not binary_data:
                    break
                course_name, roll_no, percent_marks = Grade.unpack(binary_data)
                if course_name.strip('\x00') == course:
                    student = Student.search(roll_no)
                    print(f"Course: {course_name}, Roll Number: {roll_no}, "
                          f"Percentage: {percent_marks}, {student}")
    @staticmethod
    def transcripts(start_roll, end_roll):
        size = struct.calcsize(Grade.structure)
        with open('grades.dat', 'rb') as file:
            while True:
                binary_data = file.read(size)
                if not binary_data:
                    break
                _, roll_no, percent_marks = Grade.unpack(binary_data)
                if start_roll <= roll_no <= end_roll:
                    student = Student.search(roll_no)
                    print(f"Roll Number: {roll_no}, Percentage: {percent_marks}, {student}")
while True:
    print("\nMenu:")
    print("1. Quit the management system")
    print("2. Add a student (check for NO duplicates)")
    print("3. View student by roll no")
    print("4. Edit student by roll no (check for NO duplicates)")
    print("5. Delete student by roll no")
    print("6. List student by semester")
    print("7. List students by name")
    print("8. Print students list")
    print("9. Add grade of a student for a course (check for NO duplicates)")
    print("10. Import grades for a course for many students from a TABed text file (NO DUPS)")
    print("11. View grades of a student")
    print("12. Edit grades of a student for a course (NO DUPS, SKIP IF TIME IS SHORT)")
    print("13. Delete grades of a student for a course (SKIP IF TIME IS SHORT)")
    print("14. List Student wise (1 student) grade of courses")
    print("15. List Course wise grade (1 course) of students")
    print("16. Award sheet (courses one by one, with students enrolled in it)")
    print("17. Summary sheet (courses info, one by one, with one line for each student in it)")
    print("18. Transcripts for a range of students")

    choice = int(input("\nEnter your choice (1-18): "))
    if choice == 1:
        print("Quitting the management system. Goodbye!")
        break
    elif choice == 2:
        roll = input("Enter roll number: ")
        name = input("Enter Name: ")
        department_code = input("Enter Department Code: ")
        semester = int(input("Enter Semester: "))
        last_semester_percent = float(input("Enter Last Semester Percentage: "))
        phone_number = input("Enter Phone Number: ")
        a = Student(roll, name, department_code, semester, last_semester_percent, phone_number)
        a.add(a)
    elif choice == 3:
        num = input("Enter roll number: ")
        Student.search(num)
    elif choice == 4:
        num = input("Enter roll number: ")
        Student.edit(num)
    elif choice == 5:
        num = input("Enter roll number to delete: ")
        Student.delete(num)
    elif choice == 6:
        sem = int(input("Enter semester: "))
        Student.list_by_semester(sem)
    elif choice == 7:
        student_name = input("Enter student name: ")
        Student.list_by_name(student_name)
    elif choice == 8:
        print("Printing all students:")
        Student.print_list()
    elif choice == 9:
        course = input("Enter course name: ")
        roll_no = input("Enter roll number: ")
        percent_marks = float(input("Enter percentage marks: "))
        grade = Grade(course, roll_no, percent_marks)
        grade.add(grade)
    elif choice == 10:
        file_name = input("Enter file name with TAB separated data: ")
        Grade.import_grades_from_file(file_name)
    elif choice == 11:
        num = input("Enter roll number: ")
        Grade.view_student_grades(num)
    elif choice == 12:
        roll_no = input("Enter roll number: ")
        course = input("Enter course name: ")
        Grade.edit_student_grades(roll_no, course)
    elif choice == 13:
        roll_no = input("Enter roll number: ")
        course = input("Enter course name: ")
        Grade.delete_student_grades(roll_no, course)
    elif choice == 14:
        roll_no = input("Enter roll number: ")
        Grade.list_student_grades(roll_no)
    elif choice == 15:
        course = input("Enter course name: ")
        Grade.list_course_grades(course)
    elif choice == 16:
        course = input("Enter course name: ")
        Grade.award_sheet(course)
    elif choice == 17:
        course = input("Enter course name: ")
        Grade.summary_sheet(course)
    elif choice == 18:
        start_roll = input("Enter start roll number: ")
        end_roll = input("Enter end roll number: ")
        Grade.transcripts(start_roll, end_roll)