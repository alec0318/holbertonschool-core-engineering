#!/usr/bin/env python3
"""ABC is imported"""
from abc import ABC, abstractmethod

"""Animal class is created"""


class Animal(ABC):
    """Sound method"""
    @abstractmethod
    def sound(self):
        pass


"""Dog subclass"""


class Dog(Animal):
    def sound(self):
        return "Bark"


"""Cat subclass"""


class Cat(Animal):
    def sound(self):
        return "Meow"
