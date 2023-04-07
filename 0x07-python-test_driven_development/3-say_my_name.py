#!/usr/bin/python3

""" 3_say_my_name is a function that says your name"""

def say_my_name(first_name, last_name=""):
    """prints both names: first and the last

    args: first_name a str of first name
            last_name a str of lastname
        """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
