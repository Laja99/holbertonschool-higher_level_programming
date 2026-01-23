#!/usr/bin/python3
"""
Module for text indentation
Contains function to print text with 2 new lines after ., ? and :
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text (str): The text to print

    Raises:
        TypeError: If text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    n = len(text)

    while i < n:
        # Skip spaces at the beginning of a line
        if text[i] == ' ' and (i == 0 or text[i-1] in '.?:' or
                               text[i-1] == '\n'):
            i += 1
            continue

        print(text[i], end='')

        if text[i] in '.?:':
            print("\n")
            i += 1
            # Skip spaces after punctuation
            while i < n and text[i] == ' ':
                i += 1
            continue

        i += 1
