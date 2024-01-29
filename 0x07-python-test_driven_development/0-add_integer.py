#!/usr/bin/python3
"""Add integer function"""


def add_integer(a, b=98):
    """
    add_integer - sum of to integers
    Args:
        a: first int to be added
        b: second int to be added

    Raises:
        TypeError as TE:  if either a or b are not (int/float)

    Returns:
        either the sum of a and b or TypeError
    """
    try:
        if not isinstance(a, (int, float)):
            raise TypeError("a must be an integer")
        elif not isinstance(b, (int, float)):
            raise TypeError("b must be an integer")
        else:
            return (int(a) + int(b))
    except TypeError as TE:
        return (TE)


if (__name__ == "__main__"):
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
