#!/usr/bin/python3
"""Create o_json_string function"""
import json


def o_json_string(my_obj):
    """Returns the JSON representation of an object (string)"""
    json_o = json.dumps(my_obj)
