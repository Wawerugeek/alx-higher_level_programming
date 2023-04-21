#!/usr/bin/python3
"""this module defines class rectangle which inherits from base"""
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
        """method to validate if its integer: used method because of DRY"""
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
        var = "\n" * self.y + (" " * self.x + "#" * self.width + "\n") \
              * self.height
        print(var, end="")

    def __str__(self):
        """this method overrides the __str__ to return new string rep"""
        return f"[Rectangle] ({self.id}) "\
            f"{self.__x}/{self.__y} - {self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """this method takes various number of non-keyword argument
        following the below procedure
        1st argument should be the id attribute
        2nd argument should be the width attribute
        3rd argument should be the height attribute
        4th argument should be the x attribute
        5th argument should be the y attribute
        """
        if len(args) >= 1:
            self.id = args[0]
        if len(args) >= 2:
            self.width = args[1]
        if len(args) >= 3:
            self.height = args[2]
        if len(args) >= 4:
            self.x = args[3]
        if len(args) >= 5:
            self.y = args[4]
        elif kwargs and not args:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """this module returns the dictionary rep. of rectangle"""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
