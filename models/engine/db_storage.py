#!/usr/bin/python3
"""This module defines a class to manage Database storage for hbnb clone"""
import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

from models.base_model import Base


class DBStorage:
    """ This class manages storage of hbnb models in Database """
    __engine = None
    __session = None

    def __init__(self):
        """ Connecting with database, Creating engine """
        DB_USER = os.environ.get('HBNB_MYSQL_USER')
        DB_PASS = os.environ.get('HBNB_MYSQL_PWD')
        DB_HOST = os.environ.get('HBNB_MYSQL_HOST')
        DB_NAME = os.environ.get('HBNB_MYSQL_DB')
        HBNB_ENV = os.environ.get('HBNB_ENV')

        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'.format(DB_USER,
                                                        DB_PASS,
                                                        DB_NAME),
            pool_pre_ping=True)

        if HBNB_ENV == 'test':
            Base.metadata.dropall(self.__engine)

    def all(self, cls=None):
        """ Returns a dictionary of models currently in storage """
        results_dict = {}
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review
        if cls is None:
            models = [User, State, City, Amenity, Place, Review]
            results_list = []
            for model in models:
                query_list = self.__session.query(model).all()
                results_list = results_list + query_list
        else:
            if type(cls) == str:
                cls = eval(cls)
            results_list = self.__session.query(cls).all()

        for result in results_list:
            results_dict[f"{type(result).__name__}.{result.id}"] = result

        return results_dict

    def new(self, obj):
        """ Adds new object to the session """
        self.__session.add(obj)

    def save(self):
        """ Saves storage to the database """
        self.__session.commit()

    def delete(self, obj=None):
        """ Deletes an object from the database """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """ Loads objects from the database """
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(Session)
        self.__session = Session

    def close(self):
        """Closes the SQLAlchemy session."""
        self.__session.remove()
