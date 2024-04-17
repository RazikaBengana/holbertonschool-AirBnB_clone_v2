#!/usr/bin/python3
"""Unit test suite for testing file storage mechanism in a simple storage system"""

import unittest
from models.base_model import BaseModel
from models import storage
import os


@unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") == "db",
                 "Skip tests if environment is set to database storage. Only test file storage.")
class test_fileStorage(unittest.TestCase):
    """Tests the file storage of the custom model system"""

    def setUp(self):
        """Clear the storage dictionary before each test to ensure a clean state"""
        del_list = []
        for key in storage._FileStorage__objects.keys():
            del_list.append(key)

        for key in del_list:
            del storage._FileStorage__objects[key]

    def tearDown(self):
        """Ensure that the file 'file.json' is removed after each test"""
        try:
            os.remove('file.json')

        except (Exception):
            pass

    def test_obj_list_empty(self):
        """Test if the storage is empty at initialization"""
        self.assertEqual(len(storage.all()), 0)

    def test_new(self):
        """Test the creation of a new instance and its existence in the storage"""
        new = BaseModel()

        for obj in storage.all().values():
            temp = obj
            self.assertTrue(temp is obj)

    def test_all(self):
        """Test that all returns a dictionary"""
        new = BaseModel()
        temp = storage.all()
        self.assertIsInstance(temp, dict)

    def test_base_model_instantiation(self):
        """Test that 'file.json' does not exist after creating a new BaseModel"""
        new = BaseModel()
        self.assertFalse(os.path.exists('file.json'))

    def test_empty(self):
        """Test that saving a BaseModel creates a non-empty 'file.json'"""
        new = BaseModel()
        thing = new.to_dict()
        new.save()
        new2 = BaseModel(**thing)
        self.assertNotEqual(os.path.getsize('file.json'), 0)

    def test_save(self):
        """Test that the save method actually creates 'file.json'"""
        new = BaseModel()
        storage.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_reload(self):
        """Test reloading of all objects from 'file.json' into storage"""
        new = BaseModel()
        storage.save()
        storage.reload()

        for obj in storage.all().values():
            loaded = obj
            self.assertEqual(new.to_dict()['id'], loaded.to_dict()['id'])

    def test_reload_empty(self):
        """Test reloading from an empty 'file.json', expecting a ValueError"""
        with open('file.json', 'w') as f:
            pass

        with self.assertRaises(ValueError):
            storage.reload()

    def test_reload_from_nonexistent(self):
        """Test that reloading from a nonexistent file returns None"""
        self.assertEqual(storage.reload(), None)

    def test_base_model_save(self):
        """Test that BaseModel can save itself, thereby creating 'file.json'"""
        new = BaseModel()
        new.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_type_path(self):
        """Test that the internal path variable is a string"""
        self.assertEqual(type(storage._FileStorage__file_path), str)

    def test_type_objects(self):
        """Test that storage.all() returns a dictionary"""
        self.assertEqual(type(storage.all()), dict)

    def test_key_format(self):
        """Test that keys in storage dictionary are correctly formatted"""
        new = BaseModel()
        _id = new.to_dict()['id']

        for key in storage.all().keys():
            temp = key
            self.assertEqual(temp, 'BaseModel' + '.' + _id)

    def test_storage_var_created(self):
        """Test the type of storage variable to ensure it's a FileStorage instance"""
        from models.engine.file_storage import FileStorage
        print(type(storage))
        self.assertEqual(type(storage), FileStorage)
