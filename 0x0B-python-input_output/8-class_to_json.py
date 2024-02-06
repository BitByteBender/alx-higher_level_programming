#!/usr/bin/python3
""" Class to JSON """


def class_to_json(obj):
    """
    Function that returns a dict description

    Args:
        obj: an instance of a class

    Returns:
        reutns dict description of object with simple DS
    """
    return (obj.__dict__)
