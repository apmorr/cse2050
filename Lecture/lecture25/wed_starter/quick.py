from time_f import time_f
from merge import merge


def is_sorted(L): return all(L[i] <= L[i+1] for i in range(len(L)-1))

def quick(L):
    """Uses quicksort to sort L in-place"""


if __name__ == '__main__':
    import random
    n =100 
    L = [random.randint(0, 100) for i in range(n)]


    """
    ##### Compare quicksort to mergesort #####
    for n in [1000, 2000, 3000, 4000]:
        L = [random.randint(0, n) for i in range(n)]

        t_quick = 1000*time_f(quick, L)
        t_merge = 1000*time_f(merge, L)
        
        print(f"n={n}")
        print(f"\tt_quick: {t_quick:.3f} ms")
        print(f"\tt_merge: {t_merge:.3f} ms")
    """