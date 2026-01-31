#!/usr/bin/python3
"""
Module task_01_duck_typing
Demonstrates abstract base classes (ABCs) and duck typing in Python.

Defines:
- Shape: Abstract base class with area and perimeter methods.
- Circle: Concrete class implementing Shape.
- Rectangle: Concrete class implementing Shape.
- shape_info: Function that prints area and perimeter using duck typing.
"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Abstract base class for geometric shapes.

    Any class that inherits from Shape must implement the following methods:
    - area(): returns the area of the shape.
    - perimeter(): returns the perimeter of the shape.
    """

    @abstractmethod
    def area(self):
        """Calculate and return the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate and return the perimeter of the shape."""
        pass


class Circle(Shape):
    """
    Represents a circle shape.

    Attributes:
        radius (float or int): The radius of the circle.
    """

    def __init__(self, radius):
        """
        Initialize a Circle instance.

        Args:
            radius (float or int): The radius of the circle.
        """
        self.radius = radius

    def area(self):
        """
        Calculate and return the area of the circle.

        Returns:
            float: The area, using the formula π * r^2.
        """
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """
        Calculate and return the perimeter (circumference) of the circle.

        Returns:
            float: The perimeter, using the formula 2 * π * r.
        """
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    Represents a rectangle shape.

    Attributes:
        width (float or int): The width of the rectangle.
        height (float or int): The height of the rectangle.
    """

    def __init__(self, width, height):
        """
        Initialize a Rectangle instance.

        Args:
            width (float or int): The width of the rectangle.
            height (float or int): The height of the rectangle.
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Calculate and return the area of the rectangle.

        Returns:
            float: The area, using the formula width * height.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculate and return the perimeter of the rectangle.

        Returns:
            float: The perimeter, using the formula 2 * (width + height).
        """
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Display the area and perimeter of a shape using duck typing.

    This function does not check the type of the object explicitly.
    It assumes the object has .area() and .perimeter() methods.

    Args:
        shape: An object implementing area() and perimeter() methods.
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
