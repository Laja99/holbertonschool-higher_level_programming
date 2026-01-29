#!/usr/bin/python3
"""
Square module that defines a square and supports area comparison
"""


class Square:
    """Class that defines a square"""

    def __init__(self, size=0):
        """
        Initialize a square with a given size.

        Args:
            size (int or float): The size of the square side (default is 0).

        Raises:
            TypeError: if size is not a number (int or float)
            ValueError: if size is less than 0
        """
        self.size = size

    @property
    def size(self):
        """Getter for the size attribute."""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter for the size attribute.

        Args:
            value (int or float): New size value.

        Raises:
            TypeError: if value is not a number (int or float)
            ValueError: if value is less than 0
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate and return the area of the square."""
        return self.__size ** 2

    def __eq__(self, other):
        return self.area() == other.area()

    def __ne__(self, other):
        return self.area() != other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    def __le__(self, other):
        return self.area() <= other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __ge__(self, other):
        return self.area() >= other.area()
