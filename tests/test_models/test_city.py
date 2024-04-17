#!/usr/bin/python3
"""Unit test suite for the City class"""

import unittest
import os
from os import getenv
from models.city import City
from models.base_model import BaseModel
import pep8


class TestCity(unittest.TestCase):
    """Test cases for the City class"""

    @classmethod
    def setUpClass(cls):
        """Set up class method to initialize testing environment before tests are run"""
        cls.city = City()
        cls.city.name = "LA"
        cls.city.state_id = "CA"

    @classmethod
    def teardown(cls):
        """Clean up after all test cases have been executed"""
        del cls.city

    def tearDown(self):
        """Clean up after each test case is executed"""
        try:
            os.remove("file.json")

        except Exception:
            pass

    def test_pep8_City(self):
        """Test that the City class conforms to PEP8"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/city.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_checking_for_docstring_City(self):
        """Ensure the City class has docstrings"""
        self.assertIsNotNone(City.__doc__)

    def test_attributes_City(self):
        """Check if City class has specific attributes"""
        self.assertTrue('id' in self.city.__dict__)
        self.assertTrue('created_at' in self.city.__dict__)
        self.assertTrue('updated_at' in self.city.__dict__)
        self.assertTrue('state_id' in self.city.__dict__)
        self.assertTrue('name' in self.city.__dict__)

    def test_is_subclass_City(self):
        """Test if the City class is a subclass of BaseModel"""
        self.assertTrue(issubclass(self.city.__class__, BaseModel))

    def test_attribute_types_City(self):
        """Check the type of City attributes"""
        self.assertEqual(type(self.city.name), str)
        self.assertEqual(type(self.city.state_id), str)

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") == 'db', 'Skip test when using a database')
    def test_save_City(self):
        """Test saving a city and its updated timestamp"""
        self.city.save()
        self.assertNotEqual(self.city.created_at, self.city.updated_at)

    def test_to_dict_City(self):
        """Check the dictionary representation of a City instance"""
        self.assertEqual('to_dict' in dir(self.city), True)


if __name__ == "__main__":
    unittest.main()
