#!/usr/bin/python3
"""
returns True if the object is exactly an instance of the specified class ; otherwise False.
"""

def is_same_class(obj, a_class):
    """
    Checks if object is an instance of specified class

    Args:
        obj(any): object to check
        a_class (type): type to check against

    Returns: Boolean (True or False)
    """

    return type(obj) == a_class
