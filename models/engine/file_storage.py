#!/usr/bin/python3
"""
Defines the FileStorage class
"""


import json
from datetime import datetime


class FileStorage:
    """
    Serializes instances to a JSON file and deserializes JSON file to instances
    """
    __file_path = 'file.json'
    __object = {}

    def all(self):
        return FileStorage.__object

    def new(self, obj):
        key = type(obj).__name__ + '.' + obj.id
        FileStorage.__object[key] = obj

    def save(self):
        """Serializes to json"""
        with open(FileStorage.__file_path, 'w+') as f:
            obj_dict = {}
            for key, value in FileStorage.__object.items():
                obj_dict[key] = value.to_dict()
            json.dump(obj_dict, f)

    def reload(self):
        """Deserializes json file"""
        try:
            with open(FileStorage.__file_path, 'r') as f:
                obj_dict = json.loads(f.read())
                from models.base_model import BaseModel
                from models.user import User
                from models.state import State
                from models.city import City
                from models.amenity import Amenity
                from models.place import Place
                from models.review import Review
                for key, value in obj_dict.items():
                    if value['__class__'] == 'BaseModel':
                        FileStorage.__object[key] = BaseModel(**value)
                    elif value['__class__'] == 'User':
                        FileStorage.__object[key] = User(**value)
                    elif value['__class__'] == 'State':
                        FileStorage.__object[key] = State(**value)
                    elif value['__class__'] == 'City':
                        FileStorage.__object[key] = City(**value)
                    elif value['__class__'] == 'Amenity':
                        FileStorage.__object[key] = Amenity(**value)
                    elif value['__class__'] == 'Place':
                        FileStorage.__object[key] = Place(**value)
                    elif value['__class__'] == 'Review':
                        FileStorage.__object[key] = Review(**value)
        except FileNotFoundError:
            pass
