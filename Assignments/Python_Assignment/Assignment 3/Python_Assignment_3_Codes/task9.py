import re

class Customer:
    def __init__(self, customer_id, first_name, last_name, email, phone_number, address):
        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        self.address = address

    def validate_email(self, email):
        pattern = re.compile(r"[^@]+@[^@]+\.[^@]+")
        return bool(pattern.match(email))

    def validate_phone_number(self, phone_number):
        return len(str(phone_number)) == 10 and str(phone_number).isdigit()

    @property
    def customer_id(self):
        return self._customer_id

    @customer_id.setter
    def customer_id(self, value):
        self._customer_id = value

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self._first_name = value

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        self._last_name = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if self.validate_email(value):
            self._email = value
        else:
            raise ValueError("Invalid email format")

    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, value):
        if self.validate_phone_number(value):
            self._phone_number = value
        else:
            raise ValueError("Invalid phone number format")

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value

    def print_info(self):
        print(f"Customer ID: {self.customer_id}")
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Phone Number: {self.phone_number}")
        print(f"Address: {self.address}")


class Account:
    account_counter = 1000

    def __init__(self, account_type, balance, customer):
        self.account_number = Account.account_counter
        Account.account_counter += 1
        self.account_type = account_type
        self.balance = balance
        self.customer = customer

    @property
    def account_number(self):
        return self._account_number

    @account_number.setter
    def account_number(self, value):
        self._account_number = value

    @property
    def account_type(self):
        return self._account_type

    @account_type.setter
    def account_type(self, value):
        self._account_type = value

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        self._balance = value

    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, value):
        self._customer = value

    def print_info(self):
        print(f"Account Number: {self.account_number}")
        print(f"Account Type: {self.account_type}")
        print(f"Balance: {self.balance}")
        print("Customer Information:")
        self.customer.print_info()
class SavingsAccount(Account):
    def __init__(self, Account_NO=None, Account_Type=None, Account_Balance=None, Interest_Rate=None):
        super().__init__(Account_NO, Account_Type, Account_Balance)
        self.Interest_Rate = Interest_Rate

    def calculate_interest(self):
        if self.Interest_Rate:
            result = self._Account_Balance * self.Interest_Rate
            self._Account_Balance += result
            print("Calculated interest rate for this account:", result)
        else:
            print("No interest rate specified for SavingsAccount")


class CurrentAccount(Account):
    OVERDRAFT_LIMIT = 1000

    def __init__(self, Account_NO=None, Account_Type=None, Account_Balance=None, overdraftLimit=None):
        super().__init__(Account_NO, Account_Type, Account_Balance)
        self.overdraftLimit = self.OVERDRAFT_LIMIT

    def withdraw(self, amount):
        if amount <= self._Account_Balance + self.overdraftLimit:
            self._Account_Balance -= amount
            print(f"Withdrawal of amount {amount} has been done")
        else:
            print("Insufficient balance in your account and overdraft limit exceeded")


class Bank:
    accounts = []

    def create_account(self, customer, account_type, balance):
        account = Account(account_type, balance, customer)
        Bank.accounts.append(account)
        print(f"Account created successfully. Account Number: {account.account_number}")

    def get_account_balance(self, account_number):
        account = None
        for acc in Bank.accounts:
            if acc.account_number == account_number:
                account = acc
                break
        if account:
            return account.balance
        else:
            return None

    def deposit(self, account_number, amount):
        account = None
        for acc in Bank.accounts:
            if acc.account_number == account_number:
                account = acc
                break
        if account:
            account.balance += amount
            return account.balance
        else:
            return None

    def withdraw(self, account_number, amount):
        account = None
        for acc in Bank.accounts:
            if acc.account_number == account_number:
                account = acc
                break
        if account and account.balance >= amount:
            account.balance -= amount
            return account.balance
        else:
            return None

    def transfer(self, from_account_number, to_account_number, amount):
        from_account = None
        for acc in Bank.accounts:
            if acc.account_number == from_account_number:
                from_account = acc
                break

        to_account = None
        for acc in Bank.accounts:
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
        account = None
        for acc in Bank.accounts:
            if acc.account_number == account_number:
                account = acc
                break
        if account:
            account.print_info()
        else:
            print("Account not found.")

class BankApp:
    def main(self):
        bank = Bank()
        while True:
            print("1. Create Account")
            print("2. Get Account Balance")
            print("3. Deposit")
            print("4. Withdraw")
            print("5. Transfer")
            print("6. Get Account Details")
            print("7. Exit")

            choice = int(input("Enter your choice: "))

            if choice == 1:
                print("1. Savings Account")
                print("2. Current Account")
                account_type_choice = int(input("Choose the account type: "))
                customer_id = input("Enter Customer ID: ")
                first_name = input("Enter First Name: ")
                last_name = input("Enter Last Name: ")
                email = input("Enter Email: ")
                phone_number = input("Enter Phone Number: ")
                address = input("Enter Address: ")

                customer = Customer(customer_id, first_name, last_name, email, phone_number, address)

                balance = float(input("Enter Initial Balance: "))
                if account_type_choice == 1:
                    account_type = "Savings"
                else:
                    account_type = "Current"

                bank.create_account(customer, account_type, balance)

            elif choice == 2:
                account_number = int(input("Enter Account Number: "))
                balance = bank.get_account_balance(account_number)
                if balance is not None:
                    print(f"Account Balance: {balance}")
                else:
                    print("Account not found.")

            elif choice == 3:
                account_number = int(input("Enter Account Number: "))
                amount = float(input("Enter Deposit Amount: "))
                new_balance = bank.deposit(account_number, amount)
                if new_balance is not None:
                    print(f"Deposit successful. New Balance: {new_balance}")
                else:
                    print("Account not found or invalid amount.")

            elif choice == 4:
                account_number = int(input("Enter Account Number: "))
                amount = float(input("Enter Withdrawal Amount: "))
                new_balance = bank.withdraw(account_number, amount)
                if new_balance is not None:
                    print(f"Withdrawal successful. New Balance: {new_balance}")
                else:
                    print("Account not found or insufficient balance.")

            elif choice == 5:
                from_account_number = int(input("Enter From Account Number: "))
                to_account_number = int(input("Enter To Account Number: "))
                amount = float(input("Enter Transfer Amount: "))
                success = bank.transfer(from_account_number, to_account_number, amount)
                if success:
                    print("Transfer successful.")
                else:
                    print("Transfer failed. Check account details or insufficient balance.")

            elif choice == 6:
                account_number = int(input("Enter Account Number: "))
                bank.get_account_details(account_number)

            elif choice == 7:
                print("Exiting...")
                break

            else:
                print("Invalid choice. Please try again.")

bank_app = BankApp()
bank_app.main()
