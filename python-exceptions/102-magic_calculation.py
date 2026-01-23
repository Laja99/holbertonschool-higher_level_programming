#!/usr/bin/python3


def magic_calculation(a, b):
    """
    Returns a ** + b ** if a < b, else returns a + b.
    """
    return (a ** b) + (b ** a) if a < b else a + b
