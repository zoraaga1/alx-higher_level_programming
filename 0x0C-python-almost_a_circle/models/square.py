#!/usr/bin/python3
"""Create Square class"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class, inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Class constructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """String representation of Square"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """Returns the size value"""
        return self.width

    @size.setter
    def size(self, value):
        """Set size value"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.width = value

    def update(self, *args, **kwargs):
        """Assigns arguments to attributes using key-value pairs:
        If *args exists and is not empty, **kwargs must be skipped
        *args: id, size, x, y in this order
        **kwargs: key/value pairs representing attributes
        """
