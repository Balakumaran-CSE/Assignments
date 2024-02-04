class Account:
    account_counter = 1000

    def __init__(self, account_type, balance, customer):
        self.account_number = Account.account_counter
        Account.account_counter += 1
        self.account_type = account_type
        self.balance = balance
        self.customer = customer


class SavingsAccount(Account):
    def __init__(self, customer, balance=500, interest_rate=0.02):
        super().__init__("Savings", customer, balance)
        self.interest_rate = interest_rate

class CurrentAccount(Account):
    def __init__(self, customer, balance, overdrafted_limit):
        super().__init__("Current", balance, customer)
        self.overdrafted_limit = overdrafted_limit