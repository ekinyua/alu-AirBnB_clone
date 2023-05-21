#!/usr/bin/python3
"""Unit test for the Review class"""
import unittest
import pep8
from models.review import Review


class Test_Review(unittest.TestCase):
    """ Test_Review class"""

    def test_pep8_conformance(self):
        """ Test that we conform to PEP8 """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/review.py'])
        self.assertEqual(result.total_errors, 0, "Fix pep8")

    def test_doctring(self):
        """ Test doctrings """
        self.assertIsNotNone(Review.__doc__)

    def has_attributes(self):
        """ Test """
        self.assertIsNotNone(hasattr(Review, 'place_id'))
        self.assertIsNotNone(hasattr(Review, 'user_id'))
        self.assertIsNotNone(hasattr(Review, 'text'))
