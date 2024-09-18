import struct

# Define the format strings for struct_pack and struct_unpack
student_format = '11s30s2si11sf'
grade_format = '20s11sf'

def add_student(data_file, roll_number, name, department_code, semester, last_semester_marks, phone_number):
    with open(data_file, 'ab') as file:
        # Check for duplicate roll number
        if not is_duplicate(file, roll_number, 0):
            record = struct.pack(student_format, roll_number.encode(), name.encode(), department_code.encode(),
                                 semester, last_semester_marks, phone_number.encode())
            file.write(record)
            print(f"Student with roll number {roll_number} added successfully.")
        else:
            print(f"Student with roll number {roll_number} already exists.")

def view_student(data_file, roll_number):
    with open(data_file, 'rb') as file:
        while True:
            record = file.read(struct.calcsize(student_format))
            if not record:
                print(f"Student with roll number {roll_number} not found.")
                break
            values = struct.unpack(student_format, record)
            if values[0].decode().strip('\x00') == roll_number:
                print(f"Roll Number: {values[0].decode()}, Name: {values[1].decode()}, Department: {values[2].decode()}, Semester: {values[3]}, Marks: {values[4]}, Phone: {values[5].decode()}")
                break

def edit_student(data_file, roll_number, new_name, new_department_code, new_semester, new_last_semester_marks, new_phone_number):
    with open(data_file, 'r+b') as file:
        while True:
            record = file.read(struct.calcsize(student_format))
            if not record:
                print(f"Student with roll number {roll_number} not found.")
                break
            current_position = file.tell() - struct.calcsize(student_format)
            values = list(struct.unpack(student_format, record))
            if values[0].decode().strip('\x00') == roll_number:
                # Check for duplicate roll number
                if not is_duplicate(file, roll_number, 0):
                    values[1] = new_name.encode()
                    values[2] = new_department_code.encode()
                    values[3] = new_semester
                    values[4] = new_last_semester_marks
                    values[5] = new_phone_number.encode()
                    file.seek(current_position)
                    file.write(struct.pack(student_format, *values))
                    print(f"Student with roll number {roll_number} edited successfully.")
                else:
                    print(f"Cannot edit. Student with roll number {roll_number} already exists.")
                break

def delete_student(data_file, roll_number):
    with open(data_file, 'r+b') as file:
        while True:
            record = file.read(struct.calcsize(student_format))
            if not record:
                print(f"Student with roll number {roll_number} not found.")
                break
            current_position = file.tell() - struct.calcsize(student_format)
            values = struct.unpack(student_format, record)
            if values[0].decode().strip('\x00') == roll_number:
                file.seek(current_position)
                file.truncate()
                print(f"Student with roll number {roll_number} deleted successfully.")
                break

def list_students_by_semester(data_file, semester):
    with open(data_file, 'rb') as file:
        while True:
            record = file.read(struct.calcsize(student_format))
            if not record:
                break
            values = struct.unpack(student_format, record)
            if values[3] == semester:
                print(f"Roll Number: {values[0].decode()}, Name: {values[1].decode()}, Department: {values[2].decode()}, Semester: {values[3]}, Marks: {values[4]}, Phone: {values[5].decode()}")

def list_students_by_name(data_file, name):
    with open(data_file, 'rb') as file:
        while True:
            record = file.read(struct.calcsize(student_format))
            if not record:
                break
            values = struct.unpack(student_format, record)
            if values[1].decode().strip('\x00') == name:
                print(f"Roll Number: {values[0].decode()}, Name: {values[1].decode()}, Department: {values[2].decode()}, Semester: {values[3]}, Marks: {values[4]}, Phone: {values[5].decode()}")

def print_students_list(data_file):
    with open(data_file, 'rb') as file:
        while True:
            record = file.read(struct.calcsize(student_format))
            if not record:
                break
            values = struct.unpack(student_format, record)
            print(f"Roll Number: {values[0].decode()}, Name: {values[1].decode()}, Department: {values[2].decode()}, Semester: {values[3]}, Marks: {values[4]}, Phone: {values[5].decode()}")

def add_grade(data_file, course, roll_number, percent_marks):
    with open(data_file, 'ab') as file:
        # Check for duplicate entry
        if not is_duplicate(file, (course, roll_number), (0, 1)):
            record = struct.pack(grade_format, course.encode(), roll_number.encode(), percent_marks)
            file.write(record)
            print(f"Grade for course {course} added for student with roll number {roll_number} successfully.")
        else:
            print(f"Grade for course {course} already exists for student with roll number {roll_number}.")

def import_grades_from_file(data_file, course, file_path):
    with open(data_file, 'ab') as file:
        with open(file_path, 'r') as import_file:
            for line in import_file:
                data = line.strip().split('\t')
                roll_number, percent_marks = data[0], float(data[1])
                # Check for duplicate entry
                if not is_duplicate(file, (course, roll_number), (0, 1)):
                    record = struct.pack(grade_format, course.encode(), roll_number.encode(), percent_marks)
                    file.write(record)
                    print(f"Grade for course {course} added for student with roll number {roll_number} successfully.")
                else:
                    print(f"Grade for course {course} already exists for student with roll number {roll_number}.")

