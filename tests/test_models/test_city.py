#!/usr/bin/python3
"""Unit test for the City class"""
import unittest
import pep8
from models.city import City


class Test_City(unittest.TestCase):
    """ Test_City class"""

    def test_pep8_conformance(self):
        """ Test that we conform to PEP8 """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/city.py'])
        self.assertEqual(result.total_errors, 0, "Fix pep8")

    def test_doctring(self):
        """ Test doctrings """
        self.assertIsNotNone(City.__doc__)

    def has_attributes(self):
        """ Test """
        self.assertIsNotNone(hasattr(City, 'name'))
        self.assertIsNotNone(hasattr(City, 'state_id'))
