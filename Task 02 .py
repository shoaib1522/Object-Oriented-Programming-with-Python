class LowBalException(Exception):
    def __init__(self, message="Withdrawal amount exceeds available balance. Transaction cancelled."):
        self.message = message
        super().__init__(self.message)
class BankAccount:
    def __init__(self, account_number, min_balance, initial_balance):
        self.__account_number = account_number
        self.__min_balance = min_balance
        self.__cur_balance = initial_balance

    def __str__(self):
        return f"Account Number: {self.__account_number}, Current Balance: {self.__cur_balance}"

    def withdraw(self, amount):
        try:
            if amount <= 0:
                raise ValueError("Withdrawal amount must be greater than zero.")

            if amount > self.__cur_balance - self.__min_balance:
                raise LowBalException()

            self.__cur_balance -= amount
            print(f"Withdrawal successful. Current balance: {self.__cur_balance}")

        except LowBalException as e:
            print(f"LowBalException: {e}")
account1 = BankAccount(1001, 1000, 5000)
print(account1)

account1.withdraw(1000)  
account1.withdraw(3000)  
# account1.withdraw(-500)  
account1.withdraw(200)   
