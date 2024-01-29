#!/usr/bin/python3
"""Simple Rectangle class"""


class Rectangle:
    """public class attributes"""
    number_of_instances = 0
    print_symbol = '#'

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
        Rectangle.number_of_instances += 1

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

    """Public Instance Method"""
    def area(self):
        """
        Calc rectangle area
        Returns:
            calculated rectangle area(int)
        """
        return (self.__height * self.__width)

    """Public Instance Method"""
    def perimeter(self):
        """
        Calc rectangle perimeter
        Returns:
            either 0 if height or width equal 0
            or
            calculated perimeter
        """
        if (self.__width == 0 or self.__height == 0):
            return (0)
        else:
            return (2 * (self.__width + self.__height))

    """
    Instance method that returns informal
    and nicely printable string representation of an instance
    """
    def __str__(self):
        """
        Returns a string representation of the rectangle
        with '#' char
        """
        str_rect = ""
        smbl = self.print_symbol

        if (self.__width == 0 or self.__height == 0):
            return (str_rect)

        for i in range(self.__height):
            str_rect += str(smbl) * self.__width
            if (i != self.__height - 1):
                str_rect += '\n'

        return (str_rect)

    """Instance method"""
    def __repr__(self):
        """
        Instance method that returns an "official" string
        representation of the rectangle object
        """
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    """Instance method"""
    def __del__(self):
        """
        Instance method called when an instance is deleted
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    """Static Method"""
    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Returns the biggest rectangle based on the area
        Args:
            rect_1: rectangle instance 1
            rect_2: rectangle instance 2
        Note:
            raises TypeError: (if rect_1 or rect_2 not instances)
        Returns:
            rect_1 if both have same area value
            or rect_1 if area is the biggest
            otherwise rect_2
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if (rect_1.area() >= rect_2.area()):
            return (rect_1)
        else:
            return (rect_2)
