#!/usr/bin/python3
"""Square class"""


class Square:
    """Private instance attribute"""
    def __init__(self, size=0):
        """
        Square class constructor
        Args:
            size: integer square size
        """
        self.__size = size

    """Getter Method"""
    @property
    def size(self):
        """
        Getter Method
        Returns:
            current square size(int)
        """
        return (self.__size)

    """Setter Method"""
    @size.setter
    def size(self, value=0):
        """
        Setter Method
        Args:
            size: integer square size
        Note:
            checks if size is an integer
            checks if size is greater than 0
            sets the __size attribute
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    """Public instance method"""
    def area(self):
        """
        Calc square area
        Returns:
            calculated quare area(int)
        """
        return (self.__size ** 2)

    """Public instance method"""
    def my_print(self):
        """
        Prints a square pattern
        Note:
            if size is 0 prints empty line
        """
        if self.size == 0:
            print()
        else:
            for i in range(self.size):
                print("#" * self.size)