def view_grades(data_file, roll_number):
    with open(data_file, 'rb') as file:
        while True:
            record = file.read(struct.calcsize(grade_format))
            if not record:
                print(f"No grades found for student with roll number {roll_number}.")
                break
            values = struct.unpack(grade_format, record)
            if values[1].decode().strip('\x00') == roll_number:
                                print(f"Course: {values[0].decode()}, Roll Number: {values[1].decode()}, Percent Marks: {values[2]}")

def edit_grades(data_file, course, roll_number, new_percent_marks):
    with open(data_file, 'r+b') as file:
        while True:
            record = file.read(struct.calcsize(grade_format))
            if not record:
                print(f"No grades found for student with roll number {roll_number} and course {course}.")
                break
            current_position = file.tell() - struct.calcsize(grade_format)
            values = list(struct.unpack(grade_format, record))
            if values[0].decode().strip('\x00') == course and values[1].decode().strip('\x00') == roll_number:
                # Check for duplicate entry
                if not is_duplicate(file, (course, roll_number), (0, 1)):
                    values[2] = new_percent_marks
                    file.seek(current_position)
                    file.write(struct.pack(grade_format, *values))
                    print(f"Grade for course {course} edited for student with roll number {roll_number} successfully.")
                else:
                    print(f"Cannot edit. Grade for course {course} already exists for student with roll number {roll_number}.")
                break

def delete_grades(data_file, course, roll_number):
    with open(data_file, 'r+b') as file:
        while True:
            record = file.read(struct.calcsize(grade_format))
            if not record:
                print(f"No grades found for student with roll number {roll_number} and course {course}.")
                break
            current_position = file.tell() - struct.calcsize(grade_format)
            values = struct.unpack(grade_format, record)
            if values[0].decode().strip('\x00') == course and values[1].decode().strip('\x00') == roll_number:
                file.seek(current_position)
                file.truncate()
                print(f"Grade for course {course} deleted for student with roll number {roll_number} successfully.")
                break

def list_student_grades(data_file, roll_number):
    with open(data_file, 'rb') as file:
        while True:
            record = file.read(struct.calcsize(grade_format))
            if not record:
                break
            values = struct.unpack(grade_format, record)
            if values[1].decode().strip('\x00') == roll_number:
                print(f"Course: {values[0].decode()}, Percent Marks: {values[2]}")

def list_course_grades(data_file, course):
    with open(data_file, 'rb') as file:
        while True:
            record = file.read(struct.calcsize(grade_format))
            if not record:
                break
            values = struct.unpack(grade_format, record)
            if values[0].decode().strip('\x00') == course:
                print(f"Roll Number: {values[1].decode()}, Percent Marks: {values[2]}")

def award_sheet(data_file):
    # Implement based on your specific requirements
    pass

def summary_sheet(data_file):
    # Implement based on your specific requirements
    pass

def transcripts(data_file, start_roll_number, end_roll_number):
    with open(data_file, 'rb') as file:
        while True:
            record = file.read(struct.calcsize(student_format))
            if not record:
                break
            values = struct.unpack(student_format, record)
            roll_number = values[0].decode().strip('\x00')
            if start_roll_number <= roll_number <= end_roll_number:
                print(f"Roll Number: {roll_number}, Name: {values[1].decode()}, Department: {values[2].decode()}, Semester: {values[3]}, Marks: {values[4]}, Phone: {values[5].decode()}")
                # Add code to print corresponding grades for this student
                # print(student_grades(data_file, roll_number))

# Helper function to check for duplicate entries
def is_duplicate(file, key, key_indices):
    file.seek(0)
    while True:
        record = file.read(struct.calcsize(student_format) if len(key) == len(key_indices) == 1 else struct.calcsize(grade_format))
        if not record:
            break
        values = struct.unpack(student_format if len(key) == 1 else grade_format, record)
        if all(values[i].decode().strip('\x00') == key[i] for i in key_indices):
            return True
    return False

# Example usage
data_file = 'student_data.bin'

# Add a student
add_student(data_file, '12345678901', 'John Doe', 'CS', 2, 85.5, '12345678901')

# View a student
view_student(data_file, '12345678901')

# Edit a student
edit_student(data_file, '12345678901', 'John Doe Updated', 'CS', 3, 90.0, '12345678901')

# Delete a student
delete_student(data_file, '12345678901')

# List students by semester
list_students_by_semester(data_file, 2)

# List students by name
list_students_by_name(data_file, 'John Doe')

# Print all students
print_students_list(data_file)

# Add a grade
add_grade(data_file, 'Math101', '12345678901', 95.0)

# Import grades from a file
import_grades_from_file(data_file, 'Physics101', 'grades_import.txt')

# View grades of a student
view_grades(data_file, '12345678901')

# Edit grades of a student
edit_grades(data_file, 'Math101', '12345678901', 97.5)

# Delete grades of a student
delete_grades(data_file, 'Math101', '12345678901')

# List grades for a student
list_student_grades(data_file, '12345678901')

# List grades for a course
list_course_grades(data_file, 'Physics101')

# Generate transcripts for a range of students
transcripts(data_file, '12345678901', '12345678905')
