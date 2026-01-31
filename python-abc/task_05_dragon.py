#!/usr/bin/env python3
"""Dragon with Swim and Fly abilities using mixins."""

class SwimMixin:
    """Adds swimming ability to a creature"""
    def swim(self):
        print("The creature swims!")

class FlyMixin:
    """Adds flying ability to a creature"""
    def fly(self):
        print("The creature flies!")

class Dragon(SwimMixin, FlyMixin):
    """Dragon class that can swim, fly, and roar"""
    def roar(self):
        print("The dragon roars!")


if __name__ == "__main__":
    draco = Dragon()
    draco.swim()
    draco.fly()
    draco.roar()
