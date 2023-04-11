#!/usr/bin/python3


class MyList(list):
    """class inherits from list
        prints a list in ascending order
        """
    def print_sorted(self):
        """function to sort"""
        print(sorted(self))
