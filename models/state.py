#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
import os
import models


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship('City', cascade='all, delete',
                              backref='state')
    else:

        @property
        def cities(self):
            """cities property getter"""
            city_lst = []
            for city in models.storage.all(City).values():
                if self.id == city.state_id:
                    city_lst.append(city)
            return city_lst
