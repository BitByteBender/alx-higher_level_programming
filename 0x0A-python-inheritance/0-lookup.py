#!/usr/bin/python3
""" lookup Function """


def lookup(obj):
    """
    Returns list of available attrs, methods of obj

    Args:
        obj: object to lookup

    Returns:
        a list of object
    """
    return (dir(obj))
