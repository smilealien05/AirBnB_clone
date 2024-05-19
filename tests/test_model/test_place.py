#!/usr/bin/python3
""" testing place cls"""
from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class test_Place(test_basemodel):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        new = self.value()
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_description(self):
        new = self.value()
        self.assertEqual(type(new.description), str)

