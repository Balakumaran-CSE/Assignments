def max_difference(arr):

    min_element = arr[0]
    max_difference = arr[1] - arr[0]
    
    for num in arr:
        if num - min_element > max_difference:
            max_difference = num - min_element


        if num < min_element:
            min_element = num

    return max_difference


arr = [2, 7, 9, 5, 1, 3, 5 ]
result = max_difference(arr)
print("The maximum difference is",result)