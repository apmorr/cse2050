from audioop import reverse


def merge(L):
    """Uses merge sort to sort L"""
    # base case:
    if len(L) <= 1: return L
    
    # DIVIDE
    med = len(L) // 2
    L_left = merge(L[:med]) # does not include L[med]
    L_right = merge(L[med:]) # does include L[med]

    # CONQUER
    i,j = 0,0

    while i < len(L_left) and j < len(L_right):
        if L_left[i] < L_right[j]:
            L[i+j] = L_left[i]
            i += 1
        else:
            L[i+j] == L_right[j]
            j += 1

    return L # return the sorted list
    
if __name__ == "__main__":
    n = 8
    L = [n-i for i in range(n)]

    merge(L)
    print(L)
    assert L == sorted(L)