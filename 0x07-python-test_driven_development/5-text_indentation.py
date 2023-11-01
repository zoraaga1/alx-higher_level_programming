#!/usr/bin/python3
"""Write a function that prints
a text with 2 new lines
after each of these characters: ., ? and :"""

def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    new_str = ""
    for ch in text:
        if ch in {'.', '?', ':'}:
            new_str += ch + '\n\n'
        else:
            new_str += ch
    print(new_str)
