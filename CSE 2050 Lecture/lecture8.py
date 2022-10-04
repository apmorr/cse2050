# Abstract Data Type (ADT)
# Tells users what they can do with an object but it does not specify how it is done.

# Stack ADT
# Operations: 
# push(item) - adds item to top of stack
# pop() - removes and returns the top item of a stack
# s = Stack()
# s.push("apple")
# s.push([1, 2, 3])
# last in, first out

from LinearADTs import Stack_Wrapper, Queue_Wrapper, Deque_Wrapper
import unittest

class TestStackWrapper(unittest.TestCase):
    def test_init(self):
        S = Stack_Wrapper()
        self.assertEqual(len(S), 0)
    
    def test_push_pop(self):
        S = Stack_Wrapper()
        n = 10
        for i in range(n):
            S.push(i)

        for i in range(n):
            self.assertEqual(S.pop(), n-1-i)

class TestQueueWrapper(unittest.TestCase):
    def test_init(self):
        Q = Queue_Wrapper()
        self.assertEqual(len(Q), 0)
    
    def test_push_pop(self):
        Q = Queue_Wrapper()
        n = 10
        for i in range(n):
            self.assertEqual(len(Q), n-i)
            Q.enqueue(i)

        for i in range(n):
            self.assertEqual(Q.dequeue(), n-1-i)


# Queue
# First in, first out
# enqueue: adds item to queue
# dequeue: removes and returns first item in queue
# q = Queue()
# q.enqueue(1)
# q.enqueue("apple")
# q.enqueue([1, 2, 3])
# 1-apple-[1,2,3]
# q.dequeue()
# apple-[1,2,3]



# Linked Lists
# Each item contains a node, a node points to the next item
# String nodes together
# Attributes:
# Keep track of head (pointer to first node)
# Keep track of length (num. of nodes in list)
# Each node object needs to keep track of the item in it, and the next item it points to
# add_first()
# add_last()
# remove_first() # must be coded in
# remove_last() # must be coded in

# Big dick energy