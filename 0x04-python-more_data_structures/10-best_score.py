#!/usr/bin/python3

def best_score(a_dictionary):
    if not a_dictionary:
        return None

    max_value = max(a_dictionary.values())
    max_keys = [key for key, value in
                a_dictionary.items() if value == max_value]

    if len(max_keys) == 1:
        return max_keys[0]
    else:
        return max_keys
