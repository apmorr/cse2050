class Node:
    def __init__(self, _item, _next=None, _prev=None):
        self._item = _item
        self._next = _next
        self._prev = _prev

    def __repr__(self):
        p = self._prev._item if self._prev else None
        n = self._next._item if self._next else None
        return f"Node({self._item}, prv={p}, nxt={n})"


class DoublyLinkedList:
    def __init__(self):
        """Initializes empty DLL"""
        self._head = None
        self._tail = None
        self._len = 0

    def add_first(self, item):
        """Adds item to beginning of DLL"""
        new_node = Node(item, _next = self._head)
        if len(self) == 0:
            self._head = new_node
            self._tail = new_node
            return
        
        else: 
            self._head._prev = new_node # update old heads previous pointer
            self._head = new_node # update DLL._head

        self._len += 1

       
    def add_last(self, item):
        """Adds item to end of DLL"""
       
    def remove_first(self):
        """Removes and returns first item in DLL"""
        
    def remove_last(self):
        """Removes and returns last item in DLL"""
        # Edge case: empty DLL
        if len(self) == 0: raise RuntimeError("Cannot remove last from empty DLL")

        # Edge case: 1 item in DLL
        if len(self) == 1: 
            data = self._head._item
            self._head = None
            self._tail = None
            self._len -= 1
            return data
        
        # General case
        else:
            data = self._tail._item
            self._tail._prev._next = None # Update penultimate._next to None
            self._tail = self._tail._prev # Update self._tail to penultimate
            self._len -= 1 # reduce length
            return data

    def __len__(self):
        """Returns the number of nodes in the DLL"""
        return self._len

#n1 = Node('a')
#n2 = Node('b')
#n3 = Node('c')

#n1._next = n2

#n2._prev = n1
#n2._next = n3

#n3._prev = n2

# 'a' <-> 'b' <-> 'c'