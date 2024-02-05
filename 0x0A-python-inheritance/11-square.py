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

    def area(self):
        """ Calculates rectangle area """
        return (self.__width * self.__height)

    def __str__(self):
        """  String representation of rectangle obj """
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))


class Square(Rectangle):
    """ Square class inherits from Rectangle class """
    def __init__(self, size):
        """
        Inits a square obj
        Args:
            size: size of the square
        """
        super().__init__(size, size)

    def __str__(self):
        """ String representation of square obj """
        return "[Square] {}/{}".format(
            self._Rectangle__width,
            self._Rectangle__height
        )
