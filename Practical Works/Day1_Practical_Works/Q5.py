def repeating_element(arr):

    frequency_list = [0] * (max(arr) + 1)

    for num in arr:
        frequency_list[num] += 1
    print(frequency_list)
    for num in arr:
        if frequency_list[num] == 1:
            return num

    return None


arr = [9, 4, 9, 6, 7, 4]
result = repeating_element(arr)
print(result)
