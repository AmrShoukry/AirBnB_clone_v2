#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

import os


class State(BaseModel, Base):
    """ State class """
    if os.getenv("HBNB_TYPE_STORAGE") != "db":
        name = ""
    else:
        __tablename__ = "states"
        __table_args__ = ({'mysql_default_charset': 'latin1'})
        name = Column(String(128), nullable=False)
        cities = relationship('City', back_populates='state',
                              cascade='all, delete, save-update')

    if os.getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            from models import storage
            from models.city import City
            """ getter - to get all state's cities """
            cities_found = [item for item in storage.all(City).values()
                            if item.state_id == self.id]
            return cities_found
