#!/usr/bin/python3
"""
generation module for Python project
"""


def append_write(filename="", text=""):
    """
    a function that append a string to the end of file (UTF8)
    return: the number of characters added
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
