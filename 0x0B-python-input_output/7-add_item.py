#!/usr/bin/python3
"""module that adds all arguments to a python list and the save"""
import sys


if __name__ == "__main__":
    """we import from  two modules"""
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

    try:
        j_list = load_from_json_file("add_item.json")
    except FileNotFoundError:
        j_list = []
    j_list.extend(sys.argv[1:])
    save_to_json_file(j_list, "add_item.json")
