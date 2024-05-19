#!/usr/bin/python3
"""Defines a FileStorage class"""
import os
import json
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class FileStorage:
    """The FileStorage class"""
    __file_path = 'storage_engines.json'
    __objects = {}

    def all(self):
        """Return all objects in the __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        str_objects = {}
        for key, obj in self.__objects.items():
            str_objects[key] = obj.to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(str_objects, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as f:
                dict_objects = json.load(f)
                for key, value in dict_objects.items():
                    self.__objects[key] = eval(value['__class__'])(**value)

