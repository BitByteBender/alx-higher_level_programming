#!/usr/bin/python3
""" Append to a file """


def append_write(filename="", text=""):
    """
    Function that appends string into a text file
    and returns a number count of chars added

    Args:
        filename: text file to write/append into
        text: string to append to file

    Notes:
        creates if file and append if it doesn't exist

    Returns:
        number of chars added to file
    """
    with open(filename, mode='a', encoding="utf-8") as file:
        return (file.write(text))
