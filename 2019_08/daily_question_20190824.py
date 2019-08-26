'''
Given an array nums, write a function to move all 0's to the end of it while
maintaining the relative order of the non-zero elements.

Example:
Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
You must do this in-place without making a copy of the array.
Minimize the total number of operations.
'''

class Solution:
    def moveZeros(self, nums):
        last = len(nums) - 1
        i = 0
        while i <= last:
            if (nums[i] == 0):
                j = i
                while(j < last):
                    temp = nums[j]
                    nums[j] = nums[j+1]
                    nums[j+1] = temp
                    j += 1
                last -= 1
            else:
                i += 1
        print(nums)

nums = [0, 0, 0, 2, 0, 1, 3, 4, 0, 0]
Solution().moveZeros(nums)
# [2, 1, 3, 4, 0, 0, 0, 0, 0, 0]
