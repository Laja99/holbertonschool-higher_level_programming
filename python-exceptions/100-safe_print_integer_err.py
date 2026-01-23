#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    """
    Prints an integer with a newline.
    Returns True if value is an integer and printed successfully.
    Otherwise, prints error to stderr and returns False.
    """
    try:
        print("{:d}".format(value))
        return True
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return False
