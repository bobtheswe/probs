def fn(nums):
    return nums[1:] + [nums[0]]

input = [1,2,3,4,5]
output = [2,3,4,5,1]
print(fn(input) == output)

input = [3]
output = [3]
print(fn(input) == output)

