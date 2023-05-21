#!/usr/bin/python3
"""Unit test for the State class"""
import unittest
import pep8
from models.state import State


class Test_State(unittest.TestCase):
    """ Test_State class"""

    def test_pep8_conformance(self):
        """ Test that we conform to PEP8 """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/state.py'])
        self.assertEqual(result.total_errors, 0, "Fix pep8")

    def test_doctring(self):
        """ Test doctrings """
        self.assertIsNotNone(State.__doc__)

    def has_attributes(self):
        """ Test """
        self.assertIsNotNone(hasattr(State, 'name'))
