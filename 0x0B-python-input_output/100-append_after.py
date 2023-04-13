#!/usr/bin/python3
"""module that inserts a line to a file"""


def append_after(filename="", search_string="", new_string=""):
    """function will insert a text to a file having unique string"""
    text = ""
    with open(filename) as file:
        for string in file:
            text += string
            if search_string in string:
                text += new_string

    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)
