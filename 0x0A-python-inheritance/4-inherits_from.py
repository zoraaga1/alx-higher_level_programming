#!/usr/bin/python3
"""create inherits_from function"""


def inherits_from(obj, a_class):
    """returns True if the object
    is an instance of a class that inherited
    otherwise false """
    return issubclass(type(obj), a_class) and type(obj) != a_class
