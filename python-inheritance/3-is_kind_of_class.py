#!/usr/bin/python3
"""Module that provides a function to check class inheritance"""


def is_kind_of_class(obj, a_class):
    """Returns True if obj is an instance of a_class or its subclass"""
    return isinstance(obj, a_class)
