#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    """
    Executes a function safely.

    Args:
        fct: A function to execute.
        *args: Arguments to pass to the function.

    Returns:
        The result of the function if successful, otherwise None.
        Prints the exception to stderr if an error occurs.
    """
    try:
        return fct(*args)
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None
