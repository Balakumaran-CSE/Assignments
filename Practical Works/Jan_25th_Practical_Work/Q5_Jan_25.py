from math import *
C=50
H=30
numbers=input()
D=numbers.split(',')
D=[int(i) for i in D]
result=[]
for l in D:
    Q=int(sqrt((2*C*l)/H))
    result.append(Q)
print(result)