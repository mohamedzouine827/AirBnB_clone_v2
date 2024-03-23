#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    if getenv('HBNB_TYPE_STORAGE') == "db":
        name = Column(String(128), nullable=False)
        cities = relationship('City',  backref='state',
                              cascade="all, delete-orphan")
    else:
        name = ""

        @property
        def cities(self):
            from models.__init__ import storage
            list_cities = []
            dic = storage.all(City)
            for key, obj in dic.items():
                if obj.state_id == self.id:
                    list_cities.append(obj)
            return list_cities
