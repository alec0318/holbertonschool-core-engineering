#!/usr/bin/env python3
"""Parent class is imported"""

BaseGeometry = __import__('base_geometry').BaseGeometry

"""Class Reactagle is created"""


class Rectangle(BaseGeometry):
    """Instance is created"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
