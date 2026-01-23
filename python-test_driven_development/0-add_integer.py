#!/usr/bin/python3
"""
This module contains one function, add_integer.
It adds two integers and checks their types.
Floats are casted to integers before addition.
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
