#!/usr/bin/python3
"""Unit test for the User class"""
import unittest
import pep8
from models.user import User


class Test_User(unittest.TestCase):
    """ Test_User class"""

    def test_pep8_conformance(self):
        """ Test that we conform to PEP8 """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/user.py'])
        self.assertEqual(result.total_errors, 0, "Fix pep8")

    def test_doctring(self):
        """ Test doctrings """
        self.assertIsNotNone(User.__doc__)

    def has_attributes(self):
        """ Test """
        self.assertIsNotNone(hasattr(User, 'email'))
        self.assertIsNotNone(hasattr(User, 'password'))
        self.assertIsNotNone(hasattr(User, 'first_name'))
        self.assertIsNotNone(hasattr(User, 'last_name'))
