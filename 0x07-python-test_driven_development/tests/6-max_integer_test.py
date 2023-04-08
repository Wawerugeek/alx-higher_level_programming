#!/usr/bin/python3
"""a file with unittests for max_integer([]) function"""

import unittest
max_integer = __import__('6-max_integer').max_integer

"""we create a test case by accessing Testcase method"""
class TestMaxInteger(unittest.TestCase):
    def test_first_element(self):
        """Test the first one"""
        first = [40, 30, 20, 10]
        self.assertEqual(max_integer(first), 40)

    def test_last_max(self):
        """Test the last one"""
        last = [10, 10, 90, 100]
        self.assertEqual(max_integer(last), 100)

    def test_empty(self):
        """Test for an empty list passed"""
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_single(self):
        """looks for single element in the lis"""
        single = [2]
        self.assertEqual(max_integer(single), 2)
    def test_negative(self):
        """test for negative in list"""
        negative = [-4, -199, -23, -1]
        self.assertEqual(max_integer(negative), -1)
    def test_strings(self):
        """test when given a string"""
        strings = ["what", "happened"]
        self.assertEqual(max_integer(strings), 's')

    def test_floats(self):
        """tests for floats"""
        floats = [3, 7.8, 9.8 3, 5]
        self.assertEqual(max_integer(floats), 9.8)

if __name__ == '__main__':
    unittest.main()

