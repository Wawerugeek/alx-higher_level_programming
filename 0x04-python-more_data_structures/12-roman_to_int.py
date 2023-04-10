#!/usr/bin/python3


def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman_dictionary = {
            '1': 1, 'V': 5, 'X': 10, 'C': 100, 'D': 500, 'M': 1000
            }
    current = 0
    prev = 0
    for cha in roman_string:
        value = roman_dictionary.get(c, 0)
        if value == 0:
            return 0
        if value > prev:
            current += - 2 * prev
        else:
            current += value
        prev = value
    return current
