#!/usr/bin/env python3
"""ABC is imported"""
from abc import ABC, abstractmethod

"""Animal class is created"""


def Animal(ABC):
    """Sound method"""
    @abstractmethod
    def sound(self):
        pass


"""Dog subclass"""


def Dog(Animal):
    def sound(self):
        return "Bark"


"""Cat subclass"""


def Cat(Animal):
    def sound(self):
        return "Meow"
