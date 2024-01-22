def fun(heights, k):
    min_height = min(heights)
    max_height = max(heights)

    for i in range(len(heights)):
        if heights[i] - k >= min_height:
            heights[i] -= k
        elif heights[i] + k <= max_height:
            heights[i] += k


    new_min_height = min(heights)
    new_max_height = max(heights)


    return new_max_height - new_min_height

tower_heights = [1, 15, 10]
k_value = 6
result = fun(tower_heights, k_value)
print("The minimum difference after modifications:", result)