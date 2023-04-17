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
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
