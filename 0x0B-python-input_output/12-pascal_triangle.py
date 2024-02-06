#!/usr/bin/python3
""" Pascal's Triangle """


def pascal_triangle(n):
    """
    Returns pascal's triangle of n(integers)

    Args:
        n: number of rows in pascal's triangle

    Returns:
        list of lists of integers representing pascal's triangle of n
    """
    if (n <= 0):
        return ([])

    trg = []

    for r in range(n):
        rw = [1] * (r + 1)
        if (r > 1):
            back = trg[-1]
            c = 1
            while (c < r):
                rw[c] = back[c - 1] + back[c]
                c += 1
        trg.append(rw)
    return (trg)
