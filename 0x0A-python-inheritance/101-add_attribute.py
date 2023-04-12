#!/usr/bin/python3
"""module that adds new attribute to an object"""


def add_attribute(obj, name, value):
    """adding new attribute is possible using hasattr"""
    if not hasattr(obj, '__dict__'):
        raise TypeError(f"can't add new attribute")
    """set a new attribute"""
    setattr(obj, name, value)
