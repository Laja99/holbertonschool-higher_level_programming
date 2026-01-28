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
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size


    @property
    def size(self):
        """
        Getter for the size attribute.
        Returns:
        int: the current size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter for the size attribute. Validates value before setting.
        Args:
            value (int): New size value
        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    def area(self):
        """
        multiplying the length of one side by itself
        :param self: to take self.__size
        """
        return self.__size * self.__size
