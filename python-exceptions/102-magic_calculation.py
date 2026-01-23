#!/usr/bin/python3


def magic_calculation(a, b):
    """
    Performs a specific calculation:
    - If a < b, returns the sum of squares from a to b - 1.
    - Otherwise, returns the sum a + b.
    """
    if a < b:
        result = 0
        for i in range(a, b):
            result += i ** 2
        return result
    else:
        return a + b
