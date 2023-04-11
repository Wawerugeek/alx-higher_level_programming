#!/usr/bin/python3
"""module that return True if obj is same as instance"""


def is_same_class(obj, a_class):
    """test whether its of the same instance"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
