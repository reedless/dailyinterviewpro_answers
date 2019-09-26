'''
You have a landscape, in which puddles can form.
You are given an array of non-negative integers representing the elevation at
each location. Return the amount of water that would accumulate if it rains.

For example: [0,1,0,2,1,0,1,3,2,1,2,1] should return 6 because 6 units of water can get trapped here.
       X
   X███XX█X
 X█XX█XXXXXX
# [0,1,0,2,1,0,1,3,2,1,2,1]
'''

def capacity(arr):
    acc = 0
    prev = 0
    sum = 0

    for num in arr:
        if (num <= prev):


print (capacity([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
# 6
