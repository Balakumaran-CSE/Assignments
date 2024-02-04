from abc import ABC, abstractmethod
from typing import List

class Customer:
    def __init__(self, customer_id, name, email):
        self.customer_id = customer_id
        self.name = name
        self.email = email

class Account(ABC):
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


class ICustomerServiceProvider(ABC):
    @abstractmethod
    def get_account_balance(self, account_number):
        pass

    @abstractmethod
    def deposit(self, account_number, amount):
        pass

    @abstractmethod
    def withdraw(self, account_number, amount):
        pass

    @abstractmethod
    def transfer(self, from_account_number, to_account_number, amount):
        pass

    @abstractmethod
    def get_account_details(self, account_number):
        pass


class IBankServiceProvider(ABC):
    @abstractmethod
    def create_account(self, customer, acc_type, balance):
        pass

    @abstractmethod
    def list_accounts(self):
        pass

    @abstractmethod
    def calculate_interest(self):
        pass


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
        print(f"Account created successfully. Account Number: {account.account_number}")
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
                if isinstance(account, SavingsAccount) and account.balance - amount < 500:
                    print("Withdrawal violates minimum balance rule.")
                    return account.balance
                account.balance -= amount
                return account.balance
        return None

    def transfer(self, from_account_number, to_account_number, amount):
        from_account = None
        for acc in CustomerServiceProviderImpl.accounts:
            if acc.account_number == from_account_number:
                from_account = acc
                break

        to_account = None
        for acc in CustomerServiceProviderImpl.accounts:
            if acc.account_number == to_account_number:
                to_account = acc
                break

        if from_account and to_account and from_account.balance >= amount:
            from_account.balance -= amount
            to_account.balance += amount
            return True
        else:
            return False

    def get_account_details(self, account_number):
        for account in CustomerServiceProviderImpl.accounts:
            if account.account_number == account_number:
                return {"account": account, "customer": account.customer}
        return None
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

class BankApp:
    def __init__(self):
        self.customer_service_provider = BankSerciceProviderImpl()

    def display_menu(self):
        print("\nBanking System Menu:")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Get Balance")
        print("5. Transfer")
        print("6. Get Account Details")
        print("7. List Accounts")
        print("8. Exit")

    def create_account_submenu(self):
        print("\nSelect Account Type:")
        print("1. Savings Account")
        print("2. Current Account")
        print("3. Zero Balance Account")

    def main(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")

            if choice == "1":
                self.create_account_submenu()
                acc_type_choice = input("Enter your choice for account type: ")
                if acc_type_choice in ["1", "2", "3"]:
                    name = input("Enter customer name: ")
                    email = input("Enter customer email: ")
                    customer = Customer(customer_id=None, name=name, email=email)

                    if acc_type_choice == "1":
                        self.customer_service_provider.create_account(customer, "Savings", balance=500)
                    elif acc_type_choice == "2":
                        self.customer_service_provider.create_account(customer, "Current", balance=1000)
                    elif acc_type_choice == "3":
                        self.customer_service_provider.create_account(customer, "ZeroBalance", balance=0)
                else:
                    print("Invalid choice. Please enter a valid option.")

            elif choice == "2":
                account_number = int(input("Enter Account Number: "))
                amount = float(input("Enter Deposit Amount: "))
                self.customer_service_provider.deposit(account_number, amount)

            elif choice == "3":
                account_number = int(input("Enter Account Number: "))
                amount = float(input("Enter Withdrawal Amount: "))
                self.customer_service_provider.withdraw(account_number, amount)

            elif choice == "4":
                account_number = int(input("Enter Account Number: "))
                balance = self.customer_service_provider.get_account_balance(account_number)
                if balance is not None:
                    print(f"Current Balance: {balance}")
                else:
                    print("Account not found.")

            elif choice == "5":
                from_account_number = int(input("Enter From Account Number: "))
                to_account_number = int(input("Enter To Account Number: "))
                amount = float(input("Enter Transfer Amount: "))
                success = self.customer_service_provider.transfer(from_account_number, to_account_number, amount)
                if success:
                    print("Transfer successful.")
                else:
                    print("Transfer failed. Please check account details and balance.")

            elif choice == "6":
                account_number = int(input("Enter Account Number: "))
                account_details = self.customer_service_provider.get_account_details(account_number)
                if account_details is not None:
                    print("Account Details:")
                    print(f"Account Number: {account_details['account'].account_number}")
                    print(f"Customer Name: {account_details['customer'].name}")
                    print(f"Balance: {account_details['account'].balance}")
                    if hasattr(account_details['account'], 'interest_rate'):
                        print(f"Interest Rate: {account_details['account'].interest_rate}")
                else:
                    print("Account not found.")

            elif choice == "7":
                accounts = self.customer_service_provider.list_accounts()
                if accounts:
                    print("List of Accounts:")
                    for account in accounts:
                        print(f"Account Number: {account.account_number}, Type: {account.account_type}")
                else:
                    print("No accounts found.")

            elif choice == "8":
                print("Exiting the Banking System. Goodbye!")
                break

            else:
                print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    bank_app = BankApp()
    bank_app.main()
