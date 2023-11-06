#!/usr/bin/python3
"""Square class Module"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Inherits Rectangle"""
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__sizeof = size
    
    def area(self):
        return self.__width * self.__height
