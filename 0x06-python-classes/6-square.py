#!/usr/bin/python3
""""Define a class called Square."""


class Square:
    """
    a class Square that defines a square by:
    (based on 3-square.py)
    Private instance attribute: size:
    property def size(self): to retrieve it
    property setter def size(self, value):
    to set it:
    size must be an integer,
    otherwise raise a TypeError exception
    with the message size must be an integer
    if size is less than 0,
    raise a ValueError exception with the message size must be >= 0
    Instantiation with optional size:
    def __init__(self, size=0):
    Public instance method: def area(self):
    that returns the current square area
    """

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Get the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """Retrieve position"""
        return self.__position

    @position.setter
    def position(self, value):
        """set the position"""
        if not (isinstance(value, tuple) and len(value) == 2 and
                all(isinstance(i, int) and i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Returns the current square area."""

        area = self.__size ** 2

    def my_print(self):
        """
        Prints in stdout the square with the character #.
        if size is equal to 0, print an empty line
        Position is used to offset the square.
        """

        if self.__size == 0:
            print()

        else:
            if self.__position[1] > 0:
                print("\n" * self.__position[1], end="")
            for i in range(self.__size):
                if self.__position[0] > 0:
                    print(" " * self.__position[0], end="")
                print("#" * self.__size)
