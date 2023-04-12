#!/usr/bin/python3
"""a class Rectangle that inherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """constructor with two arguments"""
    def __init__(self, width, height):
        """args:
        width: int
        height: int """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """implementation of the method area"""
        return self.__height * self.__width

    def __str__(self):
        """returns string represenation of the rectangle"""
        return (f"[Rectangle] {self.__width}/{self.__height}")
