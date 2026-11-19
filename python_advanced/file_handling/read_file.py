#!/usr/bin/env python3
"""function that opens a file"""

def read_file(filename=""):
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read())
