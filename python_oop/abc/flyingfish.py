#!/usr/bin/env python3

"""Class fish"""


class Fish:

    """swim method"""
    def swim(self):
        print("the fish is swimming")

    """hebitat method"""
    def habitat(self):
        print("The fish lives in water")


"""class bird"""


class Bird:

    """fly method"""
    def fly(self):
        print("The bird is flying")

    """habitat methd"""
    def habitat(self):
        print("The fish lives in water")


"""FlyFish method"""


class FlyingFish(Fish, Bird):

    """fly method"""
    def fly(self):
        print("The flying fish is soaring!")

    """swim method"""
    def swim(self):
        print("The flying fish is swimming!")

    """habitat method"""
    def habitat(self):
        print("The flying fish lives both in the water and the sky!")


fish = FlyingFish()

fish.fly()
fish.swim()
fish.habitat()

print(FlyingFish.__mro__)
