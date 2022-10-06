from solve_puzzle import solve_puzzle as puzzle
import unittest

class TestSolvePuzzle(unittest.TestCase):
        def testClockwise(self):
                """Tests a board solveable using only CW moves"""

                # 2 0
                # 0 1

                self.assertEqual(puzzle([2,0,1,0]), True)

        def testCounterClockwise(self):
                """Tests a board solveable using only CCW moves"""

                # 2 0
                # 0 3

                self.assertEqual(puzzle([2,0,3,0]), True)

        def testMixed(self):
                """Tests a board solveable using only a combination of CW and CCW moves"""

                # 2 3
               # 0   1
                #  0

                self.assertEqual(puzzle([2,3,1,0,0]), True)

        
        def testUnsolveable(self):
                """Tests an unsolveable board"""

                # 2 0
                # 0 2
                #[2, 0, 2, 0]
                #Visited = {0, 2}
                #[1, 1, 1]
                #if 3 in visited: True
                self.assertEqual(puzzle([2,0,2,0]), False)

                # 2 0
               # 0   1
                #  0

                self.assertEqual(puzzle([2,0,1,0,0]), False)

unittest.main()