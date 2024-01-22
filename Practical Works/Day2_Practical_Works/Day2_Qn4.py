def fun(n):
    if n == 1:
        return "1"

    prev_term = "1"
    for _ in range(2, n + 1):
        new_term = ""
        count = 1
        for i in range(1, len(prev_term)):
            if prev_term[i] == prev_term[i - 1]:
                count += 1
            else:
                new_term += str(count) + prev_term[i - 1]
                count = 1
        new_term += str(count) + prev_term[-1]
        prev_term = new_term
    return prev_term
n=int(input("Enter a number: "))
print(fun(n))
