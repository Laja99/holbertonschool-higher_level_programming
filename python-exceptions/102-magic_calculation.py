#!/usr/bin/python3


def magic_calculation(a, b):
    """
    Mimics a bytecode-based calculation.
    """
    result = 0
    if a < b:
        for i in range(a, b):
            result += i ** 2
    else:
        result = a + b
    return result
