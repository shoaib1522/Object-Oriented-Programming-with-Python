import sqlite3
def create_table():
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS books (
            accno TEXT PRIMARY KEY,
            title TEXT,
            subtitle TEXT,
            author TEXT,
            coauthors TEXT,
            pages INTEGER,
            price REAL,
            category TEXT
        )
    ''')
    conn.commit()
    conn.close()
def add_book():
    accno = input("Enter accession number: ")
    title = input("Enter title: ")
    subtitle = input("Enter subtitle: ")
    author = input("Enter author: ")
    coauthors = input("Enter coauthors: ")
    pages = int(input("Enter number of pages: "))
    price = float(input("Enter price: "))
    category = input("Enter category (issuable or not issuable): ")
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO books VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (accno, title, subtitle, author, coauthors, pages, price, category))
    print("Book added successfully!")
    conn.commit()
    conn.close()
def search_book():
    accno = input("Enter accession number to search: ")
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM books WHERE accno = ?
    ''', (accno,))
    book = cursor.fetchone()
    if book:
        print("Book found:")
        print(book)
    else:
        print("Book not found.")
    conn.close()
def delete_book():
    accno = input("Enter accession number to delete: ")
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    cursor.execute('''
        DELETE FROM books WHERE accno = ?
    ''', (accno,))
    if cursor.rowcount > 0:
        print("Book deleted successfully!")
    else:
        print("Book not found.")
    conn.commit()
    conn.close()
def list_all_books():
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM books
    ''')
    books = cursor.fetchall()
    if books:
        print("List of all books:")
        for book in books:
            print(book)
    else:
        print("No books found in the library.")
    conn.close()
def edit_book():
    accno = input("Enter accession number to edit: ")
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM books WHERE accno = ?
    ''', (accno,))
    book = cursor.fetchone()
    if book:
        print("Current details of the book:")
        print(book)
        title = input("Enter new title (Press Enter to keep current): ") or book[1]
        subtitle = input("Enter new subtitle (Press Enter to keep current): ") or book[2]
        author = input("Enter new author (Press Enter to keep current): ") or book[3]
        coauthors = input("Enter new coauthors (Press Enter to keep current): ") or book[4]
        pages = int(input(f"Enter new number of pages (Press Enter to keep current {book[5]}): ") or book[5])
        price = float(input(f"Enter new price (Press Enter to keep current {book[6]}): ") or book[6])
        category = input("Enter new category (Press Enter to keep current): ") or book[7]
        cursor.execute('''
            UPDATE books SET title=?, subtitle=?, author=?, coauthors=?, pages=?, price=?, category=? WHERE accno=?
        ''', (title, subtitle, author, coauthors, pages, price, category, accno))
        print("Book updated successfully!")
    else:
        print("Book not found.")
    conn.commit()
    conn.close()
def main():
    create_table()
    while True:
        print("\nMenu:")
        print("a) Add, s) Search, d) Delete, l) List All, e) Edit, q) Quit")
        choice = input("Enter your choice: ").lower()
        if choice == 'a':
            add_book()
        elif choice == 's':
            search_book()
        elif choice == 'd':
            delete_book()
        elif choice == 'l':
            list_all_books()
        elif choice == 'e':
            edit_book()
        elif choice == 'q':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid input. Choose from the options below.")
if __name__ == "__main__":
    main()
