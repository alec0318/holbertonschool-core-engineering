#!/usr/bin/env python3
"""function that appends to the file"""


def append_write(filename="", text=""):

    """opens the file"""
    with open(filename, "a", encoding="utf-8") as file:

        """appends the new string and returns it"""
        return file.write(text)
