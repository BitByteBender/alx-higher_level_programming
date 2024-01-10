#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    newMatrix = []
    if not matrix:
        return (None)
    else:
        for i in range(0, len(matrix)):
            rowFiller = []
            for j in range(0, len(matrix[i])):
                rowFiller.append(matrix[i][j] ** 2)
            newMatrix.append(rowFiller)
        return (newMatrix)
