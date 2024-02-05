#!/usr/bin/python3
""" BaseGeometry class """


class BaseGeometry:
    """ Public instance method """
    def area(self):
        """
        Method that raises an exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        validates value

        Args:
            name: value name being validated
            value: value to be validated

        Notes:
            If value is not an intger raise TypeError
            If value is less or equal 0 raise ValueError
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """ Rectangle class inherits from BaseGeometry main class """
    def __init__(self, width, height):
        """
        Inits a rectangle obj

        Args:
            width: rectanlge widht
            height: rectangle height
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
