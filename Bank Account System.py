import tkinter as tk
from tkinter import messagebox, simpledialog
import sqlite3
from datetime import datetime

class BankSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Meezan Bank")
        self.root.geometry("500x500")

        self.create_database()
        self.create_main_screen()

    

    def create_database(self):
        conn = sqlite3.connect('bankig_system.db')
        c = conn.cursor()

        c.execute('''
                  CREATE TABLE IF NOT EXISTS users (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      name TEXT NOT NULL,
                      address TEXT NOT NULL,
                      father_name TEXT NOT NULL,
                      username TEXT NOT NULL UNIQUE,
                      password TEXT NOT NULL
                  )
                  ''')

        c.execute('''
                  CREATE TABLE IF NOT EXISTS transactions (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      user_id INTEGER,
                      transaction_type TEXT NOT NULL,
                      amount REAL NOT NULL,
                      date TEXT NOT NULL,
                      FOREIGN KEY (user_id) REFERENCES users (id)
                  )
                  ''')

        conn.commit()
        conn.close()

   

 

  

    def create_main_screen(self):
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack()

        label = tk.Label(self.main_frame, text="Meezan Bank", font=('Helvetica', 20))
        label.pack(pady=20)

        login_label = tk.Label(self.main_frame, text="Login", font=('Helvetica', 16))
        login_label.pack()

        login_username_label = tk.Label(self.main_frame, text="Username:")
        login_username_label.pack()
        self.login_username_entry = tk.Entry(self.main_frame)
        self.login_username_entry.pack()

        login_password_label = tk.Label(self.main_frame, text="Password:")
        login_password_label.pack()
        self.login_password_entry = tk.Entry(self.main_frame, show="*")
        self.login_password_entry.pack()

        login_button = tk.Button(self.main_frame, text="Login", command=self.login)
        login_button.pack(pady=10)

        signup_label = tk.Label(self.main_frame, text="Sign Up", font=('Helvetica', 16))
        signup_label.pack()

        name_label = tk.Label(self.main_frame, text="Name:")
        name_label.pack()
        self.name_entry = tk.Entry(self.main_frame)
        self.name_entry.pack()

        address_label = tk.Label(self.main_frame, text="Address:")
        address_label.pack()
        self.address_entry = tk.Entry(self.main_frame)
        self.address_entry.pack()

        father_name_label = tk.Label(self.main_frame, text="Father's Name:")
        father_name_label.pack()
        self.father_name_entry = tk.Entry(self.main_frame)
        self.father_name_entry.pack()

        username_label = tk.Label(self.main_frame, text="Username:")
        username_label.pack()
        self.username_entry = tk.Entry(self.main_frame)
        self.username_entry.pack()

        password_label = tk.Label(self.main_frame, text="Password:")
        password_label.pack()
        self.password_entry = tk.Entry(self.main_frame, show="*")
        self.password_entry.pack()

        signup_button = tk.Button(self.main_frame, text="Sign Up", command=self.create_account)
        signup_button.pack(pady=10)

   

   

    def login(self):
        username = self.login_username_entry.get()
        password = self.login_password_entry.get()

        if username and password:  
            conn = sqlite3.connect('bankig_system.db')
            c = conn.cursor()

            c.execute('SELECT * FROM users WHERE username=? AND password=?', (username, password))
            user = c.fetchone()
            conn.close()

            if user:
                self.show_dashboard(user)
            else:
                messagebox.showerror('Error', 'Invalid username or password')
        else:
            messagebox.showerror('Error', 'Please enter both username and password')


    def create_account(self):
        name = self.name_entry.get()
        address = self.address_entry.get()
        father_name = self.father_name_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()

        if name and address and father_name and username and password:  
            conn = sqlite3.connect('bankig_system.db')
            c = conn.cursor()

            try:
                c.execute('''
                        INSERT INTO users (name, address, father_name, username, password)
                        VALUES (?, ?, ?, ?, ?)
                        ''', (name, address, father_name, username, password))
                conn.commit()
                conn.close()

                messagebox.showinfo('Success', 'Account created successfully!')
                self.clear_entries()
            except sqlite3.IntegrityError:
                messagebox.showerror('Error', 'Username already exists!')
        else:
            messagebox.showerror('Error', 'Please fill in all the fields')

    def show_dashboard(self, user):
        self.main_frame.destroy()

        dashboard_frame = tk.Frame(self.root)
        dashboard_frame.pack()

        label = tk.Label(dashboard_frame, text=f'Welcome to Meezan Bank, {user[1]}!', font=('Helvetica', 16))
        label.pack(pady=20)

        deposit_button = tk.Button(dashboard_frame, text='Deposit Amount', command=lambda: self.deposit(user))
        deposit_button.pack(pady=10)

        withdraw_button = tk.Button(dashboard_frame, text='Withdraw Amount', command=lambda: self.withdraw(user))
        withdraw_button.pack(pady=10)

        transfer_button = tk.Button(dashboard_frame, text='Transfer to Other Bank User', command=lambda: self.transfer(user))
        transfer_button.pack(pady=10)

        transaction_button = tk.Button(dashboard_frame, text='Transaction History', command=lambda: self.show_transactions(user))
        transaction_button.pack(pady=10)

        user_detail_button = tk.Button(dashboard_frame, text='Personal Details', command=lambda: self.show_user_details(user))
        user_detail_button.pack(pady=10)

        current_balance_button = tk.Button(dashboard_frame, text='Current Balance', command=lambda: self.show_current_balance(user))
        current_balance_button.pack(pady=10)

        logout_button = tk.Button(dashboard_frame, text='Logout', command=lambda: self.logout(dashboard_frame))
        logout_button.pack(pady=10)


    def deposit(self, user):
        amount_str = simpledialog.askstring('Deposit Amount', 'Enter the amount to deposit:')
        if amount_str:
            try:
                amount = float(amount_str)
                conn = sqlite3.connect('bankig_system.db')
                c = conn.cursor()

                c.execute('INSERT INTO transactions (user_id, transaction_type, amount, date) VALUES (?, ?, ?, ?)',
                          (user[0], 'Deposit', amount, datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
                conn.commit()
                conn.close()

                messagebox.showinfo('Success', f'Amount {amount} deposited successfully!')
            except ValueError:
                messagebox.showerror('Error', 'Invalid amount. Please enter a valid number.')

    def withdraw(self, user):
        amount_str = simpledialog.askstring('Withdraw Amount', 'Enter the amount to withdraw:')
        if amount_str:
            try:
                amount = float(amount_str)

                conn = sqlite3.connect('bankig_system.db')
                c = conn.cursor()

                c.execute('SELECT SUM(amount) FROM transactions WHERE user_id=? AND transaction_type=?',
                          (user[0], 'Deposit'))
                total_deposits = c.fetchone()[0] or 0

                if amount > total_deposits:
                    messagebox.showerror('Error', 'Insufficient balance!')
                else:
                    c.execute('INSERT INTO transactions (user_id, transaction_type, amount, date) VALUES (?, ?, ?, ?)',
                              (user[0], 'Withdraw', amount, datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
                    conn.commit()
                    conn.close()
                    messagebox.showinfo('Success', f'Amount {amount} withdrawn successfully!')
            except ValueError:
                messagebox.showerror('Error', 'Invalid amount. Please enter a valid number.')

    def transfer(self, user):
        amount_str = simpledialog.askstring('Transfer Amount', 'Enter the amount to transfer:')
        if amount_str:
            try:
                amount = float(amount_str)

                recipient_username = simpledialog.askstring('Recipient Username', 'Enter the recipient\'s username:')
                if recipient_username:
                    conn = sqlite3.connect('bankig_system.db')
                    c = conn.cursor()

                    c.execute('SELECT * FROM users WHERE username=?', (recipient_username,))
                    
                    recipient = c.fetchone()

                    if recipient:
                        c.execute('SELECT SUM(amount) FROM transactions WHERE user_id=? AND transaction_type=?',
                                  (user[0], 'Deposit'))
                        total_deposits = c.fetchone()[0] or 0

                        if amount > total_deposits:
                            messagebox.showerror('Error', 'Insufficient balance!')
                        else:
                            c.execute('INSERT INTO transactions (user_id, transaction_type, amount, date) VALUES (?, ?, ?, ?)',
                                      (user[0], 'Withdraw', amount, datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
                            c.execute('INSERT INTO transactions (user_id, transaction_type, amount, date) VALUES (?, ?, ?, ?)',
                                      (recipient[0], 'Deposit', amount, datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
                            conn.commit()
                            conn.close()
                            messagebox.showinfo('Success', f'Amount {amount} transferred to {recipient[1]} successfully!')
                    else:
                        messagebox.showerror('Error', 'User not found!')
                else:
                    messagebox.showerror('Error', 'Username not provided!')
            except ValueError:
                messagebox.showerror('Error', 'Invalid amount. Please enter a valid number.')

    def show_transactions(self, user):
        conn = sqlite3.connect('bankig_system.db')
        c = conn.cursor()

        c.execute('SELECT * FROM transactions WHERE user_id=? ORDER BY date DESC', (user[0],))
        transactions = c.fetchall()

        conn.close()

        if transactions:
            transaction_history = 'Transaction History:\n\n'
            for transaction in transactions:
                transaction_history += f'{transaction[4]} - {transaction[2]}: {transaction[3]}\n'
            messagebox.showinfo('Transaction History', transaction_history)
        else:
            messagebox.showinfo('Transaction History', 'No transactions yet.')
    def show_user_details(self, user):
        user_details_window = tk.Toplevel(self.root)
        user_details_window.title('User Details')

        user_details_label = tk.Label(user_details_window, text=f'User Details for {user[1]}')
        user_details_label.pack(pady=10)

        details_text = f"Name: {user[1]}\nAddress: {user[2]}\nFather's Name: {user[3]}\nUsername: {user[4]}"
        details_label = tk.Label(user_details_window, text=details_text)
        details_label.pack(pady=10)

    def show_current_balance(self, user):
            conn = sqlite3.connect('bankig_system.db')
            c = conn.cursor()

            c.execute('SELECT SUM(amount) FROM transactions WHERE user_id=? AND transaction_type=?', (user[0], 'Deposit'))
            total_deposits = c.fetchone()[0] or 0

            c.execute('SELECT SUM(amount) FROM transactions WHERE user_id=? AND transaction_type=?', (user[0], 'Withdraw'))
            total_withdrawals = c.fetchone()[0] or 0

            current_balance = total_deposits - total_withdrawals

            conn.close()

            current_balance_window = tk.Toplevel(self.root)
            current_balance_window.title('Current Balance')

            balance_label = tk.Label(current_balance_window, text=f'Current Balance for {user[1]}: {current_balance}')
            balance_label.pack(pady=10)



    def logout(self, frame_to_destroy):
        frame_to_destroy.destroy()
        self.create_main_screen()

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)
        self.father_name_entry.delete(0, tk.END)
        self.username_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    bank_system = BankSystem(root)
    root.mainloop()
