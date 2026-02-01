#!/usr/bin/python3
"""
generation module for Python project
"""


def write_file(filename="", text=""):
    """
    a function that writes a string to a text file (UTF8)
    return: the number of characters written
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
