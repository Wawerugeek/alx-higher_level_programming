#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    result_matrix = []

    for row in matrix:
        result_row = []
        for cols in row:
            mult = cols * cols
            result_row.append(mult)
        result_matrix.append(result_row)

    return result_matrix
