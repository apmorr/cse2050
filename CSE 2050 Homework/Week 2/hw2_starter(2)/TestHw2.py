# Start here. Once you have good test, move on to hw2.py

import unittest
from hw2 import Card, Deck, is_group
import random

class TestCard(unittest.TestCase):
    def test_init(self):
        """Tests that we can initialize cards w/ number/color/shading/shaper"""
        c1 = Card(2, "green", "striped", "diamond")

        self.assertEqual(c1.number, 2)
        self.assertEqual(c1.color, "green")
        self.assertEqual(c1.shading, "striped")
        self.assertEqual(c1.shape, "diamond")

    def test_str(self):
        """test that we can get a good string representation of GroupCard instances"""
        c1 = Card(2, "green", "striped", "diamond")

        self.assertEqual(str(c1), "Card(2, green, striped, diamond)")
        
    def test_eq(self):
            """Tests that two cards are equal iff all attributes (number, color, shading, shape) are equal"""
            c1 = Card(2, "green", "striped", "diamond")
            c2 = Card(3, "blue", "striped", "emerald")
            c3 = Card(2, "green", "striped", "diamond")
            
            self.assertEqual(c1, c3)


# Write your own docstrings for the tests below
class TestDeck(unittest.TestCase):
    def test_init(self):
        """Tests that we can initialize decks with one copy of each card"""
        d1 = Deck()
        self.assertEqual(len(d1), 81)

    def test_draw_top(self):
        """Tests that we can draw and reveal the top card in a deck"""
        d1 = Deck()
        c1 = Card(3, "purple", "solid", "oval")
        self.assertEqual(d1.draw_top(), c1)
        self.assertEqual(len(d1), 80)

    def test_shuffle(self):
        """Tests that we can shuffle the deck to randomize the order of the cards"""
        d1 = Deck()
        c1 = Card(1, "blue", "solid", "oval")
        c2 = Card(3, "blue", "solid", "squiggle")
        random.seed(1)
        d1.shuffle()

        self.assertEqual(d1.draw_top(), c1)
        random.seed(2)
        d1.shuffle()
        
        self.assertEqual(d1.draw_top(), c2)

# After Card and Deck are working, write and test the alg below.
# Include a docstring.
class TestSimulator(unittest.TestCase):
    def test_is_group(self):
        """Tests whether not a group of three cards is a valid group"""

        c1 = Card(3, "blue", "solid", "oval")
        c2 = Card(3, "blue", "solid", "oval")
        c3 = Card(3, "blue", "solid", "oval")
        c4 = Card(2, "orange", "striped", "squiggle")

        self.assertTrue(is_group(c1, c2, c3))
        self.assertFalse(is_group(c1, c2, c4))


unittest.main() # runs all unittests above