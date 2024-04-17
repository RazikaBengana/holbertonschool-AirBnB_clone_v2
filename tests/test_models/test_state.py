#!/usr/bin/python3
"""Unit test suite for the State class"""

import unittest
import os
from models.state import State
from models.base_model import BaseModel
import pep8


class TestState(unittest.TestCase):
    """Test cases for the State class"""

    @classmethod
    def setUpClass(cls):
        """Set up test cases environment before all tests run"""
        cls.state = State()
        cls.state.name = "CA"

    @classmethod
    def teardown(cls):
        """Clean up after all tests have run"""
        del cls.state

    def tearDown(self):
        """Clean up after each test case runs"""
        try:
            os.remove("file.json")

        except Exception:
            pass

    def test_pep8_Review(self):
        """Test the State class for PEP 8 compliance"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/state.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_checking_for_docstring_State(self):
        """Ensure that all methods in State have docstrings"""
        self.assertIsNotNone(State.__doc__)

    def test_attributes_State(self):
        """Test that State instances have the correct attributes"""
        self.assertTrue('id' in self.state.__dict__)
        self.assertTrue('created_at' in self.state.__dict__)
        self.assertTrue('updated_at' in self.state.__dict__)
        self.assertTrue('name' in self.state.__dict__)

    def test_is_subclass_State(self):
        """Verify that State is a subclass of BaseModel"""
        self.assertTrue(issubclass(self.state.__class__, BaseModel))

    def test_attribute_types_State(self):
        """Check the types of State attributes"""
        self.assertEqual(type(self.state.name), str)

    def test_save_State(self):
        """Test the save functionality of the State class"""
        self.state.save()
        self.assertNotEqual(self.state.created_at, self.state.updated_at)

    def test_to_dict_State(self):
        """Verify the dictionary representation of State instances"""
        self.assertEqual('to_dict' in dir(self.state), True)


if __name__ == "__main__":
    unittest.main()
