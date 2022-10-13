def is_sorted(L):
    """Checks that L is monotonically increasing"""
    return not any(L[i] > L[i+1] for i in range(len(L) - 1))

def print_list(L, tab=False):
    """prints out L using rows of '=' to visualize item size"""
    for idx, item in enumerate(L):
        if tab: print(f"idx:{idx}", "=" * item, f"{item}")

# Invariant - something that is always true at any point in an algorithm
# at the end of i outer loops, the i biggest items are in their final positions
# at the end of (n-1) outer loops, the (n-1) biggest items are in their final positions
# which means at the end of (n-1) outer loops, only 1 item has not been sorted

#adaptive - running time depends on the input asympotically

def bubble_sort(L): # Quadratic sorting algorithm
    n = len(L)
    for i in range(n-1):
        sorted_flag = True
        for j in range(n-1-i): # inner loop does most of the work
            if L[j] > L[j+1]: # checks if items are out of order
                sorted_flag = False
                L[j], L[j+1] = L[j+1], L[j] # two write operations, swaps positions

            if sorted_flag: return


def selection_sort(L):
    n = len(L)

    for i in range(n-1):
        # find the ith biggest item

        i_big = 0
        for j in range(1, n-i):
            if L[j] > L[i_big]:
                i_big = j

        L[j], L[i_big] = L[i_big], L[j]

        # swap it