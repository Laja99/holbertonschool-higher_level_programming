#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """Print x elements of a list safely.

    Args:
        my_list (list): List of any type
        x (int): Number of elements to print

    Returns:
        int: Number of elements printed
    """
    printed = 0
    i = 0

    while i < x:
        try:
            print("{}".format(my_list[i]), end="")
            printed += 1
        except IndexError:
            break
        i += 1

    print()
    return printed
