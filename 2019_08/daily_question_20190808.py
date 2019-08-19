'''
Implement a class for a stack that supports all the regular functions (push, pop),
and an additional function of max() which returns the maximum element in the stack (return None if the stack is empty).
Each method should run in constant time.
'''

class MaxStack:
    def __init__(self):
        self.stack = []
        self.max_elems = [None]

    def push(self, val):
       self.stack.append(val)
       
       if (self.max_elems[-1] == None):
           self.max_elems.append(val)
       elif (val > self.max_elems[-1]):
           self.max_elems.append(val)

    def pop(self):
       elem = self.stack.pop()
       if (elem == self.max_elems[-1]):
           self.max_elems.pop()

    def max(self):
        return self.max_elems[-1]

s = MaxStack()

print (s.max())
# None
s.push(1)
s.push(2)
s.push(3)
s.push(2)
print (s.max())
# 3
s.pop()
s.pop()
print (s.max())
# 2
s.pop()
s.pop()
print (s.max())
# None
