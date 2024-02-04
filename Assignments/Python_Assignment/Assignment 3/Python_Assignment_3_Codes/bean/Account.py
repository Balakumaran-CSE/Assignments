class Account():
    last_acc_no = 0

    def __init__(self, account_type, customer, balance):
        Account.last_acc_no += 1
        self.account_number = Account.last_acc_no
        self.account_type = account_type
        self.customer = customer
        self.balance = balance

class SavingsAccount(Account):
    def __init__(self, customer, balance=500, interest_rate=0.02):
        super().__init__("Savings", customer, balance)
        self.interest_rate = interest_rate
    def calculate_interest(self):
        if self.interest_rate:
            result = self.balance * self.interest_rate
            self.balance += result
            print("Calculated interest rate for this account:", result)
        else:
            print("No interest rate specified for SavingsAccount")
class CurrentAccount(Account):
    def __init__(self, customer, balance, overdraft_limit):
        super().__init__("Current", customer, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount > self.balance + self.overdraft_limit:
            print("Withdrawal exceeds available balance and overdraft limit.")
        else:
            self.balance -= amount
            print(f"Withdrawal successful. Current balance: {self.balance}")

class ZeroBalanceAccount(Account):
    def __init__(self, customer):
        super().__init__("ZeroBalance", customer, 0)

