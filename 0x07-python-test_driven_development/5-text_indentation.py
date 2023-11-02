#!/usr/bin/python3
"""Write a function that prints
a text with 2 new lines
after each of these characters: ., ? and :"""


def text_indentation(text):
    """Print 2 new lines after .,?"""
    str_error = "text must be a string"
    new_text = ""
    flag = False
    if type(text) is not str:
        raise TypeError(str_error)
    new_text = ""
    for char in text:
        new_text += char
        if char in [".", "?", ":"]:
            new_text += "\n\n"

    print(new_text)
