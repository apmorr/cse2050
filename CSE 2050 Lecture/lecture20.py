# You should never have mutable arguments as your default function parameters.
# Instead:

class Stack:
    def __init__(self, items=None):
        if items is not None:
            self._L = items
        else:
            self._L = []

# Introduction to recursion

# Call stack is useful for debugging

def a():
    return b()

def b():
    return c()

def c():
    return 1

a()

def sum_k(k): # O(n), O(n) memory
    # Base case
    if k == 1: return 1
    return k + sum_k(k-1) # Call stack debugging: Every time this is ran, a new stack is shown

def sum_k_iter(k): # O(n), O(1) memory
    total = 0
    for i in range(k):
        total += (i + 1)

    return total

assert sum_k(1) == 1
assert sum_k(2) == 3
assert sum_k(3) == 6
assert sum_k(4) == 10
assert sum_k(5) == 15


# fib: 0, 1, 1, 2, 3, 5, 8, 13, 21
# fib(n)/fib(n-1) -> golden ratio ~1.6

counter = 0

def fib(k, solved=None):
    if solved is None: # Memoization (saving stuff we've already done)
        solved = set()
    
    global counter
    counter += 1

    if k in [0, 1]: return k

    if (k-1) in solved: # Boosts efficiency
        return solved[k-1]
    else:
        f1 = fib(k-2)

    if (k-2) in solved: # Boosts efficiency
        f2 = solved[k-2]
    else:
        f2 = fib(k-1)

    solved[k] = f1 + f2
    return solved[k]

fib(5)
print(counter)
assert fib(0) == 0
assert fib(1) == 1
assert fib(2) == 1
assert fib(5) == 5


# Recursive stack


# Numeric series examples



# Read book, watch VQs before Wednesday


