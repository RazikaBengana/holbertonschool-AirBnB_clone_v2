#!/usr/bin/python3
"""This script sets up a database connection using SQLAlchemy"""

from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session


class DBStorage:
    """Define a class for interacting with the database"""

    __engine = None
    __session = None

    def __init__(self):
        """Initialize the database engine and drops all tables if in 'test' environment"""
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".format(
            getenv("HBNB_MYSQL_USER"),
            getenv("HBNB_MYSQL_PWD"),
            getenv("HBNB_MYSQL_HOST"),
            getenv("HBNB_MYSQL_DB"),
            pool_pre_ping=True
        ))

        if getenv("HBNB_ENV") == "test":
            from models.base_model import Base
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query all rows of all or a specific table if class 'cls' is provided"""
        from models.base_model import Base
        from models.amenity import Amenity
        from models.city import City
        from models.place import Place
        from models.review import Review
        from models.user import User
        from models.state import State

        new_dict = {}
        all_class = [City, State, User, Place, Review, Amenity]
        list_objects = []

        if cls is None:
            for i in range(len(all_class)):
                list_objects += self.__session.query(all_class[i]).all()

        else:
            list_objects += self.__session.query(cls).all()

        for element in list_objects:
            key = "{}.{}".format(element.__class__.__name__, element.id)
            new_dict[key] = element

        return new_dict

    def new(self, obj):
        """Add a new object to the session"""
        self.__session.add(obj)

    def save(self):
        """Commit changes to the database"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete an object from the session"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Recreate all tables and starts a new session"""
        from models.base_model import Base
        from models.amenity import Amenity
        from models.city import City
        from models.place import Place
        from models.review import Review
        from models.user import User
        from models.state import State
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """Close the current session"""
        self.__session.close()
