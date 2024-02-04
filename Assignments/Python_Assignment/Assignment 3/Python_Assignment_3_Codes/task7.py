class Customer:
    def __init__(self, CustomerID=None, First_Name=None, Last_Name=None, Email=None, Phone_NO=None, Address=None):
        self.CustomerID = CustomerID
        self.First_Name = First_Name
        self.Last_Name = Last_Name
        self.Email = Email
        self.Phone_NO = Phone_NO
        self.Address = Address

    @property
    def CustomerID(self):
        return self._CustomerID

    @CustomerID.setter
    def CustomerID(self, value):
        self._CustomerID = value

    @property
    def First_Name(self):
        return self._First_Name

    @First_Name.setter
    def First_Name(self, value):
        self._First_Name = value

    @property
    def Last_Name(self):
        return self._Last_Name

    @Last_Name.setter
    def Last_Name(self, value):
        self._Last_Name = value

    @property
    def Email(self):
        return self._Email

    @Email.setter
    def Email(self, value):
        self._Email = value

    @property
    def Phone_NO(self):
        return self._Phone_NO

    @Phone_NO.setter
    def Phone_NO(self, value):
        self._Phone_NO = value

    @property
    def Address(self):
        return self._Address

    @Address.setter
    def Address(self, value):
        self._Address = value

    def print_info(self):
        print("Customer ID: ", self.CustomerID)
        print("First Name: ", self.First_Name)
        print("Last Name: ", self.Last_Name)
        print("Email: ", self.Email)
        print("Phone Number: ", self.Phone_NO)
        print("Address: ", self.Address)

class Account:
    def __init__(self, Account_NO=None, Account_Type=None, Account_Balance=None):
        self._Account_NO = Account_NO
        self._Account_Type = Account_Type
        self._Account_Balance = Account_Balance

    @property
    def Account_NO(self):
        return self._Account_NO

    @Account_NO.setter
    def Account_NO(self, value):
        self._Account_NO = value

    @property
    def Account_Type(self):
        return self._Account_Type

    @Account_Type.setter
    def Account_Type(self, value):
        self._Account_Type = value

    @property
    def Account_Balance(self):
        return self._Account_Balance

    @Account_Balance.setter
    def Account_Balance(self, value):
        self._Account_Balance = value

    def Deposit(self, Amount:int):
        if Amount > 0:
            self._Account_Balance += Amount
            print(f"Amount of {Amount} has been deposited")
        else:
            print("Enter a valid amount")

    def Withdraw(self, Amount:int):
        if Amount <= self._Account_Balance:
            self._Account_Balance -= Amount
            print(f"Withdrawal of amount {Amount} has been done")
        else:
            print("Insufficient balance in your account")
    def Deposit(self, Amount:float):
        if Amount > 0:
            self._Account_Balance += Amount
            print(f"Amount of {Amount} has been deposited")
        else:
            print("Enter a valid amount")

    def Withdraw(self, Amount:float):
        if Amount <= self._Account_Balance:
            self._Account_Balance -= Amount
            print(f"Withdrawal of amount {Amount} has been done")
        else:
            print("Insufficient balance in your account")

    def calculate_interest(self):
        result = self._Account_Balance * 0.045
        self._Account_Balance+=result
        print("Calculated interest rate for this account: ",result)
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
    def main(self):
        while True:
            print("1. Create Savings Account")
            print("2. Create Current Account")
            print("3. Exit")

            choice = int(input("Enter your choice: "))

            if choice == 1:
                sa = SavingsAccount()
                sa.Account_NO = input("Enter account number: ")
                sa.Account_Type = 'Savings'
                sa.Account_Balance = float(input("Enter initial balance: "))
                sa.Interest_Rate = float(input("Enter interest rate: "))
                sa.Deposit(float(input("Enter the amount to be deposited: ")))
                sa.calculate_interest()

            elif choice == 2:
                ca = CurrentAccount()
                ca.Account_NO = input("Enter account number: ")
                ca.Account_Type = 'Current'
                ca.Account_Balance = float(input("Enter initial balance: "))
                ca.withdraw(float(input("Enter withdrawal amount: ")))

            elif choice == 3:
                print("Exiting...")
                break

            else:
                print("Invalid choice. Please try again.")


b1 = Bank()
b1.main()
