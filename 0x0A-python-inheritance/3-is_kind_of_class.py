#!/usr/bin/python3
"""module that returns True if the object is an instance of,
or if the object is an instance of a class
that inherited from, the specified class ; otherwise False."""


def is_kind_of_class(obj, a_class):
    """returns: Bool --> True or false
    args: obj, class"""
    return isinstance(obj, a_class)
