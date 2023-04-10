#!/usr/bin/python3


def multiply_by_2(a_dictionary):
    new_dict = dict()

    for key, value in a_dictionary.items():
        mv = value * 2
        new_dict[key] = mv
    return new_dict
