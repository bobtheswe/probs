def fn(nums):
        i = 0
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
        return i + 1


input = [1,1,2]
output = 2
print(fn(input) == output)

input = [0,0,1,1,1,2,2,3,3,4]
output = 5
print(fn(input) == output)
