n=int(input("Enter the number: "))
l=[]
for i in range(n):
    ele=int(input("Enter the number who's factorial is to be find: "))
    l.append(ele)
for j in l:
    fact = 1
    for time in range(1,j+1):
        fact=fact*time
    print(fact,end=",")
