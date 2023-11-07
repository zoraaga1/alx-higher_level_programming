#!/usr/bin/python3
"""Create Student class """


class Student:
    """ defines a student by:
    Public instance attributes:
        first_name
        last_name
        age"""
    def __init__(self, first_name, last_name, age):
        """Defines attr"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns the dictionary description
        with simple data structure"""
        if attrs is not None and all(isinstance(attr, str) for attr in attrs):
            return {attr: getattr(self, attr)
                    for attr in attrs if hasattr(self, attr)}
        else:
            return self.__dict__
