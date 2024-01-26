#!/usr/bin/python3

def add_integer(a, b=98):
    try:
        if not isinstance(a, (int, float)):
            raise TypeError("a must be an integer")
        elif not isinstance(b, (int, float)):
            raise TypeError("b must be an integer")
        else:
            return (int(a) + int(b))
    except TypeError as TE:
        return (TE)
