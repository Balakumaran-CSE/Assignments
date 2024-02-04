while True:
    password = input("Enter your password: ")
    if len(password) < 8:
        print("Your password must be at least 8 characters long.")
    elif not any(char.isupper() for char in password):
        print("Your password must contain at least one uppercase letter.")
    elif not any(char.isdigit() for char in password):
        print("Your password must contain at least one digit.")
    else:
        print("Password successfully created. Your account is now secure.")
        break