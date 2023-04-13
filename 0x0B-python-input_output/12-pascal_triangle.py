#!/usr/bin/python3
"""module that return a listof ints rep pascal triangle n"""


def pascal_triangle(n):
    """will return a lisr of ints"""
    if n <= 0:
        return []
    f_tri = [[1]]
    while len(f_tri) is not n:
        var = [1]
        for x in range(len(f_tri[-1]) - 1):
            var.append(f_tri[-1][x] + f_tri[-1][x + 1])
        var.append(1)
        f_tri.append(var)
    return f_tri
