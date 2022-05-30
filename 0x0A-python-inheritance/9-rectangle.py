#!/usr/bin/python3
'''Write a class Rectangle that inherits from BaseGeometry
(7-base_geometry.py). (task based on 8-rectangle.py)
the area() method must be implemented.
print() should print, and str() should return, the following
rectangle description: [Rectangle] <width>/<height>'''


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
        return (f"[Rectangle] {self.__height}/{self.__width}")
