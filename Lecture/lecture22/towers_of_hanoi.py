# Towers of Hanoi Problem

def tower_solver(L_source, L_aux, L_dest):
    if n == 1:
        L_dest.append(L_source.pop())
    if n == 2:
        L_aux.append(L_source.pop())
        L_dest.append(L_source.pop())
        L_dest.append(L_aux.pop())

n = 3
L_source_orig = [n-i for i in range(n)]
L_aux_orig = []
L_dest_orig = []


def valid_moves(piece, towers):
    for tower in towers:
        for piece in tower:
            if min(tower) == piece:
                
            else: return None