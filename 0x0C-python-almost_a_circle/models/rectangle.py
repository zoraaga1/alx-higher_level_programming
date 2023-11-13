#!/usr/bin/python3
"""Create Rectangle class"""


from models.base import Base


class Rectangle(Base):
    """Rectangle class, inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        '''Constructor.'''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        """Prints human readeable string"""
        return (
            f"[Rectangle] ({self.id}) "
            f"{self.x}/{self.y} - {self.width}/{self.height}"
        )

    @property
    def width(self):
        """Getter method for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width value"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        """Getter method for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height value"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """Getter method for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Set the x value"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """Getter method for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Set the y value"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """Returns the area value of the Rectangle instance"""
        return self.height * self.width

    def display(self):
        """Prints in stdout
        the Rectangle instance with the character #,
         taking care of x and y offsets"""
        for _ in range(self.y):
            print()

        for i in range(self.__height):
            for _ in range(self.x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            print()

    def update(self, *args, **kwargs):
        """Assigns arguments to attributes using key-value pairs:
        If *args exists and is not empty, **kwargs must be skipped
        *args: id, width, height, x, y in this order
        **kwargs: key/value pairs representing attributes
        """
        if args:
            attrs = ["id", "width", "height", "x", "y"]
            for i in range(len(args)):
                setattr(self, attrs[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle"""
        return {
            'id' : self.id,
            'width' : self.width,
            'height' : self.height,
            'x' : self.x,
            'y' : self.y
        }
