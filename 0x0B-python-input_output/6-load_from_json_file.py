#!/usr/bin/python3
"""this module creates an object from a JSON file"""
import json
"""json module"""


def load_from_json_file(filename):
    """open the json file for creation"""
    with open(filename) as jfile:
        json.load(jfile)
