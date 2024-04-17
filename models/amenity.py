#!/usr/bin/python3
"""This module defines the Amenity class inherited from BaseModel and Base"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String


class Amenity(BaseModel, Base):
    """Defines the Amenity class which represents amenities in a database"""

    __tablename__ = "amenities"  # Set the name of the table in the database
    name = Column(String(128), nullable=False)  # Define a column 'name' with type String and cannot be null
