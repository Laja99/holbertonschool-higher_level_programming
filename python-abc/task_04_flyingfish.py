#!/usr/bin/python3
"""
Module task_04_flyingfish
Demonstrates multiple inheritance in Python with Fish and Bird classes
and a FlyingFish class that inherits from both.
"""


class Fish:
    """Represents a fish with swimming behavior and aquatic habitat."""

    def swim(self):
        """Prints that the fish is swimming."""
        print("The fish is swimming")

    def habitat(self):
        """Prints the natural habitat of the fish."""
        print("The fish lives in water")


class Bird:
    """Represents a bird with flying behavior and aerial habitat."""

    def fly(self):
        """Prints that the bird is flying."""
        print("The bird is flying")

    def habitat(self):
        """Prints the natural habitat of the bird."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    Represents a flying fish that can both swim and fly.

    Inherits from Fish and Bird, overriding methods to reflect dual abilities.
    """

    def swim(self):
        """Prints that the flying fish is swimming."""
        print("The flying fish is swimming!")

    def fly(self):
        """Prints that the flying fish is soaring."""
        print("The flying fish is soaring!")

    def habitat(self):
        """Prints that the flying fish lives both in water and the sky."""
        print("The flying fish lives both in water and the sky!")


if __name__ == "__main__":
    flying_fish = FlyingFish()
    flying_fish.swim()
    flying_fish.fly()
    flying_fish.habitat()

    print(FlyingFish.mro())
    print(FlyingFish.__mro__)
