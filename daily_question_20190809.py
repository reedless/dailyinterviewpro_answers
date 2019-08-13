'''
You are given a positive integer N which represents the number of steps in a staircase.
You can either climb 1 or 2 steps at a time. Write a function that returns the number of unique ways to climb the stairs.
'''
import operator as op
from functools import reduce

def ncr(n, r):
    if (r == 0):
        return 1
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return (numer // denom)

def staircase(n):
    k = 0
    sum = 0
    while (k < n):
        sum += ncr(n, k)
        k += 1
        n -= 1
    return sum

print (staircase(4))
# 5
print (staircase(5))
# 8
