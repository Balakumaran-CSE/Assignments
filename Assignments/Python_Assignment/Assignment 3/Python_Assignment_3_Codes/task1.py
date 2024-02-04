credit_score = int(input("Enter your credit score: "))
annual_income = float(input("Enter your annual income: "))
if credit_score > 700 and annual_income >= 50000:
    print("Congratulations! You are eligible for a loan.")
else:
    print("Sorry, you are not eligible for a loan at this time.")

