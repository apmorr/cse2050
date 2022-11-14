class Entry:
    def __init__(self, item, priority):
        self.item = item
        self.prioritty = priority

    def __lt__(self, other):
        return self.priority < other.priority

    def __repr__(self):
        return f"Entry(item={self.item}, priority={self.priority})"

    
class PriorityQueue:
    def __init__(self):
        self._L = []
    def __len__(self):
        return len(self._L)
    
    def insert(self, item, priority):
        """Adds item w/ priority to priority queue"""
        self._L.append(Entry(item, priority))

    def remove_min(self):
        """Remove and return minimum priority item"""
        min_entry = min(self._L)
        self._L.remove(min_entry)
        return min_entry


if __name__ == '__main__':

    e1 = ('chapter 19', 5)
    e2 = ('vqs', 4)
    e3 = ('lab10', 2)
    e4 = ('hw9', 1)
    e5 = ('hw10', 3)
    e6 = ('final', 5)

    pq = PriorityQueue()
    for entry in [e1, e2, e3, e4, e5, e6]:
        pq.insert(item=entry[0], priority=entry[1])

    while pq:
        print(pq.remove_min())