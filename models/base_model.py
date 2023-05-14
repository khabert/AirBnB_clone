#!/usr/bin/env python3

""" contains a classs BaseModel defining all common attributes and methods
"""

from datetime import datetime
import models
import uuid
import storage

class BaseModel:
    """base class from which other subclasses derive"""

    def __init__(self, *args, **kwargs):
        """initialisation"""
        if Kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            if hasattr(self, "created_at") and type(self.created_at) is str:
                self.created_at = datetime.strptime(kwargs["created_at"], time)
            if hasattr(self, "updated_at") and type (self.updated_at) is str:
                self.updated_at = datetime.strptime(kwargs["updated_at"], time)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
            model.storage.save()

    def __str__(self):
        """Base class string represeantation"""
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__,self.id, self.__dict__)

    def save(self):
        """updates the public instance attribute updated_at with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__ of the instance"""
        newdict = self.__dict__.copy()
        newdict["__class__"] = self.__class__.__name__
        newdict["created_at"] = self.created_at.isoformat()
        newdict["created_at"] = self.updated_at.isoformat()

        return newdict

