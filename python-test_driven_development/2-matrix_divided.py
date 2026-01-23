#!/usr/bin/python3
"""
This module provides a function to divide all elements of a matrix by a divisor.
"""
def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div.

    Args:
        matrix (list of lists of int/float): The matrix to divide
        div (int/float): The number to divide by

    Returns:
        list of lists of floats: A new matrix with all elements divided by div

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats
        TypeError: If each row of the matrix is not of the same size
        TypeError: If div is not a number
        ZeroDivisionError: If div is 0
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists of integers/floats)")
    if len(matrix) == 0 or any(len(row) != len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if any(not all(isinstance(el, (int, float)) for el in row) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists of integers/floats)")

    new_matrix = []
    for row in matrix:
        new_row = [round(el / div, 2) for el in row]
        new_matrix.append(new_row)
    
    return new_matrix
