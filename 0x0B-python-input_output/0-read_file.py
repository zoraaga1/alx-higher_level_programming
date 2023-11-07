#!/usr/bin/python3
"""Create read_file function"""


def read_file(filename=""):
    """Reads a text file (UTF8) and prints it to stdout:"""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                print(line, end='')  # Printing each line without an additional newline
    except Exception as e:
        print("An error occurred:", e)
