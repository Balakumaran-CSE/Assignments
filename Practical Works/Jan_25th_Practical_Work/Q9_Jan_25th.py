input=input("Enter the sequence: ")
words=input.split()
unique_word=[]
for i in words:
    if i not in unique_word:
        unique_word.append(i)
unique_word.sort()
for word in unique_word:
    print(word,end=" ")
