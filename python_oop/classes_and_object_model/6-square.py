#!/usr/bin/env python3
"""Class is created"""


class Square:
    """Square is created"""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    """Str method is created"""
    def __str__(self):
        if self.__size == 0:
            return ""
        else:
            result = "\n" * self.position[1]
            for i in range(self.__size):
                result += " " * self.position[0]
                result += "#" * self.__size

                if i < self.__size - 1:
                    result += "\n"

            return result

    """Constructor"""
    @property
    def size(self):
        return self.__size

    """Setter"""
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    """Position Cnstructor"""
    @property
    def position(self):
        return self.__position

    """Position setter"""
    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        return self.__size * self.__size

    """My_print"""
    def my_print(self):
        print(self)
