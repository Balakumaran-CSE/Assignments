from services1.BankRepositoryImpl import BankRepositoryImpl
from services1.DBUtil import DBUtil


class BankApp():
    def main(self):

        obj = DBUtil()
        bank = BankRepositoryImpl()
        print("Banking System Menu: ")


        while True:
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