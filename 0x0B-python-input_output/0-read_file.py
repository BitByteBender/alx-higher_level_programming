#!/usr/bin/python3
""" file reader function """


def read_file(filename=""):
    """
    Function that reads a .txt file

    Args:
        filename: name of file(txt) to read

    """
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end='')
