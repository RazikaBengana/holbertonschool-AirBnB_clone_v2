#!/usr/bin/python3
"""This script defines classes and relationships for a hospitality service database"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from models.review import Review
from models.amenity import Amenity
from os import getenv
from sqlalchemy.orm import relationship
from models import storage



# Association table for many-to-many relationship between places and amenities
place_amenity = Table("place_amenity", Base.metadata,
                      Column("place_id", String(60),
                             ForeignKey("places.id"),
                             nullable=False, primary_key=True),
                      Column("amenity_id", String(60),
                             ForeignKey("amenities.id"),
                             nullable=False, primary_key=True))


class Place(BaseModel, Base):
    """Represents a place for rent"""

    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    if getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship("Review", backref="place",
                               cascade="all, delete", passive_deletes=True)
    else:
        @property
        def reviews(self):
            """Return the list of Review instances associated with this place"""
            new_list = []
            all_review = storage.all(Review)

            for element in all_review.values():
                if self.id == element.place_id:
                    new_list.append(element)

            return new_list

    if getenv("HBNB_TYPE_STORAGE") == "db":
        amenities = relationship("Amenity", viewonly=False,
                                 secondary=place_amenity,
                                 backref="place_amenities")
    else:
        @property
        def amenities(self):
            """Return the list of Amenity instances associated with this place"""
            new_list = []
            all_amen = storage.all(Amenity)

            for element in all_amen.values():
                if self.id == element.place_id:
                    new_list.append(element)

            return new_list

        @amenities.setter
        def amenities(self, cls):
            """Add an Amenity instance to the place if it's not already associated"""
            if not isinstance(cls, Amenity):
                return

            self.amenity_ids.append(cls.id)
