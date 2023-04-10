#!/usr/bin/python3


def best_score(a_dictionary):
    if not a_dictionary:
        return None
    initial = None
    max_score = None
    for key, value in a_dictionary.items():
        if max_score is None or max_score > max_score:
            max_score = value
            initial = key
    return initial
