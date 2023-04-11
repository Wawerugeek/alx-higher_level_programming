#!/usr/bin/python3
"""module that returns True if the object
is an instance of a class that inherited
(directly or indirectly) from the specified class ; otherwise False."""


def inherits_from(obj, a_class):
    """
    Check if the given object is an instance of a class
    that has inherited (directly or indirectly)
    from the specified class.

    Args:
        obj (object): The object to be checked.
        a_class (class): The class to compare against.

    Returns:
        bool: True if the object is an instance of a class
        that has inherited from the specified class,
        False otherwise.
    """
    return (type(obj) is not a_class and issubclass(type(obj), a_class))
