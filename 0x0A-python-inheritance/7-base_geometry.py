#!/usr/bin/python3
'''following the steps of the previous excercise, add a new instance method
called def integer_validator(self, name, value):'''


class BaseGeometry:
    '''class'''

    def area(self):
        '''public instance method not implemented'''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''public instance method'''
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
