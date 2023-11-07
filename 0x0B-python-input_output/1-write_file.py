#!/usr/bin/python3
"""Create write_file function"""


def write_file(filename="", text=""):
    """Writes a string to a text file
    Returns the number of characters written"""
    with open(filename, "w", encoding="UTF-8") as file:
        char_count = file.write(text)
        return char_count
