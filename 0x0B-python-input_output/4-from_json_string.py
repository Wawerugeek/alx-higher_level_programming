#!/usr/bin/python3
"""module that returns a python object from json string"""
import json
"""module to help us work with json"""


def from_json_string(my_str):
    """deserializing (not correct name though)"""
    return json.loads(my_str)
