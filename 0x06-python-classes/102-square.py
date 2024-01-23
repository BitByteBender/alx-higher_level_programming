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
        Getter method
        Returns:
            current square size(int)
        """
        return (self.__size)

    """Setter Method"""
    @size.setter
    def size(self, value=0):
        """
        Setter method
        Args:
            size: integer square size
        Note:
            checks if size is an integer
            checks if size is greater than or equal 0
            sets the size
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    """Public instance Method"""
    def area(self):
        """
        Calc Square area
        Returns:
            calculated square area(int)
        """
        return (self.__size ** 2)
    """
    def comparators(self, comp):
        dictResult = {
            "Greater than": self.area() > comp.area(),
            "less than": self.area() < comp.area(),
            "Greater than Or Equal": self.area() >= comp.area(),
            "Less than Or Equal": self.area() <= comp.area(),
            "Equals": self.area() == comp.area(),
            "Not Equal": self.area() != comp.area()
        }
        return (dictResult)
    """

    def __lt__(self, other):
        """
        Less than comparison method
        """
        return (self.area() < other.area())

    def __le__(self, other):
        """
        Less than or equal comparison method
        """
        return (self.area() <= other.area())

    def __eq__(self, other):
        """
        Equal comparison method
        """
        return (self.area() == other.area())

    def __ne__(self, other):
        """
        Not equal comparison method
        """
        return (self.area() != other.area())

    def __gt__(self, other):
        """
        Greater than comparison method
        """
        return (self.area() > other.area())

    def __ge__(self, other):
        """
        Greater than or equal comparison method
        """
        return (self.area() >= other.area())
