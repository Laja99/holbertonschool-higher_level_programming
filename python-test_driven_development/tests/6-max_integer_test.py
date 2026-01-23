#!/usr/bin/python3
"""Unittest for max_integer([..])
This module contains test cases for the max_integer function.
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Defines test cases for the max_integer function."""

    def test_max_at_end(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_at_beginning(self):
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_max_in_middle(self):
        self.assertEqual(max_integer([1, 4, 3, 2]), 4)

    def test_one_element(self):
        self.assertEqual(max_integer([7]), 7)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-5, -9, -3, -10]), -3)

    def test_mixed_signs(self):
        self.assertEqual(max_integer([-10, 0, 5, -2]), 5)

    def test_duplicate_max(self):
        self.assertEqual(max_integer([2, 3, 5, 5, 1]), 5)

    def test_floats(self):
        self.assertEqual(max_integer([1.5, 2.3, 0.9, 2.3]), 2.3)

    def test_strings(self):
        with self.assertRaises(TypeError):
            max_integer(["a", "b", 3])

    def test_string_list(self):
        self.assertEqual(max_integer(["apple", "banana", "pear"]), "pear")

    def test_none_argument(self):
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_no_argument(self):
        self.assertIsNone(max_integer())


if __name__ == '__main__':
    unittest.main()
