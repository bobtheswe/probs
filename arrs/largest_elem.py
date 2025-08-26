# find largest elemnt of an array
def fn(input):
    l = 0
    for num in input:
        if num > l:
            l = num
    return l

input = [2,5,1,3,0]
output = 5
print(fn(input) == output)

input = [8,10,5,7,9]
output = 10
print(fn(input) == output)
