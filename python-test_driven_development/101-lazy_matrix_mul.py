#!/usr/bin/python3
"""
This module provides a function lazy_matrix_mul
that multiplies two matrices using NumPy.
"""


import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiply two matrices using NumPy"""

    try:
        result = np.matmul(m_a, m_b)
    except ValueError:
        raise ValueError("m_a and m_b can't be multiplied")
    except TypeError:
        e = "m_a and m_b must be lists of lists of integers or floats"
        raise TypeError(e)

    return result
