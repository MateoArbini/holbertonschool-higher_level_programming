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
            raise TypeError(f"{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError(f"{:s} must be greater than 0".format(name))
