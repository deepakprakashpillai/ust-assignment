class BankAccount:
    bank_name = "Bank of Python"

    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if BankAccount.validate_amount(amount):
            self.balance += amount
            print(f"Deposited {amount} to {self.account_holder}'s account.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if BankAccount.validate_amount(amount):
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew {amount} from {self.account_holder}'s account.")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    def display_info(self):
        return f"Account Holder: {self.account_holder}, Balance: {self.balance}, Bank: {BankAccount.bank_name}"

    @classmethod
    def update_bank_name(cls, new_name):
        cls.bank_name = new_name
        print(f"Bank name updated to '{cls.bank_name}'.")

    @staticmethod
    def validate_amount(amount):
        return amount > 0

account = BankAccount("Alice", 1000)

print(account.display_info())

account.deposit(500)
account.withdraw(200)

print(account.display_info())

BankAccount.update_bank_name("Bank of Python2")

print(f"Bank name for account: {account.bank_name}")

account.deposit(-100)

print(account.display_info())
