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
        if size >= 0:
            self.__size = size
        elif not isinstance(size, int):
            raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
