n = int(input("Enter the number: "))
for i in range(1, n + 1):
    print("({}:{})".format(i, i*i), end=",")