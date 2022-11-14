# Import what you need
from RecordsMap import *
import unittest
import random

# Include unittests here. Focus on readability, including comments and docstrings.

class TestLocalRecord(unittest.TestCase):
    def test_init(self):
        """Ensures we can create a localrecord with desired parameters"""
        r1 = LocalRecord((31.2045, -11.3107))
        self.assertEqual(r1.pos, (31.0, -11.0))
        self.assertEqual(r1.max, None)
        self.assertEqual(r1.min, None)

        r2 = LocalRecord((31.2045, -11.3107), max=60.22, min=29.5322, precision = 3)
        self.assertEqual(r2.pos, (31.204, -11.311))
        self.assertEqual(r2.max, 60.22)
        self.assertEqual(r2.min, 29.5322)

    def test_hash(self):
        """Ensures we receive correct hash"""
        r1 = LocalRecord((31.2045, -11.3107))

        h = hash((round(31.2045, 0), round(-11.3107, 0)))

        self.assertEqual(hash(r1), h)

    def test_eq(self):
        """Ensures localrecords can be compared"""
        r1 = LocalRecord((31.2045, -11.3107))
        r2 = LocalRecord((31.2045, -11.3107))
        r3 = LocalRecord((31.2045, -543.3453))
        self.assertEqual(r1, r2)
        self.assertNotEqual(r1, r3)

    def test_add_report(self):
        """Ensures we have the ability to add a report to localrecord properly adjusting min and max"""
        r1 = LocalRecord((31.2045, -11.3107))
        self.assertEqual(r1.max, None)
        self.assertEqual(r1.min, None)
        r1.add_report(50)
        self.assertEqual(r1.max, 50)
        self.assertEqual(r1.min, 50)
        r1.add_report(10)
        self.assertEqual(r1.max, 50)
        self.assertEqual(r1.min, 10)
        r1.add_report(45)
        self.assertEqual(r1.max, 50)
        self.assertEqual(r1.min, 10)


class TestRecordsMap(unittest.TestCase):
    def test_add_one_report(self):
        """Ensures functionality of RecordMap's len, get, contains, and add_report methods"""
        rm = RecordsMap()
        r1 = (13.4, -2.2)
        r2 = (15.6, -2.0)
        r3 = (16.7, -8.4)

        self.assertFalse(r1 in rm)
        rm.add_report(r1, 44)
        self.assertTrue(r1 in rm)
        self.assertFalse(r2 in rm)
        self.assertFalse(r3 in rm)

        self.assertEqual(len(rm), 1)

        self.assertEqual(rm[r1], (44, 44))

        with self.assertRaises(KeyError):
            rm[r3]

    def test_add_many_reports(self):
        """Ensures functionality of RecordMap's len, get, contains, and add_report methods for multiple reports"""
        rm = RecordsMap()
        r1 = (13.4, -2.2)
        r2 = (15.6, -2.0)
        r3 = (16.7, -8.4)
        r4 = (11, 11)
        r5 = (99, 99)

        self.assertFalse(r1 in rm)
        rm.add_report(r1, 99)
        self.assertTrue(r1 in rm)
        self.assertFalse(r2 in rm)
        self.assertFalse(r3 in rm)
        rm.add_report(r2, 11)
        rm.add_report(r3, 34)
        self.assertTrue(r2 in rm)
        self.assertTrue(r3 in rm)

        self.assertEqual(len(rm), 3)
        rm.add_report(r4, 674)
        self.assertEqual(len(rm), 4)

        self.assertEqual(rm[r1], (99, 99))
        self.assertEqual(rm[r2], (11, 11))
        self.assertEqual(rm[r3], (34, 34))
        self.assertEqual(rm[r4], (674, 674))
        self.assertNotEqual(rm[r4], (200, 199))
        self.assertNotEqual(rm[r4], (199, 200))

        with self.assertRaises(KeyError):
            rm[r5]


unittest.main()