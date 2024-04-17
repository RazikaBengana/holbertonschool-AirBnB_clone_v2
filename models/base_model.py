#!/usr/bin/python3
"""This module defines the base model class for all objects in hbnb project"""

import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime
from os import getenv


# Declare a base for all models
Base = declarative_base()


class BaseModel:
    """
    A base class for all models in HBnB project;
    Attributes include id, created_at, and updated_at
    """

    # Columns for id, created_at, and updated_at with appropriate constraints and defaults
    id = Column(String(60), unique=True, primary_key=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow(), nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow(), nullable=False)

    def __init__(self, *args, **kwargs):
        """
        Initialize a new BaseModel instance;
        UUID, created_at, and updated_at are set if not provided
        """
        if not kwargs:
            # Assign new UUID and timestamps if object created without explicit parameters
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

        else:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)

            # Assign UUID if it wasn't included
            if "id" not in kwargs:
                self.id = str(uuid.uuid4())

            if "created_at" not in kwargs:
                self.created_at = datetime.now()

            else:
                self.created_at = datetime.strptime(kwargs['created_at'], '%Y-%m-%dT%H:%M:%S.%f')

            if "updated_at" not in kwargs:
                self.updated_at = datetime.now()

            else:
                self.updated_at = datetime.strptime(kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')

    def __str__(self):
        """String representation of the BaseModel class"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """
        Save the model to the database through session management;
        Also update the updated_at attribute to current time
        """
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """
        Return a dictionary containing all keys/values of the instance and class name;
        This method is useful for serializing SQLAlchemy objects
        """
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary['__class__'] = (str(type(self)).split('.')[-1]).split('\'')[0]
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()

        if "_sa_instance_state" in dictionary.keys():
            dictionary.pop('_sa_instance_state')
        return dictionary

    def delete(self):
        """
        Delete the current instance from the storage by calling the delete method
        """
        from models import storage
        storage.delete()
