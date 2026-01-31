#!/usr/bin/python3
"""
Module 101-add_attribute
Adds a new attribute to an object if possible.
"""


def add_attribute(obj, attr, value):
    """
    Adds a new attribute to an object if it can accept new attributes.

    Raises:
        TypeError: if the object cannot have new attributes.
    """
    if hasattr(obj, "__dict__"):
        setattr(obj, attr, value)
    else:
        raise TypeError("can't add new attribute")
