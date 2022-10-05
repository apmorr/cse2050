def solveable(p_idxs, k_idx):
    """Returns True (false) if all pawn locations can be capture by sequential knight moves"""
    # 1) Base case - is the puzzle solved?
    
    if p_idxs is None: return True
    if p_idxs == {}: return True

    # 2) Find all valid_moves

    validMoves = valid_moves(k_idx)

    # 3) Try all valid_moves

    for move in validMoves:
        for i in p_idxs.copy():
            if move == i:
                p_idxs.remove(i)
                solveable(p_idxs, move)

    # 4) If nothing worked in step 3, there's no solution with the knight in this position

    else: return False


def valid_moves(k_idx):
    """Returns set of all valid moves from k_idx, assuming an 8x8 chess board"""
    possibleMoves = set()

    possibleMoves.add((k_idx[0]+2, k_idx[1]+1))
    possibleMoves.add((k_idx[0]+2, k_idx[1]-1))
    possibleMoves.add((k_idx[0]-2, k_idx[1]+1))
    possibleMoves.add((k_idx[0]-2, k_idx[1]-1))
    possibleMoves.add((k_idx[0]+1, k_idx[1]+2))
    possibleMoves.add((k_idx[0]+1, k_idx[1]-2))
    possibleMoves.add((k_idx[0]-1, k_idx[1]+2))
    possibleMoves.add((k_idx[0]-1, k_idx[1]-2))

    for move in possibleMoves.copy():
        if (move[0] > 7 or move[0] < 0 or move[1] > 7 or move[1] < 0):
            possibleMoves.remove(move)

    return possibleMoves