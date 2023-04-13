#!/usr/bin/python3
"""module that writes an object to a text file using json rep"""
import json
"""the json module needs to be imported"""


def save_to_json_file(my_obj, filename):
    """write to the obj"""
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)
