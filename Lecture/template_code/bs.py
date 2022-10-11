from time_f import time_f

def bs(L, item):
    """returns True iff item in L using binary search"""
    # base case for empty list
    if len(L) == 0: return False
    i_med = len(L) // 2
    # find the median item
    # if that's what we are looking for - return True
    if L[i_med] == item: return True
    # if median item is less than item: search right
    elif L[i_med] < item: return bs(L[i_med+1:], item)
    # if medina item is greater than item: search left
    elif L[i_med] > item: return bs(L[:i_med], item)

    return False
   

if __name__ == '__main__':
    n = 10
    L = [i for i in range(n)]

    # test True
    for i in range(n):
        assert i in L
    
    # test False on either end of list
    assert not n in L
    assert not -1 in L

    # test false in middle of list
    for i in range(n):
        assert not (i+.5) in L

    print("tests pass!")

    # how long?
    #print(time_f(bs, (L, -1))*1000)
