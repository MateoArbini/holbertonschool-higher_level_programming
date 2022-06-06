#!/usr/bin/python3
'''
Unittest for square class
'''


import unittest
import json
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class test_Square(unittest.TestCase):
    '''class'''
    def test_square_attributes(self):
        '''testing attributes'''
        with self.assertRaises(TypeError):
            test1 = Square("Holberton")

        with self.assertRaises(TypeError):
            test1 = Square()

        with self.assertRaises(TypeError):
            test1 = Square(4.5)

        with self.assertRaises(ValueError):
            test1 = Square(-10)

        with self.assertRaises(TypeError):
            test1 = Square([2, 3])

        with self.assertRaises(ValueError):
            test1 = Square(0)

        with self.assertRaises(TypeError):
            test1 = Square((4, 5))

        with self.assertRaises(TypeError):
            test1 = Square(True)

        with self.assertRaises(TypeError):
            test1 = Square(5, "Holberton")

        with self.assertRaises(TypeError):
            test1 = Square(2, 4.5)

        with self.assertRaises(ValueError):
            test1 = Square(5, -10)

        with self.assertRaises(TypeError):
            test1 = Square(5, [2, 3])

        with self.assertRaises(TypeError):
            test1 = Square(5, (5, 5))

        with self.assertRaises(TypeError):
            test1 = Square(5, True)

        with self.assertRaises(TypeError):
            test1 = Square(5, {'k': 5})

        with self.assertRaises(TypeError):
            test1 = Square(5, 5, "Holberton")

        with self.assertRaises(TypeError):
            test1 = Square(5, 5, 4.5)

        with self.assertRaises(ValueError):
            test1 = Square(5, 5, -10)

        with self.assertRaises(TypeError):
            test1 = Square(5, 5, [3, 4])

        with self.assertRaises(TypeError):
            test1 = Square(5, 5, (3, 4))

        with self.assertRaises(TypeError):
            test1 = Square(5, 5, True)

        with self.assertRaises(TypeError):
            test1 = Square(5, 5, {'k': 5})

    def test_area(self):
        '''testing area function'''
        test1 = Square(5, 5)
        self.assertEqual(test1.area(), 25)

    def test_str(self):
        '''testing self'''
        test1 = Square(10)
        self.assertEqual(str(test1), "[Square] (23) 0/0 - 10")

        test1 = Square(10, 5)
        self.assertEqual(str(test1), "[Square] (24) 5/0 - 10")

        test1 = Square(10, 5, 9)
        self.assertEqual(str(test1), "[Square] (25) 5/9 - 10")

        test1 = Square(10, 5, 9, 4)
        self.assertEqual(str(test1), "[Square] (4) 5/9 - 10")

    def test_kwargs(self):
        '''testing update kwargs'''
        test1 = Square(10, 10, 10, 10)
        test1.update(size=5)
        self.assertEqual(str(test1), "[Square] (10) 10/10 - 5")
