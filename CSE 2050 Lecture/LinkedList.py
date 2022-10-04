# Linked List
# Ordered Collection of nodes
# Nodes are non-sequential in memory
# Each node stores an item, and the location of the next node

# O(1) to add to beginning and add to end
# Expensive to remove from the end
# Better behavior than typical list in general
# Sequential lists can remove from middle of list easier than linked lists

# Add to both ends instantaneously, struggles for items in the middle
# If a pointer goes to None, that's the end of the linked list
# If the head of the list is empty, it goes to None

class Node:
    def __init__(self, item, _next=None):
        self.item = item
        self._next = _next

    def __repr__(self): # Shows Python how to print an object
        return f"Node({self.item}, {self._next})"


class LinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._len = 0

    def add_first(self, item):
        new_node = Node(item, self._head)
        self._head = new_node
    
        if len(self) == 0: # Edge case
            self._tail = new_node

        self._len += 1 # You have to manually keep track of length
        
    def remove_last(self):
        if len(self) == 0:
            raise RuntimeError("Cannot remove last from empty linked list")

        to_return = self._tail.item

        if len(self) == 1:
            self._head = None
            self._tail = None
            self._len -= 1
            return to_return

        penultimate = self._head

        # when I have one node, penultimate._next = None
        # so penultimate._next._next is equivalent to None._next
        while penultimate._next._next is not None: # Checks where the penultimate of the linked list is
            penultimate = penultimate._next

        penultimate._next = None

        self._tail = penultimate

        self._len -= 1

        return to_return

    def __len__(self):
        return self._len


        

if __name__ == '__main__':
    pass
    # test cases here
    n1 = Node(3, None) # Click to make a breakpoint at the side, with red dot
    n2 = Node("hello", n1) # Breakpoints show useful information, stops execution at each breakpoint
    n3 = Node([1, 2, 3], n2)
    print()

    # [1, 2, 3] -> "hello" -> 3 -> None

    # Test linked list
    ll = LinkedList()
    n = 5
    for i in range(n):
        ll.add_first(i)

    # 0
    # 1 -> 0
    # 2 -> 1 -> 0
    # 3 -> 2 -> 1 -> 0
    # ...

    for i in range(n):
        assert ll.remove_last() == i

    try:
        ll.remove_last()

    except RuntimeError:
        pass
        # missed this

# In run and debug mode, you can see local and global variables at the left side.
# Step into: Shows what happens when you create the node, one line at a time
