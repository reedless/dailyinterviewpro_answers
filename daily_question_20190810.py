'''
Given a list of numbers, find if there exists a pythagorean triplet in that list.
A pythagorean triplet is 3 variables a, b, c where a^2 + b^2 = c^2

Example:
Input: [3, 5, 12, 5, 13]
Output: True
Here, 5^2 + 12^2 = 13^2.
'''

def findPythagoreanTriplets(nums):
    squares = [num**2 for num in nums]
    sums = []

    for i in range(len(squares)):
        for j in range(i+1, len(squares)):
            sums.append(squares[i] + squares[j])

    for sum in sums:
        if sum in squares:
            return True
            
    return False
print (findPythagoreanTriplets([3, 12, 5, 13]))
# True

print (findPythagoreanTriplets([3, 12, 5]))
# False
