#!/usr/bin/python3
"""Create Square class"""

from rectangle import Rectangle

class Square(Rectangle):
    """Square class, inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Class constructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """String representation of Square"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"