

def find(nums, target):
    seen = set()
    print(seen)
    for num in nums:
        complement = target - num
        if complement in seen:
            print("Pair found:", (complement, num))
        seen.add(num)
nums = []
target = int(input("Enter the target"))
n=int(input("Enter the number of elements:"))
for i in range(n):
    element=int(input("Enter the elements"))
    nums.append(element)
find(nums, target)
