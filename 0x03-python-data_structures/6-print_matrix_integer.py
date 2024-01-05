#!/usr/bin/python3

i = 0


def print_matrix_integer(matrix=[[]]):
    global i
    if not matrix[0]:
        print()
        return

    if (i < len(matrix)):
        for j in range(0, len(matrix[i])):
            cond = ' ' if (j < len(matrix[i]) - 1) else '\n'
            print("{}".format(matrix[i][j]), end=cond)
        i += 1
        print_matrix_integer(matrix)
