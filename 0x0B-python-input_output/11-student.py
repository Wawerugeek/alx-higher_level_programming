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

    def to_json(self, attrs=None):
        """public method that gets dic represenation"""
        return {x: y for x, y in self.__dict__.items()
                if x in attrs} if attrs is not None else self.__dict__

    def reload_from_json(self, json):
        for x, y in json.items():
            setattr(self, x, y)
