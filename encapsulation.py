# Encapsulation: Hiding internal details and exposing only necessary parts.
class BankAccount:
    def __init__(self, balance=0):
        self.__balance = balance  # Private attribute (can't access directly)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance: {self.__balance}")
        else:
            print("Invalid withdrawal.")

    def get_balance(self):
        return self.__balance  # Public method to access private data

# Usage
account = BankAccount(100)
account.deposit(50)
account.withdraw(30)
print("Final balance:", account.get_balance())
# Trying to access private: account.__balance  # This would raise an error