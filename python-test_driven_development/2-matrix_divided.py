#!/usr/bin/python3
"""Module for matrix division"""


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a divisor
    Args:
        matrix: List of lists containing integers or floats
        div: Number to divide by (integer or float)

    Returns:
        New matrix with all elements divided by div

    Raises:
        TypeError: If matrix is not valid
        ZeroDivisionError: If div is zero
    """
    msg_error = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not isinstance(matrix, list):
        raise TypeError(msg_error)

    if not matrix:
        raise TypeError(msg_error)

    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(msg_error)

    row_size = len(matrix[0])
    for row in matrix:
        if len(row) != row_size:
            raise TypeError("Each row of the matrix must have the same size")

    for row in matrix:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(msg_error)

    new_matrix = []
    for row in matrix:
        new_row = []
        for element in row:
            new_element = round(element / div, 2)
            new_row.append(new_element)
        new_matrix.append(new_row)

    return new_matrix
