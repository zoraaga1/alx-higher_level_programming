#!/usr/bin/python3
"""Create Base class"""


import json
import csv


class Base:
	"""a base of all other classes in this project
	private class attribute: __nb_objects
	class constructor:
		def __init__(self, id=None)"""
	__nb_objects = 0

	def __init__(self, id=None):
		'''Constructor.'''
		if id is not None:
			self.id = id
		else:
			Base.__nb_objects += 1
			self.id = Base.__nb_objects

	@staticmethod
	def to_json_string(list_dictionaries):
		"""Returns the JSON string representation of list_dictionaries"""
		if list_dictionaries is None or not list_dictionaries:
			return "[]"
		else:
			return json.dumps(list_dictionaries)

	@classmethod
	def save_to_file(cls, list_objs):
		"""Writes the JSON string representation of list_objs to a file"""
		if list_objs is None:
			list_objs = []

		filename = f"{cls.__name__}.json"

		with open(filename, 'w') as file:
			json_string = cls.to_json_string([obj.to_dictionary()
											  for obj in list_objs])
			file.write(json_string)

	@staticmethod
	def from_json_string(json_string):
		"""Returns the list of the JSON string representation json_string"""
		if json_string is None or not json_string:
			return []
		else:
			return json.loads(json_string)

	@classmethod
	def create(cls, **dictionary):
		"""Returns an instance with all attributes already set"""
		if cls.__name__ == "Rectangle":
			dummy_instance = cls(1, 1)
		elif cls.__name__ == "Square":
			dummy_instance = cls(1)
		else:
			dummy_instance = None

		dummy_instance.update(**dictionary)
		return dummy_instance

	@classmethod
	def load_from_file(cls):
		"""Returns a list of instances"""
		filename = f"{cls.__name__}.json"

		try:
			with open(filename, 'r') as file:
				json_string = file.read()
				dictionaries = cls.from_json_string(json_string)
				instances = [cls.create(**d) for d in dictionaries]
				return instances
		except FileNotFoundError:
			return []

	@classmethod
	def save_to_file_csv(cls, list_objs):
		"""Serializes and saves instances to a CSV file"""
		filename = f"{cls.__name__}.csv"
		with open(filename, 'w', newline='') as file:
			writer = csv.writer(file)
			if cls.__name__ == "Rectangle":
				for obj in list_objs:
					writer.writerow([obj.id, obj.width, obj.height, obj.x, obj.y])
			elif cls.__name__ == "Square":
				for obj in list_objs:
					writer.writerow([obj.id, obj.size, obj.x, obj.y])

	@classmethod
	def load_from_file_csv(cls):
		"""Deserializes and returns a list of instances from a CSV file"""
		filename = f"{cls.__name__}.csv"
		try:
			with open(filename, 'r', newline='') as file:
				reader = csv.reader(file)
				instances = []
				for row in reader:
					if cls.__name__ == "Rectangle":
						args = [int(row[0]), int(row[1]), int(row[2]), int(row[3]), int(row[4])]
						instance = cls.create(**cls.dummy(*args))
					elif cls.__name__ == "Square":
						args = [int(row[0]), int(row[1]), int(row[2]), int(row[3])]
						instance = cls.create(**cls.dummy(*args))
					instances.append(instance)
				return instances
		except FileNotFoundError:
			return []
