#!/usr/bin/python3
"""Module for defining State model and its behavior"""

from models.base_model import BaseModel, Base
from models.city import City
from models import storage
from os import getenv
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """Representation of a state in a database or storage system"""

    __tablename__ = "states"  # Name of the table in the database
    name = Column(String(128), nullable=False)  # State name field definition

    if getenv("HBNB_TYPE_STORAGE") == "db":
        # Relationship between states and cities for database storage
        cities = relationship("City", backref="state", cascade="all, delete")

    else:
        @property
        def cities(self):
            """Get a list of cities in a state stored in file storage"""
            new_list = []
            all_cities = storage.all(City)  # Retrieve all city objects from storage

            for element in all_cities.values():
                if self.id == element.state_id:  # Check if the city belongs to the current state
                    new_list.append(element)

            return new_list
