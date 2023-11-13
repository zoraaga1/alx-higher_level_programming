#!/usr/bin/python3
"""Create Base class"""


import json


class Base:
    """a base of all other classes in this project
    private class attribute: __nb_objects
    class constructor:
        def __init__(self, id=None)"""
    __nb_objects = 0

    def __init__(self, id=None):
        '''Constructor.'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

        @staticmethod
        def save_to_file(cls, list_objs):
            """Writes the JSON string representation of list_objs to a file"""
