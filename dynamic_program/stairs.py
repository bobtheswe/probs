# You are given an integer n representing the number of steps to reach the top of a staircase. 
# You can climb with either 1 or 2 steps at a time.

# Return the number of distinct ways to climb to the top of the staircase.

def fn(n):
    cache = {}
    def walk(steps):
        if steps in cache:
            return cache[steps]
        if steps == 0:
            return 1
        if steps < 0:
            return 0 #invalid path

        cache[steps] = walk(steps - 2) + walk(steps - 1)
        return cache[steps]
    
    return walk(n)

input = 3
output = 3
print(fn(input) == output)

print(fn(5) == 8)