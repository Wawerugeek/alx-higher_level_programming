#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    num = 0
    for i in range(x):
        try:
            print(my_list[i], end="")
            num += 1
        except IndexError:
            break
    print()
    return num
