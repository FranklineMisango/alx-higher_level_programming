#!/usr/bin/python3

"""
A child of the Rectangle
"""
Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """
    implementation
    """
    def __init__(self, size):
        """
        Initialization

        Args:
            size (int)
        """
        super().__init(size, size)
        self.__size = size

    def __str__(self):
        """string representation
        Returns:
            str: string
        """
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
