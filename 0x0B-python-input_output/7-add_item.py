#!/usr/bin/python3
"""module that adds all arguments to a python list and the save"""
import sys


save_to_json_file = __import__('5-save_to_json_file.py').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file.py').load_from_json_file

try:
    j_list = load_from_json_file('add_item.jsom')
except FileNotFoundError:
    j_list = []

if len(sys.argv) > 1:
    for i in range(1, len(sys.argv):
            j_list.append(sys.argv[i]

save_to_json_file(j_list, "add_item.json")
