import unittest
from lecture4 import Student, Faculty

class TestStudent(unittest.TestCase):

    def setUp(self):
        self.s1 = Student('nick', 'nic21003')

    def test_init(self):
        # assert s1.name == 'nick'
        self.assertEqual(self.s1.get_name(), 'nick')
        self.assertEqual(self.s1.get_netid(), 'nic21003')

        # ensure that value is true: self.assertTrue()
        # self.assertAlmostEqual() for rounding errors

    def test_change_name(self):
        self.assertEqual(self.s1.get_name(), 'nick')
        self.s1.set_name('nicholas')
        self.assertEqual(self.s1.get_name(), 'nicholas')

    def test_add_course(self): pass

class TestFaculty(unittest.TestCase):
    def setUp(self):
        self.f1 = Faculty('nic21003', 'nick')

    def test_init(self):
        self.assertEqual(self.f1.name, 'nick')

    def test_(self): pass


unittest.main() # runs every method beginning with "Test"


# unittests can be better than assert statements because unittests do not show what the value of the failed assert is. 
# unittests tell you the value that caused the failed test.

# Use a single-leading underscore to set a private attribute. It suggests that you shouldn't modify the file outside of the class it's in.