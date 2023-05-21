#!/usr/bin/python3
"""Unit test for the Base class"""
import unittest
import pep8
from models.engine.file_storage import FileStorage


class Test_FileStorage(unittest.TestCase):
    """ Test_BaseModel class"""

    def setUp(self):
        """ Setup data for every test """
        self.test_file_storage = FileStorage()

    def tearDown(self):
        """ Clean the dat for the next test """
        pass

    def test_instance(self):
        """ Test if an object is an instance from BaseModel """
        self.assertIsInstance(self.test_file_storage, FileStorage)

    def test_has_attributes(self):
        """ Test if the class has all the attributes"""
        pass

    def test_pep8_conformance(self):
        """ Test that we conform to PEP8 """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0, "Fix pep8")

    def test_doctring(self):
        """ Test doctrings """
        self.assertIsNotNone(FileStorage.__doc__)
        self.assertIsNotNone(FileStorage.all.__doc__)
        self.assertIsNotNone(FileStorage.new.__doc__)
        self.assertIsNotNone(FileStorage.save.__doc__)
        self.assertIsNotNone(FileStorage.reload.__doc__)
