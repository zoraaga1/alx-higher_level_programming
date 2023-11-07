#!/usr/bin/python3
"""Create class_to_json function"""


def class_to_json(obj):
    """Returns the dictionary description
    with simple data structure"""
    serializable_data = {}
    for attr in obj.__dict__:
        value = getattr(obj, attr)
        if isinstance(value, (list, dict, str, int, bool)):
            serializable_data[attr] = value
    return serializable_data
