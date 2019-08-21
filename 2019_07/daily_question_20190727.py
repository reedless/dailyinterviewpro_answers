'''
You are given two linked-lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

Example:
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''

# Definition for singly-linked list.
class ListNode(object):
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution:
    def addHelper(self, l1, l2):
        sum = l1.val + l2.val
        if (sum > 9):
            if (l1.next):
                l1.next.val += 1
            elif (l2.next):
                l2.next.val += 1
            else:
                l1.next = ListNode(1)
            return (sum - 10)
        return sum

    def addTwoNumbers(self, l1, l2):
        if (not l1) and (not l2):
            return None
        elif not l1:
            return l2
        elif not l2:
            return l1
        else:
            node = ListNode(self.addHelper(l1, l2))
            node.next = self.addTwoNumbers(l1.next, l2.next)
            return node


l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)
l1.next.next.next = ListNode(5)
l1.next.next.next.next = ListNode(1)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

result = Solution().addTwoNumbers(l1, l2)
while result:
  print (result.val),
  result = result.next
# 7 0 8 5 1
