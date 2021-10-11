#!/usr/bin/python3
"""
returns True if the object is an instance of a class \
that inherited (directly or indirectly) from the \
specified class ; otherwise False.
"""


def inherits_from(obj, a_class):
    """
    Checks parenthood

    Args:
        obj(any): object to check
        a_class (type): type to check against

    Returns: Boolean (True or False)
    """

    return type(obj) != a_class and issubclass(type(obj), a_class)
