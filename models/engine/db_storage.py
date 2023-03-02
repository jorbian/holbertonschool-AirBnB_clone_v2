#!/usr/bin/python3
from os import getenv
from models.base_model import Base, BaseModel
from models.review import Review
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DBStorage:
    __engine = None
    __session = None
    def __init__(self):
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}"
                            .format(getenv('HBNB_MYSQL_USER'),
                                    getenv('HBNB_MYSQL_PWD'),
                                    getenv('HBNB_MYSQL_HOST'),
                                    getenv('HBNB_MYSQL_DB')),
                                    pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def reload(self):
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def remove(self, obj=None):
        if obj is not None:
            self.__session.delete(obj)

    def all(self):
        obs = self.__session.query(Review).all()
        return obs

    def close(self):
        self.__session.close()

    def total(self):
        return len(self.__session.query(Review).all())
