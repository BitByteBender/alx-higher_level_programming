#!/usr/bin/python3

def print_square(size):
    """
    prints a square using '#' char
    Args:
        size: integer size of a square
    Notes:
        raises TypeError if size is not an integer
        or if size is a float less than 0
        raises ValueError if size is less than 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if (size < 0):
        raise ValueError("size must be >= 0")

    [print('#' * size) for i in range(size)]


if (__name__ == "__main__"):
    import doctest
    doctest.testfile("tests/4-print_square.txt")
