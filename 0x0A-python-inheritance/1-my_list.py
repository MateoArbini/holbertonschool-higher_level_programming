#!/usr/bin/python3
'''create a class named "MyList" that inherits from list. Also, create a public
instance method called def print_sorted(self):  that prints the list, but
sorted (ascending sort).
'''


class MyList(list):
    '''class'''
    def __init__(self):
        '''initializing class'''
        pass

    def print_sorted(self):
        '''function to print the list sorted'''
        print(sorted(self))
