# TODO: implement the following 3 functions. Use docstrings, whitespace, and comments.

def cocktail_sort(L):
# Define two functions for left and right direction sorting
    def left_sort(L): # left to right
        n = len(L)
        for j in range(n-1):
            if L[j] > L[j+1]:
                L[j], L[j+1] = L[j+1], L[j]
        return L

    def right_sort(L): # right to left
        n = len(L)
        for j in range(n-1, 0, -1):
            if L[j] < L[j-1]:
                L[j], L[j-1] = L[j-1], L[j]
        return L

# After each direction, check if the list is sorted. If True, return the sorted list.
    loop = True
    direction = "Left"
    while loop:
        if sorted(L) == L: loop = False
        else:
            if direction == "Left":
                left_sort(L)
                direction = "Right"
            else:
                right_sort(L)
                direction = "Left"

    return L


# If false, continue doing steps until it is sorted.

def bs_sublist(L, left, right, item):
    midpoint = (left + right) // 2
    if item < L[left]:
        return left-1
    elif item > L[right]:
        return right
    elif L[midpoint] == item:
        return midpoint
    elif item < L[midpoint]:
        right = midpoint-1
        return bs_sublist(L, left, right, item)
    else:
        left = midpoint
        return left

# creates a binary search tree with a given list.
# left = values smaller than item
# right = values larger than item
# returns position

def opt_insertion_sort(L): pass
# use a binary search tree to reduce number of comparisons
# pos = bs_sublist(L, left, right, item) - must do this according to PDF
# must define bs_sublist() first in order to implement this function

def insertion_sort(L):
    """Naive insertion sort. Adaptive, but still slow."""
    n = len(L)
    for j in range(n): # go through every item
        for i in range(n - 1 - j, n - 1): # bubble it into a sorted sublist
            if L[i] > L[i+1]:                 # 1 comparison
                L[i], L[i+1] = L[i+1], L[i]   # 2 writes 
            else: break