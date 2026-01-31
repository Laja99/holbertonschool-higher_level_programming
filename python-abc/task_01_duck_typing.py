#!/usr/bin/env python3
"""
Task 01: Abstract Shape class with Circle and Rectangle implementations,
demonstrating duck typing with a shape_info function.
"""

from abc import ABC, abstractmethod
import math

class Shape(ABC):
    """Abstract base class for shapes"""
    
    @abstractmethod
    def area(self):
        """Calculate the area of the shape"""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate the perimeter of the shape"""
        pass


class Circle(Shape):
    """Circle shape implementing Shape abstract class"""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Return area of the circle"""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Return perimeter of the circle"""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle shape implementing Shape abstract class"""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """Return area of the rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Return perimeter of the rectangle"""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Prints the area and perimeter of any object that has .area() and .perimeter()
    """
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())
