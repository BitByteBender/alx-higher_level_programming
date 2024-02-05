#!/usr/bin/python3
""" Exact same class """


def is_same_class(obj, a_class):
    """
    Checks if object is exactly instance of specified class

    Args:
        obj: object to be checked
        a_class: comparison class

    Returns:
        True if obj is exactly an instance of the specified class
        otherwise False
    """
    return (type(obj) is a_class)
