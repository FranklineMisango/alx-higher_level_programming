#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    Tests the max_integer file
    """
    def test_maxInteger(self):
        """Checks if the right value is returned"""
        self.assertAlmostEqual(max_integer([0, 1, 3, 5, 7]), 7)
        self.assertAlmostEqual(max_integer([0, 9, 7]), 9)
        self.assertAlmostEqual(max_integer([5, 0, 1, 3]), 5)
        self.assertAlmostEqual(max_integer([0, 10, 5, 7]), 10)
        self.assertAlmostEqual(max_integer([0, 10, -5, 7]), 10)
        self.assertAlmostEqual(max_integer([-10, -5, -7]), -5)
        self.assertAlmostEqual(max_integer([7]), 7)

    def test_type(self):
        """Checks that the right type is returned"""
        self.assertRaises(ValueError, max_integer, ["a", 1, "s"])

    def test_empty(self):
        """Checks the result of an empty string"""
        self.assertAlmostEqual(max_integer([]), None)
