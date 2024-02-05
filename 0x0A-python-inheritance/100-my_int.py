#!/usr/bin/python3
""" MyInt class inherits from int """


class MyInt(int):
    """ MyInt class """

    def __eq__(self, int_val):
        """
        Overides equality operator
        Args:
            int_val: obj to be compared
        Returns:
            True if real value of MyInt instance
            is not equal to int_val
            otherwise False
        """
        return (self.real != int_val)

    def __ne__(self, int_val):
        """
        Overides inequality operator

        Args:
            int_val: obj to be compared

        Returns:
            True if real value of MyInt instance
            is equal to int_val
            otherwise False
        """
        return (self.real == int_val)
