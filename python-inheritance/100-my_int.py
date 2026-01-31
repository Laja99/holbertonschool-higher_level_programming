#!/usr/bin/python3
"""
Module 100-my_int
Defines a MyInt class that inherits from int with inverted == and != operators.
"""


class MyInt(int):
    """Rebel integer: == and != operators are inverted."""

    def __eq__(self, other):
        """Inverts equality: returns True if values are not equal."""
        return int(self) != other

    def __ne__(self, other):
        """Inverts inequality: returns True if values are equal."""
        return int(self) == other
