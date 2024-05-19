#!/usr/bin/python3
"""Defines a BaseModel class"""
import uuid
from datetime import datetime
import models


class BaseModel():
    """The BaseModel class"""
    def __init__(self, *args, **kwargs):
        """The Constructor"""
        if kwargs:
            self.new_obj(kwargs)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def new_obj(self, kwargs):
        """Initialize attributes using keyword arguments"""
        formate = '%Y-%m-%dT%H:%M:%S.%f'
        for key, value in kwargs.items():
            if key == '__class__':
                continue
            if key == 'created_at' or key == 'updated_at':
                value = datetime.strptime(value, formate)
            setattr(self, key, value)

    def __str__(self):
        """Return string info about class"""
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """Use to update time for updated_at attribute"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Return a dict representation"""
        dict_obj = self.__dict__.copy()
        dict_obj['__class__'] = self.__class__.__name__
        dict_obj['updated_at'] = self.updated_at.isoformat()
        dict_obj['created_at'] = self.created_at.isoformat()
        return dict_obj

