#!/usr/bin/python3
"""This module defines a class to manage db storage for hbnb clone"""
from sqlalchemy import create_engine
from os import getenv
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class DBStorage:
    """ db storage """
    __engine = None
    __session = None

    def __init__(self):
        """ mr constructor """
        env = getenv('HBNB_ENV')
        user = getenv('HBNB_MYSQL_USER')
        password = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        database = getenv('HBNB_MYSQL_DB')
        engine_url = 'mysql+mysqldb://{}:{}@{}/{}'.format(
                      user, password, host, database)
        self.__engine = create_engine(engine_url, pool_pre_ping=True)
        if (env == "test"):
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """ query on the current database session """
        filtred_dict = {}
        classes = [User, Place, State, City, Amenity, Review]
        if cls:
            objs = self.__session.query(cls).all()
            for obj in objs:
                filtred_dict[obj.to_dict()['__class__'] + '.' + obj.id] = obj
        for clss in Base.__subclasses__():
            objs = self.__session.query(clss).all()
            for obj in objs:
                filtred_dict[obj.to_dict()['__class__'] + '.' + obj.id] = obj
        return filtred_dict

    def new(self, obj):
        """  add the object to the current database session """
        if obj:
            self.__session.add(obj)
        # self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """ commit all changes """
        self.__session.commit()

    def delete(self, obj=None):
        """ Delete the obj from db """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """ reload """
        Base.metadata.create_all(self.__engine)
        session_factory = scoped_session(
            sessionmaker(bind=self.__engine, expire_on_commit=False)
        )
        self.__session = session_factory()
