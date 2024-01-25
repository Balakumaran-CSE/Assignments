input=input("Enter the sequence")
input_in_char=[char for char in input]
upper_count=0
lower_count=0
for i in input_in_char:
    if i.isupper():
        upper_count+=1
    elif i.islower():
        lower_count+=1
print("UPPER CASE ",upper_count)
print("LOWER CASE ",lower_count)