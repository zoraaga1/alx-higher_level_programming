#!/usr/bin/python3
"""Create append_after function """


def append_after(filename="", search_string="", new_string=""):
    """Inserts new_string after each line
    containing search_string in the filename"""
    with open(filename, "r") as file:
        lines = file.readlines()

    with open(filename, "w") as file:
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string + "\n")
