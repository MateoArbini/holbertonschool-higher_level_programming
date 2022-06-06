#!/usr/bin/python3
'''
Unittest for rectangle class
'''

import sys
import io
import unittest
import json
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class test_Rectangle(unittest.TestCase):
    '''class'''
    def test_id(self):
        '''testeamos id'''
        test2 = Rectangle(784, 422, 45, 65, 5)
        self.assertEqual(test2.id, 5)

    def test_data(self):
        '''testeamos data que se le pasa por atributo'''
        with self.assertRaises(TypeError):
            test1 = Rectangle("Holberton", 2)

        with self.assertRaises(TypeError):
            test1 = Rectangle(["School", "Holberton"], 2)

        with self.assertRaises(TypeError):
            test1 = Rectangle({'key': 3}, 2)

        with self.assertRaises(ValueError):
            test1 = Rectangle(0, 2)

        with self.assertRaises(ValueError):
            test1 = Rectangle(-4, 2)

        with self.assertRaises(TypeError):
            test1 = Rectangle(True, 2)

        with self.assertRaises(TypeError):
            test1 = Rectangle()

        with self.assertRaises(TypeError):
            test1 = Rectangle(2, "Holberton")

        with self.assertRaises(TypeError):
            test1 = Rectangle(2, ["Holberton", "School"])

        with self.assertRaises(TypeError):
            test1 = Rectangle(2, {"key": 6})

        with self.assertRaises(ValueError):
            test1 = Rectangle(2, 0)

        with self.assertRaises(ValueError):
            test1 = Rectangle(4, -2)

        with self.assertRaises(TypeError):
            test1 = Rectangle(2, False)

        with self.assertRaises(TypeError):
            test1 = Rectangle(1, 2, "Hello")

        with self.assertRaises(TypeError):
            test1 = Rectangle(1, 2, ["Holberton", "School"])

        with self.assertRaises(TypeError):
            test1 = Rectangle(1, 2, (1, 2, 3))

        with self.assertRaises(TypeError):
            test1 = Rectangle(1, 2, {"key": 5})

        with self.assertRaises(ValueError):
            test1 = Rectangle(1, 2, -5)

        with self.assertRaises(ValueError):
            test1 = Rectangle(1, 2, -6)

        with self.assertRaises(TypeError):
            test1 = Rectangle(1, 2, True)

        with self.assertRaises(TypeError):
            test1 = Rectangle(1, 2, 3, "Holberton")

        with self.assertRaises(TypeError):
            test1 = Rectangle(1, 2, 3, [4, 5])

        with self.assertRaises(TypeError):
            test1 = Rectangle(1, 2, 3, (3, 4))

        with self.assertRaises(TypeError):
            test1 = Rectangle(1, 2, 3, {"key": 3})

        with self.assertRaises(TypeError):
            test1 = Rectangle(1, 2, 3, True)

    def test_display(self):
        '''test output'''
        test1 = Rectangle(2, 3)
        captureOutput = io.StringIO()
        sys.stdout = captureOutput
        test1.display()
        self.assertEqual(captureOutput.getvalue(), ("##\n##\n##\n"))
        '''en este caso testeamos el display que deberia salir en
        la pantalla'''

    def test_update(self):
        '''testeamos la funcion del update'''
        test1 = Rectangle(4, 4, 4, 4, 4)
        self.assertEqual(str(test1), "[Rectangle] (4) 4/4 - 4/4")

        test1 = Rectangle(4, 4, 4, 4, 4)
        test1.update(1, 2)
        self.assertEqual(str(test1), "[Rectangle] (1) 4/4 - 2/4")

        test1 = Rectangle(4, 4, 4, 4, 4)
        new_dic = {'id': 1, 'width': 1, 'height': 1, 'x': 1, 'y': 1}
        test1.update(**new_dic)
        self.assertEqual(str(test1), "[Rectangle] (1) 1/1 - 1/1")

        test1.update()
        self.assertEqual(str(test1), "[Rectangle] (1) 1/1 - 1/1")


if __name__ == "__main__":
    unittest.main()
