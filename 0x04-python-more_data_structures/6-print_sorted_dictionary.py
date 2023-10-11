#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    sort_keys = sorted(a_dictionary.keys())

    for key in sort_keys:
        value = a_dictionary[key]
        print("{}: {}".format(key, value))
