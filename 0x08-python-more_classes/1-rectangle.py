#!/usr/bin/python3
"""Create Rectangla class"""


class Rectangle:
    """Instantiation with optional width and height:
        def __init__(self, width=0, height=0):
        private instance attribute: width,
        with property and setter
        private instance attribute: height,
        with property and setter"""

    def __init__(self, width=0, height=0):
        self._width = width
        self._height = height
    
    @property
    def width(self):
        """Retrieves the width"""
        return self._width

    @width.setter
    def width(self, value):
        """set the width of the rectangle """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value
    @property
    def height(self):
        """Retrieves the height"""
        return self._height
    
    @height.setter
    def height(self, value):
        """set the height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value
