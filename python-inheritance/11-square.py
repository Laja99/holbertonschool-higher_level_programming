#!/usr/bin/python3
"""
Module 10-square
Defines a Square class that inherits from Rectangle.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square, inheriting from Rectangle."""

    def __init__(self, size):
        """
        Initialize a square with validated size.

        Args:
            size (int): The size of the square's sides.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Return the area of the square."""
        return self.__size * self.__size

    def __str__(self):
        """Return a printable description of the square."""
        return ("[Square] {}/{}".format(
            self._Rectangle__width, self._Rectangle__height))
