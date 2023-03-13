#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    my_list = mylist[::-1]
    for x in range(my_list):
        print("{:d}".format(my_list[x]))
