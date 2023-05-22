#!/usr/bin/python3
"""Unit test for the Base class"""
import time
import pep8
import unittest
from models.base_model import BaseModel


class Test_BaseModel(unittest.TestCase):
    """ Test_BaseModel class"""

    def setUp(self):
        """ setup data for every test """
        self.test_base = BaseModel()

    def tearDown(self):
        """ clean the dat for the next test """
        pass

    def test_instance(self):
        """ test if an object is an instance from BaseModel """
        self.assertIsInstance(self.test_base, BaseModel)

    def test_pep8_conformance(self):
        """ Test that we conform to PEP8 """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0, "Fix pep8")

    def test_doctring(self):
        """ Test doctrings """
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)

    def test_str(self):
        self.assertIsNotNone(self.test_base)

    def test_dict(self):
        obj_dict = self.test_base.__dict__
        self.assertEqual(self.test_base.__class__.__name__, "BaseModel")
        self.assertTrue(isinstance(obj_dict, dict))

    def test_save(self):
        baseModel = BaseModel()
        updated_at_before_save = baseModel.updated_at
        time.sleep(0.5)
        baseModel.save()
        updated_at_after_save = baseModel.updated_at
        self.assertNotEqual(baseModel.updated_at, baseModel.created_at)
        self.assertNotEqual(updated_at_before_save, updated_at_after_save)

    # test BaseModel before and after clling save method
    def test_save_before_save(self):
        self.assertEqual(self.testModel.updated_at,
                         self.testModel.created_at)
    # test BaseModel before and after clling save method

    def test_save_after_save(self):
        self.testModel.save()
        self.assertNotEqual(self.testModel.updated_at,
                            self.testModel.created_at)
    # def test_save(self):
    #     self.test_base.save()
    #     self.assertNotEqual(self.test_base.created_at, self.test_base.updated_at)

    def has_attribute(self):
        self.assertTrue(hasattr(BaseModel, "id"))
        self.assertTrue(hasattr(BaseModel, "created_at"))
        self.assertTrue(hasattr(BaseModel, "updated_at"))
