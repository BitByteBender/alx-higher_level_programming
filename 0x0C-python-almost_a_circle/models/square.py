#!/usr/bin/python3
""" import class rectangle """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square class core """

    def __init__(self, size, x=0, y=0, id=None):
        """
        child Class constructor

        Args:
            size: square size
            x: square x axis(coord)
            y: square y axis(coord)
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Getter method
        Returns:
            current square size
        """
        return (self.width)

    @size.setter
    def size(self, value=0):
        """
        Setter method

        Args:
            value: square width value
        """
        self.width = value
        self.height = value

    def __str__(self):
        """
        Returns string representation of rectangle instance

        using format:
            [Rectangle] (<id>) <x>/<y> - <width>/<height>

        Returns:
            formatted string representation
        """
        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                  self.y, self.width))
