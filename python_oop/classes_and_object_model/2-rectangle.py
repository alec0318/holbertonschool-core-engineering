#!/usr/bin/env python3
"""Class is created"""


class Rectangle:

    """Instance is created"""
    def __init__(self, width, height):
        self.width = width
        self.height = height

    """Str method"""
    def __str__(self):
        return f"The width is {self.width} and height is {self.height}"

    """width constructor"""
    @property
    def width(self):
        return self.__width

    """width setter"""
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    """height constructor"""
    @property
    def height(self):
        return self.__height

    """height setter"""
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    """area method"""
    def area(self):
        return self.__height * self.__width

    """perimeter method"""
    def perimeter(self):
        return 2 * (self.__width + self.__height)

    """my_print method"""
    def my_print(self):
        print(self)
