#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
from models.base_model import BaseModel
from models.state import State
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.city import City
from models.user import User


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage
        if cls specified, only returns that class"""
        if cls is not None:
            if type(cls) is str:
                cls = eval(cls)
            spec_rich = {}
            for ky, vl in self.__objects.items():
                if cls == type(vl):
                    spec_rich[ky] = vl
            return spec_rich
        return self.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Deserializes jason into __objects (poor jason)"""
        try:
            with open(self.__file_path, encoding='utf-8') as fred:
                richard = json.load(fred)
                for key, value in richard.items():
                    obj = eval(value['__class__'])(**value)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """if obj deletes obj from __objects"""
        try:
            key = obj.__class__.__name__ + "." + obj.id
            del self.__objects[key]
        except (AttributeError, KeyError):
            pass
