#!/usr/bin/python3
"""
Module for text indentation
This module defines a function that prints text with a newline
after '.', '?' and ':' characters, removing leading/trailing spaces.
"""


def text_indentation(text):
    """
    Prints a text with a newline after '.', '?' and ':'.

    Args:
        text (str): The text to process and print.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    line = ""
    while i < len(text):
        if text[i] in ".?:":
            line += text[i]
            print(line.strip())   # print punctuation line
            line = ""
            i += 1
            while i < len(text) and text[i] == " ":
                i += 1
        else:
            line += text[i]
            i += 1
    if line.strip():
        print(line.strip(), end="")
