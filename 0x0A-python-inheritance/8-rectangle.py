#!/usr/bin/python3
"""a class Rectangle that inherits from BaseGeometry"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """constructor with two arguments"""
    def __init__(self, width, height):
        """args:
        width: int
        height: int """
        BaseGeometry.integer_validator(self, "width", width)
        self.__width = width
        BaseGeometry.integer_validator(self, "height", height)
        self.__height = height
