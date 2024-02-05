from bean1.Account import SavingsAccount, CurrentAccount
from services1.CustomerServiceProviderImpl import CustomerServiceProviderImpl
from bean1 import IBankServiceProvider

class BankServiceProviderImpl(CustomerServiceProviderImpl, IBankServiceProvider):

    def create_account(self, customer, acc_no, acc_type, balance):
        account = None
        if acc_type == "Savings":
            account = SavingsAccount(customer, balance)
        elif acc_type == "Current":
            account = CurrentAccount(customer, balance, overdrafted_limit=1000)

        else:
            print("Invalid account type.")
        if account:
            self.accounts[acc_no] = account
            return account

    def list_accounts(self):
        return list(self.accounts.values())

    def get_account_details(self, account_number):
        return self.get_account_details(account_number)

    def calculate_interest(self):
        for account in self.accounts.values():
            if isinstance(account, SavingsAccount):
                interest = account.balance * account.interest_rate
                print(f"Account {account.account_number}: Interest calculated - {interest}")
