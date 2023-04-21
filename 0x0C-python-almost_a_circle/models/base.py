#!/usr/bin/python3
import csv
import json
import turtle
import time

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

    @staticmethod
    def from_json_string(json_string):
        """static method that returns list rep of json str rep"""
        if json_string is None or not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """method that returns instance of all attr"""
        if cls.__name__ == "Square":
            new = cls(1)
        if cls.__name__ == "Rectangle":
            new = cls(1, 1)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """method that returns list of instances"""
        file = f"{cls.__name__}.json"
        try:
            with open(file, "r") as load:
                l_inst = Base.from_json_string(load.read())
                return [cls.create(**f) for f in l_inst]
        except IOError:
            pass
        return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Return json serialization of list dict"""
        file = f"{cls.__name__}.csv"
        with open(file, "w", newline='') as c_file:
            if list_objs is None or not list_objs:
                c_file.write("[]")
            else:
                if cls.__name__ == "Square":
                    f_name = ["id", "size", "x", "y"]
                else:
                    f_name = ["id", "width", "height", "x", "y"]
                c_write = csv.DictWriter(c_file, f_name = f_name)
                for objs in list_objs:
                    c_write.writerow(objs.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """returns list of classes from CSV file"""
        objs = []
        file = f"{cls.__name__}.csv"
        with open(file, "r", newline='', encoding="utf-8") as c_file:
            c_read = csv.reader(c_file)
            for row in c_read:
                row = [int(z) for z in row]
                if cls.__name__ == "Square":
                    dic = {
                        "id": row[0],
                        "size": row[1],
                        "x": row[2],
                        "y": row[3]
                    }
                if cls.__name__ == "Rectangle":
                    dic = {
                        "id": row[0],
                        "width": row[1],
                        "height": row[2],
                        "x": row[3],
                        "y": row[4]
                    }
                objs.append(cls.create(**dic))
            return objs

    @staticmethod
    def draw(list_rectangles, list_squares):
        """this method opens all rectangles and squares and draws them"""
        turtle.Screen().colormode(255)
        for a in list_rectangles + list_squares:
            turt = turtle.Turtle()
            turt.color(200, 8, 199)
            turt.pensize(1)
            turt.penup()
            turt.pendown()
            turt.setpos((a.x + turt.pos()[0], a.y - turt.pos()[1]))
            turt.pensize(10)
            turt.forward(a.width)
            turt.left(90)
            turt.forward(a.height)
            turt.left(90)
            turt.forward(a.width)
            turt.left(90)
            turt.forward(a.height)
            turt.left(90)
            turt.end_fill()

        time.sleep(10)
