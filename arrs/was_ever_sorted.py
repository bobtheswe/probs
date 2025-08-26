# was given array was ever sorted and rotated.
# could be improved, dont need to actually rotate array just need to count the breaks
# each "has been sorted array" only has 1 time there is a greater value
def fn(nums):
    i = 0
    breaks = 0
    while i < len(nums) - 1:
        if nums[i] > nums[i + 1]:
            breaks += 1
        i += 1
    if nums[-1] > nums[0]:
        breaks += 1
    return breaks < 2

input = [3,4,5,1,2]
output = True
print(fn(input) == output)

input = [2,1,3,4]
output = True
print(fn(input) == output)

input = [1,2,3]
output = True
print(fn(input) == output)