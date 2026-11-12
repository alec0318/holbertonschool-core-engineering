#!/usr/bin/env python3
"""Class is created"""


class BaseGeometry:

    """area method"""
    def area(self):
        raise Exception("area() is not implemented")

    """integer_validator method"""
    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
