#!/usr/bin/env python3

"""class SwimMixin"""


class SwimMixin:

    """swim method"""
    def swim(self):
        print("The creature swims!")


"""class FlyMixin"""


class FlyMixin:

    """fly method"""
    def fly(self):
        print("The creature flies!")


"""class Dragon"""


class Dragon(SwimMixin, FlyMixin):

    """roar method"""
    def roar(self):
        print("The dragon roars!")


dra = Dragon()

dra.swim()
dra.fly()
dra.roar()
