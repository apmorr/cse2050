from hw5 import solveable, valid_moves
import unittest

class TestValidMoves(unittest.TestCase):
        def testValidMoves(self):
                """Tests that valid_moves returns correct positions"""
                # 'k' denotes a knight
                # 'x' denotes possible moves
                # Positions should be given in (row, column) tuples
                #  0 1 2 3 4 5 6 7
                #0 - - - - - - - -
                #1 - - - - - - - -
                #2 - - - - - - - -
                #3 - - - - - - - -
                #4 - - - - - - - -
                #5 - x - - - - - -
                #6 - - x - - - - -
                #7 k - - - - - - -
                # TODO: Fill in the data to test valid_moves on the board above

                k_idx = (7,0)
                expected_valid_moves = 2
                self.assertEqual(len(valid_moves(k_idx)), expected_valid_moves)

                # TODO: Write tests for valid_moves for the following boards
                #  0 1 2 3 4 5 6 7
                #0 k - - - - - - -
                #1 - - x - - - - -
                #2 - x - - - - - -
                #3 - - - - - - - -
                #4 - - - - - - - -
                #5 - - - - - - - -
                #6 - - - - - - - -
                #7 - - - - - - - -

                k_idx = (0,0)
                expected_valid_moves = 2
                self.assertEqual(len(valid_moves(k_idx)), expected_valid_moves)
                

                #  0 1 2 3 4 5 6 7
                #0 - - - - - - - k
                #1 - - - - - x - -
                #2 - - - - - - x -
                #3 - - - - - - - -
                #4 - - - - - - - -
                #5 - - - - - - - -
                #6 - - - - - - - -
                #7 - - - - - - - -

                k_idx = (0,7)
                expected_valid_moves = 2
                self.assertEqual(len(valid_moves(k_idx)), expected_valid_moves)
                

                #  0 1 2 3 4 5 6 7
                #0 - - - - - - - -
                #1 - - - - - - - -
                #2 - - - - - - - -
                #3 - - - - - - - -
                #4 - - - - - - - -
                #5 - - - - - - x -
                #6 - - - - - x - -
                #7 - - - - - - - k

                k_idx = (7,7)
                expected_valid_moves = 2
                self.assertEqual(len(valid_moves(k_idx)), expected_valid_moves)

                #  0 1 2 3 4 5 6 7
                #0 - - - - - - - -
                #1 - - x - x - - -
                #2 - x - - - x - -
                #3 - - - k - - - -
                #4 - x - - - x - -
                #5 - - x - x - - -
                #6 - - - - - - - -
                #7 - - - - - - - -

                k_idx = (3,3)
                expected_valid_moves = 8
                self.assertEqual(len(valid_moves(k_idx)), expected_valid_moves)
 

class TestSolveable(unittest.TestCase):
        def testUnsolveable(self):
                """Test a few unsolveable puzzles"""

                #  0 1 2 3 4 5 6 7
                #0 - - - - - - - -
                #1 - - p - p - - -
                #2 - p - - - p - -
                #3 - - - k - - - -
                #4 - p - - - p - -
                #5 - - p - p - - -
                #6 - - - - - - - -
                #7 - - - - - - - -

                self.assertEqual(solveable({(1,2), (2,1), (4,1), (5,2), (1,4), (2,5), (4,5), (5,4)}, (3,3)), False)

                # #  0 1 2 3 4 5 6 7
                # #0 - - - - - - - -
                # #1 - - - - - - - -
                # #2 - - - - - - - -
                # #3 - - - - - - - -
                # #4 - - - - - - - -
                # #5 - - - - - - p -
                # #6 - - - - - p - -
                # #7 - - - - - - - k

                self.assertEqual(solveable({(6,5), (5,6)}, (7,7)), False)

                # #  0 1 2 3 4 5 6 7
                # #0 - - - - - - - -
                # #1 - - - - - - - p
                # #2 - - - - - - - -
                # #3 - - - - - - - -
                # #4 - - - - - - - -
                # #5 - - - - - - - -
                # #6 - - - - - - - -
                # #7 k - - - - - - -

                self.assertEqual(solveable({(1,7)}, (7,0)), False)


        def testSolveableSimple(self):
                """Test a simple solveable puzzle"""

                #  0 1 2 3 4 5 6 7
                #0 - - - - - - - -
                #1 - - - - - - - -
                #2 - - - - - - - -
                #3 - - - - - - - -
                #4 - - - - - - - -
                #5 - - - - - - - -
                #6 - - - - - - - -
                #7 k - - - - - - -

                self.assertEqual(solveable({}, (7, 0)), True)

                #  0 1 2 3 4 5 6 7
                #0 - - - - - - - -
                #1 - - - - - - - -
                #2 - - - - - - - -
                #3 - - - - - - - -
                #4 - - - - - - - -
                #5 - p - - - - - -
                #6 - - - - - - - -
                #7 k - - - - - - -

                self.assertEqual(solveable({(5,1)}, (7,0)), True) # 1

                #  0 1 2 3 4 5 6 7
                #0 p - - - - - - -
                #1 - - p - - - - -
                #2 - k - - - - - -
                #3 - - - - - - - -
                #4 - - - - - - - -
                #5 - - - - - - - -
                #6 - - - - - - - -
                #7 - - - - - - - -

                self.assertEqual(solveable({(0,0), (1,2)}, (2,1)), True)
        

        def testSolveableHard(self):
                """Test a few more complex solveable puzzles - try to break your recursive algorithm to help you catch any mistakes"""

                #  0 1 2 3 4 5 6 7
                #0 - - p - - - - -
                #1 - - - - p - - -
                #2 - - - - - - p -
                #3 - - - k - - - -
                #4 - - - - - p - -
                #5 - - p - - - - -
                #6 - - - - p - - -
                #7 - - - - - - - -

                # self.assertEqual(solveable({(0,2), (1,4), (2,6), (4,5), (5,2), (6,4)}, (3,3)), True) # 2
                
                #  0 1 2 3 4 5 6 7
                #0 - - - - - - - -
                #1 - - - - - - - -
                #2 - - - - - - - -
                #3 - - - - - - - -
                #4 - - - - - - - -
                #5 p p p p - - - -
                #6 - p p - - - - -
                #7 k p p p - - - -

                # self.assertEqual(solveable({(5,0), (5,1), (5,2), (5,3), (6,1), (6,2), (7,1), (7,2), (7,3)}, (7,0)), True)



unittest.main()