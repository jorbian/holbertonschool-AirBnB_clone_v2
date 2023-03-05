#!/usr/bin/python3
"""Defines unittests for console.py."""
import os
import unittest
import models
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.engine.base import Engine


class TestHBNBCommand(unittest.TestCase):
    """Unittests for testing the HBNB command interpreter."""
    pass


if __name__ == "__main__":
    unittest.main()
