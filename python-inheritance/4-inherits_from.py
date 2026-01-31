#!/usr/bin/python3
"""Module that checks inherited classes"""


def inherits_from(obj, a_class):
    """Returns True if obj is instance of a subclass of a_class"""
    return isinstance(obj, a_class) and type(obj) is not a_class
