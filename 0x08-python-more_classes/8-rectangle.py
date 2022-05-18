#!/usr/bin/python3
'''function that creates a class named "Recatangle'''


class Rectangle:
    '''Here we create the class'''
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        '''private instance attribute named width'''
        return self.__width

    @width.setter
    def width(self, value):
        '''setter of the private instance width'''
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        '''private instance attribute named height'''
        return self.__height

    @height.setter
    def height(self, value):
        '''setter of the private instance height'''
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        '''public method to calculate the area of the rectangle'''
        return self.__width * self.__height

    def perimeter(self):
        '''public method to calculate the perimeter of the rectangle'''
        result = 0
        if self.__width <= 0 or self.__height <= 0:
            result = 0
        else:
            result = (self.__width * 2) + (self.__height * 2)
        return result

    def __str__(self):
        '''function to print the rectangle'''
        string = ""
        symbol = str(self.print_symbol)
        if self.__height <= 0 or self.__width <= 0:
            return string
        for hei in range(self.__height):
            for wid in range(self.__width):
                string = string + symbol
            string = string + '\n'
        string = string[:-1]
        return string

    def __repr__(self):
        '''method to return a string representation of the object'''
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        '''method to return a message when an instance is deleted'''
        del self
        if Rectangle.number_of_instances > 0:
            Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        '''staticmethod that returns the biggest rectangle based on the area'''
        object1 = isinstance(rect_1, Rectangle)
        object2 = isinstance(rect_2, Rectangle)

        if object1 is False:
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif object2 is False:
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1 >= rect_2:
            return rect_1
        else:
            return rect_2
