#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    score = 0
    weight = 0

    for tupple in my_list:
        num += tupple[0] * tupple[1]
        den += tupple[1]
    return (score / weight)
