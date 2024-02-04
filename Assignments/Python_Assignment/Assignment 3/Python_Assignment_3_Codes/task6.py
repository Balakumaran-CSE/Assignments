transaction_history = []
opt='''Enter your Choice for Bank Transaction
           1------>Deposit
           2------>Withdrawal
           3------>Exit
        '''
print(opt)
while True:
    choice = input("Enter your choice (1-3): ")
    if choice == '1':
        amount = float(input("Enter the deposit amount: "))
        transaction_history.append(('Deposit', amount))
        print(f"Deposit of {amount:.2f} done.")
    elif choice == '2':
        amount = float(input("Enter the withdrawal amount: "))
        transaction_history.append(('Withdrawal', amount))
        print(f"Withdrawal of {amount:.2f} from your account.")
    elif choice == '3':
        print("Transaction History:")
        for transaction_type, amount in transaction_history:
            print(f"{transaction_type}: {amount:.2f}")
        print("Thank you for Banking with us!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 3.")
