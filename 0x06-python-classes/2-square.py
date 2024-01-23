#!/usr/bin/python3
"""Square class"""


class Square:
    """Square class with a private instance attribute"""
    def __init__(self, size=0):
        """
        Square class constructor
        Args:
            size: integer square size
        Note:
            checks if size is an integer
            checks if size is greater than or equal 0
            sets the size
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
