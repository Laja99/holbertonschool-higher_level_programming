#!/usr/bin/python3
"""
Module for text indentation
Contains function to print text with a newline after ., ? and :
"""


def text_indentation(text):
    """
    Prints a text with a newline after each of these characters: ., ? and :

    Args:
        text (str): The text to print

    Raises:
        TypeError: If text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    while i < len(text):
        if text[i] in ".?:":
            print(text[i])
            print()
            i += 1
            while i < len(text) and text[i] == " ":
                i += 1
        else:
            print(text[i], end="")
            i += 1
