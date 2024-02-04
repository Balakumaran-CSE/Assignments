from abc import ABC, abstractmethod
from datetime import datetime
import mysql.connector
class Customer:
    def __init__(self, customer_id, first_name, last_name, email, phone_number, address):
        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        self.address = address

class Account:
    account_counter = 1000

    def __init__(self, account_type, balance, customer):
        self.account_number = Account.account_counter
        Account.account_counter += 1
        self.account_type = account_type
        self.balance = balance
        self.customer = customer

class Transaction:

    def __init__(self,account,description,date_time,transaction_amount):
        self.account=account
        self.description=description
        self.date_time=date_time
        self.transaction_amount=transaction_amount

class SavingsAccount(Account):
    def __init__(self, customer, balance=500, interest_rate=0.02):
        super().__init__("Savings", customer, balance)
        self.interest_rate = interest_rate

class CurrentAccount(Account):
    def __init__(self, customer, balance, overdrafted_limit):
        super().__init__("Current", balance, customer)
        self.overdrafted_limit = overdrafted_limit


class ZeroBalanceAccount(Account):
    def __init__(self,customer,balance=0):
        super().__init__(customer)
        self.balance=balance

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

    @abstractmethod
    def get_transactions(self, account_number, from_date, to_date):
        pass

class IBankServiceProvider(ABC):

    @abstractmethod
    def create_account(self,customer,account_number,account_type,balance):
        pass

    @abstractmethod
    def lisAccounts(self):
        pass

    @abstractmethod
    def getAccountDetails(self,account_number):
        pass

    @abstractmethod
    def calculateInterest(self):
        pass

class CustomerServiceProviderImpl(ICustomerServiceProvider):
    def __init__(self):
        self.accounts={}
        self.transactions=[]

    def get_account_balance(self, account_number):
        if account_number in self.accounts:
            return self.accounts[account_number].balance
        else:
            return None

    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            self.accounts[account_number].balance+=amount
            transaction=Transaction(self.accounts[account_number],'Deposit',datetime.now(),amount)
            self.transactions.append(transaction)
            print(f"Deposited an amount of {amount}")
            return self.accounts[account_number].balance
        return None

    def withdraw(self, account_number, amount):
        if account_number in self.accounts:
            account=self.accounts[account_number]

            if isinstance(account,SavingsAccount) and account.balance-amount<500:
                print("Insufficient fund in your account")
            elif isinstance(account,CurrentAccount) and account.balance+account.overdrafted_limit<amount:
                print("Insufficient fund in your account")
            else:
                account.balance-=amount
                transaction=Transaction(account,'Withdraw',datetime.now(),amount)
                self.transactions.append(transaction)
                return account.balance
        return None

    def transfer(self, from_account_number, to_account_number, amount):
        from_balance = self.get_account_balance(from_account_number)
        if from_balance is not None and from_balance >= amount:
            self.withdraw(from_account_number, amount)
            to_balance = self.deposit(to_account_number, amount)
            transaction=Transaction(self.accounts[from_account_number],'Tranfer- Sending Amount',datetime.now(),amount)
            self.transactions.append(transaction)
            transaction1=Transaction(self.accounts[to_account_number], 'Tranfer- Receive Amount', datetime.now(),
                                      amount)
            self.transactions.append(transaction1)
            if to_balance is not None:
                return to_balance
        print("Error: Insufficient funds for transfer.")
        return None

    def get_account_details(self, account_number):
        if account_number in self.accounts:
            return self.accounts[account_number]
        else:
            return None

    def get_transactions(self, account_number, from_date, to_date):
        if account_number in self.accounts:
            account_transactions = [transaction for transaction in self.transactions
                                     if transaction.account.account_number == account_number
                                     and from_date <= transaction.date_time <= to_date]
            return account_transactions
        else:
            return None


class BankServiceProviderImpl(CustomerServiceProviderImpl, IBankServiceProvider):

    def create_account(self, customer, acc_no, acc_type, balance):
        account = None
        if acc_type == "Savings":
            account = SavingsAccount(customer, balance)
        elif acc_type == "Current":
            account = CurrentAccount(customer, balance, overdrafted_limit=1000)
        elif acc_type == "ZeroBalance":
            account = ZeroBalanceAccount(customer)
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

class IBankRepository(ABC):

    @abstractmethod
    def createAccount(self,con,customer,account_type,balance):
        pass
    @abstractmethod
    def listAccount(self,con):
        pass
    @abstractmethod
    def calculateInterest(self, con, user_interest_rate):
        pass
    @abstractmethod
    def getAccountBalance(self,con,account_number):
        pass
    @abstractmethod
    def createCustomer(self,con, first_name, last_name,DOB,email,phone_no,address ):
        pass
    @abstractmethod
    def deposit(self,con,account_number,amount):
        pass
    @abstractmethod
    def withdraw(self,con,account_number,amount):
        pass
    @abstractmethod
    def transfer(self,con,from_account_number,to_account_number,amount):
        pass
    @abstractmethod
    def getAccountdetails(self,con,account_number):
        pass
    @abstractmethod
    def getTransactions(self,con,account_number,from_date,to_date):
        pass
    @abstractmethod
    def generateCustomerId(self,con):
        pass

