#!/usr/bin/python3

import os
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """Manage File storage (serializes/deserializes)"""

    def __init__(self):
        """instantiate the instance"""
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        data = {}
        for key, obj in self.__objects.items():
            data[key] = obj.to_dict()

        with open(self.__file_path, "w", encoding='utf-8') as file_json:
            json.dump(data, file_json)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        if not os.path.isfile(self.__file_path):
            return
        with open(self.__file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            for key, value in data.items():
                class_name, class_id = key.split('.')
                cls = eval(class_name)
                self.__objects[key] = cls(**value)
