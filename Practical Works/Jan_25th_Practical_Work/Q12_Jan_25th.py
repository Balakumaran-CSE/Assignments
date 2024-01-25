input=input("Enter the sequence")
word=[char for char in input]
letters=0
numbers=0
for i in word:
    if i.isalpha():
        letters+=1
    elif i.isdigit():
        numbers+=1
print("Letters ",letters)
print("Numbers ",numbers)