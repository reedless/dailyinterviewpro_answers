'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
- Open brackets are closed by the same type of brackets.
- Open brackets are closed in the correct order.
- Note that an empty string is also considered valid.

Input: "((()))"
Output: True

Input: "[()]{}"
Output: True

Input: "({[)]"
Output: False
'''

class Solution:
  def isValid(self, s):
    stack = []
    for c in s:
        #small optimisation
        if len(stack) > len(s)/2:
            return False

        if c in ['(', '[', '{']:
            stack.append(c)
        elif c == ')':
            if stack.pop() != '(':
                return False
        elif c == ']':
            if stack.pop() != '[':
                return False
        elif c == '}':
            if stack.pop() != '{':
                return False
        #invalid character if reached here
        else:
            return False

    return stack == []

# Test Program
s = "()(){(())"
# should return False
print(Solution().isValid(s))

s = ""
# should return True
print(Solution().isValid(s))

s = "([{}])()"
# should return True
print(Solution().isValid(s))
