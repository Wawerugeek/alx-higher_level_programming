#!/usr/bin/python3
"""function that appends a string at the end"""


def append_write(filename="", text=""):
    """this will append at the end of the line"""
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
