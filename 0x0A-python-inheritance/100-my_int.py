#!/usr/bin/python3
"""module that inherits from int"""


class MyInt(int):
    """it inherits from my_int"""
    def __eq__(self, value):
        """invert the behavior of == with != """
        return super().__ne__(value)

    def __ne__(self, value):
        """invert the behavior of != with =="""
        return super().__eq__(value)
