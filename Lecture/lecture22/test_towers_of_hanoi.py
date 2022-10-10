from towers_of_hanoi import tower_solver, valid_moves
import unittest

class TowerTest(unittest.TestCase):
    def valid_move_test(self):
        '''Tests that we can find the valid next moves for a singular piece'''
        self.assertEqual(valid_moves(2, [1, 2, 3]), None) # Tests that if the piece is not a minimum value at its pole, there are no valid moves
        self.assertEqual(valid_moves(1, [1, 2, 3]), )