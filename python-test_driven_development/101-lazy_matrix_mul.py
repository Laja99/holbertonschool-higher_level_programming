#!/usr/bin/python3
import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """Multiply two matrices using NumPy"""

    try:
        result = np.matmul(m_a, m_b)
    except ValueError:
        raise ValueError("m_a and m_b can't be multiplied")
    except TypeError:
        raise TypeError("m_a and m_b must be lists of lists of integers or floats")

    return result
