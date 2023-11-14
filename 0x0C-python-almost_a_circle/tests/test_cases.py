import unittest
from models.rectangle import Rectangle
from models.square import Square
from models.base import Base


class TestBase(unittest.TestCase):

    def test_init(self):
        # Test Case 1: Creating an instance without specifying id
        obj1 = Base()
        self.assertEqual(obj1.id, 1)

        # Test Case 2: Creating an instance with a specific id
        obj2 = Base(5)
        self.assertEqual(obj2.id, 5)

    def test_to_json_string(self):
        # Test Case 1: Empty list
        result = Base.to_json_string([])
        self.assertEqual(result, "[]")

        # Test Case 2: List of dictionaries
        result = Base.to_json_string([{'id': 1, 'name': 'object1'}, {'id': 2, 'name': 'object2'}])
        self.assertEqual(result, '[{"id": 1, "name": "object1"}, {"id": 2, "name": "object2"}]')

    def test_from_json_string(self):
        # Test Case 1: Empty string
        result = Base.from_json_string("")
        self.assertEqual(result, [])

        # Test Case 2: JSON string
        result = Base.from_json_string('[{"id": 1, "name": "object1"}, {"id": 2, "name": "object2"}]')
        self.assertEqual(result, [{'id': 1, 'name': 'object1'}, {'id': 2, 'name': 'object2'}])

    def test_create(self):
        # Test Case 1: Creating a Rectangle instance
        result = Base.create(id=1, width=3, height=4)
        self.assertIsInstance(result, Rectangle)

        # Test Case 2: Creating a Square instance
        result = Base.create(id=1, size=5)
        self.assertIsInstance(result, Square)

    def test_dummy(self):
        # Test Case 1: Creating a dummy Rectangle dictionary
        result = Base.dummy(id=1, width=3, height=4)
        self.assertEqual(result, {'id': 1, 'width': 3, 'height': 4})

        # Test Case 2: Creating a dummy Square dictionary
        result = Base.dummy(id=1, size=5)
        self.assertEqual(result, {'id': 1, 'size': 5})

    def test_load_from_file_and_save_to_file(self):
        # Test Case 1: Saving to file and loading from file
        r1 = Rectangle(3, 4, 1, 2)
        r2 = Rectangle(5, 6, 3, 4)
        Rectangle.save_to_file([r1, r2])
        loaded_rectangles = Rectangle.load_from_file()
        self.assertEqual(len(loaded_rectangles), 2)
        self.assertIsInstance(loaded_rectangles[0], Rectangle)

    def test_load_from_file_csv_and_save_to_file_csv(self):
        # Test Case 1: Saving to CSV file and loading from CSV file
        r1 = Rectangle(3, 4, 1, 2)
        r2 = Rectangle(5, 6, 3, 4)
        Rectangle.save_to_file_csv([r1, r2])
        loaded_rectangles_csv = Rectangle.load_from_file_csv()
        self.assertEqual(len(loaded_rectangles_csv), 2)
        self.assertIsInstance(loaded_rectangles_csv[0], Rectangle)

    def test_draw(self):
        # Test Case: Drawing using turtle
        list_rectangles = [Rectangle(100, 40), Rectangle(90, 110, 30, 10), Rectangle(20, 25, 110, 80)]
        list_squares = [Square(35), Square(15, 70, 50), Square(80, 30, 70)]

        # Not testing the actual drawing, just checking if the function runs without errors
        Base.draw(list_rectangles, list_squares)
