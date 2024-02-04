info={
    'A101':15000,
    'A102':16000,
    'A103':17000,
    'A104':18000
}
while True:
    type=input("Enter the account number")
    if type in info.keys():
        print("You are a valid customer")
        print(f"Your Balance for Account_Id:{type} is {info[type]}")
        break
    else:
        print("Invalid Account Number. Please Try Again....")