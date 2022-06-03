#!/usr/bin/python3
'''
Write the class Square that inherits from Rectangle:

    * In the file models/square.py
    * Class Square inherits from Rectangle
    * Class constructor: def __init__(self, size, x=0, y=0, id=None)::
        - Call the super class with id, x, y, width and height - this super
          call will use the logic of the __init__ of the Rectangle class. The
          width and height must be assigned to the value of size
        - You must not create new attributes for this class, use all attributes
          of Rectangle - As reminder: a Square is a Rectangle with the same
          width and height
        - All width, height, x and y validation must inherit from Rectangle -
          same behavior in case of wrong data
    * The overloading __str__ method should return [Square] (<id>) <x>/<y> -
    <size> - in our case, width or height
'''


from models.rectangle import Rectangle


class Square(Rectangle):
    '''class'''
    def __init__(self, size, x=0, y=0, id=None):
        '''constructor initializing'''
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        '''return a string'''
        return (f"[{self.__class__.__name__}] ({self.id}) \
{self.x}/{self.y} - {self.size}")

    @property
    def size(self):
        '''getter size'''
        return self.__size

    @size.setter
    def size(self, value):
        '''setter size'''
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value <= 0:
            raise ValueError("size must be > 0")
        else:
            self.__size = value
