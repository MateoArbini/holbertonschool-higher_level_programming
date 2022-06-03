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

from models.base import Base


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
    def width(self, value):
        '''setter width'''
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        '''getter height'''
        return self.__height

    @height.setter
    def height(self, value):
        '''setter height'''
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        '''getter x'''
        return self.__x

    @x.setter
    def x(self, value):
        '''setter x'''
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        '''getter y'''
        return self.__y

    @y.setter
    def y(self, value):
        '''setter y'''
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        '''public method that returns the area of the Rectangle instance'''
        return self.__width * self.__height

    def display(self):
        '''function that display the rectangle instance with the char #'''
        if self.__height == 0 or self.__width == 0:
            print()
        else:
            if self.__y >= 1:
                for i in range(self.__y):
                    print()
            for f in range(self.__height):
                print(' ' * self.__x + '#' * self.__width)

    def __str__(self):
        '''method that returns a string'''
        return (f"[{self.__class__.__name__}] ({self.id}) \
{self.__x}/{self.__y} - {self.__width}/{self.__height}")

    def update(self, *args, **kwargs):
        '''function that assigns an argument to each attribute'''
        if args and args is not None:
            i = 0
            for arg in args:
                if i == 0:
                    self.id = arg
                if i == 1:
                    self.__width = arg
                if i == 2:
                    self.__height = arg
                if i == 3:
                    self.__x = arg
                if i == 4:
                    self.__y = arg
                i += 1
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "width":
                    self.__width = value
                if key == "height":
                    self.__height = value
                if key == "x":
                    self.__x = value
                if key == "y":
                    self.__y = value
