#!/usr/bin/python3
""" Load, add, save """
import sys
from os.path import exists

if (__name__ == "__main__"):
    filename = "add_item.json"
    save = __import__("5-save_to_json_file").save_to_json_file
    load = __import__("6-load_from_json_file").load_from_json_file

    if exists(filename):
        elements = load(filename)
    else:
        elements = []

    elements.extend(sys.argv[1:])
    save(elements, filename)
