# You are given an integer array nums where nums[i] represents the amount of money the ith house has. 
# The houses are arranged in a straight line, i.e. the ith house is the neighbor of the (i-1)th and (i+1)th house.

# You are planning to rob money from the houses, but you cannot rob two adjacent houses because the security system 
# will automatically alert the police if two adjacent houses were both broken into.

# Return the maximum amount of money you can rob without alerting the police.
def fn(nums):
    cache = {}
        
    def walk(idx, curr_sum = 0):
        key = (idx, curr_sum)
        if key in cache:
            return cache[key]
        if idx >= len(nums): #end of the line
            return curr_sum
        
        curr_sum += nums[idx] #must do something with index 0
        result = max(walk(idx + 2, curr_sum), walk(idx + 3, curr_sum))
        cache[key] = result
        return result

    return max(walk(0), walk(1))

input = [1,1,3,3]
output = 4
print(fn(input) == output)

input = [2,9,8,3,6]
output = 16
print(fn(input) == output)