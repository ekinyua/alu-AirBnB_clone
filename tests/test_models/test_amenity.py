#!/usr/bin/python3
"""Unit test for the Amenity class"""
import unittest
import pep8
from models.amenity import Amenity


class Test_Amenity(unittest.TestCase):
    """ Test_Amenity class"""

    def test_pep8_conformance(self):
        """ Test that we conform to PEP8 """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/amenity.py'])
        self.assertEqual(result.total_errors, 0, "Fix pep8")

    def test_doctring(self):
        """ Test doctrings """
        self.assertIsNotNone(Amenity.__doc__)

    def has_attributes(self):
        """ Test attributes """
        self.assertIsNone(hasattr(Amenity, "name"))
