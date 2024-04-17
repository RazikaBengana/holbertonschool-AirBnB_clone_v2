#!/usr/bin/python3
"""Unit test suite for the Review class"""

import unittest
import os
from os import getenv
from models.review import Review
from models.base_model import BaseModel
import pep8


class TestReview(unittest.TestCase):
    """Defines test cases for the Review class"""

    @classmethod
    def setUpClass(cls):
        """Set up class method to initialize test instances"""
        cls.rev = Review()
        cls.rev.place_id = "4321-dcba"
        cls.rev.user_id = "123-bca"
        cls.rev.text = "The strongest in the Galaxy"

    @classmethod
    def teardown(cls):
        """Clean up class method to remove test instances after testing"""
        del cls.rev

    def tearDown(self):
        """Tear down method to clean up files after each test method"""
        try:
            os.remove("file.json")

        except Exception:
            pass

    def test_pep8_Review(self):
        """Test that the code conforms to the PEP8 style guide"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/review.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_checking_for_docstring_Review(self):
        """Test to ensure each method has a docstring"""
        self.assertIsNotNone(Review.__doc__)

    def test_attributes_review(self):
        """Test the existence of attributes in the Review instance"""
        self.assertTrue('id' in self.rev.__dict__)
        self.assertTrue('created_at' in self.rev.__dict__)
        self.assertTrue('updated_at' in self.rev.__dict__)
        self.assertTrue('place_id' in self.rev.__dict__)
        self.assertTrue('text' in self.rev.__dict__)
        self.assertTrue('user_id' in self.rev.__dict__)

    def test_is_subclass_Review(self):
        """Test if 'Review' is a subclass of 'BaseModel'"""
        self.assertTrue(issubclass(self.rev.__class__, BaseModel), True)

    def test_attribute_types_Review(self):
        """Test the types of attributes of 'Review' are correctly set"""
        self.assertEqual(type(self.rev.text), str)
        self.assertEqual(type(self.rev.place_id), str)
        self.assertEqual(type(self.rev.user_id), str)

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") == 'db', "Skip if database storage is used.")
    def test_save_Review(self):
        """Test saving a 'Review' instance and checking 'created_at' and 'updated_at' are updated"""
        self.rev.save()
        self.assertNotEqual(self.rev.created_at, self.rev.updated_at)

    def test_to_dict_Review(self):
        """Test that 'to_dict' method is available in 'Review'"""
        self.assertEqual('to_dict' in dir(self.rev), True)


if __name__ == "__main__":
    unittest.main()