class BankRepositoryImpl(IBankRepository):
    def __init__(self):
        self.counter = 1000
        self.account_list = []
        self.counter2=15

    def generateAccountNumber(self,con):
        cur=con.cursor()
        cur.execute("SELECT MAX(account_id) from Accounts")
        max_account_id=cur.fetchone()[0]
        max_account_id+=1
        return str(max_account_id)
    def generateCustomerId(self,con):
        cur = con.cursor()
        cur.execute("SELECT MAX(customer_id) FROM Customers")
        max_customer_id = cur.fetchone()[0]
        max_customer_id += 1
        return str(max_customer_id)
    def listAccount(self, con):
        cur = con.cursor()
        cur.execute("SELECT * FROM Accounts")
        res = cur.fetchall()
        return res

    def createCustomer(self, con, first_name, last_name, DOB, email, phone_no, address):
        cur = con.cursor()
        customer_id = self.generateCustomerId(con)
        cur.execute("INSERT INTO Customers VALUES (%s, %s, %s, %s, %s, %s, %s)",
                    (customer_id, first_name, last_name, DOB, email, phone_no, address))
        con.commit()
        print(f"Welcome {first_name}")

        return Customer(customer_id, first_name, last_name, email, phone_no, address)

    def createAccount(self, con, customer, account_type, balance):
        account = None
        account_number = self.generateAccountNumber(con)

        if account_type == "Savings":
            account = SavingsAccount(customer, balance)
        elif account_type == "Current":
            account = CurrentAccount(customer, balance, overdrafted_limit=1000)
        elif account_type == "ZeroBalance":
            account = ZeroBalanceAccount(customer)
        else:
            print("Invalid account type.")
            return  # exit the function if the account type is invalid

        if account:
            try:
                cur = con.cursor()
                cur.execute(
                    "INSERT INTO Accounts (account_id, customer_id, account_type, balance) VALUES (%s, %s, %s, %s)",
                    (account_number, customer.customer_id, account_type, balance))
                con.commit()
                print(
                    f"{account_type} Account for Customer ID {customer.customer_id} created successfully with Account Number {account_number}...")
                self.account_list.append(account)
            except Exception as e:
                print(f"Error in createAccount: {e}")

    def calculateInterest(self, con, user_interest_rate):
        try:
            cur = con.cursor()
            cur.execute("SELECT account_id, balance, account_type FROM Accounts WHERE account_type = 'Savings'")
            savings_accounts = cur.fetchall()

            for account_id, balance, account_type in savings_accounts:
                if account_type == 'Savings':
                    account = SavingsAccount(None)
                    account.account_number = account_id
                    account.balance =float(balance)
                    interest_rate = float(user_interest_rate)
                    interest = account.balance * interest_rate
                    new_balance = account.balance + interest

                    cur.execute("UPDATE Accounts SET balance = %s WHERE account_id = %s", (new_balance, account_id))
                    con.commit()
                    print(f"Account {account_id}: Interest calculated - {interest}. New balance - {new_balance}")
        except Exception as e:
            print(f"Error in calculateInterest: {e}")

    def getAccountBalance(self, con, account_number):
        cur = con.cursor()
        cur.execute("SELECT balance FROM Accounts WHERE account_id = %s", (account_number,))
        res = cur.fetchone()
        return res

    def deposit(self, con, account_number, amount):
        try:

            cur=con.cursor()
            transaction_type='Deposit'
            cur.execute("INSERT INTO Transactions (account_id,transaction_type,amount,transaction_date) VALUES (%s, %s, %s, %s)",(account_number,transaction_type,amount,datetime.now()))
            con.commit()
            print(f"Deposit of amount {amount} done successfully...")

            cur2=con.cursor()
            cur2.execute("UPDATE Accounts SET balance = balance + %s WHERE account_id = %s", (amount, account_number))
            con.commit()

        except Exception as e:
            con.rollback()
            print(e)
    def withdraw(self, con, account_number, amount):
        try:
            cur=con.cursor()
            transaction_type='Withdrawal'
            cur.execute(
                "INSERT INTO Transactions (account_id, transaction_type, amount, transaction_date) VALUES (%s, %s, %s, %s)",
                (account_number, transaction_type, amount, datetime.now()))
            print(f"Withdrawal of amount {amount} from account {account_number} done successfully")
            con.commit()
            cur2=con.cursor()
            cur2.execute("UPDATE Accounts SET balance = balance - %s WHERE account_id = %s",(amount,account_number))
            con.commit()
        except Exception as e:
            print(e)

    def transfer(self, con, from_account_number, to_account_number, amount):
        try:
            cur = con.cursor()
            cur.execute("SELECT balance FROM Accounts WHERE account_id = %s", (from_account_number,))
            from_balance = cur.fetchone()
            if from_balance[0] > amount:
                with con.cursor() as cur:
                    # Deduct amount from the sender's account
                    cur.execute("UPDATE Accounts SET balance = balance - %s WHERE account_id = %s",
                                (amount, from_account_number))

                    # Add amount to the receiver's account
                    cur.execute("UPDATE Accounts SET balance = balance + %s WHERE account_id = %s",
                                (amount, to_account_number))
                    print(f"Amount Transfered Successfully from Account {from_account_number} to {to_account_number}")
                con.commit()
        except Exception as e:
            print(e)


    def getAccountdetails(self, con, account_number):
        cur=con.cursor()
        cur.execute("SELECT * FROM Accounts WHERE account_id = %s",(account_number,))
        details=cur.fetchone()
        print("=" * 20)
        print("Account Details: ")
        print("="*20)
        print(f"Account ID: {details[0]}")
        print(f"Customer ID: {details[1]}")
        print(f"Account Type: {details[2]}")
        print(f"Balance: {details[3]}")

    def getTransactions(self, con, account_number, from_date, to_date):
        try:
            with con.cursor() as cur:
                cur.execute("SELECT * FROM Transactions WHERE account_id = %s AND transaction_date BETWEEN %s AND %s",
                            (account_number, from_date, to_date))
                res = cur.fetchall()
            print(f"Transaction Details for {account_number}")
            for transaction in res:
                transaction_id, account_id, transaction_type, amount, transaction_date= transaction
                print(f"Transaction ID :{transaction_id}, Account ID :{account_id}, Type : {transaction_type}, Date: {transaction_date}")
        except Exception as e:
            print(f"Error: {e}")

