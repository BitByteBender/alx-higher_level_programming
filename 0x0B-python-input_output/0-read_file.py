#!/usr/bin/python3

def read_file(filename=""):
    """
    Function that reads file

    Args:
        filename: name of file(txt) to read
    """
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end='')
