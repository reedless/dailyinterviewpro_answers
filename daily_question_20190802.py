'''
Given a list of numbers with only 3 unique numbers (1, 2, 3), sort the list in O(n) time.
Challenge: Try sorting the list using constant space.

Example 1:
Input: [3, 3, 2, 1, 3, 2, 1]
Output: [1, 1, 2, 2, 3, 3, 3]
'''

def sortNums(nums):
    one_border = 0
    three_border = len(nums)-1

    i = 0
    while (i < three_border):
        num = nums[i]
        if (num == 1):
            if (i == one_border):
                one_border += 1
                i += 1
            else:
                a = nums[one_border]
                nums[one_border] = 1
                nums[i] = a

        elif (num == 2):
            i += 1

        else:
            b = nums[three_border]
            nums[three_border] = 3
            three_border -= 1
            nums[i] = b

    return nums

print(sortNums([3, 3, 2, 1, 3, 2, 1]))
# [1, 1, 2, 2, 3, 3, 3]
