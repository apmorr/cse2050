import time # time module, useful for accessing time functions such as current computer time

def time_f(func, arg, n_trials=10):
    start = time.time() # time before function runs
    for i in range(n_trials):
        func(arg)
    end = time.time() # time after function ends
    return (end-start) / n_trials # returns the time elapsed
    # Note: Minimum time is the best approximation for runtime


def sum_n(n):
    """Returns the sum of the first n positive integers"""
    total = 0 # 1
    for i in range(n): # n
        total += i + 1 # n + 1
    return total # 1
    # Total runtime: 2n+2

def sum_better(n):
    """a faster way to sum integers"""
    return n/2 * (n+1)

    
# {VariableToPrint:AlignmentWidth.DecimalPoints}

print("-" * 20)
print(f"{'n':10}{'time (ms)':10}{'t_better (ms)':10}")
print("-" * 20)
for n in [1000, 2000, 3000, 4000, 5000]:
    t = 1000*time_f(sum_n, n)
    print(f"{n:<10}\t{t:<10.3g}") # Specifies table whitespace size. the < indicates left-right

    if __name__ == "__main__":
        assert sum_n(1) == 1 # 1
        assert sum_n(2) == 3 # 1 + 2
        assert sum_n(3) == 6 # 1 + 2 + 3
        assert sum_n(4) == 10 # 1 + 2 + 3 + 4

        for i in range(1, 100):
            assert sum_n(i) == sum_better(i)


# print(time.time()) returns the time in seconds


