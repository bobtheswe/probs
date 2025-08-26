def fn(nums):
    if len(nums) < 2:
        return (-1, -1)
    smallest = min(nums)
    largest = max(nums)

    second_smallest = 1000000000000
    second_largest = -1

    for num in nums:
        if num < second_smallest and num > smallest:
            second_smallest = num
        if num > second_largest and num < largest:
            second_largest = num

    return (second_smallest, second_largest)

input = [1,2,4,7,7,5]
output = (2, 5) #second smallest and second largest
print(fn(input) == output)

input = [1]
output = (-1, -1) #second smallest and second largest
print(fn(input) == output)

input = [1, 1, 2, 3]
output = (2, 2) #second smallest and second largest
print(fn(input) == output)

input = [5, 5, 10, 10]
output = (10, 5) #second smallest and second largest
print(fn([5, 5, 10, 10]) == output)