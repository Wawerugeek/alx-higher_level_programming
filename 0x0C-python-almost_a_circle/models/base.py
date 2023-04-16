#!/usr/bin/python3
"""this module contains the Base class"""


class Base:
    """private class attribute"""
    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor with one argument"""
        if id is not None:
            """assign id if provided"""
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
