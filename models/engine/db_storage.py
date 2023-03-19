#!/usr/bin/python3
from os import getenv
from sqlalchemy import create_engine, inspect, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".format(
                                            getenv('HBNB_MYSQL_USER'),
                                            getenv('HBNB_MYSQL_PWD'),
                                            getenv('HBNB_MYSQL_HOST'),
                                            getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)

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
        metadata = MetaData()
        metadata.reflect(bind=self.__engine)
        if cls is None:
            for table in metadata.sorted_tables:
                stmt = table.select()
                results = self.__session.execute(stmt).fetchall()
                for row in results:
                    obj_key = "{}.{}".format(table.name, row.id)
                    obj_dct[obj_key] = row
        else:
            qry = self.__session.query(cls)
            for obj in qry:
                obj_key = "{}.{}".format(type(obj).__name__, obj.id)
                obj_dct[obj_key] = obj
        return obj_dct

    def gettables(self):
        inspector = inspect(self.__engine)
        return inspector.get_table_names()

    def close(self):
        self.__session.close()

    def hcf(self, cls):
        metadata = MetaData()
        metadata.reflect(bind=self.__engine)
        table = metadata.tables.get(cls.__tablename__)
        self.__session.execute(table.delete())
        self.save()
