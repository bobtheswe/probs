def fn(nums):
    counts = []
    count = 0
    for num in nums:
        if num == 1:
            count += 1
        else:
            counts.append(count)
            count = 0
    counts.append(count)
    return max(counts)

input = [1,1,0,1,1,1]
output = 3
print(fn(input) == output)

input = [1,0,1,1,0,1]
output = 2
print(fn(input) == output)
