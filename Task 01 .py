import os

file_path = "courses_data.txt"

def display_menu():
    print("\nMenu:")
    print("a) Add")
    print("s) Search")
    print("d) Delete")
    print("l) List All")
    print("e) Edit")
    print("q) Quit")

def add_course():
    code = input("Enter course code (max 8 characters): ").strip()[:8]
    title = input("Enter course title (max 40 characters): ").strip()[:40]
    credits = input("Enter credits hours: ")
    semester = input("Enter default semester: ")
    course_type = input("Enter course type (core/elective): ").strip().lower()

    with open(file_path, 'a') as file:
        file.write(f"{code},{title},{credits},{semester},{course_type}\n")
    print("Course added successfully.")

def search_course():
    code_to_search = input("Enter course code to search: ").strip()[:8]
    with open(file_path, 'r') as file:
        for line in file:
            code, title, credits, semester, course_type = line.strip().split(',')
            if code == code_to_search:
                print(f"Code: {code}, Title: {title}, Credits: {credits}, Semester: {semester}, Type: {course_type}")
                return
    print("Course not found.")

def delete_course():
    code_to_delete = input("Enter course code to delete: ").strip()[:8]
    with open(file_path, 'r') as file:
        lines = file.readlines()
    with open(file_path, 'w') as file:
        for line in lines:
            code, _, _, _, _ = line.strip().split(',')
            if code != code_to_delete:
                file.write(line)
    print("Course deleted successfully.")

def list_all_courses():
    with open(file_path, 'r') as file:
        for line in file:
            code, title, credits, semester, course_type = line.strip().split(',')
            print(f"Code: {code}, Title: {title}, Credits: {credits}, Semester: {semester}, Type: {course_type}")

def edit_course():
    code_to_edit = input("Enter course code to edit: ").strip()[:8]
    with open(file_path, 'r') as file:
        lines = file.readlines()
    with open(file_path, 'w') as file:
        for line in lines:
            code, title, credits, semester, course_type = line.strip().split(',')
            if code == code_to_edit:
                new_title = input(f"Enter new title for {code}: ").strip()[:40]
                new_credits = input(f"Enter new credits for {code}: ")
                new_semester = input(f"Enter new semester for {code}: ")
                new_course_type = input(f"Enter new type (core/elective) for {code}: ").strip().lower()
                file.write(f"{code},{new_title},{new_credits},{new_semester},{new_course_type}\n")
                print("Course edited successfully.")
            else:
                file.write(line)

def main():
    menu_options = {'a': add_course, 's': search_course, 'd': delete_course, 'l': list_all_courses, 'e': edit_course, 'q': quit}

    if not os.path.exists(file_path):
        open(file_path, 'w').close()

    while True:
        display_menu()
        choice = input("Enter your choice: ").lower()

        if choice in menu_options:
            if choice == 'q':
                print("Exiting program. Goodbye!")
                break
            else:
                menu_options[choice]()
        else:
            print("Invalid input. Choose from the options below.")

if __name__ == "__main__":
    main()
