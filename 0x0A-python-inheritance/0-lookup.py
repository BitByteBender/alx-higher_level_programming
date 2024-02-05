#!/usr/bin/python3

def lookup(obj):
    """
    Returns list of available attrs, methods of obj

    Args:
        obj: object to lookup

    Returns:
        a list of object
    """
    return (dir(obj))
