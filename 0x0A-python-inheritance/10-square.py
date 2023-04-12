#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
"""class square that inherits from subclass rectangle"""


class Square(Rectangle):
    """building its constructor"""
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
    
    def area(self):
        """method area implementation"""
        return self.__size * self.__size
