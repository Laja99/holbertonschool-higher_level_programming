#!/usr/bin/python3
"""
Square generation module for Python project
"""


class Square:
    """ class Square that defines a square by multiply size"""

    def __init__(self, size=0):
        """
        Docstring for __init__
        :param size=0: for Square

        Raises:
        raise ValueError : if size < 0
        raise TypeError : if size not intger
        """

        if not isinstance(size, int):
            raise TypeError("size must be >= 0")
        if size < 0:
            raise ValueError("size must be an integer")

        self.__size = size
