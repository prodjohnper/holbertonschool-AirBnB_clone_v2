#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
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
            for key, val in models.storage.all().items():
                try:
                    if val.state_id == self.id:
                        city_lst.append(val)
                except AttributeError:
                    pass
            return city_lst
