#!/usr/bin/python3
""" Only sub of class """


def inherits_from(obj, a_class):
    """
    Checks object

    Args:
        obj: object to be checked
        a_class: comparison class

    Returns:
        True if obj is an instance of a class that inherited from
        a_class otheriwse False
    """
    return (issubclass(type(obj), a_class) and type(obj) is not a_class)
