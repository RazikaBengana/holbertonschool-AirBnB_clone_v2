#!/usr/bin/python3
"""Module that defines a User model inheriting from BaseModel and Base"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """Defines attributes and relationships for the User model"""

    __tablename__ = "users"  # Specify the table name in the database
    email = Column(String(128), nullable=False)  # User email, cannot be null
    password = Column(String(128), nullable=False)  # User password, cannot be null
    first_name = Column(String(128), nullable=True)  # User first name, can be null
    last_name = Column(String(128), nullable=True)  # User last name, can be null
    places = relationship("Place", backref="user", cascade="all, delete",
                          passive_deletes=True)  # Relationship to the Place model
    reviews = relationship("Review", backref="user",
                           cascade="all, delete",
                           passive_deletes=True)  # Relationship to the Review model
