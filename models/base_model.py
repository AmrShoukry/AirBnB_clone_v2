#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import os

if os.environ.get('HBNB_TYPE_STORAGE') != "db":
    Base = object
else:
    Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""
    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow(), nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow(), nullable=False)

    def __init__(self, *args, **kwargs):
        """Instantiates a new model"""
        if not kwargs:
            from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        elif 'flagged_as_new' in kwargs:
            from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            del kwargs['flagged_as_new']
            self.__dict__.update(kwargs)
            storage.new(self)
        else:
            if 'id' not in kwargs:
                kwargs['id'] = str(uuid.uuid4())
            if 'updated_at' not in kwargs:
                kwargs['updated_at'] = datetime.now()
            if 'created_at' not in kwargs:
                kwargs['created_at'] = datetime.now()

            if '__class__' in kwargs:
                del kwargs['__class__']
            self.__dict__.update(kwargs)

            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        if type(self.created_at) is str:
            dictionary['created_at'] = self.created_at
        else:
            dictionary['created_at'] = self.created_at.isoformat()
        if type(self.updated_at) is str:
            dictionary['updated_at'] = self.updated_at
        else:
            dictionary['updated_at'] = self.updated_at.isoformat()
        if "_sa_instance_state" in dictionary:
            del dictionary["_sa_instance_state"]
        return dictionary

    def delete(self):
        """ delete the current instance from the storage """
        from models import storage
        storage.delete(self)
