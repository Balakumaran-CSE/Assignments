l=[]
n=int(input("Enter the number of elements"))
for i in range(n):
    elements=int(input("Enter the elements "))
    l.append(elements)
mul=1
for k in range(n):
    temp=l[k]
    for m in l:
        if m==temp:
            continue
        else:
            mul=mul*m
    print(mul)
    mul=1

