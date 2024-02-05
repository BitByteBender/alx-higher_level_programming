#!/usr/bin/python3
""" MyList Class """


class MyList(list):
    """ MyList class inherits from list """
    def print_sorted(self):
        """
        Method prints a list in asc order
        """
        sortedList = sorted(self)
        print(sortedList)
