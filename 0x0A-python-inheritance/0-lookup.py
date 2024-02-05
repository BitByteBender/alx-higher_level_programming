#!/usr/bin/python3

def lookup(obj):
    """
    Returns list of available attrs, methods of obj
    """
    return (dir(obj))
