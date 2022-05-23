#!/usr/bin/python3
import unittest
"""Unittest for max_integer([..])
"""

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    '''class to create the cases'''
    def test_max_integer(self):
        self.assertEqual(max_integer([1, 2, 3]), 3)
        self.assertEqual(max_integer([1, -1, -2]), 1)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([None]), None)
        self.assertEqual(max_integer([-1, -2, -64, -34]), -1)
        self.assertEqual(max_integer([3, 3, 3]), 3)
        self.assertEqual(max_integer([5]), 5)
        '''testing case when a variable named "x" is created and it has
        a value of 5 and it is inserted into the list'''
        x = 10
        self.assertEqual(max_integer([1, 2, 3, 10]), 10)
    
    if __name__ == "__main__":
        unittest.main()
