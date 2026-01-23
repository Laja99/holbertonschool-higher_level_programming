#!/usr/bin/python3


def magic_calculation(a, b):
    """
    Returns:
    - a ** b + b ** a if a < b
    - otherwise, a + b + 1.0
    """
    if a < b:
        return a ** b + b ** a
    else:
        return a + b + 1.0
