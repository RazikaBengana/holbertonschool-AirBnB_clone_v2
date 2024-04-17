#!/usr/bin/python3
"""Unit test suite for the User class"""

import unittest
import os
from models.user import User
from models.base_model import BaseModel
import pep8


class TestUser(unittest.TestCase):
    """Test cases for the User class"""

    @classmethod
    def setUpClass(cls):
        """Set up resources before running any tests in this class"""
        cls.user = User()
        cls.user.first_name = "Kevin"
        cls.user.last_name = "Yook"
        cls.user.email = "yook00627@gmail.com"
        cls.user.password = "secret"

    @classmethod
    def teardown(cls):
        """Clean up resources after running all tests in this class"""
        del cls.user

    def tearDown(self):
        """Remove any resources that were set up for the test"""
        try:
            os.remove("file.json")

        except Exception:
            pass

    def test_pep8_User(self):
        """Check that the 'user.py' file conforms to PEP8"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/user.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_checking_for_docstring_User(self):
        """Ensure User class has a docstring"""
        self.assertIsNotNone(User.__doc__)

    def test_attributes_User(self):
        """Verify that User has all expected attributes"""
        self.assertTrue('email' in self.user.__dict__)
        self.assertTrue('id' in self.user.__dict__)
        self.assertTrue('created_at' in self.user.__dict__)
        self.assertTrue('updated_at' in self.user.__dict__)
        self.assertTrue('password' in self.user.__dict__)
        self.assertTrue('first_name' in self.user.__dict__)
        self.assertTrue('last_name' in self.user.__dict__)

    def test_is_subclass_User(self):
        """Check if User is a subclass of BaseModel"""
        self.assertTrue(issubclass(self.user.__class__, BaseModel))

    def test_attribute_types_User(self):
        """Test the type of User attributes"""
        self.assertEqual(type(self.user.email), str)
        self.assertEqual(type(self.user.password), str)
        self.assertEqual(type(self.user.first_name), str)
        self.assertEqual(type(self.user.last_name), str)

    def test_save_User(self):
        """Test the save method of User"""
        self.user.save()
        self.assertNotEqual(self.user.created_at, self.user.updated_at)

    def test_to_dict_User(self):
        """Test the to_dict method of User"""
        self.assertTrue('to_dict' in dir(self.user))

if __name__ == "__main__":
    unittest.main()
