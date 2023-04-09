#!/usr/bin/python3
"""a function to input squares of a function"""


def square_matrix_simple(matrix=[]):
    """Initialize an empty list to store the values"""
    result_matrix = []

    for row in matrix:
        result_row = []
        for cols in row:
            mult = cols * cols
            result_matrix.append(mult)
        result_matrix.append(result_row)

    return result_matrix
