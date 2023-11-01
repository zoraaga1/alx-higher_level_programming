#!/usr/bin/python3
""" a function that divides all elements of a matrix."""


def matrix_divided(matrix, div):
    """dived matrix using div number"""
    new_matrix = []
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    typeError = "matrix must be a matrix (list of lists) of integers/floats"
    if (
        not all(isinstance(row, list) for row in matrix) or
        not all(isinstance(element, (int, float))
                for row in matrix for element in row)
    ):
        raise TypeError(typeError)
    size_error = "Each row of the matrix must have the same size"
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError(size_error)
    for row in matrix:
        new_row = [round(element / div, 2) for element in row]
        new_matrix.append(new_row)

    return new_matrix
