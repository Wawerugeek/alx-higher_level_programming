#!/usr/bin/python3
"""This module prints the values in a list with ascending order"""


class MyList(list):
    """class inherits from list
        prints a list in ascending order
        """
    def print_sorted(self):
        """function to sort"""
        print(sorted(self))
