#!/usr/bin/python3

"""Function to print a square"""

def print_square(size):
    """size is the length of the square """

    if type(size) is not int:
        raise TypeError('size must be an interger')
    
    """check valueError if size is less than 0"""

    if size < 0:
        raise ValueError('size must be >=0')

    for side in range(size):
        print('#' * size)
