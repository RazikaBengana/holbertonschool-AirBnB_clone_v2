#!/usr/bin/python3
"""This script manages persistent storage of objects in a file-based database"""

import json


class FileStorage:
    """Handles the serialization and deserialization of Python objects to and from a JSON file"""
    __file_path = 'file.json'  # Path to the JSON file where objects are stored
    __objects = {}  # Dictionary to store objects

    def all(self, cls=None):
        """
        Return a dictionary of all stored objects, optionally filtered by class type;
        If 'cls' is not provided, it returns all objects;
        If 'cls' is provided, it returns only objects of that class
        """
        if cls is None:
            return FileStorage.__objects

        else:
            new_dict = {}

            for key, value in FileStorage.__objects.items():
                if value.__class__ == cls:
                    new_dict[key] = value
            return new_dict

    def new(self, obj):
        """
        Add a new object to the storage dictionary;
        The object's class name and ID are used to generate a unique key
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.all()[key] = obj

    def save(self):
        """
        Serialize the storage dictionary to JSON and write it to the file;
        This method overwrites the existing file content
        """
        with open(FileStorage.__file_path, 'w') as f:
            temp = {key: obj.to_dict() for key, obj in FileStorage.__objects.items()}
            json.dump(temp, f)

    def reload(self):
        """
        Deserialize the JSON file to objects, if the file exists;
        Each object's dictionary is converted back into an instance of the appropriate class
        """
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
            'BaseModel': BaseModel, 'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review
        }

        try:
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)

        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """
        Delete an object from the storage dictionary, if the object is provided
        """
        if obj:
            obj_key = "{}.{}".format(obj.__class__.__name__, obj.id)
            del FileStorage.__objects[obj_key]

    def close(self):
        """
        Call the 'reload' method to update the storage dictionary with any changes from the file
        """
        self.reload()
