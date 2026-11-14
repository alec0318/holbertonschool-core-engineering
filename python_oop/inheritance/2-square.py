#!/usr/bin/env python3

"""BaseGeometry is imported"""
BaseGeometry = __import__('base_geometry').BaseGeometry

"""Rectangle is imported"""
Rectangle = __import__('2-rectangle').Rectangle

"""Class Square is created"""


class Square(Rectangle):

    """Instance Method"""
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    """Str method"""
    def __str__(self):
        return f"[Square] {self.__size}/{self.__size}"
