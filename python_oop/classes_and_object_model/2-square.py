#!/usr/bin/env python3
"""Clas is defined"""


class Square:
    """Constructor"""

    def __init__(self, size=0):
        """Validation"""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        elif size < 0:
            raise ValueError("size must be >= 0")

        else:
            self.__size = size
