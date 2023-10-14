#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    new_dict = a_dictionary.copy()  # Create a copy of the original dictionary
    for key, val in a_dictionary.items():
        if val == value:
            del new_dict[key]  # Delete the key from the new dictionary
    return new_dict
