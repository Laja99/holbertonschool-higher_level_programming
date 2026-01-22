#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """Print the first x elements of a list safely.

    Args:
        my_list (list): List of any elements
        x (int): Number of elements to print

    Returns:
        int: Number of elements printed
    """
    printed = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            printed += 1
        except IndexError:
            break
    print()
    return printed
