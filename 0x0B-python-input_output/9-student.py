#!/usr/bin/python3
"""module that defines class student"""


class Student:
    """the class instantiation/constructor"""
    def __init__(self, first_name, last_name, age):
        """setting the attributes of student object
        args:
        first-name
        last_name
        int """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """public method that gets dic represenation"""
        return self.__dict__
