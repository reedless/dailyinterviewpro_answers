'''
You are given an array of k sorted singly linked lists.
Merge the linked lists into a single sorted linked list and return it.
'''

class Node(object):
  def __init__(self, val, next=None):
    self.val = val
    self.next = next

  def __str__(self):
    c = self
    answer = ""
    while c:
      answer += str(c.val) if c.val else ""
      c = c.next
    return answer

def merge(lists):
  while ()

a = Node(1, Node(3, Node(5)))
b = Node(2, Node(4, Node(6)))
print merge([a, b])
# 123456
