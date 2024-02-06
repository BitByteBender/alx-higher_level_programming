#!/usr/bin/python3
""" Save Object to a file """
import json


def save_to_json_file(my_obj, filename):
    """
    Writes or appends an obj to a txt file, using JSON representation

    Args:
        my_obj: object to be saved
        filename: file to save into
    """
    with open(filename, mode='w', encoding="utf-8") as file:
        return (json.dump(my_obj, file, sort_keys=True))
