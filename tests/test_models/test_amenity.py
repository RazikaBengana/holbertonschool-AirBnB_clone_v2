#!/usr/bin/python3
"""Unit test suite for the Amenity class"""

import unittest
import os
from models.amenity import Amenity
from models.base_model import BaseModel
import pep8


class TestAmenity(unittest.TestCase):
    """Test cases for the Amenity class"""

    @classmethod
    def setUpClass(cls):
        """Set up an instance of Amenity before all tests"""
        cls.amenity = Amenity()
        cls.amenity.name = "Breakfast"

    @classmethod
    def teardown(cls):
        """Clean up after all tests have run"""
        del cls.amenity

    def tearDown(self):
        """Remove files created during testing"""
        try:
            os.remove("file.json")

        except Exception:
            pass

    def test_pep8_Amenity(self):
        """Check that the Amenity class conforms to PEP8"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/amenity.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_checking_for_docstring_Amenity(self):
        """Ensure that the Amenity class has a docstring"""
        self.assertIsNotNone(Amenity.__doc__)

    def test_attributes_Amenity(self):
        """Verify the attributes of an Amenity instance"""
        self.assertTrue('id' in self.amenity.__dict__)
        self.assertTrue('created_at' in self.amenity.__dict__)
        self.assertTrue('updated_at' in self.amenity.__dict__)
        self.assertTrue('name' in self.amenity.__dict__)

    def test_is_subclass_Amenity(self):
        """Test if Amenity is a subclass of BaseModel"""
        self.assertTrue(issubclass(self.amenity.__class__, BaseModel), True)

    def test_attribute_types_Amenity(self):
        """Check the type of the attributes in Amenity"""
        self.assertEqual(type(self.amenity.name), str)

    def test_save_Amenity(self):
        """Test the save method of the Amenity class"""
        self.amenity.save()
        self.assertNotEqual(self.amenity.created_at, self.amenity.updated_at)

    def test_to_dict_Amenity(self):
        """Test the conversion of Amenity attributes to a dictionary"""
        self.assertEqual('to_dict' in dir(self.amenity), True)


if __name__ == "__main__":
    unittest.main()
