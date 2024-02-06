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

    def to_json(self):
        """
        Retrieves a dict represnetation of student instance
        Returns:
            dict representation
        """
        return (self.__dict__)
