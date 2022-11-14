##### TODO 1 #####
def price_to_profit(L):
    profit_list = [0]
    n = len(L)
    for i in range(0, n):
        if i == (n - 1):
            return profit_list
        
        difference = L[i+1] - L[i]
        profit_list.append(difference)
    

# brute force solution
def max_profit_brute(L):
    """Finds maximum profit. Assumes L is a list of profits (i.e. change in price every day), not raw prices"""
    n = len(L)
    max_sum = 0 # assume we can at least break even - buy and sell on the same day

    # outer loop finds the max profit for each buy day
    for i in range(n):
       # total profit if we bought on day i and sold on day j
        total = L[i]
        if total > max_sum: max_sum = total
        
        for j in range(i+1, n): 
            total += L[j] # total profit if we sell on day j
                          # we assume L[j] is the profit if we bought on day j-1 and sold on day j
                          # i.e., L is the change in value each day, relative to the day before
            if total > max_sum: max_sum = total

    return max_sum


##### TODO 2 #####
# you'll need a helper function or default parameters here
def max_profit(L, left=0, right=None):  # O(nlogn)
    """A faster method of finding the maximum profit possible via divide and conquer. Takes a list of profits."""
    if left == right:
        return L[right]
    if right is None:
        right = (len(L) - 1)
    median = ((left + right) // 2)

    p1 = max_profit(L, left, median)
    p2 = max_profit(L, (median + 1), right)
    p3 = max_profit_crossing(L, left, right, median)

    if (p1 > p2) and (p1 > p3):
        return p1
    elif (p1 < p2) and (p2 > p3):
        return p2
    else:
        return p3


##### TODO 3 #####
def max_profit_crossing(L, left, right, median):
    """Finds the maximum profit possible given we wait more than a day after we sell."""
   # O(n): Max profit if we sell on the median?
    pa = 0
    temp = 0
    for i in range(median, left, -1):
        temp += L[i]
        if (temp > pa): pa = temp
        
   # O(n): Max profit if we buy on the median?
    pb = 0
    temp = 0
    for i in L[(median + 1):(right + 1)]:
        temp += i
        if (temp > pb): pb = temp

   # O(1): Max profit if we buy before and sell after?
    pc = (pa + pb)
    if (pc > pa) and (pc > pb): return pc
    elif (pa > pb) and (pa > pb): return pa
    else: return pb