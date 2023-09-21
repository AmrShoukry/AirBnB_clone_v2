#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship

import os
if os.getenv("HBNB_TYPE_STORAGE") != "db":
    pass
else:
    place_amenity = Table(
        "place_amenity",
        Base.metadata,
        Column('place_id', String(60), ForeignKey('places.id', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True, nullable=False),
        Column('amenity_id', String(60), ForeignKey('amenities.id', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True, nullable=False),
        mysql_charset="latin1"
    )


class Place(BaseModel, Base):
    """ A place to stay """
    if os.getenv("HBNB_TYPE_STORAGE") != "db":
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []
    else:
        __tablename__ = "places"
        __table_args__ = ({'mysql_default_charset': 'latin1'})
        # city_id = Column(String(60), ForeignKey('cities.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
        city_id = Column(String(60), ForeignKey('cities.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer(), default=0, nullable=False)
        number_bathrooms = Column(Integer(), default=0, nullable=False)
        max_guest = Column(Integer(), default=0, nullable=False)
        price_by_night = Column(Integer(), default=0, nullable=False)
        latitude = Column(Float(), nullable=True)
        longitude = Column(Float(), nullable=True)
        user = relationship('User', back_populates='places')
        cities = relationship('City', back_populates='places')
        reviews = relationship('Review', back_populates='place', cascade='all, delete, save-update')
        amenities = relationship('Amenity', secondary='place_amenity', viewonly=False, back_populates='place_amenities')
        amenity_ids = []

    if os.getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def reviews(self):
            from models import storage
            from models.review import Review

            """ getter - to get all places's reviews """
            review_list = [item for item in storage.all(Review).values()
                            if item.place_id == self.id]
            return review_list

        @property
        def amenities(self):
            return self.amenity_ids

        @amenities.setter
        def amenities(self, value):
            from models.amenity import Amenity
            if type(value) is Amenity:
                self.amenity_ids.append(value)
