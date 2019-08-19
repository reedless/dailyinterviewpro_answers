'''
Given a sequence of numbers, find the longest sequence that contains only 2 unique numbers.

Example:
Input: [1, 3, 5, 3, 1, 3, 1, 5]
Output: 4
The longest sequence that contains just 2 unique numbers is [3, 1, 3, 1]
'''

def findSequence(seq):
    longest = 0
    unique_numbers = []
    longest_sequence = []
    for num in seq:
        if (num in unique_numbers):
            longest_sequence.append(num)
        else:
            if (len(unique_numbers) < 2):
                unique_numbers.append(num)
                longest_sequence.append(num)
            else:
                unique_numbers = [longest_sequence.pop(), num]
                longest_sequence = unique_numbers

        if (len(longest_sequence) > longest):
            longest = len(longest_sequence)

    return longest
print (findSequence([1, 3, 5, 3, 1, 3, 1, 5]))
# 4
