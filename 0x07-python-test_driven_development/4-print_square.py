#!/usr/bin/python3
"""Create print_square function"""


def print_square(size):
    """prints a square of #"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    if size == 0:
        return

    for _ in range(size):
        print("#" * size)
