#!/usr/bin/env python3
"""Parent class is created"""


class BaseGeometry:

    """Area method"""
    def area(self):
        raise Exception("Area is not defined yet")

    """Integer_validator method"""
    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")


"""Class Reactagle is created"""


class Rectangle(BaseGeometry):
    """Instance is created"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
