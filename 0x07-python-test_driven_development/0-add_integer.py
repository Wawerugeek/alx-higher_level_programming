#!/usr/bin/python3
""" THis is an interget addition function"""

def add_integer(a, b=98):
    """a and b must be integers or floats"""
    if not(isinstance(b, int) or isinstance(b, float):
        raise TypeError("b must be integer")
    if not(isinstance(a, int) or isinstance(a, float):
        raise TypeError("a must be integer")

    if type(a) == float:
        a = int(a)

    if isinstance(b, float):
        b = int(b)

    """ perfom the addition operation"""
     return (a + b)
