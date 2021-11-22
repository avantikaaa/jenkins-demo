#!/usr/bin/python3

import unittest

from build import *

class Test(unittest.TestCase):
    def test_addition(self):
        data = [5, 10]
        expected = 15
        self.assertEqual(addition(data[0], data[1]), expected)

    def test_subtraction(self):
        data = [5, 10]
        expected = -5
        self.assertEqual(subtraction(data[0], data[1]), expected)

    def test_multiplication(self):
        data = [5, 10]
        expected = 50
        self.assertEqual(multiplication(data[0], data[1]), expected)

    def test_division(self):
        data = [10, 2]
        expected = 5
        self.assertAlmostEqual(division(data[0], data[1]), expected)

if __name__ == '__main__':
    unittest.main()