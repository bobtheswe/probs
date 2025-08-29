def fn(nums):
    seen = {}
    for num in nums:
        seen[num] = True
    
    # [0,n] interval
    # need a +1 for python range(len()) functionality
    for i in range(len(nums) + 1):
        if i not in seen:
            return i
        
input = [3,0,1]
output = 2
print(fn(input) == output)

input = [0,1]
output = 2
print(fn(input) == output)

input = [9,6,4,2,3,5,7,0,1]
output = 8
print(fn(input) == output)
