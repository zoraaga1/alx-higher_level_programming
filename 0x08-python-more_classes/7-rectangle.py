#!/usr/bin/python3
"""Create Rectangla class"""


class Rectangle:
    """Instantiation with optional width and height:
        def __init__(self, width=0, height=0):
        private instance attribute: width,
        with property and setter
        private instance attribute: height,
        with property and setter"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """Str method for print from main module."""
        if self.__height == 0 or self.__width == 0:
            return ''
        rect = []
        for i in range(self.__height):
            [rect.append(str(self.print_symbol)) for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
                return ("".join(rect))

    def __repr__(self):
        """Returns a string representation of the rectangle"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Prints Bye rectangle... if an instance was deleted"""
        Rectangle.number_of_instances -= 1
        print('Bye rectangle...')

    @property
    def width(self):
        """Retrieves the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set the width of the rectangle """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """set the height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the rectangle perimete"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2*(self.__width + self.__height)
