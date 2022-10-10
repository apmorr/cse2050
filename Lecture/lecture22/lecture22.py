def sum_k_recr(k): # Recursive sum algorithm
    if k == 1: return k
    return k + sum_k_recr(k-1)


def sum_k_iter(k): # Iterative sum algorithm
    total = 0
    for i in range(k):
        total+=i+1
    return total

