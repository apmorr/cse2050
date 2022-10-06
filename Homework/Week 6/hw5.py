import copy

def solveable(p_idxs, k_idx):
    """Returns True (false) if all pawn locations can be capture by sequential knight moves"""
    # 1) Base case - is the puzzle solved?

    if k_idx in p_idxs:
        p_idxs.remove(k_idx)
    
    if len(p_idxs) == 0: return True

    
    # 2) Find all valid_moves

    validMoves = valid_moves(k_idx)

    # 3) Try all valid_moves

    if len(validMoves) == 0: return False

    
    pawn_squares = set()
    for move in validMoves:
        for i in p_idxs:
            if move == i:
                pawn_squares.add(i)

    for pawn in pawn_squares:
        if solveable(p_idxs, pawn): return True

                # Create set with all moves that land on pawns
                # Recursively return solveable landing on each of those pawns

    # 4) If nothing worked in step 3, there's no solution with the knight in this position

    else: 
        p_idxs.add(k_idx)
        return False


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