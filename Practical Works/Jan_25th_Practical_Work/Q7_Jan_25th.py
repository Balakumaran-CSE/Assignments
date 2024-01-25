X=int(input("Enter the first number"))
Y=int(input("Enter the second number"))
for i in range(X):
    for j in range(Y):
        print(i*j,end="")
    print()