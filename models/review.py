#!/usr/bin/python3
"""Module for Review class that represents reviews left by users"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey


class Review(BaseModel, Base):
    """Defines attributes and behavior for the Review resource, which includes text, place_id, and user_id"""

    __tablename__ = 'reviews'  # Name of the table in the database
    text = Column(String(1024), nullable=False)  # Review text with max length 1024 characters, cannot be null
    place_id = Column(String(60), ForeignKey('places.id', ondelete='CASCADE'),
                      nullable=False)  # Foreign key to places table with cascade delete
    user_id = Column(String(60), ForeignKey('users.id', ondelete='CASCADE'),
                     nullable=False)  # Foreign key to users table with cascade delete

