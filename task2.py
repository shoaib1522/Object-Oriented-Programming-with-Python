import sqlite3
from datetime import datetime, timedelta
def create_members_table():
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS members (
            membership_number INTEGER PRIMARY KEY,
            full_name TEXT,
            address TEXT,
            contact_number TEXT,
            category TEXT,
            membership_start_date TEXT,
            membership_expiry_date TEXT,
            membership_closing_date TEXT,
            fine_paid REAL
        )
    ''')
    conn.commit()
    conn.close()
def calculate_expiry_date(category):
    current_date = datetime.now()
    if category == 'A':
        expiry_date = current_date + timedelta(days=5*365)
    elif category == 'B':
        expiry_date = current_date + timedelta(days=3*365)
    elif category == 'C' or category == 'M':
        expiry_date = current_date + timedelta(days=365)
    else:
        expiry_date = None
    return expiry_date.strftime('%Y-%m-%d')
def add_member():
    full_name = input("Enter full name: ")
    address = input("Enter address: ")
    contact_number = input("Enter contact number: ")
    category = input("Enter category (A/B/C/M): ")

    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    membership_start_date = datetime.now().strftime('%Y-%m-%d')
    membership_expiry_date = calculate_expiry_date(category)

    cursor.execute('''
        INSERT INTO members (full_name, address, contact_number, category, 
                            membership_start_date, membership_expiry_date, membership_closing_date, fine_paid)
        VALUES (?, ?, ?, ?, ?, ?, NULL, 0.0)
    ''', (full_name, address, contact_number, category, membership_start_date, membership_expiry_date))
    conn.commit()
    conn.close()
    print("Member added successfully.")
def update_membership_closing_date():
    membership_number = input("Enter membership number of member to close: ")

    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()

    closing_date = datetime.now().strftime('%Y-%m-%d')
    cursor.execute('''
        UPDATE members SET membership_closing_date = ? WHERE membership_number = ?
    ''', (closing_date, membership_number))
    conn.commit()
    conn.close()
    print("Membership closed successfully.")
def display_menu():
    print("Menu:")
    print("a) Add Member, u) Update Membership Closing Date, l) List All Members, q) Quit")
def main():
    create_members_table()
    display_menu()
    
    while True:
        user_input = input("Enter your choice: ").lower()

        if user_input == 'a':
            add_member()
        elif user_input == 'u':
            update_membership_closing_date()
        elif user_input == 'l':
            conn = sqlite3.connect('library.db')
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM members')
            members = cursor.fetchall()
            conn.close()

            for member in members:
                print(member)
        elif user_input == 'q':
            break
        else:
            print("Invalid input. Choose from the options in the menu.")
            display_menu()

if __name__ == "__main__":
    main()