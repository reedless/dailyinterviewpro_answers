'''
Input: A = [1,3,3,5,7,8,9,9,9,15], target = 9
Output: [6,8]

Input: A = [100, 150, 150, 153], target = 150
Output: [1,2]

Input: A = [1,2,3,4,5,6,10], target = 9
Output: [-1, -1]
'''

class Solution:
    def getRange(self, arr, target):
        found = False
        first = 0
        last = 0

        for num in arr:
            if (num < target):
                first += 1
                last += 1
            elif (num == target):
                found = True
                last += 1

        if (found):
            return [first, last - 1]

        return [-1, -1]


    '''
    i = 0
    c = 0
    last = 0

    while (c < target and i < len(arr)):
        c = arr[i]
        i += 1

    i += 1
    first = i
    if (first >= len(arr)):
        return [-1, -1]

    c = arr[i]
    while (c == target and i < len(arr)):
        last = i

    return [first, last]
    '''

# Test program
arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8]
x = 2
print(Solution().getRange(arr, x))
# [1, 4]
