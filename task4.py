import sqlite3
from datetime import datetime, timedelta
def category_wise_active_members():
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT category, COUNT(*) FROM members
        WHERE membership_closing_date IS NULL AND membership_expiry_date > date('now')
        GROUP BY category
    ''')
    categories = cursor.fetchall()
    conn.close()

    print("Category-wise active members:")
    for category in categories:
        print(f"{category[0]}: {category[1]}")

def count_of_titles_issued():
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT accession_number, COUNT(*) FROM circulation
        GROUP BY accession_number
    ''')
    titles = cursor.fetchall()
    conn.close()

    print("Count of each title issued to members:")
    for title in titles:
        print(f"{title[0]}: {title[1]}")
category_wise_active_members()
count_of_titles_issued()