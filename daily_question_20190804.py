'''
Given a list of numbers, where every number shows up twice except for one number, find that one number.

Example:
Input: [4, 3, 2, 4, 1, 3, 2]
Output: 1

Challenge: Find a way to do this using O(1) memory.
'''

def singleNumber(nums):
    if (len(nums) == 1):
        return nums[0]
    else:
        first = nums[0]
        for i in range(1, len(nums)):
            if (nums[i] == first):
                nums.pop(i)
                nums.pop(0)
                return singleNumber(nums)

print(singleNumber([4, 3, 2, 4, 1, 3, 2]))
# 1
