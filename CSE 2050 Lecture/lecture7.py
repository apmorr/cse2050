def is_sorted(L):
    """Returns a boolean representing if L is sorted"""
    n = len(L)
    return not any(L[i] > L[i + 1] for i in range(n-1))

def bubble_sort(L):
    """Sorts L using an inefficient bubble sort"""
    n = len(L)

    for i in range(n):
        for j in range(n-1):
            if L[j] > L[j+1]:
                L[j+1], L[j] = L[j], L[j+1] # Tuple unpacking
                # n^2 - n + 2 efficiency


if __name__ == "__main__":
    # Test is_sorted
    n = 500
    L = [i for i in range(n)]
    assert is_sorted(L)
    L[-1] = -1
    assert not is_sorted(L)

    bubble_sort(L)
    assert is_sorted(L)