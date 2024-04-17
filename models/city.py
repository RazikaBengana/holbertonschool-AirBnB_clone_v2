#!/usr/bin/python3
"""This module defines classes for city and state management using SQL ORM"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """City class inherits from BaseModel and Base, mapping to the 'cities' table in the database"""

    __tablename__ = 'cities'  # Name of the table in the database
    name = Column(String(128), nullable=False)  # Column 'name' with type String and cannot be null
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)  # ForeignKey to 'states' table
    places = relationship("Place", backref="cities", cascade="all, delete",
                          passive_deletes=True)  # Relationship to 'Place' class with cascade deletion

