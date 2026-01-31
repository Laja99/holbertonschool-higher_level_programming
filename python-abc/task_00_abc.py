#!/usr/bin/env python3
"""
Abstract class Animal and its subclasses Dog and Cat.
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract class representing an animal"""

    @abstractmethod
    def sound(self):
        """Abstract method to be implemented by subclasses"""
        pass


class Dog(Animal):
    """Dog class implementing Animal abstract class"""
    def sound(self):
        return "Bark"


class Cat(Animal):
    """Cat class implementing Animal abstract class"""
    def sound(self):
        return "Meow"
