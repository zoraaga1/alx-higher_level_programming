#!/usr/bin/python3
"""Create Student class """


class Student:
    """ defines a student by:
    Public instance attributes:
        first_name
        last_name
        age"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns the dictionary description
    with simple data structure"""
    serializable_data = {}
    for attr in obj.__dict__:
        value = getattr(obj, attr)
        if isinstance(value, (list, dict, str, int, bool)):
            serializable_data[attr] = value
    return serializable_data
