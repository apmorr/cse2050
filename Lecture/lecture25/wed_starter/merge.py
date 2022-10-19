def is_sorted(L): return all(L[i] <= L[i+1] for i in range(len(L)-1))

def merge(L):
    """Uses merge sort to sort L"""
    
    # base case - trivially sorted
    if len(L) <= 1: return L

    # DIVIDE
    med = len(L) // 2

    L_left = merge(L[:med]) # does not include L[med]
    L_right = merge(L[med:])    # includes L[med]

    # CONQUER : L_left and L_right are sorted

    i, j = 0, 0

    while i < len(L_left) and j < len(L_right):

        if L_left[i] < L_right[j]:
            L[i+j] = L_left[i]
            i += 1

        else:
            L[i+j] = L_right[j]
            j += 1

    L[i+j:] = L_left[i:] + L_right[j:]

    return L 
    

    

if __name__ == '__main__':
    import random
    n = int(1E6) 
    L = [random.randint(0, 100) for i in range(n)]

    #assert not is_sorted(L)
    merge(L)
    assert is_sorted(L) 
    # sorted, reverse sorted, random all take ~same time
