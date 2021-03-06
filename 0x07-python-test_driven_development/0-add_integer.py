#!/usr/bin/python3
'''
function that adds 2 numbers of type int and returns the result
'''


def add_integer(a, b=98):
    '''
    function that adds two integers
    '''
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
