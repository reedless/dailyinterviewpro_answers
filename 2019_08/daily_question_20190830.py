'''
Implement a queue class using two stacks.
A queue is a data structure that supports the FIFO protocol (First in = first out).
Your class should support the enqueue and dequeue methods like a standard queue.
'''

class Queue:
    def __init__(self):
        self.head = []
        self.stack = []

    def enqueue(self, val):
        self.stack.append(val)

    def dequeue(self):
        while (self.stack):
            elem = self.stack.pop()
            self.head.append(elem)

        result = self.head.pop()

        while (self.head):
            elem = self.head.pop()
            self.stack.append(elem)
            
        return result

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print (q.dequeue())
print (q.dequeue())
print (q.dequeue())
# 1 2 3
