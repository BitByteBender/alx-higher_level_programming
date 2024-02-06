#!/usr/bin/python3
""" Load Object from a JSON file """
import json


def load_from_json_file(filename):
    """
    Loads an obj from a JSON file

    Args:
        filename: file to load from

    Returns:
        obj loaded from JSON file
    """
    with open(filename, mode='r', encoding="utf-8") as file:
        return (json.load(file))
