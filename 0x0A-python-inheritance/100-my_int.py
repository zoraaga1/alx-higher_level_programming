#!/usr/bin/python3
"""Square class Module"""


class MyInt(int):
    """Class MyInt inherits from int"""
    def __eq__(self, other):
        """Inverts == operator"""
        return super().__ne__(other)

    def __ne__(self, other):
        """Inverts != operator"""
        return super().__eq__(other)
