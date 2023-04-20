#!/usr/bin/python3
import json
"""this module contains the Base class"""


class Base:
    """private class attribute"""
    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor with one argument"""
        if id is not None:
            """assign id if provided"""
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """static method returns JSON serialization of list dicts"""
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """class method that deserialize json string to file
        args:
        list_objs : json string rep
        """
        if list_objs is not None:
            list_objs = [obj.to_dictionary() for obj in list_objs]
        with open(f"{cls.__name__}.json", "w", encoding="utf-8") as jsonF:
            jsonF.write(cls.to_json_string(list_objs))
