import unittest, random
from hw6 import cocktail_sort, opt_insertion_sort, bs_sublist

#TODO: implement unittests below. Use docstrings, whitespace, and comments.
# Hint 1 - start by defining a function that checks if a list is sorted
# Hint 2 - fix the random seed to make your bugs consistent (makes debugging easier)

class TestCocktailSort(unittest.TestCase):
   def test_Sorted(self):
      """Tests that a sorted list remains sorted"""
      self.assertEqual(cocktail_sort([0,1,2,3,4,5]), sorted([0,1,2,3,4,5]))

   def test_Reverse(self):
      """Tests that a reversed list can be cocktail sorted"""
      self.assertEqual(cocktail_sort([5,4,3,2,1,0]), sorted([5,4,3,2,1,0]))

   def test_Random(self):
      """Tests that a randomly generated list can be cocktail sorted"""
      randomList = []
      for i in range(5):
         x = random.randint(0,100)
         randomList.append(x)
      self.assertEqual(cocktail_sort(random.shuffle(randomList)), sorted(randomList))

   def test_ArbitrarySize(self):
      """Tests that lists of any length can be cocktail sorted"""
      listLength = random.randint(0,100)
      newList = [i for i in range(listLength)]
      random.shuffle(newList)
      self.assertEqual(cocktail_sort(newList), sorted(newList))

class TestOptInsertionSort(unittest.TestCase):
   def test_Sorted(self): 
      """Tests that a sorted list remains sorted"""
      self.assertEqual(opt_insertion_sort([0,1,2,3,4,5]), sorted([0,1,2,3,4,5]))

   def test_Reverse(self): 
      """Tests that a reversed list can be opt insertion sorted"""
      self.assertEqual(opt_insertion_sort([5,4,3,2,1,0]), sorted([5,4,3,2,1,0]))

   def test_Random(self):
      """Tests that a randomly generated list can be opt insertion sorted"""
      randomList = []
      for i in range(5):
         x = random.randint(0,100)
         randomList.append(x)
      self.assertEqual(opt_insertion_sort(random.shuffle(randomList)), sorted(randomList))

   def test_ArbitrarySize(self): 
      """Tests that lists of any length can be opt insertion sorted"""
      listLength = random.randint(0,100)
      newList = [i for i in range(listLength)]
      random.shuffle(newList)
      self.assertEqual(opt_insertion_sort(newList), sorted(newList))

# bs_sublist tests are provided for you.
class TestBinarySearchSublist(unittest.TestCase):
   def testExtremes(self):
      """Tests binary search on items less than min or greater than max of sublist"""
      #id:  0    1    2    3    4    5    6    7
      L = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
      #         |--------sorted sublist---------|
      self.assertEqual(bs_sublist(L, left=1, right=7, item='a'), 0)

      #id:  0    1    2    3    4    5    6    7
      L = ['i', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
      #         |--------sorted sublist---------|
      self.assertEqual(bs_sublist(L, left=1, right=7, item='i'), 7)

   def testWithinUnique(self):
      """Tests binary search on items within the bounds of a sublist, but does not appear in that sublist"""
      #id:  0    1    2    3    4    5    6    7
      L = ['?', 'a', 'c', 'e', 'g', 'i', 'k', 'm']
      #         |--------sorted sublist---------|
      for i, char in enumerate('bdfhjl'):
         L[0] = char
         self.assertEqual(bs_sublist(L, left=1, right=7, item=char), 1+i)

   def testWithinDuplicate(self):
      """Tests binary search on item within the bounds of a sublist, that do appear in that sublist. Should return the minimum index."""
      #id:  0    1    2    3    4    5    6    7
      L = ['?', 'a', 'b', 'c', 'd', 'e', 'f', 'g']
      #         |--------sorted sublist---------|

      for i, char in enumerate('abcdefgh'):
         self.assertEqual(bs_sublist(L, left=1, right=7, item=char), i)

   def testArbitrarySize(self):
      """Tests binary search on sublists of arbitrary size"""
      lower = 'abcdefghijklmnopqrstuvwxyz'

      for n in range(2, 27):
         L = [lower[i] for i in range(n)]
         self.assertEqual(bs_sublist(L, left=1, right=n-1, item='a'), 0)      # ['a', 'b', ...] returns 0

         for i, char in enumerate(lower[1:n]):
            L[0] = char
            self.assertEqual(bs_sublist(L, left=1, right=n-1, item=char), i)  # ['?', b', ...] returns i

      # n = 2
      # id:  0    1    2    3    4    5    6    7
      # L = ['a', 'b',]   # pos = 0
      # L = ['b', 'b',]   # pos = 0
      # L = ['c', 'b',]   # pos = 1
      #           |--------sorted sublist---------|
      # n = 3
      # L = ['a', 'b', 'c']  # pos = 0
      # L = ['b', 'b', 'c']  # pos = 0
      # L = ['c', 'b', 'c']  # pos = 1
      # L = ['d', 'b', 'c']  # pos = 2

      # n = 4
      # L = ['a', 'b', 'c', 'd']   # pos = 0
      # L = ['b', 'b', 'c', 'd']   # pos = 0
      # L = ['c', 'b', 'c', 'd']   # pos = 1
      # L = ['d', 'b', 'c', 'd']   # pos = 2
      # L = ['e', 'b', 'c', 'd']   # pos = 3

      # n = 5
      # L = ['a', 'b', 'c', 'd', 'e']   # pos = 0
      # L = ['b', 'b', 'c', 'd', 'e']   # pos = 0
      # L = ['c', 'b', 'c', 'd', 'e']   # pos = 1
      # L = ['d', 'b', 'c', 'd', 'e']   # pos = 2
      # L = ['e', 'b', 'c', 'd', 'e']   # pos = 3
      # L = ['f', 'b', 'c', 'd', 'e']   # pos = 4

unittest.main()