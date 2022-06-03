#!/usr/bin/python3

'''
Write the first class Base:

    Create a folder named models with an empty file __init__.py
    inside - with this file, the folder will become a Python package

    Create a file named models/base.py:

    Class Base:
    * private class attribute __nb_objects = 0
    * class constructor: def __init__(self, id=None)::
          - if id is not None, assign the public instance attribute id with
            this argument value - you can assume id is an integer and you don’t
            need to test the type of it.
          - otherwise, increment __nb_objects and assign the new value to the
            public instance attribute id.
    This class will be the “base” of all other classes in this project.
    The goal of it is to manage id attribute in all your future classes and
    to avoid duplicating the same code (by extension, same bugs).
'''


import json


class Base:
    '''class'''
    __nb_objects = 0

    def __init__(self, id=None):
        '''initializing constructor'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''returns the JSON string representation of list_dictionaries'''
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return str(json.dumps(list_dictionaries))
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''write a json string representation to file'''
        filename = f"{cls.__name__}.json"
        empty_list = []

        if list_objs is not None:
            for element in list_objs:
                empty_list = empty_list + [element.to_dictionary()]
        else:
            json_list = Base.to_json_string(empty_list)
            with open(filename, "w", encoding="utf-8") as j:
                j.write(json_list)
