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

    def fetch(self, id=None, size=None, x=None, y=None):
        """the fetch internal method checks whether the values are none
        and if not it will update the instances of attrs.
        1st argument should be the id attribute
        2nd argument should be the size attribute
        3rd argument should be the x attribute
        4th argument should be the y attribute
        kwargs must be skipped if args exists
        """
        if id is not None:
            self.id = id
        if size is not None:
            self.size = size
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        """this method checks whether is */** and updates
        instances"""
        if kwargs:
            self.fetch(**kwargs)
        elif args:
            self.fetch(*args)

    def to_dictionary(self):
        """the dictionary representation of class square"""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
