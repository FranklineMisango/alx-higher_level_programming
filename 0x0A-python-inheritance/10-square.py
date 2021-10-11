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
