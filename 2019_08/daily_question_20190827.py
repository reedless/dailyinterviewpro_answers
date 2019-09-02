'''
You are given an array of integers. Return the largest product that
can be made by multiplying any 3 integers in the array.

Example:

[-4, -4, 2, 8] should return 128 as the largest product can be made by multiplying -4 * -4 * 8 = 128.

'''

def maximum_product_of_three(lst):
    lst.sort()
    cand1 = lst[0] * lst[1] * lst[-1]
    cand2 = lst[-3] * lst[-2] * lst[-1]
    if (cand1 > cand2):
        return cand1
    else:
        return cand2

print (maximum_product_of_three([-4, -4, 2, 8]))
# 128
