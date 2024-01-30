#!/usr/bin/python3

def matrix_divided(matrix, div):
    """
    Divides all matrix elements

    Args:
        matrix: list of lists of integers or floats
        div: divisor number
    Returns:
        new matrix
    Raises:
        TypeError: if matrix is not a list of integer/floats lists
        or if div is not a number
        ZeroDivisionError: if div is 0
    """
    rslt = []

    if not matrix or all(not row for row in matrix):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    if not all(
        isinstance(number, (int, float))
        for rows in matrix for number in rows if rows
    ):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    if not all(
        len(rows) == len(matrix[0])
        for rows in matrix
    ):
        raise TypeError(
            "Each row of the matrix must have the same size"
        )

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if (div == 0):
        raise ZeroDivisionError("divisionby zero")

    for rows in matrix:
        rws = [round((number / div), 2) for number in rows]
        rslt.append(rws)
    return (rslt)


if (__name__ == "__main__"):
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
