#!/usr/bin/python3
"""
generation module for Python project
"""


def read_file(filename=""):
    """function that reads file and prints it"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
