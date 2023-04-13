#!/usr/bin/python3
import json
"""function that return JSON representation of an object"""


def to_json_string(my_obj):
    """it will take python object and return json str rep"""
    return json.dumps(my_obj)

