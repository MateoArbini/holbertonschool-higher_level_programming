#!/usr/bin/python3
'''Write a class Square that inherits from Rectangle (9-rectangle.py):
Instantiation with size: def __init__(self, size)::
    size must be private. No getter or setter
    size must be a positive integer, validated by integer_validator
the area() method must be implemented'''


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''class inheritance from Rectangle'''
    def __init__(self, size):
        '''initializing class'''
        super().integer_validator("size", size)
        self.__size = size
