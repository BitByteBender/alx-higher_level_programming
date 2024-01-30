#!/usr/bin/python3


def say_my_name(first_name, last_name=""):
    """
    function that prints given first & last name
    Args:
        first_name: string first name to be printed
        last_name: string last name to be printed
    Notes:
        checks if first/last name are of type string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))


if (__name__ == "__main__"):
    import doctest
    doctest.testfile("tests/3-say_my_name.txt")
