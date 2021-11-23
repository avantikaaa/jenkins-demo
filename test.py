#!/usr/bin/python3

import unittest

from build import *

class Test(unittest.TestCase):
    def test_addition(self):
        data = [21, 3]
        expected = 24
        self.assertEqual(addition(data[0], data[1]), expected)

    def test_subtraction(self):
        data = [21, 3]
        expected = 18
        self.assertEqual(subtraction(data[0], data[1]), expected)

    def test_multiplication(self):
        data = [21, 3]
        expected = 63
        self.assertEqual(multiplication(data[0], data[1]), expected)

    def test_division(self):
        data = [21, 3]
        expected = 7
        self.assertAlmostEqual(division(data[0], data[1]), expected)

    def test_successor(self):
        data = 3
        expected = 4
        self.assertAlmostEqual(successor(data), expected)

if __name__ == '__main__':
    unittest.main()
