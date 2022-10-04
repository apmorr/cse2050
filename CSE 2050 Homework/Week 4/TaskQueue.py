class Task(): # A task for the operating system to complete
    def __init__(self, id, cycles_left, next=None, prev=None):
        self.id = id
        self.cycles_left = cycles_left
        self.next = next
        self.prev = prev

    def __repr__(self):
        return f"Task(ID: {self.id}, Cycles: {self.cycles_left}, Next: {self.next})"

    def reduce_cycles(self, num):
        self.cycles_left -= num

class TaskQueue(): # Circular data structure
    def __init__(self, current = None, cycles_per_task = 1):
        self.current = current
        self.cycles_per_task = cycles_per_task
        self._len = 0

    def __len__(self):
        return self._len

    def is_empty(self):
        return (self._len == 0)

    def add_task(self, task):
        if self.is_empty():
            self.current = task
            self.current.prev = task
            self.current.next = task
            self._len += 1
        else:
            self.current.prev.next = task
            task.prev = self.current.prev
            task.next = self.current
            self.current.prev = task
            self._len += 1


    def remove_task(self, id):
        current_item = self.current

        if self._len == 0:
            raise RuntimeError(f"id {id} not in TaskQueue")

        i = 0
        while(i != self._len):
            if current_item.id == id:
                current_item.prev.next = current_item.next
                current_item.next.prev = current_item.prev
                if current_item == self.current:
                    if current_item == current_item.next:
                        self.current = None
                    else:
                        self.current = self.current.next
                self._len -= 1
                return
            else:
                current_item = current_item.next
                i += 1

        else:
            raise RuntimeError(f"id {id} not in TaskQueue")

        
    def execute_tasks(self):
        current = self.current
        inc = 0

        while (self.is_empty() == False):
            if current.cycles_left >= self.cycles_per_task:
                current.reduce_cycles(self.cycles_per_task)
                inc += self.cycles_per_task
            else:
                self.remove_task(current.id)
                inc += current.cycles_left
                print(f"Finished task {current.id} after {inc} clock cycles")
            
            current = current.next
        
        return inc
        


