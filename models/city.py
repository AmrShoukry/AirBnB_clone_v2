#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = "cities"
    __table_args__ = ({'mysql_default_charset': 'latin1'})
    state_id = Column(String(60),
                      ForeignKey('states.id',
                                 ondelete='CASCADE',
                                 onupdate='CASCADE'),
                      nullable=False)
    name = Column(String(128), nullable=False)
    state = relationship('State', back_populates='cities')
    places = relationship('Place', back_populates='cities', cascade='all, delete, save-update')
