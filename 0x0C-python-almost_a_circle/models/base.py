#!/usr/bin/python3
""" Creating: Base class """
import json


class Base:
    """ Base class core """

    """
    __nb_objects: Private class attr
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Class constructor

        Args:
            id: Base class id

        Notes:
            if id is not None, assign public instance attr id
            otherwise increment __nb_objects and assign it to id
        """
        if (id is not None):
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """
        Returns The JSON representatiion of an obj
        """
        if (list_dictionaries is None) or (list_dictionaries == []):
            return ("[]")
        else:
            return (json.dumps(list_dictionaries))
