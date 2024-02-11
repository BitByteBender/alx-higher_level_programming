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

    def update(self, *args, **kwargs):
        """
        Update square attrs

        Args:
            *args: attrs assignment values
             1st arg is id attr
             2nd arg is size attr
             3rd arg is x attr
             4th arg is y attr

            **kwargs: keyword args
        """
        if ((args or len(args)) != 0):
            if (len(args) > 0):
                self.id = args[0]
            if (len(args) > 1):
                self.size = args[1]
            if (len(args) > 2):
                self.x = args[2]
            if (len(args) > 3):
                self.y = args[3]
        else:
            if "size" in kwargs:
                self.size = kwargs["size"]
                del kwargs["size"]

            for (key, value) in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Dictionary representation of a Square

        Returns:
            A dict representation
        """
        return (
               {'id': self.id,
                'x': self.x,
                'size': self.size,
                'y': self.y}
               )
