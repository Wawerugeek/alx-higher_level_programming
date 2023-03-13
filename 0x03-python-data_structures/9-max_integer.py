#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return "None"
    else:
        mx_int = my_list[0]
        for i in range(len(my_list)):
            if my_list[i] > mx_int:
                mx_int = my_list[i]
            return mx_int 
