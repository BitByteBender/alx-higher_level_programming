#!/usr/bin/python3
""" From JSON string to object """
import json


def from_json_string(my_str):
    """
    Returns an obj represented by a JSON string

    Args:
        my_str: JSON string

    Returns:
        converted obj from JSON str
    """
    return (json.loads(my_str))
