#!/usr/bin/python3
"""module that return True if obj is same as instance"""


def is_same_class(obj, a_class):
    """test whether its of the same instance
    Args: obj (object): the object to be checked
    a_class: the class to compare with 

    returns: bool true/false
    """
    return type(obj) is a_class
