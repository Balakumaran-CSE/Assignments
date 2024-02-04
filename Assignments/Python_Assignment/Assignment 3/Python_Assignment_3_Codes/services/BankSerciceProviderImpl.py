from services.CustomerServiceProviderImpl import CustomerServiceProviderImpl
from services.IBankServiceProvider import IBankServiceProvider
from bean.Account import SavingsAccount
class BankSerciceProviderImpl(CustomerServiceProviderImpl,IBankServiceProvider):

    account_list=[]
    branchName=''
    branchAddress=''

    def create_account(self, customer, acc_type, balance):
        account = super().create_account(customer, acc_type, balance)
        self.account_list.append(account)
        return account
    def list_accounts(self):
        return BankSerciceProviderImpl.account_list

    def calculate_interest(self):
        for account in BankSerciceProviderImpl.account_list:
            if hasattr(account, 'interest_rate'):
                interest = account.balance * account.interest_rate
                account.balance += interest
                if isinstance(account, SavingsAccount):
                    print(
                        f"Interest of {interest} added to Savings Account {account.account_number}. New balance: {account.balance}")

