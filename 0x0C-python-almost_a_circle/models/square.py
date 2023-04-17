#!/usr/bin/python3
"""This module represents a class square that inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """the class attributes"""
    def __init__(self, size, x=0, y=0, id=None):
        """The class constructor"""
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    @property
    def size(self):
        """defining the getter method"""
        return self.height

    @size.setter
    def size(self, value):
        """the setter method"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """the update module that follows the following
        1st argument should be the id attribute
        2nd argument should be the size attribute
        3rd argument should be the x attribute
        4th argument should be the y attribute
        kwargs must be skipped if args exists
        """
        if len(args) >= 1:
            self.id = args[0]
        if len(args) >= 2:
            self.size = args[1]
        if len(args) >= 3:
            self.x = args[2]
        if len(args) >= 4:
            self.y = args[3]
        elif kwargs and not args:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.size = kwargs["x"]
            if "y" in kwargs:
                self.size = kwargs["y"]
