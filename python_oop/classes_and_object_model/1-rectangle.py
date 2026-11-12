#!/usr/bin/env python3
"""Class is created"""


class Rectangle:
    """Instance is. created"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    """String method is created"""

    def __str__(self):
        return f"Width = {self.width} Height = {self.height}"

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

    """print instance"""
    def my_print(self):
        print(self)
