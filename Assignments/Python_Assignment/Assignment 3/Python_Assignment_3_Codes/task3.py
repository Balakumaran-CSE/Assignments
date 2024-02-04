num_customers = int(input("Enter the number of customers: "))
for customer in range(1, num_customers + 1):
    print(f"Customer {customer}:")
    initial_balance = float(input("Enter the initial balance: "))
    annual_interest_rate = float(input("Enter the annual interest rate (in percentage): "))
    years = int(input("Enter the number of years: "))
    future_balance = initial_balance * (1 + annual_interest_rate/100)**years
    print(f"Future Balance for Customer {customer} after {years} years: {future_balance:.2f}")
