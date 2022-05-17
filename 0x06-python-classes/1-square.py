#!/usr/bin/python3
'''function that creates a class named "Square", which is defined by
a private instance attribute called "size", and instantiation with
"size" (no type/value verification'''


class Square:
    '''Here we create a new class named "Square"'''
    def __init__(self, size):
        '''Here we initialize the class created, withe the parameters
        "self", and size. This last parameter, is a private attribute,
        and that is why is has two "__" before the name. The reason why
        this attribute is private, it is because the size of a square is
        crucial for a square and many things depend on it. So we need to take
        the control of it and keep it privately.'''
        self.__size = size
