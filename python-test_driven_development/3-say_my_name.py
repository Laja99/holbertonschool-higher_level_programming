#!/usr/bin/python3
"""
Module for printing name
Contains function to print "My name is <first name> <last name>"
"""


def say_my_name(first_name, last_name=""):
    """
    Prints "My name is <first_name> <last_name>"

    Args:
        first_name (str): The first name
        last_name (str, optional): The last name. Defaults to "".

    Raises:
        TypeError: If first_name is not a string
        TypeError: If last_name is not a string
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    if not first_name and not last_name:
        print("My name is")
    elif not last_name:
        print(f"My name is {first_name}")
    elif not first_name:
        print(f"My name is {last_name}")
    else:
        print(f"My name is {first_name} {last_name}")
