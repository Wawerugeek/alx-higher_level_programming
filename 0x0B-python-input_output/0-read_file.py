#!/usr/bin/python3
"""function that reads a text file"""


def read_file(filename=""):
    """reading a file and prints it to standard output"""
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read(), end="")
