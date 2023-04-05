#!/usr/bin/python3
"""DEfine class locked"""
class LockedClass:
    """prevent class instanciation not unless its first_name"""
    __slots__=["first_name"]
