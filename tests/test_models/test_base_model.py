#!/usr/bin/python3
"""Unit test suite for the BaseModel class"""

import unittest
import os
from os import getenv
from models.base_model import BaseModel
import pep8


class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class"""

    @classmethod
    def setUpClass(cls):
        """Set up class method to initialize the BaseModel instance before each test"""
        cls.base = BaseModel()
        cls.base.name = "Kev"
        cls.base.num = 20

    @classmethod
    def teardown(cls):
        """Clean up actions after all tests have run"""
        del cls.base

    def tearDown(self):
        """Remove files generated during tests to avoid side effects"""
        try:
            os.remove("file.json")

        except Exception:
            pass

    def test_pep8_BaseModel(self):
        """Test if the code complies with PEP8 standards"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/base_model.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_checking_for_docstring_BaseModel(self):
        """Ensure all methods of BaseModel have appropriate docstrings"""
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_method_BaseModel(self):
        """Test the presence of essential methods in BaseModel"""
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))

    def test_init_BaseModel(self):
        """Test if the BaseModel instance is correctly initialized"""
        self.assertTrue(isinstance(self.base, BaseModel))

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") == 'db', 'Skip if storage type is DB')
    def test_save_BaseModel(self):
        """Test saving a BaseModel instance and updating 'updated_at' timestamp"""
        self.base.save()
        self.assertNotEqual(self.base.created_at, self.base.updated_at)

    def test_to_dict_BaseModel(self):
        """Test the dictionary representation method of BaseModel"""
        base_dict = self.base.to_dict()
        self.assertEqual(self.base.__class__.__name__, 'BaseModel')
        self.assertIsInstance(base_dict['created_at'], str)
        self.assertIsInstance(base_dict['updated_at'], str)


if __name__ == "__main__":
    unittest.main()
