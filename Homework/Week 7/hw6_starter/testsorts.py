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

print(left_sort([5,2,2,2,2,2,1]))
assert left_sort([5,2,2,2,2,2,1]) == [2,2,2,2,2,1,5]
assert right_sort([5,2,2,2,2,2,1]) == [1,5,2,2,2,2,2]


