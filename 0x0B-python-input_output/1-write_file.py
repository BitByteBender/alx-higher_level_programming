#!/usr/bin/python3
""" Write to a file """


def write_file(filename="", text=""):
    """
    Function that writes a string into a text file
    and returns a number count of chars

    Args:
        filename: text file to write into
        text: string to count its chars

    Returns:
        chars count in string
    """
    with open(filename, mode='w', encoding="utf-8") as file:
        return (file.write(text))
