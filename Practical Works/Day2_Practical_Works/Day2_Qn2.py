def min_squares(n):
    dp = [0] + [i for i in range(1, n + 1)]
    for i in range(1, n + 1):
        j = 1
        while j * j <= i:
            dp[i] = min(dp[i], dp[i - j * j] + 1)
            j += 1
    return dp[n]
n = int(input("enter the number"))
result = min_squares(n)
print(result)