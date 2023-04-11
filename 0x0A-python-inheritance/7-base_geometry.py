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
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
