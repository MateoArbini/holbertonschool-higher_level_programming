#!/usr/bin/python3
'''
function that prints a square with the char #
'''


def print_square(size):
    '''function'''
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for x in range(size):
            print('#', end="")
        print()
