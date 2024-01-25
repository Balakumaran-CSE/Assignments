input=input("Enter the sequence of binary numbers")
binary_num=input.split(',')
decimal_num=[]
for i in binary_num:
    decimal_num.append(int(i,2))
for j in decimal_num:
    if j%5==0:
        print(bin(j)[2:],end=",")

