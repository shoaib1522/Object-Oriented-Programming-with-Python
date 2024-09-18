import sqlite3
from datetime import datetime, timedelta

def create_circulation_table():
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS circulation (
            serial_number INTEGER PRIMARY KEY AUTOINCREMENT,
            mem_number TEXT,
            accno TEXT,
            issue_date DATE,
            return_date DATE
        )
    ''')

    conn.commit()
    conn.close()

def issue_book():
    mem_number = input("Enter membership number: ")
    accno = input("Enter accession number of the book: ")

    if not check_member_existence(mem_number) or not check_book_existence(accno):
        print("Invalid member or book. Please check the details.")
        return

    if not check_book_limit(mem_number):
        print("Member has reached the book limit for their category.")
        return

    if not check_book_availability(accno):
        print("The book is not available for issuance.")
        return

    issue_date = datetime.now().date()
    return_date = issue_date + timedelta(days=14)

    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO circulation (mem_number, accno, issue_date, return_date)
        VALUES (?, ?, ?, ?)
    ''', (mem_number, accno, issue_date, return_date))

    print("Book issued successfully!")

    cursor.execute('''
        UPDATE books SET status='issued' WHERE accno=?
    ''', (accno,))

    conn.commit()
    conn.close()

def return_book():
    mem_number = input("Enter membership number: ")
    accno = input("Enter accession number of the book: ")

    if not check_circulation_record(mem_number, accno):
        print("Invalid circulation record. Please check the details.")
        return

    return_date = datetime.now().date()

    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()

    cursor.execute('''
        UPDATE circulation SET return_date=? WHERE mem_number=? AND accno=?
    ''', (return_date, mem_number, accno))

    print("Book returned successfully!")

    cursor.execute('''
        UPDATE books SET status='available' WHERE accno=?
    ''', (accno,))

    conn.commit()
    conn.close()

def list_circulation_records():
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()

    cursor.execute('''
        SELECT * FROM circulation
    ''')

    circulation_records = cursor.fetchall()

    if circulation_records:
        print("List of all circulation records:")
        for record in circulation_records:
            print(record)
    else:
        print("No circulation records found.")

    conn.close()

def check_member_existence(mem_number):
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()

    cursor.execute('''
        SELECT * FROM members WHERE mem_number = ?
    ''', (mem_number,))

    member = cursor.fetchone()

    conn.close()

    return member is not None

def check_book_existence(accno):
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()

    cursor.execute('''
        SELECT * FROM books WHERE accno = ?
    ''', (accno,))

    book = cursor.fetchone()

    conn.close()

    return book is not None
def check_book_limit(mem_number):
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT category FROM members WHERE mem_number = ?
    ''', (mem_number,))
    category = cursor.fetchone()[0]
    cursor.execute('''
        SELECT COUNT(*) FROM circulation WHERE mem_number = ? AND return_date IS NULL
    ''', (mem_number,))
    issued_books_count = cursor.fetchone()[0]
    conn.close()
    if category == 'A' and issued_books_count >= 10:
        return False
    elif category == 'B' and issued_books_count >= 7:
        return False
    elif category == 'C' and issued_books_count >= 3:
        return False
    elif category == 'M' and issued_books_count >= 5:
        return False
    else:
        return True
def check_book_availability(accno):
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT status FROM books WHERE accno = ?
    ''', (accno,))

    status = cursor.fetchone()[0]
    conn.close()
    return status == 'available'
def check_circulation_record(mem_number, accno):
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM circulation WHERE mem_number = ? AND accno = ? AND return_date IS NULL
    ''', (mem_number, accno))
    record = cursor.fetchone()
    conn.close()
    return record is not None
def main():
    create_circulation_table()
    while True:
        print("\nMenu:")
        print("i) Issue Book, r) Return Book, c) List Circulation Records, q) Quit")
        choice = input("Enter your choice: ").lower()
        if choice == 'i':
            issue_book()
        elif choice == 'r':
            return_book()
        elif choice == 'c':
            list_circulation_records()
        elif choice == 'q':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid input. Choose from the options below.")

if __name__ == "__main__":
    main()

