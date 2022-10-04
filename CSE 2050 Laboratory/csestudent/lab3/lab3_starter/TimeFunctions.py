import time

def time_function(func, args, n_trials=10):
    """Returns the number of seconds to run func with args"""
    best_time = float('inf')
    for i in range(n_trials):
        start = time.time()
        func(args)
        end = time.time()
        if (end - start) < best_time:
            best_time = (end - start)

    return best_time

    
def time_function_flexible(f, args, n_trials=10):
    """Operates the same as time_function, but uses tuple unpacking to take multiple parameters"""
    best_time = float('inf')
    for i in range(n_trials):
        start = time.time()
        f(*args) # unpacks args into separate arguments
        end = time.time()
        if (end - start) < best_time:
            best_time = (end - start)

    return best_time

if __name__ == '__main__':
    # Some tests to see if time_function works
    def test_func(L):
        for item in L:
            item *= 2

    L1 = [i for i in range(10**5)]
    t1 = time_function(test_func, L1)

    L2 = [i for i in range(10**6)] # should be 10x slower to operate on every item
    t2 = time_function(test_func, L2)

    print("t(L1) = {:.3g} ms".format(t1*1000))
    print("t(L2) = {:.3g} ms".format(t2*1000))