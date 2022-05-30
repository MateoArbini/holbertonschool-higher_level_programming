#!/usr/bin/python3
'''Write a class MyInt that inherits from int:

    MyInt is a rebel. MyInt has == and != operators inverted
    You are not allowed to import any module
'''


class MyInt(int):
    '''class'''
    def __init__(self, number):
        '''initializing class'''
        self.number = number

    def __eq__(self, other):
        '''changing signs'''
        return not self.number == other

    def __ne__(self, other):
        '''changing signs'''
        return self.number == other
