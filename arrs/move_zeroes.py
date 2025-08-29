def fn(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    # two pointer
    first = 0
    second = 1
    while first < len(nums):
        if second > len(nums) - 1:
            break
        if nums[first] == 0:
            nums[second], nums[first] = nums[first], nums[second] 
            second += 1
            continue
        first += 1
        # second should always be kept ahead of first
        if first == second:
            second += 1
    return nums

input = [0,1,0,3,12]
output = [1,3,12,0,0]
print(fn(input) == output)

input = [0,1,0,3,0]
output = [1,3,0,0,0]
print(fn(input) == output)