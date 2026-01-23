#!/usr/bin/python3
"""
 Adds two integers, casting floats to int and raising TypeError if wrong type.
"""


def add_integer(a, b=98):
    """
    Adds two integers of float
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
