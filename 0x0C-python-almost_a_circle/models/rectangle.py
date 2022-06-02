#!/usr/bin/python3
'''
Write the class Rectangle that inherits from Base:

    * In the file models/rectangle.py
    * Class Rectangle inherits from Base
    * Private instance attributes, each with its own public getter and setter:
        -   __width -> width
        -   __height -> height
        -   __x -> x
        -   __y -> y
    * Class constructor: def __init__(self, width, height, x=0, y=0, id=None):
        - Call the super class with id - this super call with use the logic
          of the __init__ of the Base class
        - Assign each argument width, height, x and y to the right attribute
'''

from . base import Base


class Rectangle(Base):
    '''class'''
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        @property
        def width(self):
            '''getter width'''
            return self.__width

        @width.setter
        def width(self):
            '''setter width'''
            self.__width = width

        @property
        def height(self):
            '''getter height'''
            return self.__height

        @height.setter
        def height(self):
            '''setter height'''
            self.__height = height

        @property
        def x(self):
            '''getter x'''
            return self.__x

        @x.setter
        def x(self):
            '''setter x'''
            self.__x = x

        @property
        def y(self):
            '''getter y'''
            return self.__y

        @y.setter
        def y(self):
            '''setter y'''
            self.__y = y
