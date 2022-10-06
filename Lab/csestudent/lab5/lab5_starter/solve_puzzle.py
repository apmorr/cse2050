def solve_puzzle(L, visited=None, pos=0): # Make sure to add input parameters here
    """Returns True(False) if a given board is (is not) solveable"""

    if visited is None: # initialize
        visited = set() # Memoization, indexes of list

    


    if pos < 0:
        pos += len(L)
    else:
        pos = pos % len(L)

    if pos in visited:
        return False

    visited.add(pos)

    if (len(L) - 1 in visited):
        return True

    if L[pos] == 0: return False

    return solve_puzzle(L, visited, pos + L[pos]) or solve_puzzle(L, visited, pos - L[pos])