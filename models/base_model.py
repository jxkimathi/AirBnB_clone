#!/usr/bin/env/python3
"""Defines all common attributes/methods for other classes"""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """The class BaseModel"""
    def __init__(self, *args, **kwargs):
        """Initialization of the class"""
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    self.__dict__[key] = datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f")
                elif key != "__class__":
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def __str__(self):
        """Returns string representation"""
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Updates the instance with the current time"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns dictionary containing all key value pairs"""
        my_dict = dict(self.__dict__)
        my_dict["__class__"] = self.__class__.__name__
        if not isinstance(my_dict["created_at"], str):
            my_dict["created_at"] = my_dict["created_at"].isoformat()
        if not isinstance(my_dict["updated_at"], str):
            my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        return my_dict
