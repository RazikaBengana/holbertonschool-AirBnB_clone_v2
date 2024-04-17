#!/usr/bin/python3
"""Unit test suite for the HBNBCommand console"""

from itertools import count
import os
import unittest
import models
import json
import cmd
from io import StringIO
from console import HBNBCommand
import console
import pycodestyle
from unittest.mock import patch
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State
from models.engine.file_storage import FileStorage


class TestBasicCaseAndDoc(unittest.TestCase):
    """
    This class tests the documentation and basic functionality of the console
    """

    def test_doc(self):
        """
        Test to ensure that all modules, classes, and methods have documentation
        """
        # Check for module documentation
        module = len(console.__doc__)
        self.assertGreater(module, 0, "Console module lacks documentation.")

        # Check for class documentation
        self.assertGreater(len(HBNBCommand.__doc__), 0, "HBNBCommand class lacks documentation.")

        # Check each method for documentation
        self.assertGreater(len(HBNBCommand.do_all.__doc__), 0, "do_all method lacks documentation.")
        self.assertGreater(len(HBNBCommand.do_create.__doc__), 0, "do_create method lacks documentation.")
        self.assertGreater(len(HBNBCommand.do_destroy.__doc__), 0, "do_destroy method lacks documentation.")
        self.assertGreater(len(HBNBCommand.do_quit.__doc__), 0, "do_quit method lacks documentation.")
        self.assertGreater(len(HBNBCommand.do_EOF.__doc__), 0, "do_EOF method lacks documentation.")
        self.assertGreater(len(HBNBCommand.do_count.__doc__), 0, "do_count method lacks documentation.")
        self.assertGreater(len(HBNBCommand.do_update.__doc__), 0, "do_update method lacks documentation.")
        self.assertGreater(len(HBNBCommand.emptyline.__doc__), 0, "emptyline method lacks documentation.")
        self.assertGreater(len(HBNBCommand.default.__doc__), 0, "default method lacks documentation.")
        self.assertGreater(len(HBNBCommand.help_all.__doc__), 0, "help_all method lacks documentation.")
        self.assertGreater(len(HBNBCommand.help_create.__doc__), 0, "help_create method lacks documentation.")
        self.assertGreater(len(HBNBCommand.help_EOF.__doc__), 0, "help_EOF method lacks documentation.")
        self.assertGreater(len(HBNBCommand.help_destroy.__doc__), 0, "help_destroy method lacks documentation.")
        self.assertGreater(len(HBNBCommand.help_quit.__doc__), 0, "help_quit method lacks documentation.")
        self.assertGreater(len(HBNBCommand.help_show.__doc__), 0, "help_show method lacks documentation.")
        self.assertGreater(len(HBNBCommand.help_update.__doc__), 0, "help_update method lacks documentation.")

        def test_pycodeStyle(self):
            """
            Test to ensure the code style complies with PEP 8
            """
            style = pycodestyle.StyleGuide(quiet=True)
            result = style.check_files(["console.py"])
            self.assertEqual(result.total_errors, 0, "Found code style errors (pycodestyle).")

        def test_emptyline(self):
            """
            Test that empty lines do not produce any output
            """
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("")
                self.assertEqual("", f.getvalue().strip())

        def test_UnknowCommand(self):
            """
            Test to ensure that unknown commands are handled correctly
            """
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("fdfdf")
                self.assertEqual("*** Unknown syntax: fdfdf", f.getvalue().strip())
