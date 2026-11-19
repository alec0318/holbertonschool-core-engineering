#!/usr/bin/env python3
"""Function that writes to a file"""


def write_file(filename="", text=""):

    """Opens the file"""
    with open(filename, "w", encoding="utf-8") as file:

        """Prints the new line to the file"""
        return file.write(text, end="")
