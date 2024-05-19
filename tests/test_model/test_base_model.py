#!/usr/bin/python3
"""Unittests for base model class"""

import unittest
from models.base_model import BaseModel
from datetime import datetime
from uuid import UUID
from models import storage


class TestsBaseModel(unittest.TestCase):

    def test_normal_cases_base_model(self):
        my_object = BaseModel()
        my_object.name = "Holbiland"
        my_object.my_number = 29
        my_object.save()
        my_object_dict = my_object.to_dict()
        self.assertEqual(my_object.name, "Holbiland")
        self.assertEqual(my_object.my_number, 29)
        self.assertEqual(my_object.__class__.__name__, "BaseModel")

if __name__ == "__main__":
    unittest.main()