class DBUtil:
    def __init__(self):
        self.con = mysql.connector.connect(host='localhost', user='root', passwd='root', database='HMBank', port='3306')
        if self.con:
            print("Connection successful")

    def __del__(self):
        if hasattr(self, 'con') and self.con.is_connected():
            self.con.close()
            print("Connection closed")


class BankApp():
    def main(self):

        obj = DBUtil()
        bank = BankRepositoryImpl()
        print("Banking System Menu: ")

        print('''
                 1------>Create Account
                 2------>Deposit
                 3------>Withdraw
                 4------>Get Balance
                 5------>Transfer
                 6------>Get Account Details
                 7------>List Accounts
                 8------>Get Transactions
                 9------>Exit
            ''')
        while True:
            choice=int(input("Enter your choice: "))
            if choice == 1:
                print("Enter the customer details: ")
                first_name = input("Enter your first name: ")
                last_name = input("Enter your last name: ")
                dob = input("Enter your Date of Birth: ")
                email = input("Enter your email")
                phone_no = int(input("Enter the phone number: "))
                address = input("Enter your address: ")

                customer = bank.createCustomer(obj.con, first_name, last_name, dob, email, phone_no, address)

                account_type = input("Enter the type of account you are willing to create: ")
                balance = int(input("Enter your initial balance: "))
                bank.createAccount(obj.con, customer, account_type, balance)

            if choice == 2:
                account_number=int(input("Enter your account number: "))
                amount=int(input("Enter the amount: "))
                bank.deposit(obj.con,account_number,amount)

            if choice == 3:
                account_number = int(input("Enter your account number: "))
                amount = int(input("Enter the amount: "))
                bank.withdraw(obj.con,account_number,amount)

            if choice == 4:
                account_number=int(input("Enter your account number: "))
                balance=bank.getAccountBalance(obj.con,account_number)
                print("Your Available balance: ",float(balance[0]))

            if choice == 5:
                from_account=int(input("Enter the from account number: "))
                to_account = int(input("Enter the from to number: "))
                amount=int(input("Enter the amount: "))
                bank.transfer(obj.con,from_account,to_account,amount)

            if choice == 6:
                account_number=int(input("Enter the account number: "))
                bank.getAccountdetails(obj.con,account_number)

            if choice == 7:
                account_list=bank.listAccount(obj.con)
                for account in account_list:
                    print(" ",account)

            if choice == 8:
                account_number=int(input("Enter the account number: "))
                from_date=input("Enter the from date: ")
                to_date = input("Enter the to date: ")
                bank.getTransactions(obj.con,account_number,from_date,to_date)

            if choice == 9:
                print("Thank you for banking with us.....")
                break;


b=BankApp()
b.main()
