#!/usr/bin/python3
"""Create load_from_json_file function"""


import json


def load_from_json_file(filename):
    """Creates an Object fr a “JSON file"""
    with open(filename, "r") as file:
        return json.load(file)
