#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """A base class for all hbnb models"""
    def __init__(self, *args, **kwargs):
        self.id = str(uuid4())
        self.created_at = self.updated_at = datetime.now()
        if kwargs:
            for ky, vl in kwargs.items():
                if ky in ('created_at', 'updated_at'):
                    setattr(self, ky, datetime.
                            strptime(vl, '%Y-%m-%dT%H:%M:%S.%f'))
                if ky != '__class__':
                    setattr(self, ky, vl)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """returns dictionary of BaseModel"""
        new_richard = self.__dict__.copy()
        new_richard["__class__"] = self.__class__.__name__
        new_richard["created_at"] = self.created_at.isoformat()
        new_richard["updated_at"] = self.updated_at.isoformat()
        return new_richard
