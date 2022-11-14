from time_f import time_f
from merge import merge
import random


def is_sorted(L): return all(L[i] <= L[i+1] for i in range(len(L)-1))

def quick(L):
    """Uses quicksort to sort L in-place"""
    return _quick(L, left=0, right=len(L))

def _quick(L, left, right):
    # base case: right-left <= 1
    if (right - left) <= 1:
        return
    

    # Options for picking a pivot
    #   1) Just pick the last item (very slow for sorted and reverse sorted lists)
    #   2) Pick the median of 3 items (first, median, last)
    #   3) Pick a random item for pivot

    # Partition around pivot
    i, j, pivot = left, (right - 2), (right - 1)

    # Pivot
    while i < j:
        while L[i] < L[pivot]: # scan to find first big item
            i += 1

        # (j>i) is evaluated every time
        #   (L[j] > L[pivot]) is only evaluated if j > i. avoids infinite loop
        # short circuits
        while j > i and L[j] >= L[pivot]: # scan to find first small item
            j -= 1

        #if L[i] > L[j]:
        if i < j:
            L[i], L[j] = L[j], L[i]

    if L[i] >= L[pivot]:
        L[pivot], L[i] = L[i], L[pivot]
        pivot = i

    # DIVIDE
    _quick(L, left=left, right=pivot)
    _quick(L, left=pivot+1, right=right)


if __name__ == '__main__':
    import random
    n = 100 
    L = [random.randint(0, 100) for i in range(n)]
    print(L)
    quick(L)
    print(L)
    assert is_sorted(L)


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