#!/usr/bin/python3
"""
Module that defines a function to print a person's full name.

Provides say_my_name(first_name, last_name="") which prints:
"My name is <first name> <last name>" with correct spacing.
"""


def say_my_name(first_name, last_name=""):
    """
    Print 'My name is <first_name> <last_name>' with proper spacing.

    Args:
        first_name (str): The first name.
        last_name (str, optional): The last name. Defaults to "".

    Raises:
        TypeError: If first_name is not a string.
        TypeError: If last_name is not a string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    if first_name and last_name:
        print(f"My name is {first_name} {last_name}")
    elif first_name:
        print(f"My name is {first_name}")
    elif last_name:
        print(f"My name is {last_name}")
    else:
        print("My name is")
