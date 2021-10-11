#!/usr/bin/python3
"""
A child of list
"""


class MyList(list):
    """
    Custom List
    """

    def print_sorted(self):
        """
        prints the list but sorted in ascending order
        """
        print(sorted(self))
