#!/usr/bin/python3
'''Write a class Square that inherits from Rectangle (9-rectangle.py). (task based on 10-square.py).

Instantiation with size: def __init__(self, size)::
    size must be private. No getter or setter
    size must be a positive integer, validated by integer_validator
    the area() method must be implemented
    print() should print, and str() should return, the square description: [Square] <width>/<height>
'''


class BaseGeometry:
    '''class'''
    def __init__(self):
        '''initializing the class basegeometry'''

    def area(self):
        '''public instance method not implemented'''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''public instance method'''
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    '''class inheritance'''
    def __init__(self, width, height):
        '''initializing class'''
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        '''function that returns the area'''
        return self.__height * self.__width

    def __str__(self):
        '''function that return a string'''
        return (f"[Rectangle] {self.__width}/{self.__height}")


class Square(Rectangle):
    '''class inheritance from Rectangle'''
    def __init__(self, size):
        '''initializing class'''
        super().integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        '''function that return a string'''
        return (f"[{type(self).__name__}] {self.__size}/{self.__size}")

