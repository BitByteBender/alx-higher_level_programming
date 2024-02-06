#!/usr/bin/python3
""" Student to JSON """


class Student:
    """ """
    def __init__(self, first_name, last_name, age):
        """
        Init a student instance with first, last name & age
        Args:
            first_name: student first name
            last_name: student last name
            age: student age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dict represnetation of student instance

        Args:
            attrs: list of attributes

        Returns:
            dict representation
        """
        if (attrs is not None):
            res = {}
            for attr in attrs:
                if hasattr(self, attr):
                    res[attr] = getattr(self, attr)
            return (res)
        else:
            return (self.__dict__)

    def reload_from_json(self, json):
        """
        Replaces all attrs of the Student instance

        Args:
            json: dictionary contains name and value attrs
        """
        for (key, value) in json.items():
            setattr(self, key, value)
