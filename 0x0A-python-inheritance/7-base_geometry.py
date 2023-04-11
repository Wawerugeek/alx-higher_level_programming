#!/usr/bin/python3
"""module to populate BaseGeometry"""


class BaseGeometry:
    """defines method area"""
    def area(self):
        """raises an exception for now"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """public instance method that validates name"""
        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
