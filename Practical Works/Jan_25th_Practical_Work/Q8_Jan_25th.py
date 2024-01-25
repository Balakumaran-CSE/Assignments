line=int(input("Enter the number of lines: "))
l=[]
for i in range(line):
    sentences=input("Enter the sentences")
    l.append(sentences)
for sent in l:
    print(sent.upper())