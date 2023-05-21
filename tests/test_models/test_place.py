#!/usr/bin/python3
"""Unit test for the Place class"""
import unittest
import pep8
from models.place import Place


class Test_Place(unittest.TestCase):
    """ Test_Place class"""

    def test_pep8_conformance(self):
        """ Test that we conform to PEP8 """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/place.py'])
        self.assertEqual(result.total_errors, 0, "Fix pep8")

    def test_doctring(self):
        """ Test doctrings """
        self.assertIsNotNone(Place.__doc__)

    def has_attributes(self):
        """ Test """
        self.assertIsNotNone(hasattr(Place, 'city_id'))
        self.assertIsNotNone(hasattr(Place, 'user_id'))
        self.assertIsNotNone(hasattr(Place, 'name'))
        self.assertIsNotNone(hasattr(Place, 'description'))
        self.assertIsNotNone(hasattr(Place, 'number_rooms'))
        self.assertIsNotNone(hasattr(Place, 'number_bathrooms'))
        self.assertIsNotNone(hasattr(Place, 'max_guest'))
        self.assertIsNotNone(hasattr(Place, 'price_by_night'))
        self.assertIsNotNone(hasattr(Place, 'latitude'))
        self.assertIsNotNone(hasattr(Place, 'longitude'))
        self.assertIsNotNone(hasattr(Place, 'amenity_ids'))
