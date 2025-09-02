# You are given an integer array nums and an integer k, 
# return true if there are two distinct indices i and j in the array such that 
# nums[i] == nums[j] and abs(i - j) <= k, otherwise return false.
def fn(nums, k):
    w = {}
    L = 0 # window starts at the beginning
    for R in range(len(nums)):
        if abs(R-L) > k:
            w.pop(nums[L])
            L += 1 #should always keep L up to date
        if nums[R] in w:
            return True # we saw our element twice
        w[nums[R]] = True

    return False

input = [1,2,3,1]
k = 3
output = True
print(fn(input) == output)

input = [2,1,2]
k = 2
output = False
print(fn(input) == output)

input = [1,2,3,1,2,3]
k = 2
output = False
print(fn(input) == output)
