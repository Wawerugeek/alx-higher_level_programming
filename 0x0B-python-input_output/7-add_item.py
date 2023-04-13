#!/usr/bin/python3
"""module that adds all arguments to a python list and the save"""
import json
import sys


save_to_json_file = __import__('5-save_to_json_file.py').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file.py').load_from_json_fi
le
if __name__ == "__main__":
    try:
        j_list = load_from_json_file('add_item.jsom')
    except FileNotFoundError:
        j_list = []

    for file in range(1, len(sys.argv)):
        j_list.appenf(sys.argv[file])
    save_to_json_file(j_list, "add_item.json")
