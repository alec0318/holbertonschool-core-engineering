#!/usr/bin/env python3
"""Class is created"""


class Square:
    """Instance is created"""

    def __init__(self, size):
        self.size = size

    """Getter is defined"""

    @property
    def size(self):
        return self.__size

    """Setter is defined"""

    @size.setter
    def size(self, value):

        """Validation"""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        elif value < 0:
            raise ValueError("size must be >= 0")

        else:

            self.__size = value

    """Instance mthod for print"""

    def my_print(self):
        if self.__size == 0:
            print()

        else:
            for i in range(self.__size):
                print("#" * self.__size)

    """Instance method for area"""

    def area(self):
        return self.__size * self.__size
