#!/usr/bin/python3
"""this module defines class rectanglei which inherits from base"""
from models.base import Base


class Rectangle(Base):
    """the class rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """defining the constructor"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.validate_int("width", value, False)
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.validate_int("height", value, False)
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.validate_int("x", value)
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.validate_int("y", value)
        self.__y = value

    def validate_int(self, name, value, test=True):
        """method to validate if its interger: used method because of DRY"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if not test and value <= 0:
            raise ValueError(f"{name} must be > 0")
        elif test and value < 0:
            raise ValueError(f"{name} must be >= 0")

    def area(self):
        """public method that returns an area of rectangle instance"""
        return self.__width * self.__height

    def display(self):
        """method that prints to stdout the rectangle instance"""
        var = "\n" * self.y + \
              (" " * self.x + "#" * self.width + "\n") * self.height
        print(var, end="")

    def __str__(self):
        """this method overrides the __str__ to return new string rep"""
        return (f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}")
