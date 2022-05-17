#!/usr/bin/python3
'''function that creates a class named "Square", that defines a square
by a private instance attribute named "size", where it has an instantation
with optional "size: def __init__(self, size=0):". Where "size" must be an
integer, otherwise raise a "TypeError" exception with the message "size must
be an integer". if "size" is less than "0", raise a "ValueError" exception with
the message "size must be >= 0".'''


class Square:
    '''Here we create a new class named "Square"'''
    def __init__(self, size=0, position=(0, 0)):
        '''Here we initialize the class created, withe the parameters
        "self", and size. This last parameter, is a private attribute,
        and that is why is has two "__" before the name. The reason why
        this attribute is private, it is because the size of a square is
        crucial for a square and many things depend on it. So we need to take
        the control of it and keep it privately.'''
        self.size = size
        self.position = position

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
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        '''Here we create the getter for method position'''
        return self.__position

    @position.setter
    def position(self, size):
        '''here we create the setter for the method position'''
        if type(size) is not tuple or len(size) != 2 or \
                type(size[0]) is not int or type(size[1]) is not int or \
                size[0] < 0 or size[1] < 0:
                    raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = size 

    def my_print(self):
        '''Prints a square with the character #'''
        if self.__size == 0:
            print()
        else:
            if self.__position[1] > 0:
                for i in range(self.__position[1]):
                    print()
            for x in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
