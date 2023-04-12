#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
"""class square that inherits from subclass rectangle"""


class Square(Rectangle):
    """building its constructor"""
    def __init__(self, size):
        """method to initialize attributes"""

        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """implementation of the area method side squared"""

        return self.__size ** 2
