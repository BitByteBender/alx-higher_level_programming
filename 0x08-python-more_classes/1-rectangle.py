#!/usr/bin/python3
"""Simple Rectangle class"""


class Rectangle:
    """Private instance attribute"""
    def __init__(self, width=0, height=0):
        """
        Rectangle class constructor
        Args:
            width: integer rectangle width
            height: integer rectangle height
        """
        self.__height = height
        self.__width = width

    """Getter Method"""
    @property
    def width(self):
        """
        Getter Method
        Returns:
            current square width(int)
        """
        return (self.__width)

    """Setter Method"""
    @width.setter
    def width(self, value=0):
        """
        Setter method
        Args:
            value: rectangle width value
        Note:
            checks if width is an integer
            checks if width value is < 0
            sets width value
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif (value < 0):
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    """Getter Method"""
    @property
    def height(self):
        """
        Getter method
        Returns:
            current square height
        """
        return (self.__height)

    """Setter Method"""
    @height.setter
    def height(self, value=0):
        """
        Setter method
        Args:
            value: rectanlge height value
        Note:
            checks if height is an integer
            checks if height value is < 0
            sets height value
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif (value < 0):
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
