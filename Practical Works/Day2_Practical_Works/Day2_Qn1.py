

input_string = "ilikego"
word_dictionary = ['i', 'like', 'sam', 'sung', 'samsung', 'mobile', 'ice',
  'cream', 'icecream', 'man', 'go', 'mango'
]

n = len(input_string )

dp = [False] * (n + 1)
dp[0] = True

for i in range(1, n + 1):
    for word in word_dictionary:
        if input_string[i - len(word):i] == word:
            inword = True
            break

if inword==True:
    print("Yes")
else:
    print("No")

