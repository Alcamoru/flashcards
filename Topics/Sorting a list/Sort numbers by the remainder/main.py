nums = [int(num) for num in list(input())]

# write your code here
nums.sort(key=lambda x: x % 3)
print(nums)
