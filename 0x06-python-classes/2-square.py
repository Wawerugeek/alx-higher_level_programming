#!/usr/bin/python3
"""Define class square"""

class Square:
    """This class defines properties of square

    Attributes:
    size:one side of square"""

    def __init__(self, size=0):
        """creates an instance of the square"""
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size musr be an interger")
        elif size <0:
            raise ValueError("size must be >=0")
        else:
            self.__size = size
