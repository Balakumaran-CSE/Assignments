def div(n):
    if n < 0:
        return div(-n)
    if n == 0 or n == 7:
        return True
    elif n < 10:
        return False
    last_digit = n - (n // 10) * 10
    remaining_digits = n // 10
    return div(remaining_digits - 2 * last_digit)
number = int(input("Enter a number: "))
if div(number):
    print("It is divisible by 7")
else:
    print("It is not divisible by 7")