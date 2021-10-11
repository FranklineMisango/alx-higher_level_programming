#!/usr/bin/python3
"""
inherits from BaseGeometry
"""


BaseGeometry = __import__(7-base_geometry).BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle implementation
    """
    def __init__(self, width, height):
        """
        Initialization

        Args:
            width(int)
            height(int)
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        calculates area & returns an int
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns a string representation
        """

        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
