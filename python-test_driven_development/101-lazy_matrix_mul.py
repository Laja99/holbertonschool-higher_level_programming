#!/usr/bin/python3
"""
This module provides a function lazy_matrix_mul
that multiplies two matrices using NumPy.
"""


import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiply two matrices using NumPy"""

    result = np.matmul(m_a, m_b)
    return result
