#!/usr/bin/python3
"""Square class Module"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Inherits Rectangle"""
    def __init__(self, size):
        super().__init__(size, size)

    def area(self):
        return self.__width * self.__height
