#!/usr/bin/python3
"""Module that defines a Square class inheriting from Rectangle."""

Rectangle = __import__('8-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square."""

    def __init__(self, size):
        """Initialize a square with validated size."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Return the area of the square."""
        return self.__size * self.__size

    def __str__(self):
        """Return a printable description of the square."""
        return "[Square] {}/{}".format(self.__size, self.__size)
