#!/usr/bin/python3
from os import getenv
from models.base_model import Base
from models.review import Review
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.user import User
from models.place import Place
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage:
    __engine = None
    __session = None
    CLS_LST = {
        'Amenity': Amenity,
        'City': City,
        'Place': Place,
        'Review': Review,
        'State': State,
        'User': User
    }

    def __init__(self):
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".format(
                                            getenv('HBNB_MYSQL_USER'),
                                            getenv('HBNB_MYSQL_PWD'),
                                            getenv('HBNB_MYSQL_HOST'),
                                            getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def reload(self):
        Base.metadata.create_all(self.__engine)
        the_session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(the_session)
        self.__session = Session()

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj is not None:
            self.__session.delete(obj)

    def all(self, cls=None):
        obj_dct = {}
        qry = []
        if cls is None:
            for cls_typ in DBStorage.CLS_LST.values():
                qry.extend(self.__session.query(cls_typ).all())
        else:
            qry = self.__session.query(cls)
        for obj in qry:
            obj_key = "{}.{}".format(type(obj).__name__, obj.id)
            obj_dct[obj_key] = obj
        return obj_dct

    def close(self):
        self.__session.close()

    def hcf(self):
        for cls in DBStorage.CLS_LST.values():
            qry = self.__session.query(cls)
            all_objs = [obj for obj in qry]
            for obj in range(len(all_objs)):
                to_delete = all_objs.pop(0)
                to_delete.delete()
        self.save()
