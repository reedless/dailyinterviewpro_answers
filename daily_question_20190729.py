'''
A palindrome is a sequence of characters that reads the same backwards and forwards.
Given a string, s, find the longest palindromic substring in s.

Note: Solution does not find longest palindrom, help pls
'''


class Solution:

    def isPalindrome(self, s):
        if (len(s) == 1):
            return True
        elif (len(s) == 2):
            return s[0] == s[1]
        else:
            return ((s[0] == s[-1]) and self.isPalindrome(s[1 : -1]))

    def longestPalindrome(self, s):
        current_index = 0
        while (current_index < len(s)/2):
            current_letter = s[current_index]
            for i in range(len(s), current_index + 1, -1):
                if (current_letter == s[i-1]):
                    candidate = s[current_index : i]
                    if (self.isPalindrome(candidate)):
                        return candidate
            current_index += 1
        return ""

# Test program
s = "tracecars"
print(str(Solution().longestPalindrome(s)))
# racecar
