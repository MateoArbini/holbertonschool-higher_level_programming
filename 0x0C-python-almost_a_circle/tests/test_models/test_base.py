#!/usr/bin/python3
'''
Unittest for base class
'''


import unittest
import json
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class test_Base(unittest.TestCase):
    '''class'''

    def test_id(self):
        '''testeamos seteo de id'''
        Base._Base__nb_objects = 0
        test1 = Base()
        test2 = Base()
        test3 = Base(3)
        test4 = Base(-4)
        test5 = Base(None)
        self.assertEqual(test1.id, 1)
        self.assertEqual(test2.id, 2)
        self.assertEqual(test3.id, 3)
        self.assertEqual(test4.id, -4)
        self.assertEqual(test5.id, 3)
        '''si no se le asigna un id especifico, se le asignara
        uno en base al orden en el que fue creado'''

        self.assertEqual(str(type(Base)), "<class 'type'>")
        self.assertEqual(str(type(Rectangle)), "<class 'type'>")
        self.assertEqual(str(type(Square)), "<class 'type'>")
        '''casos para testear de que el tipo de la instancia sea class'''

        self.assertEqual(issubclass(Base, Rectangle), False)
        self.assertEqual(issubclass(Base, Square), False)
        self.assertEqual(issubclass(Rectangle, Base), True)
        self.assertEqual(issubclass(Square, Base), True)
        self.assertEqual(issubclass(Rectangle, Square), False)
        self.assertEqual(issubclass(Square, Rectangle), True)
        '''testeamos el si las instancias son sublclases o no'''

        test1 = Square(5)
        test2 = Square(4)
        self.assertEqual(test1 is test2, False)
        self.assertEqual(isinstance(test1, Square), True)
        test3 = Rectangle(2, 3)
        test4 = Rectangle(4, 5)
        self.assertEqual(test3 is test4, False)
        self.assertEqual(isinstance(test3, Rectangle), True)
        '''testeamos is e isinstance'''

    def test_to_json_string(self):
        '''testeamos funcion json to string'''
        new_dictionary = None
        new_json_string = Base.to_json_string([new_dictionary])
        self.assertEqual(new_json_string, '[null]')
        '''en este caso, el nuevo diccionario que creamos toma el valor de
        null'''

    def test_save_to_file2(self):
        '''testeamos la funcion save to file'''
        with self.assertRaises(AttributeError):
            Base.save_to_string()
        '''en este caso, testeamos el error'''
