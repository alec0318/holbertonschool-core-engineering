#!/usr/bin/env python3
"""function that opens a file"""

def read_file(filename=""):

    """opens and reads the file"""
    with open(filename, "r", encoding="utf-8") as file:
        
        """prints the file"""
        print(file.read())
