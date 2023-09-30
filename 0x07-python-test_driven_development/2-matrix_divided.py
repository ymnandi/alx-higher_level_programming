#!/usr/bin/python3
"""Module that defines a function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """Function that divides all elements of a matrix.

    Args:
        matrix (list): List of lists of integers or floats.
        div (int or float): Number to divide each element of the matrix.

    Returns:
        list: List of lists of integers or floats. The result of the division.

    Raises:
        TypeError: If matrix is not a list of lists of integers or floats.
        TypeError: If matrix is not a rectangle (all rows should be of the
            same size).
        TypeError: If div is not an integer or float.
        ZeroDivisionError: If div is equal to 0.
    """
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) of \  integers/floats")
    for row in matrix:
        if type(row) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of \  integers/floats")
        for element in row:
            if type(element) is not int and type(element) is not float:
                raise TypeError("matrix must be a matrix (list of lists) of \  integers/floats")
    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div is 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = [[round(element / div, 2) for element in row] for row in matrix]
    return new_matrix
