'''
You are given 2 integers n and m representing an n by m grid,
determine the number of ways you can get from the top-left to the bottom-right
of the matrix by going only right or down.

Example:
n = 2, m = 2

This should return 2, since the only possible routes are:
Right, down
Down, right.
'''

def num_ways(n, m):
    right = n-1
    down = m-1
    num = 1
    deno = 1

    for i in range(right, 0, -1):
        num = num * (i + down)
        deno = deno * i
    return int(num/deno)

print(num_ways(2, 2))
# 2
print(num_ways(3, 3))
# 6
