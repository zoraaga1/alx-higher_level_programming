#!/usr/bin/python3
"""Create Base class"""


import json
import csv


class Base:
    """A base class for other classes in this project."""
    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries."""
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file."""
        if list_objs is None:
            list_objs = []

        filename = f"{cls.__name__}.json"

        with open(filename, 'w') as file:
            json_string = cls.to_json_string([obj.to_dictionary()
                                              for obj in list_objs])
            file.write(json_string)

    @classmethod
    def from_json_string(cls, json_string):
        """Returns the list of the JSON string representation json_string."""
        if json_string is None or not json_string:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set."""
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)
        else:
            dummy_instance = None

        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def dummy(cls, *args):
        """Returns a dictionary with
        attributes and their corresponding values."""
        dummy_instance = cls(1, 1)  # Create a dummy instance
        dummy_instance.update(*args)
        return dummy_instance.to_dictionary()

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances from a JSON file."""
        filename = f"{cls.__name__}.json"
        try:
            with open(filename, 'r') as file:
                json_string = file.read()
                dictionaries = cls.from_json_string(json_string)
                return [cls.create(**d) for d in dictionaries]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes and saves instances to a CSV file."""
        filename = cls.__name__ + ".csv"
        if cls.__name__ == "Rectangle":
            csv_format = ["id", "width", "height", "x", "y"]
        if cls.__name__ == "Square":
            csv_format = ["id", "size", "x", "y"]

        with open(filename, mode="w") as data:
            writer = csv.DictWriter(data, fieldnames=csv_format)
            [writer.writerow(item.to_dictionary()) for item in list_objs]

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes and returns a list of instances from a CSV file."""
        filename = f"{cls.__name__}.csv"
        try:
            with open(filename, 'r', newline='') as file:
                reader = csv.reader(file)
                instances = []
                for row in reader:
                    instance = cls.create_from_csv(row)
                    instances.append(instance)
                return instances
        except FileNotFoundError:
            return []


    @staticmethod
    def draw(list_rectangles, list_squares):
        """Opens a window and draws all the Rectangles and Squares"""
        screen = turtle.Screen()
        screen.title("Turtle Drawing")

        # Draw Rectangles
        for rectangle in list_rectangles:
            turtle.penup()
            turtle.goto(rectangle.x, rectangle.y)
            turtle.pendown()
            turtle.forward(rectangle.width)
            turtle.right(90)
            turtle.forward(rectangle.height)
            turtle.right(90)
            turtle.forward(rectangle.width)
            turtle.right(90)
            turtle.forward(rectangle.height)
            turtle.right(90)

        # Draw Squares
        for square in list_squares:
            turtle.penup()
            turtle.goto(square.x, square.y)
            turtle.pendown()
            for _ in range(4):
                turtle.forward(square.size)
                turtle.right(90)

        turtle.done()
