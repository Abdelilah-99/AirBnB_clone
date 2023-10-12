#!/usr/bin/python3

import os, json
from models.base_model import BaseModel
from models.user import User
class FileStorage:
    """Manage File storage (serializes/deserializes)"""
    def __init__(self):
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        return  self.__objects
    
    def new(self, obj):
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj
    
    def save(self):
        data = {}
        for key, obj in self.__objects.items():
            data[key] = obj.to_dict()
            
        with open(self.__file_path, "w", encoding='utf-8') as file_json:
            json.dump(data, file_json)
    
    def reload(self):
        if not os.path.isfile(self.__file_path):
            return
        with open(self.__file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            for key, value in data.items():
                class_name, class_id= key.split('.')
                cls = eval(class_name)
                self.__objects[key] = cls(**value)




