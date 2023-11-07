#!/usr/bin/python3
"""Create append_write function"""


def append_write(filename="", text=""):
    """Appends a string to a text file
    Returns the number of characters added"""
    with open(filename, "a", encoding="UTF-8") as file:
        char_count = file.write(text)
        return char_count
    