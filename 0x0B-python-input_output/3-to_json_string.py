#!/usr/bin/python3
"""module that return JSON representation of an object"""
import json
"""module that will enable us to use json file"""


def to_json_string(my_obj):
    """it will take python object and return json str rep"""
    return json.dumps(my_obj)
