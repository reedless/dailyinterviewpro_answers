'''
Given an array of n positive integers and a positive integer s,
find the minimal length of a contiguous subarray of which the sum ≥ s.
If there isn't one, return 0 instead.

Example:
Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.
'''

class Solution:
    def minSubArrayLen(self, nums, s):
        for i in range(len(nums)):
            for j in range(len(nums) - i):
                sum = 0
                for k in range(i+1):
                    sum += nums[j+k]
                if (sum >= s):
                    return i+1

        return 0

print (Solution().minSubArrayLen([2, 3, 1, 2, 4, 3], 7))
# 2
print (Solution().minSubArrayLen([2, 3, 1, 2, 2, 3], 7))
# 3
print (Solution().minSubArrayLen([1, 1, 1, 1, 1, 2], 7))
#6
print (Solution().minSubArrayLen([1, 1, 1, 1, 1, 1], 7))
# 0
