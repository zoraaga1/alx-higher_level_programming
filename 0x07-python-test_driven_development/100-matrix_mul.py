#!/usr/bin/python3
"""Creat matrix_mul function"""

def matrix_mul(m_a, m_b):
    """Multiplies two matrix"""
    for matrix in (m_a, m_b):
        if not isinstance(matrix, list):
            raise TypeError("m_a must be a list or m_b must be a list")
        if any(not isinstance(row, list) for row in matrix):
            raise TypeError("m_a must be a list of lists or m_b must be a list of lists")

    # Check for empty lists
    if not all(m_a) or not all(m_b):
        raise ValueError("m_a can't be empty or m_b can't be empty")

    # Check for integers or floats in the matrix
    for matrix, name in ((m_a, "m_a"), (m_b, "m_b")):
        for row in matrix:
            if any(not isinstance(element, (int, float)) for element in row):
                raise TypeError(f"{name} should contain only integers or floats")

    # Check for rectangle matrices
    row_sizes_m_a = set(len(row) for row in m_a)
    row_sizes_m_b = set(len(row) for row in m_b)
    if len(row_sizes_m_a) > 1 or len(row_sizes_m_b) > 1:
        raise TypeError("each row of m_a must be of the same size or each row of m_b must be of the same size")

    # Check if matrices can be multiplied
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Perform matrix multiplication
    result = [[sum(a * b for a, b in zip(row_a, col_b)) for col_b in zip(*m_b)] for row_a in m_a]
    return result
