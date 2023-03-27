#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    r_num = 0
    for i in range(r_num, x):
        try:
            print("{:d}".format(my_list[i]), end='')
            r_num += 1
        except (ValueError, TypeError):
            pass
    print()
    return r_num
