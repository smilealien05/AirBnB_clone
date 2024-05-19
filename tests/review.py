#!/usr/bin/python3
"""Defines a BaseModel class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """The Review class"""
    place_id = ''
    user_id = ''
    text = ''

