#!/usr/bin/python3
"""creat a MagicClass"""
import math


class MagicClass:
    """create a MagicClass"""
    def __init__(self, radius=0):
        if not (isinstance(radius, int) or isinstance(radius, float)):
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        return math.pi * self.__radius ** 2

    def circumference(self):
        return 2 * math.pi * self.__radius
