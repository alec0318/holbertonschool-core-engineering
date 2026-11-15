#!/usr/bin/env python3

"""Math and ABC is imported"""
import math
from abc import ABC, abstractmethod


"""Class shape is created"""


class Shape(ABC):
    """abstract method area"""
    @abstractmethod
    def area(self):
        pass

    """abstract method perimeter"""
    @abstractmethod
    def perimeter(self):
        pass


"""subclass circle"""


class Circle(Shape):
    """instance method for radius"""
    def __init__(self, radius):
        self.__radius = radius

    """perimeter perimeter method for circle"""
    def perimeter(self):
        return 2 * math.pi * self.__radius

    """instance area method for circle"""
    def area(self):
        return math.pi * self.__radius ** 2


"""subclass Rectangle"""


class Rectangle(Shape):
    """"instance method"""
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    """area"""
    def area(self):
        return self.__width * self.__height

    """perimeter"""
    def perimeter(self):
        return 2 * (self.__width + self.__height)


"""shape_info function"""


def shape_info(shape):
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
