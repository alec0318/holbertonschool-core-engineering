#!/usr/bin/env python3

"""BaseGeometry is imported"""
BaseGeometry = __import__('base_geometry').BaseGeometry

"""Class Rectangle is created"""


class Rectangle(BaseGeometry):

    """Instance method"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    """Str method"""
    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"

    """area method"""
    def area(self):
        return self.__height * self.__width
