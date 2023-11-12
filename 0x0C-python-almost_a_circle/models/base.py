#!/usr/bin/python3
"""Create Base class"""


class Base:
    """a base of all other classes in this project
    private class attribute: __nb_objects
    class constructor:
        def __init__(self, id=None)"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
