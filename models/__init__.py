#!/usr/bin/python3
"""
This module initializes the appropriate storage type according to the environment setting;
It supports two types of storage: database storage and file storage
"""

from os import getenv


# Check the environment variable HBNB_TYPE_STORAGE to determine the storage type
if getenv("HBNB_TYPE_STORAGE") == "db":
    # If the storage type is database, import DBStorage class from db_storage module
    from models.engine.db_storage import DBStorage
    # Create an instance of DBStorage
    storage = DBStorage()
    # Call reload method to initialize the storage with data from the database
    storage.reload()

else:
    # If the storage type is file, import FileStorage class from file_storage module
    from models.engine.file_storage import FileStorage
    # Create an instance of FileStorage
    storage = FileStorage()

# Call reload method to initialize the storage with data from the file system
storage.reload()
