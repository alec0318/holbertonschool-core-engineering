#!/usr/bin/env python3
"""Class is created"""


class Square:
    """Instance is created"""

    def __init__(self, size=0):
        self.size = size

    """Getter is created"""

    @property
    def size(self):
        return self.__size

    """Setter is created"""

    @size.setter
    def size(self, value):
        """Validation for size"""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        elif value < 0:
            raise ValueError("size must be >= 0")

        else:
            self.__size = value

    """Area calculation"""

    def area(self):
        return self.__size * self.__size
