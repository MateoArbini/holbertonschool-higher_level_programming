#!/usr/bin/python3
'''function that creates a class named "Square", that defines a square
by a private instance attribute named "size", where it has an instantation
with optional "size: def __init__(self, size=0):". Where "size" must be an
integer, otherwise raise a "TypeError" exception with the message "size must
be an integer". if "size" is less than "0", raise a "ValueError" exception with
the message "size must be >= 0".'''


class Square:
    '''Here we create a new class named "Square"'''
    def __init__(self, size=0):
        '''Here we initialize the class created, withe the parameters
        "self", and size. This last parameter, is a private attribute,
        and that is why is has two "__" before the name. The reason why
        this attribute is private, it is because the size of a square is
        crucial for a square and many things depend on it. So we need to take
        the control of it and keep it privately.'''
        if type(size) is int:
            self.__size = size
        else:
            raise TypeError("size must be an integer")
        if size >= 0:
            self.__size = size
        else:
            raise ValueError("size must be >= 0")

    def area(self):
        '''method that calculates the area of the square'''
        result = self.__size * self.__size
        return result

    @property
    def size(self):
        '''Here we create the getter'''
        return self.__size

    @size.setter
    def size(self, value):
        '''Here we create the setter'''
        if type(value) is int:
            self.__size = value
        else:
            raise TypeError("size must be an integer")
        if value >= 0:
            self.__size = value
        else:
            raise ValueError("size must be >= 0")
