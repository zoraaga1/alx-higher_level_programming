#!/usr/bin/python3
"""Create to_json_string function"""


import json


def to_json_string(my_obj):
    """Returns the JSON representation of an object (string)"""
    return json.dumps(my_obj)
