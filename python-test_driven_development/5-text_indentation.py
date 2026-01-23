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

    result = ""
    i = 0
    n = len(text)

    while i < n:

        result += text[i]

        if text[i] in ".?:":
            result += "\n\n"

            i += 1
            while i < n and text[i] == ' ':
                i += 1
            continue

        i += 1

    lines = result.split('\n')
    for line in lines:
        print(line.rstrip())
