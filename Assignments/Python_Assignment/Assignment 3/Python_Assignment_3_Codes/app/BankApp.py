from services.BankSerciceProviderImpl import BankSerciceProviderImpl
from bean.Customer import Customer
from Exceptions import InsufficientFundException
from Exceptions import InvalidAccountException
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
                try:
                    account_number = int(input("Enter Account Number: "))
                    amount = float(input("Enter Withdrawal Amount: "))
                    self.customer_service_provider.withdraw(account_number, amount)
                except InsufficientFundException as e:
                    print(e)

            elif choice == "4":
                account_number = int(input("Enter Account Number: "))
                balance = self.customer_service_provider.get_account_balance(account_number)
                if balance is not None:
                    print(f"Current Balance: {balance}")
                else:
                    print("Account not found.")

            elif choice == "5":
                try:
                    from_account_number = int(input("Enter From Account Number: "))
                    to_account_number = int(input("Enter To Account Number: "))
                    amount = float(input("Enter Transfer Amount: "))
                    success = self.customer_service_provider.transfer(from_account_number, to_account_number, amount)
                    if success:
                        print("Transfer successful.")
                    else:
                        print("Transfer failed. Please check account details and balance.")
                except InvalidAccountException as e:
                    print(e)
                except InsufficientFundException as e:
                    print(e)

            elif choice == "6":
                account_number = int(input("Enter Account Number: "))
                account_details = self.customer_service_provider.get_account_details(account_number)
                if account_details is not None:
                    print("Account Details:")
                    print(f"Account Number: {account_details['account'].account_number}")
                    print(f"Customer Name: {account_details['customer'].name}")
                    print(f"Balance: {account_details['account'].balance}")
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
