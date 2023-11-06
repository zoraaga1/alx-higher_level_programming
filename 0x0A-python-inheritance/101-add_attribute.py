#!/usr/bin/python3
"""Create add_attribute function"""


def add_attribute(obj, attr, value):
    """Adds a new attribute to the object if possible"""
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    obj.__dict__[attr] = value
