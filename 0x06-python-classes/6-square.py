#!/usr/bin/python3
"""Square class"""


class Square:
    """Private instance attribute"""
    def __init__(self, size=0, position=(0, 0)):
        """
        Square class constructor
        Args:
            size: integer square size
            position: tuple
        """
        self.__size = size
        self.__position = position

    """Getter method"""
    @property
    def size(self):
        """
        Getter method
        Returns:
            current square size(int)
        """
        return (self.__size)

    """Setter method"""
    @size.setter
    def size(self, value=0):
        """
        Setter Method
        Args:
            size: integer square size
        Note:
            checks if size is an integer
            checks if size is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    """Getter method"""
    @property
    def position(self):
        """
        Getter method
        Returns:
            current square position
        """
        return (self.__position)

    """Setter method"""
    @position.setter
    def position(self, value=(0, 0)):
        """
        Setter method
        Args:
            value: position attribute new value(tuple)
        Note:
            checks if tuple values are both positive integers
        """
        if not (isinstance(value, tuple)
           or len(value) != 2
           or value[0] >= 0 or value[1] >= 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    """Public instance method"""
    def area(self):
        """
        Calc square area
        Returns:
            calculated square area(int)
        """
        return (self.__size ** 2)

    """Public instance method"""
    def my_print(self):
        """
        Prints a square using '#' using position attribute
        if size is 0 prints an empty line
        """
        if self.size == 0:
            print()
        [print() for i in range(self.position[1])]
        [print(' ' * self.position[0] + '#' * self.size)
         for i in range(self.size)]
