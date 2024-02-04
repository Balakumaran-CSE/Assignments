available_balance = 15000

while True:
    opt = '''Enter the options:
       1----> Check Balance
       2----> Withdraw
       3----> Deposit
       4----> Exit'''
    print(opt)
    option = input()

    if option == '1':
        print("Available Balance:", available_balance)
    elif option == '2':
        print("Enter the amount:")
        amount = int(input())
        if available_balance <= 0 or amount % 100 != 0 or available_balance < amount:
            print("Invalid amount entered. Please check the amount.")
        else:
            available_balance -= amount
            print("Withdrawal successful. Available Balance:", available_balance)
    elif option == '3':
        print("Enter the amount to be deposited:")
        amount = int(input())
        available_balance += amount
        print("Deposit successful. Available Balance:", available_balance)
    elif option == '4':
        print("Thanks for banking with us!")
        break
    else:
        print("Invalid option. Please enter a valid option (1-4).")
