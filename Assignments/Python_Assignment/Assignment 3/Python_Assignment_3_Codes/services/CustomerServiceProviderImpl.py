from services.ICustomerServiceProvider import ICustomerServiceProvider
from bean.Account import SavingsAccount
from bean.Account import CurrentAccount
from bean.Account import ZeroBalanceAccount
from Exceptions import InsufficientFundException
from Exceptions import InvalidAccountException
from bean.Account import Account
class CustomerServiceProviderImpl(ICustomerServiceProvider):
    accounts = []

    def create_account(self, customer, acc_type, balance):
        if acc_type == "Savings":
            account = SavingsAccount(customer, balance)
        elif acc_type == "Current":
            account = CurrentAccount(customer, balance, overdraft_limit=1000)
        else:
            account = ZeroBalanceAccount(customer)
        CustomerServiceProviderImpl.accounts.append(account)
        print(f"Account created successfully. Account Number: {account.account_number} Account Type: {account.account_type}")
        return account

    def list_accounts(self):
        return CustomerServiceProviderImpl.accounts

    def get_account_balance(self, account_number):
        for account in CustomerServiceProviderImpl.accounts:
            if account.account_number == account_number:
                return account.balance
        return None

    def deposit(self, account_number, amount):
        for account in CustomerServiceProviderImpl.accounts:
            if account.account_number == account_number:
                account.balance += amount
                return account.balance
        return None

    def withdraw(self, account_number, amount):

        for account in CustomerServiceProviderImpl.accounts:

            if account.account_number == account_number:
                if account.balance < amount:
                    print("Withdrawal violates minimum balance rule.")
                    raise InsufficientFundException
                    return account.balance
                account.balance -= amount
                return account.balance
        return None

    def transfer(self, from_account_number, to_account_number, amount):
        from_account = None
        for acc in CustomerServiceProviderImpl.accounts:
            if acc.account_number == from_account_number:
                from_account = acc
                if from_account.balance < amount:
                    raise InsufficientFundException
                break


        to_account = None
        for acc in CustomerServiceProviderImpl.accounts:
            if acc.account_number == to_account_number:
                to_account = acc
                if from_account.balance < amount:
                    raise InsufficientFundException
                break


        if from_account and to_account and from_account.balance >= amount:
            from_account.balance -= amount
            to_account.balance += amount
            return True
        else:

            raise InvalidAccountException

    def get_account_details(self, account_number):
        for account in CustomerServiceProviderImpl.accounts:
            if account.account_number == account_number:
                return {"account": account, "customer": account.customer}
        return None