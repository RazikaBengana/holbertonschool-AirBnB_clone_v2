#!/usr/bin/python3
"""
Unit test suite for testing DBStorage class methods;
This module contains a series of tests to verify the functionality
and documentation of the DBStorage class and its methods
"""

import unittest
import pycodestyle
from models.engine.db_storage import DBStorage


class test_db_storage(unittest.TestCase):
    """A test case for the DBStorage class"""

    def test_doc(self):
        """
        Test cases to check if documentation is present for the DBStorage class and its methods;
        Verify that all class and method documentation strings are non-empty
        """
        module = len(DBStorage.__doc__)
        self.assertGreater(module, 0, "No documentation for DBStorage class")

        module_class = len(DBStorage.__doc__)
        self.assertGreater(module_class, 0, "No documentation for DBStorage class")

        module_class = len(DBStorage.new.__doc__)
        self.assertGreater(module_class, 0, "No documentation for new method")

        module_class = len(DBStorage.save.__doc__)
        self.assertGreater(module_class, 0, "No documentation for save method")

        module_class = len(DBStorage.delete.__doc__)
        self.assertGreater(module_class, 0, "No documentation for delete method")

        module_class = len(DBStorage.reload.__doc__)
        self.assertGreater(module_class, 0, "No documentation for reload method")

        module_class = len(DBStorage.all.__doc__)
        self.assertGreater(module_class, 0, "No documentation for all method")

        module_class = len(DBStorage.__init__.__doc__)
        self.assertGreater(module_class, 0, "No documentation for constructor")
