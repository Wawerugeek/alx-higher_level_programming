#!/usr/bin/python3
"""function that reads a text file"""


def read_file(filename=""):
    with open(filename, "r", encoding="utf-8") as file:
        prin = file.read()
        print(prin, end="")
