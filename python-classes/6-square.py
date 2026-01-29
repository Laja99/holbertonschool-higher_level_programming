#!/usr/bin/python3
"""
Square generation module for Python project
"""


class Square:
    """Class Square that defines a square by size and position."""

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a square with size and position.

        Args:
            size (int): size of the square (default 0)
            position (tuple): tuple of 2 positive integers (default (0, 0))

        Raises:
            TypeError: if size is not an integer or position is invalid
            ValueError: if size is less than 0
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter for size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for size with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getter for position."""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter for position with validation."""
        if (
            not isinstance(value, tuple) or
            len(value) != 2 or
            not all(isinstance(n, int) for n in value) or
            value[0] < 0 or value[1] < 0
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the current square area."""
        return self.__size * self.__size

    def my_print(self):
        """Print the square with '#' taking into account position."""
        if self.__size == 0:
            print()
            return

        for _ in range(self.__position[1]):
            print()

        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
