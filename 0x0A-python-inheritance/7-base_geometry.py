#!/usr/bin/python3
"""
An empty class
"""


class BaseGeometry:
    """
    Implementation
    """

    def area(self):
        """
        Raises an exception if not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Assumes that name is always a string and raises exceptions if:
        i) value is not of type integer
        ii) value is <= 0
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
