def fn(arr, k, threshold):
    curr_sum = 0
    L = 0 # start at beginning
    s = 0

    for R in range(len(arr)):
        if R - L + 1 > k:
            curr_sum -= arr[L]
            L += 1 
        # # add new to sum
        curr_sum += arr[R]
        curr_avg = curr_sum/k

        if R - L + 1 == k: 
            if curr_avg >= threshold:
                s += 1

    return s

input = [2,2,2,2,5,5,5,8], k = 3, threshold = 4
output = 3
print(fn(input) == output)

input = [11,13,17,23,29,31,7,5,2,3], k = 3, threshold = 5
output = 6
print(fn(input) == output)
