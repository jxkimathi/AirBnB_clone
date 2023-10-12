#!/usr/bin/env/python3
"""Serialize instance to a JSON file and deserialize JSON file to instance"""
from models.base_model import BaseModel
import json
import os
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage:
    """The class FileStorage"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        id = obj.to_dict()["id"]
        classname = obj.to_dict()["__class__"]
        keyname = classname+"."+id
        FileStorage.__objects[keyname] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        path = FileStorage.__file_path
        data = dict(FileStorage.__objects)
        for key, value in data.items():
            data[key] = value.to_dict()
        with open(path, "w") as file:
            json.dump(data, file)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        path = FileStorage.__file_path
        data = FileStorage.__objects
        if os.path.exists(path):
            try:
                with open(path) as file:
                    for key, value in json.load(file).items():
                        if "BaseModel" in key:
                            data[key] = BaseModel(**value)
                        if "Amenity" in key:
                            data[key] = Amenity(**value)
                        if "City" in key:
                            data[key] = City(**value)
                        if "Place" in key:
                            data[key] = Place(**value)
                        if "Review" in key:
                            data[key] = Review(**value)
                        if "State" in key:
                            data[key] = State(**value)
                        if "User" in key:
                            data[key] = User(**value)
            except Exception:
                pass
