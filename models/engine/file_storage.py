#!/usr/bin/nv python3
"""
contains the FileStorage class
"""

import json
from models.base_model import BaseModel


classes = {}

class FileStorage:
    """serializes instances to a JSON file & deserializes JSON files to instances"""
    __file_path = "file.json" #string path to JSON file
    __objects = {} #empty dict to store all objects by id

    def all(self):
        """ returns the __objects dict"""
        return self.__objects

    def new(self, obj):
        """sets in __objects obj with <obj class>.id key"""
        if obj is not None:
            key = obj.__class__.name__+"."+ obj.id
            self.__object[key] = obj

    def save(self):
        """serialises __objects to JSON file"""
       jsonobjects = {}
       for key in self.__objects:
           jsonobjects[key] = self.__objects[key].to_dict()

        with open(self.__file_path, 'w') as f:
            json.dump(jsonobjects, f)

    def reload(self):
        """deserialies the JSON file to __objects"""
        try:
            with open(self.__file_path, r) as f:
                for key in json.load(f):
                    self.__objects[key] = classes[json.load(f)[key]["class__"]](**json.load(f)[key])
        except:
            pass
