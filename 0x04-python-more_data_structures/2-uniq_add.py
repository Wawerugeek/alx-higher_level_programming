#!/usr/bin/python3


def uniq_add(my_list=[]):
    new_list = set(my_list)
    count = 0
    for x in new_list:
        count += x

    return count
