#!/usr/bin/python3
"""
Module for text indentation
This module defines a function that prints text with 2 new lines
after '.', '?' and ':' characters, removing leading/trailing spaces.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after '.', '?' and ':'.

    Args:
        text (str): The text to process and print.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    result = ""
    for char in text:
        result += char
        if char in ".?:":
            print(result.strip())
            print()
            result = ""
    if result.strip():
        print(result.strip(), end="")
