#!/usr/bin/python3
""" import class base """
from models.base import Base


class Rectangle(Base):
    """ Rectangle class core """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        child Class constructor

        Args:
            width: rectangle width
            height: rectangle height
            x: rectangle x axis(coord)
            y: rectangle y axis(coord)
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Getter method
        Returns:
            current rectangle width
        """
        return (self.__width)

    @width.setter
    def width(self, value=0):
        """
        Setter method
        Args:
            value: rectangle width value

        Note:
            check if width is int or not
            check if width value is less or equal than 0
            sets width value
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif (value <= 0):
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        Getter method
        Returns:
            current rectangle height
        """
        return (self.__height)

    @height.setter
    def height(self, value=0):
        """
        Setter method
        Args:
            value: rectangle height value

        Note:
            check if height is int or not
            check if height value is less or equal than 0
            sets height value
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif (value <= 0):
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """
        Getter method
        Returns:
            current rectangle x axis coord
        """
        return (self.__x)

    @x.setter
    def x(self, value=0):
        """
        Setter method
        Args:
            value: rectangle x axis (coord) value

        Note:
            check if x value is int or not
            check if x is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif (value < 0):
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """
        Getter method
        Returns:
            current rectangle y axis coord
        """
        return (self.__y)

    @y.setter
    def y(self, value=0):
        """
        Setter method
        Args:
            value: rectangle y axis (coord) value

        Note:
            check if y value is int or not
            check if y is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif (value < 0):
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """
        Calc rectrangle area

        Returns:
            calced area
        """
        return (self.__height * self.__width)

    def display(self):
        """
        Display rectangle using '#' and coordinations

        Returns:
            none
        """
        if self.width == 0 or self.height == 0:
            print()

        [print() for i in range(self.y)]
        for i in range(self.height):
            print(' ' * self.x + '#' * self.width)
