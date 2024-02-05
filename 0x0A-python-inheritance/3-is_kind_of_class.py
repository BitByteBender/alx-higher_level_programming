#!/usr/bin/python3
""" Same class or inherit from """


def is_kind_of_class(obj, a_class):
    """
    Checks if object is an instance of or inherited

    Args:
        obj: object to be checked
        a_class: comparison class

    Returns:
        True if obj is an instance of, or inherited from
        a_class otheriwse False
    """
    return (isinstance(obj, a_class))
