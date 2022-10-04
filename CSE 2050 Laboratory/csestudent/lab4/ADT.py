from LinkedList import LinkedList, Node # had to add Node to solve this

class Stack_L:
    def __init__(self):
        self._L = list()        # Composition: the Stack_L class has a List

    def push(self, number):
        self._L.insert(0, number) # Pushes number to front of list, not efficient
        return self._L

    def pop(self):
        return self._L.pop(0) # Removes and returns the first item of a stack

class Stack_LL:
    def __init__(self):
        self._LL = LinkedList() # Composition: the Stack_LL class has a Linked List

    def push(self, number):
        # If length of LL is 0, set head to new node with number
        # Else, set new_node to a node, set head to new_node.next
        # and set the head of self to new_node
        if self._LL._head == None:
            self._LL._head = Node(number)
        else: 
            head_node = Node(number)
            head_node.next = self._LL._head
            self._LL._head = head_node

        return self._LL

    def pop(self):
        if self._LL._head == None: raise RuntimeError("Cannot pop from empty list")
        value = self._LL._head.data
        self._LL._head = self._LL._head.next

        return value



class Queue_L:
    def __init__(self):
        self._head = 0
        self._L = list()

    def enqueue(self, value):
        self._L.append(value)

    def peek(self):
        return self._L[self._head]

    def dequeue(self):
        item = self.peek()
        self._head += 1
        return item

    def __len__(self):
        return len(self._L) - self._head

    def isempty(self):
        return len(self) == 0




class Queue_LL:
    def __init__(self):
        self._LL = LinkedList()
    
    def enqueue(self, item):
        self._LL.add_last(item)

    def dequeue(self):
        return self._LL.remove_first()

    def peek(self):
        item = self._LL.remove_first()
        self._LL.add_first(item)
        return item

    def __len__(self):
        return len(self._LL)

    def isempty(self):
        return len(self) == 0

if __name__ == '__main__':
    ##########Test Stack_L##########
    test_stack = Stack_L()
    test_stack.push(4)

    assert(test_stack._L == [4])

    test_stack = Stack_L().push(4)
    assert(test_stack.pop() == 4)

    ##########Test Stack_LL#########
    test_linkedlist = LinkedList()
    test_linkedlist.add_first(4)
    other_test = Stack_LL()
    empty_linkedlist = LinkedList()

    assert(Stack_LL().push(4) == test_linkedlist)

    ##########Test Queue_L##########
    test_queuelist = Queue_L()
    test_queuelist.enqueue(4)

    assert(test_queuelist._L == [4])
   

    ##########Test Queue_LL#########
    test_queueLL = Queue_LL()
    test_queueLL.enqueue(6)