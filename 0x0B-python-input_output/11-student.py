#!/usr/bin/python3
'''
Write a class Student that defines a student by: (based on 10-student.py)

Public instance attributes:
    first_name
    last_name
    age
    Instantiation with first_name, last_name and age:
    def __init__(self, first_name, last_name, age):
    Public method def to_json(self, attrs=None): that retrieves a dictionary
    representation of a Student instance (same as 8-class_to_json.py):
    If attrs is a list of strings, only attributes name contain in this
    list must be retrieved.
    Otherwise, all attributes must be retrieved
    Public method def reload_from_json(self, json): that replaces all
    attributes of the Student instance:
    You can assume json will always be a dictionary
    A dictionary key will be the public attribute name
    A dictionary value will be the value of the public attribute
    You are not allowed to import any module
    Now, you have a simple implementation of a serialization and
    deserialization mechanism (concept of representation of an object to
    another format, without losing any information and allow us to rebuild
    an object based on this representation)
'''


class Student:
    '''class'''
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''function that retrieves a dictionary representation of a student'''
        if attrs is None:
            return self.__dict__
        else:
            new_dic = {}
            for attribute in attrs:
                if attribute in self.__dict__.keys():
                    new_dic[attribute] = self.__dict__[attribute]
            return new_dic

    def reload_from_json(self, json):
        '''function'''
        for j, k in json.items():
            setattr(self, j, k)
