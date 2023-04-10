#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    val = a_dictionary
    sorted_keys = sorted(val.keys())

    for x in sorted_keys:
        value = val[x]
        print(f"{x} : {value}")
