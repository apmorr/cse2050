class Stack_Wrapper:
    """Implements Stack ADT w/ List Wrapper"""
    def __init__(self):
        self._L = [] # composiiton: a stack *has a* list

    def push(self, item):
        self._L.insert(0, item) # O(n)
        # self._L.append(item) # O(1)

    def pop(self):
        return self._L.pop() # O(1)

    def __len__(self):
        return len(self._L)

class Queue_Wrapper:
    """Implements Queue ADT w/ List Wrapper"""
    def __init__(self):
        self._L = []

    def push(self, item):
        pass

    def pop(self):
        pass

    def __len__(self):
        return len(self._L)

class Deque_Wrapper:
    """Implements Deque ADT w/ List Wrapper"""
