#!/usr/bin/python3
"""Define class square:
     Attributes:
     size: Private instance attribute: size:
"""


class Square:
    """class that has an attribute of size"""
    def __init__(self, size=0):
        """creates a new instance and set it to private
         Args:
        size: the side of the square
         """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
