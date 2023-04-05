#!/usr/bin/python3

"""Define class square:
    Attributes:
    size: Private instance attribute: size:
    """

class Square:
    """class that has an attribute of size"""

    def __init__(self, size):
        """creates a new instance and set it to private
        Args:
        size: the side of the square
        """
        self.__size = size
