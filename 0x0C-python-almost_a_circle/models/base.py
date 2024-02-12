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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns The JSON representatiion of an obj

        Args:
            list_dictionaries: dict list

        Returns:
          JSON str representaion
        """
        if (list_dictionaries is None) or (list_dictionaries == []):
            return ("[]")
        else:
            return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes and overrides an obj to a json file

        Args:
            cls: class name
            list_objs: list of instances
        """
        if (list_objs is None):
            list_objs = []

        with open((cls.__name__ + ".json"), mode='w',
                  encoding="utf-8") as file:
            dicts = [obj.to_dictionary() for obj in list_objs]
            file.write(cls.to_json_string(dicts))

    @staticmethod
    def from_json_string(json_string):
        """
        Returns an obj represented by JSON string

        Args:
            json_string: JSON string

        Returns:
            converted obj from JSON str
        """
        if (json_string is None) or (json_string == "[]"):
            return ([])
        else:
            return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """
        Creates an instance with all set attrs

        Args:
            **dictionary: dict of attrs

        Returns:
            instance with attrs
        """
        if (cls.__name__ == "Square"):
            dum = cls(1)
        elif (cls.__name__ == "Rectangle"):
            dum = cls(1, 1)
        else:
            return (None)

        dum.update(**dictionary)
        return (dum)
