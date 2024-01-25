    num=input("Enter the number: ")
    l=[]
    for i in range(4):
        ele=num
        for j in range(i):
            ele+=num
        l.append(ele)
    integers=[]
    for j in l:
        integers.append(int(j))
    result=0
    for number in integers:
        result+=number
    print(result)