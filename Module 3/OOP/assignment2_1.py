class BankAccount:
    bank_name = "Bank of Python"

    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount} to {self.account_holder}'s account.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew {amount} from {self.account_holder}'s account.")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    def display_info(self):
        return f"Account Holder: {self.account_holder}, Balance: {self.balance}, Bank: {BankAccount.bank_name}"

account1 = BankAccount("Alice", 1000)
account2 = BankAccount("Bob", 500)

print(account1.display_info())
print(account2.display_info())
print("-------------------------------------------------------------------")
account1.deposit(500)
account2.withdraw(200)

print(account1.display_info())
print(account2.display_info())
print("-------------------------------------------------------------------")
print(f"Bank Name for account1: {account1.bank_name}")
print(f"Bank Name for account2: {account2.bank_name}")

