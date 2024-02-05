
from datetime import datetime

from bean1.Account import SavingsAccount
from bean1.Account import CurrentAccount
from bean1.Customer import Customer
from bean1.IBankRepository import IBankRepository


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
