#!/usr/bin/python3
"""Dragon with Swim and Fly abilities using mixins."""


class SwimMixin:
    """Mixin that adds swimming ability to a creature."""
    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """Mixin that adds flying ability to a creature."""
    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Dragon class that inherits from both SwimMixin and FlyMixin."""
    def roar(self):
        """Make the dragon roar."""
        print("The dragon roars!")

    if __name__ == "__main__":
        draco = Dragon()
        draco.swim()
        draco.fly()
        draco.roar()
