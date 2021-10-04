#!/usr/bin/python3

"""
Defines a class Rectangle with private attributes width & height
Width and height must be integers otherwise raise a TypeError with a message
They must be greater than zero else raise a ValueError with a message
"""

class Rectangle:
    """
    Rectangle object with getters & setters
    """

    def __init__(self, width=0, height=0):

        self.width = width
        self.height = height

    def __str__(self):
       total = ""
       if self.__height == 0 or self.width == 0:
         return total
       for i in range(self.__height):
           total += ("#" * self.__width)
           if i is not self.__height - 1:
            total += "\n"
            return total

    def __repr__(self):
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:

            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:

            self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)
